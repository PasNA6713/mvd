<template>
  <div>
    <StatFilter class="map-filter" v-bind:theme="{'color': '#544F88'}" v-on:get-data="getData"/>
    <v-container>
      <DataTableHeaderClicker :tableHeaders="tableHeaders" :tableItems="tableItems" v-on:get-chart="getChart"/>
      <v-card class="chart-card"
        style="border-radius: 15px; max-height: 500px; margin-top: 20px"
        v-if="loaded" >
        <Chart :chart-data="chartData" />
      </v-card>
    </v-container>
  </div>
</template>

<style lang="scss" scoped> 
@import '@/styles/common.scss';
@import '@/styles/views/stat.scss';
</style>

<script>
import StatFilter from "@/components/StatFilter.vue"
import DataTableHeaderClicker from "@/components/DataTableHeaderClicker.vue"
import Chart from "@/components/Chart.vue"

import { formatedDateTime } from '@/utils/helpers.js'

export default {
  name: 'Stat',
  components: {
      StatFilter,
      DataTableHeaderClicker,
      Chart
    },
  data() {
    return {
      loaded: false,
      chartData: {},

      filterData: {},
      tableItems: [],
      tableHeaders: [
          { text: 'Время', sortable: false, align: 'start', value: 'datetime' },
          { text: 'Город', sortable: false, align: 'start', value: 'parent_region' },
          { text: 'Регион', sortable: false, align: 'start', value: 'region' },
          { text: 'Адрес', sortable: false, align: 'start', value: 'address' },
          { text: 'Категория', sortable: false, align: 'start', value: 'category' },
          { text: 'Организация', sortable: false, align: 'start', value: 'organization' },
          { text: 'Тип преследования', sortable: false, align: 'start', value: 'criminal_type' },
          { text: 'Работник', sortable: false, align: 'start', value: 'employee' },
          { text: 'Квалификация преступления', sortable: false, align: 'start', value: 'crime_qualification' },
          { text: 'Квалификация по УК', sortable: false, align: 'start', value: 'yk_qualification' },
          { text: 'Строгость', sortable: false, align: 'start', value: 'severity' },
          { text: 'Направление преступления', sortable: false, align: 'start', value: 'crime_direction' },
          { text: 'Ущерб', sortable: false, align: 'start', value: 'damage' },
          { text: 'Деньги', sortable: false, align: 'start', value: 'money' },
          { text: 'Наркотики', sortable: false, align: 'start', value: 'drug_name' },
          { text: 'Масса наркотиков', sortable: false, align: 'start', value: 'drug_weight' },
          { text: 'Количество пострадавших', sortable: false, align: 'start', value: 'victim_number' },
          { text: 'Количество погибших', sortable: false, align: 'start', value: 'dead_num' },
          { text: 'В процессе', sortable: false, align: 'start', value: 'is_operative' },
          { text: 'Это попытка', sortable: false, align: 'start', value: 'is_attempt' },
          { text: 'Освещение', sortable: false, align: 'start', value: 'light' },
      ]
    }
  },

  methods: {
    async getData(filterParams) {
      this.filterData = filterParams
      console.log(this.filterData)

       await axios.get(`${this.$store.state.backendUrl}/map/`, {
        params: {
          category: this.filterData.category,
          region: this.filterData.region,
          light: this.filterData.light,
          datetime_before: this.filterData.datetime_before, 
          datetime_after: this.filterData.datetime_after,
          time_group: this.filterData.time_group,
          parent_region: this.filterData.parent_region,
          address: this.filterData.address,
          organization: this.filterData.organization,
          criminal_type: this.filterData.criminal_type,
          employee: this.filterData.employee,
          is_operative: this.filterData.is_operative,
          crime_qualification: this.filterData.crime_qualification,
          yk_qualification: this.filterData.yk_qualification,
          severity: this.filterData.severity,
          is_attempt: this.filterData.is_attempt,
          damage: this.filterData.damage,
          crime_direction: this.filterData.crime_direction,
          money: this.filterData.money,
          drug_name: this.filterData.drug_name,
          drug_weight: this.filterData.drug_weight,
          victim_number: this.filterData.victim_number,
          dead_num: this.filterData.dead_num,
        }
		  }).then(response => {
          let points = response.data.map(arr => arr.id)

          axios.post(`${this.$store.state.backendUrl}/map/some/`, {
            ids: points
          }).then(response => {
            console.log(response.data)
            let tableItems = response.data
            for(let i=0;i<tableItems.length;i++) tableItems[i].datetime = formatedDateTime(tableItems[i].datetime)
            this.tableItems = tableItems
          })
      })
    },

    async getChart(column) {
      this.loaded = false
      await axios.get(`${this.$store.state.backendUrl}/map/plot-diagram/${column}/`, {
        params: {
          category: this.filterData.category,
          region: this.filterData.region,
          light: this.filterData.light,
          datetime_before: this.filterData.datetime_before, 
          datetime_after: this.filterData.datetime_after,
          time_group: this.filterData.time_group,
          parent_region: this.filterData.parent_region,
          address: this.filterData.address,
          organization: this.filterData.organization,
          criminal_type: this.filterData.criminal_type,
          employee: this.filterData.employee,
          is_operative: this.filterData.is_operative,
          crime_qualification: this.filterData.crime_qualification,
          yk_qualification: this.filterData.yk_qualification,
          severity: this.filterData.severity,
          is_attempt: this.filterData.is_attempt,
          damage: this.filterData.damage,
          crime_direction: this.filterData.crime_direction,
          money: this.filterData.money,
          drug_name: this.filterData.drug_name,
          drug_weight: this.filterData.drug_weight,
          victim_number: this.filterData.victim_number,
          dead_num: this.filterData.dead_num,
        }
      }).then(response => {
          let name = ""
          for (let i=0;i<this.tableHeaders.length;i++){
            if (this.tableHeaders[i].value == column) {
              name = this.tableHeaders[i].text
            }
          }

          this.chartData = {
            labels: response.data.map(x => x.field),
            datasets: [
              {
                label: `Количество преступлений по ${name}`,
                borderColor: "#EDAC48",
                pointBackgroundColor: "#EDAC48",
                borderWidth: 1,
                pointBorderColor: "white",
                backgroundColor: "#EDAC48",
                data: response.data.map(x => x.c)
              }
            ]
          }

          this.loaded = true
        })
    }
  }
}
</script>