<template>
    <yandex-map id="map"
      :settings="settings"
      :coords="mapCenter"
      :zoom="10" 
      :use-object-manager="true"
      :scrollZoom="false"
      :controls="['zoomControl']"
      @map-was-initialized="getMapInstance"
    >
    </yandex-map>
</template>

<style lang="scss" scoped>
@import '@/styles/components/map.scss';
</style>

<script>
import { yandexMap, ymapMarker } from 'vue-yandex-maps'
import { formatedDateTime } from '@/utils/helpers.js'

export default {
  name: "ClusterMap",
  
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
      clusters: [],
      points: [],
      clusterCounter: 1,
      objectManager: null,

      pressed: false,
      userPoint: {
        coords: null,
        points: null,
      },
      userPlacemark: null
    }
  },

  methods: {
    drawTable(cluster, cid) {
      for(let i=0;i<cluster.length;i++) {
        cluster[i].datetime = formatedDateTime(cluster[i].datetime)
        cluster[i].cid = cid
      }

      this.$emit('get-table',cluster)
    },

    clickPoint(e) {
      let target = e.get('objectId')
      let point = this.objectManager.objects.getById(target)

      axios.post(`${this.$store.state.backendUrl}/map/some/`,{
        ids: point.properties.points
      }).then(response => {
        this.drawTable(response.data, point.id)

        let scrollElement = document.getElementById('map');
        scrollElement.scrollBottom = scrollElement.scrollHeight;
        this.$vuetify.goTo(scrollElement);
      })
    },

    async getMapInstance(map) {
      if(map) {
        try {
          this.clusterMap = map
          this.objectManager = new ymaps.ObjectManager({
            clusterize: false,
            gridSize: 32,
            clusterDisableClickZoom: true
          })
          this.clusterMap.geoObjects.events.add('click', (e) => (this.clickPoint(e)))
          this.clusterMap.events.add('click', (e) => (this.clickUserPoint(e)))

          try {
            this.objectManager.add(this.clusters)
            this.clusterMap.geoObjects.add(this.objectManager)
          } catch (error) {
            console.log('no clusters!')
          }
        } catch (error) {
          console.log(error)
        }
      }
    },

    async clickUserPoint(e) {
      if (this.pressed) {
          if (this.userPlacemark) {
            this.clusterMap.geoObjects.remove(this.userPlacemark)
          }

          this.userPoint.coords = e.get('coords')

          await axios.post(`${this.$store.state.backendUrl}/map/range/?category=Убийство`, {
              lat: this.userPoint.coords[0],
              long: this.userPoint.coords[1]
          }).then(response => {
              this.userPlacemark = new ymaps.Placemark(this.userPoint.coords)
              this.clusterMap.geoObjects.add(this.userPlacemark)
              this.pressed = false
          })
        }
    },

    changeAccessToMap() {
      this.pressed = !this.pressed
    },

    deleteUserPoint() {
      this.clusterMap.geoObjects.remove(this.userPlacemark)
      this.userPlacemark = null
    },
  },

  watch: {
    filterParams: function(filterParams) {
      this.objectManager.removeAll()
      this.clusters = []

      axios.get(`${this.$store.state.backendUrl}/cluster/${filterParams.cluster_quontity}/`, {
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
            for (let i=0; i<response.data.length;i++){
              let cluster = {
                type: 'Feature',
                id: this.clusterCounter,
                geometry: {
                    type: 'Point',
                    coordinates: [response.data[i]["lat"], response.data[i]["long"]]
                },
                properties: {
                    points: response.data[i]["points"]
                },
                options: {
                    preset: "islands#dotIcon",
                    iconColor: "red"
                }
              }
              
              this.clusterCounter += 1
              this.clusters.push(cluster)
              this.points.push(...cluster.properties.points)
            }
          
          this.objectManager.add(this.clusters)
          axios.post(`${this.$store.state.backendUrl}/map/some/`,{
            ids: this.points
          }).then(response => {
            for(let i=0;i<response.data.length;i++) response.data[i].datetime = formatedDateTime(response.data[i].datetime)
            this.$emit('get-table',response.data)
          })
      })
    }
  }
}
</script>