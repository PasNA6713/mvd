<template>
  <v-container>
    <v-card elevation="0">
      <v-card-text>
        <v-row>
          <v-col>
            <v-autocomplete
              :items="filterData.region"
              v-model="chosedData.region"
              label="Регион"
            ></v-autocomplete>

            <v-autocomplete
              :items="filterData.category"
              v-model="chosedData.category"
              label="Категория"
            ></v-autocomplete>
          </v-col>

          <v-col>
            <v-autocomplete
              :items="filterData.light"
              v-model="chosedData.light"
              label="Освещение"
            ></v-autocomplete>

            <v-select
              v-model="chosedData.timeGroup"
              :items="Object.keys(timeGroups)"
              label="Время"
              class="md-4"
            >
            </v-select>
          </v-col>

          <v-col>
            <DateTimeField v-model="chosedData.start_date" label="С" />
            <DateTimeField v-model="chosedData.end_date" label="По" />
          </v-col>

          <v-col>
            <v-text-field
              no-data-text="Введите целое число"
              v-model.number="chosedData.clusterQuontity"
              label="Количество кластеров"
            ></v-text-field>

            <v-row justify="center" class="mt-3">
              <v-btn :color="$route.meta.theme" @click="getData" x-large dark>
                Найти
              </v-btn>
            </v-row>
          </v-col>

          <v-btn @click="clearForm" fab elevation="0" absolute right top>
            <v-icon>mdi-restart</v-icon>
          </v-btn>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>


<script>
import DateTimeField from "../DateTimeForm.vue";

export default {
  name: "MapFilter",

  components: { DateTimeField },

  data: () => ({
    filterData: {
      region: [],
      light: [],
      category: [],
    },

    timeGroups: {
      "Все время": null,
      "2.00 - 11.00": 0,
      "11.00 - 16.00": 1,
      "16.00 - 21.00": 2,
      "21.00 - 2.00": 3,
    },

    chosedData: {
      start_date: null,
      end_date: new Date(),
      timeGroup: "Все время",
      region: "",
      light: "",
      category: "",
      clusterQuontity: 1,
    },

    menu: false,
  }),

  computed: {
    filterParams() {
      let filterData = {
        region: this.chosedData.region,
        light: this.chosedData.light,
        category: this.chosedData.category,
        datetime_before: this.chosedData.end_date,
        datetime_after: this.chosedData.start_date,
        time_group: this.timeGroups[this.chosedData.timeGroup],
        cluster_quontity: this.chosedData.clusterQuontity,
      };
      return filterData;
    },
  },

  methods: {
    getFilterData() {
      Object.keys(this.filterData).forEach((field) => {
        axios
          .get(
            `${this.$store.state.backendUrl}/map/get-filter-params/${field}/`
          )
          .then((response) => {
            this.filterData[field] = response.data;
          });
      });
    },

    getData() {
      this.$emit("get-data", this.filterParams);
    },

    clearForm() {
      this.chosedData.region = "";
      this.chosedData.light = "";
      this.chosedData.category = "";
      this.chosedData.timeGroup = "Все время";
      this.chosedData.start_date = null;
      this.chosedData.end_date = new Date();
      this.chosedData.clusterQuontity = null;
    },
  },

  created() {
    this.getFilterData();
  },
};
</script>

<style>
</style>