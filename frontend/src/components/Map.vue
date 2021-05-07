<template>
  <v-card class="map-card"
  style="border-radius: 15px; height: 904px">
    <yandex-map id="map"
      :settings="settings"
      :coords="mapCenter"
      :zoom="10" 
      :use-object-manager="true"
      :controls="['zoomControl']"
      @map-was-initialized="getMapInstance"
    >
    </yandex-map>
  </v-card>
</template>

<style lang="scss" scoped>
@import '@/styles/common.scss';
@import '@/styles/components/map.scss';
</style>

<script>
import { yandexMap, ymapMarker } from 'vue-yandex-maps'
import { formatedDateTime } from '@/utils/helpers.js'

export default {
  name: "Map",
  props: {
    filterParams: Object
  },
  components: {
    yandexMap,
    ymapMarker
  },
  data() {
    return {
      clusterMap: null,
      settings: {
        apiKey: 'e70694c3-ce7f-4459-b7f6-be3d53e2cc8e',
        lang: 'ru_RU',
        coordorder: 'latlong',
        version: '2.1',
      },
      mapCenter: [59.9370, 30.3089],
      points: [],
      objectManager: null
    }
  },

  methods: {
    clickPoint(e) {
      let target = e.get('objectId')
      if (this.objectManager.clusters.getById(target)) {
        let cluster = this.objectManager.clusters.getById(target)
        let objects = cluster.properties.geoObjects
        let buf = []

        objects.forEach(element => {
          buf.push(element.id)
        })
        axios.post(`${this.$store.state.backendUrl}/map/some/`,{
          ids: buf
        }).then(response => {
          objects.sort((prev, next) => prev.id - next.id)
          let clusterData = response.data.sort((prev, next) => prev.id - next.id)

          for(let i=0;i<clusterData.length;i++) {
            objects[i].properties = {
              clusterCaption: clusterData[i].address,
              balloonContentHeader: (clusterData[i].address) ? `<a>${clusterData[i].address}</a>` : `<a>${clusterData[i].address}</a>`,
              balloonContentBody: clusterData[i].category,
              balloonContentFooter: formatedDateTime(clusterData[i].datetime), 
            }  
          } 
        })
      }
      else {
        let point = this.objectManager.objects.getById(target)
        axios.get(`${this.$store.state.backendUrl}/map/${target}/`
        ).then(response => {
          point.properties.hintContent = response.data.category + " " + formatedDateTime(response.data.datetime)
          point.properties.balloonContent = response.data.category + " " + formatedDateTime(response.data.datetime)
        })
      }
    },

    async getMapInstance(map) {
      if(map) {
        try {
          this.clusterMap = map
          this.objectManager = new ymaps.ObjectManager({
            clusterize: true,
            gridSize: 32,
            clusterDisableClickZoom: true
          })
          this.clusterMap.geoObjects.events.add('click', (e) => (this.clickPoint(e)))

          try {
            this.objectManager.add(this.points)
            this.clusterMap.geoObjects.add(this.objectManager)
          } catch (error) {
            console.log('no points!')
          }
        } catch (error) {
          console.log(error)
        }
      }
    },
  },

  watch: {
    filterParams: function(filterParams) {
      this.objectManager.removeAll()
      this.points = []

      axios.get(`${this.$store.state.backendUrl}/map/`, {
        params: {
          category: filterParams.category,
          region: filterParams.region,
          light: filterParams.light,
          datetime_before: filterParams.datetime_before, 
          datetime_after: filterParams.datetime_after,
          time_group: filterParams.time_group
        }
      }
      ).then(response => {
          for (let i=0;i<response.data.length;i++){
            let marker = {
              type: 'Feature',
              id: response.data[i]["id"],
              geometry: {
                  type: 'Point',
                  coordinates: [response.data[i]["lat"], response.data[i]["long"]]
              }
            }
            this.points.push(marker)
          }
          this.objectManager.add(this.points)
      })
    }
  }
}
</script>