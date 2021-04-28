<template>
  <div>
    <MapFilter class="map-filter" v-bind:theme="{'color': '#55884F'}" v-on:get-data="getData"/>
    <Map class="map" v-bind:filterParams="filterData" />
  </div>
</template>

<style lang="scss" scoped> 
@import '@/styles/common.scss';
@import '@/styles/views/home.scss';
</style>

<script>
import Map from "@/components/Map.vue"
import MapFilter from "@/components/MapFilter.vue"


export default {
  name: 'Home',
  components: {
    Map,
    MapFilter,
  },
  data() {
    return {
      filterData: {}
    }
  },

  methods: {
    getData(filterParams) {
      this.filterData = filterParams
    }
  }
}
</script>