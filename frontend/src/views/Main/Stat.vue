<template>
  <div>
    <MapFilter class="map-filter" v-bind:theme="{'color': '#544F88'}" v-on:get-data="getData"/>
  </div>
</template>

<style lang="scss" scoped> 
@import '@/styles/common.scss';
@import '@/styles/views/stat.scss';
</style>

<script>
import Navbar from "@/components/Navbar.vue"
import Header from "@/components/Header.vue"
import MapFilter from "@/components/MapFilter.vue"

export default {
  name: 'Home',
  components: {
        Navbar,
        Header,
        MapFilter
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