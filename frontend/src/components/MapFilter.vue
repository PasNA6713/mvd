<template>
  <v-card
  elevation="8">
    <v-row>
      <v-col cols="6">
        <v-card class="map-filter"
        elevation="5">
          <v-autocomplete class="map-filter__region"
            :items="filterData.region"
            v-model="chosedData.region"
            label="Регион"
          ></v-autocomplete>
          <v-autocomplete class="map-filter__category"
            :items="filterData.category"
            v-model="chosedData.category"
            label="Категория"
          ></v-autocomplete>
          <v-autocomplete class="map-filter__light"
            :items="filterData.light"
            v-model="chosedData.light"
            label="Освещение"
          ></v-autocomplete>
        </v-card>
      </v-col>

      <v-col cols="6" class="map-filter-2">
        <v-card
        elevation="5">
          <v-date-picker
            :color="theme.color"
            width="600px"
            range
            locale="ru"
            v-model="chosedData.date"
            :no-title="true"
            :show-current="false"
          ></v-date-picker>
        </v-card>

        <div class="common-spacer"></div>
        <v-slider
        :tick-labels="filterData.sliderTicks"
        :max="4"
        step="1"
        ticks="always"
        tick-size="3"
        v-model="chosedData.timeGroup">
        </v-slider>
      </v-col>
      <div class="common-spacer"></div>
    </v-row>

    <v-row class="filter-buttons">
      <v-btn class="filter-buttons__button" color="#EDAC48" @click="clearForm">Очистить фильтр</v-btn>
      <v-btn class="filter-buttons__button" color="#EDAC48" @click="getData">Показать на карте</v-btn>
    </v-row>
  </v-card>
</template>

<style lang="scss" scoped>
@import '@/styles/common.scss';
@import '@/styles/components/map-filter.scss';
</style>

<script>
export default {
  name: "MapFilter",
  props: {
    theme: Object
  },
  data() {
    return {
      filterData: {
        region: [],
        light: [],
        category: [],
        sliderTicks: [
          "Все время",
          "2.00 - 11.00", "11.00 - 16.00", 
          "16.00 - 21.00", "21.00 - 2.00"
        ],
      },

      chosedData: {
        date: ["", ""],
        timeGroup: 0,
        region: "",
        light: "",
        category: ""
      }
    }
  },

  computed: {
    filterParams() {
      let filterData = {
        region: this.chosedData.region,
        light: this.chosedData.light,
        category: this.chosedData.category,
        datetime_before: (this.chosedData.date[1]) ? `${this.chosedData.date[1]}T00:00:00Z` : "", 
        datetime_after: (this.chosedData.date[0]) ? `${this.chosedData.date[0]}T00:00:00Z` : "",
        time_group: this.chosedData.timeGroup
      }
      return filterData
    }
  },

  methods: {
    async getFilterData() {
      await axios.get(`${this.$store.state.backendUrl}/map/get-filter-params/`
      ).then(response => {
        this.filterData.region = response.data.region
        this.filterData.category = response.data.category
        this.filterData.light = response.data.light
      })
    },

    getData() {
      this.$emit("get-data", this.filterParams)
    },

    clearForm() {
        this.chosedData.region = ""
        this.chosedData.light = ""
        this.chosedData.category = ""
        this.chosedData.timeGroup = 0
        this.chosedData.date = ["", ""] 
    },
  },

  created() {
    this.getFilterData()
  }
}
</script>