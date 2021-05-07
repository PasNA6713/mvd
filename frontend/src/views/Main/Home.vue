<template>
  <div>
    <MapFilter class="map-filter" :theme="{'color': '#55884F'}" @get-data="getData"/>
    <v-container>
      <v-row class="maps-container">
        <v-col cols="6">
          <Map class="map" :filterParams="filterData" />
          <v-card class="chart-card"
          style="border-radius: 15px;"
          v-if="loaded" >
            <Chart :chart-data="chartData" />
          </v-card>	
        </v-col>
        <v-col cols="6">
          <ClusterMap class="map" :filterParams="filterData" @get-table="getTable"/>
          <DataTable :tableHeaders="tableHeaders" :tableItems="clusterData" v-if="loaded" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style lang="scss" scoped> 
@import '@/styles/common.scss';
@import '@/styles/views/home.scss';
</style>

<script>
import Map from "@/components/Map.vue"
import Chart from "@/components/Chart.vue"
import ClusterMap from "@/components/ClusterMap.vue"
import MapFilter from "@/components/MapFilter.vue"
import DataTable from "@/components/DataTable.vue"


export default {
  name: 'Home',
  components: {
    Map,
    ClusterMap,
    MapFilter,
    DataTable,
    Chart
  },
  data() {
    return {
      loaded: false,

      filterData: {},
      clusterData: [],
      chartData: {},
      
      tableHeaders: [
          { text: 'Время', filterable: true, align: 'start', value: 'datetime' },
          { text: 'Регион', filterable: true, align: 'start', value: 'region' },
          { text: 'Адрес', filterable: true, align: 'start', value: 'address' },
          { text: 'Категория', filterable: true, align: 'start', value: 'category' },
          { text: 'Освещение', filterable: true, align: 'start', value: 'light' },
      ]
    }
  },

  methods: {
    getData(val) {
      this.filterData = val
      
      axios.get(`${this.$store.state.backendUrl}/map/plot-bar/`, {
        params: {
          category: this.filterData.category,
          region: this.filterData.region,
          light: this.filterData.light,
          datetime_before: this.filterData.datetime_before, 
          datetime_after: this.filterData.datetime_after,
          time_group: this.filterData.time_group
        }
		  }).then(response => {
        this.chartData = {
          labels: response.data.map(x => x.month),
          datasets: [
            {
              label: "Количество преступлений по датам",
              borderColor: "EDAC48",
              pointBackgroundColor: "black",
              borderWidth: 1,
              pointBorderColor: "white",
              backgroundColor: "#EDAC48",
              data: response.data.map(x => x.c)
            }
          ]
        }
      })
    },

    getTable(val) {
      this.loaded = false
      this.clusterData = val
      this.loaded = true
    }
  }
}
</script>