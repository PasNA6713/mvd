<template>
  <div>
    <StatFilter class="map-filter" v-on:get-data="getData" />
    <DataTableHeaderClicker
      :tableHeaders="tableHeaders"
      :tableItems="tableItems"
      v-on:get-chart="getChart"
    />
    <v-card
      class="chart-card"
      style="border-radius: 15px; max-height: 500px; margin-bottom: 60px"
      v-if="loaded"
      elevation='0'
    >
      <Chart :chart-data="chartData" />
    </v-card>
  </div>
</template>

<style lang="scss" scoped>
@import "@/styles/common.scss";
@import "@/styles/views/stat.scss";
</style>

<script>
import StatFilter from "@/components/stat/StatFilter.vue";
import DataTableHeaderClicker from "@/components/stat/DataTableHeaderClicker.vue";
import Chart from "@/components/Chart.vue";

export default {
  name: "Stat",
  components: {
    StatFilter,
    DataTableHeaderClicker,
    Chart,
  },
  data() {
    return {
      loaded: false,
      chartData: {},

      tableItems: [],

      filterParams: {},

      tableHeaders: [
        { text: "Время", value: "datetime" },
        { text: "Город", value: "parent_region" },
        { text: "Регион", value: "region" },
        { text: "Адрес", value: "address" },
        { text: "Способ совершения преступления", value: "category" },
        { text: "Наименование органа", value: "organization" },
        { text: "Вид уголовного преследования", value: "criminal_type" },
        { text: "Кем выявлено", value: "employee" },
        { text: "Квалификация преступления", value: "crime_qualification" },
        { text: "Квалификация по УК", value: "yk_qualification" },
        { text: "Тяжесть", value: "severity" },
        { text: "Направленность", value: "crime_direction" },
        { text: "Ущерб", value: "damage" },
        { text: "Деньги", value: "money" },
        { text: "Наименование наркотика", value: "drug_name" },
        { text: "Масса наркотиков", value: "drug_weight" },
        { text: "Количество пострадавших", value: "victim_number" },
        { text: "Количество погибших", value: "dead_num" },
        { text: "В процессе", value: "is_operative" },
        { text: "Приготовление/покушение", value: "is_attempt" },
        { text: "Освещение", value: "light" },
      ],
    };
  },

  methods: {
    getData(filterParams) {
      this.filterParams = filterParams;
      axios
        .get(`${this.$store.state.backendUrl}/map/detail/`, {
          params: filterParams,
        })
        .then((r) => {
          this.tableItems = r.data;
        });
    },

    async getChart(column) {
      if (column != undefined) {
        this.loaded = false;
        await axios
          .get(`${this.$store.state.backendUrl}/map/plot-diagram/${column}/`, {
            params: this.filterParams,
          })
          .then((response) => {
            let name = "";
            for (let i = 0; i < this.tableHeaders.length; i++) {
              if (this.tableHeaders[i].value == column) {
                name = this.tableHeaders[i].text;
              }
            }

            this.chartData = {
              labels: response.data.map((x) => x.field),
              datasets: [
                {
                  label: `Количество преступлений по ${name}`,
                  borderColor: "#EDAC48",
                  pointBackgroundColor: "#EDAC48",
                  borderWidth: 1,
                  pointBorderColor: "white",
                  backgroundColor: "#EDAC48",
                  data: response.data.map((x) => x.c),
                },
              ],
            };

            this.loaded = true;
          });
      }
    },
  },
};
</script>