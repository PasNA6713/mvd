<template>
  <v-card elevation="0">
    <v-row class="px-3">
      <v-col cols="3" v-for="field in Object.keys(filter)" :key="field">
        <v-autocomplete
          v-if='typeof(filterParams[field])=="object"'
          :items="filterParams[field]"
          v-model="chosedData[filter[field]]"
          :label="field"
          clearable
        ></v-autocomplete>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="3">
        <DateTimeField v-model="chosedData.datetime_after" label="С" />
      </v-col>

      <v-col cols="3">
        <DateTimeField v-model="chosedData.datetime_before" label="По" />
      </v-col>

      <v-col cols="3">
        <v-select
          v-model="chosedData.time_group"
          :items="Object.keys(timeGroups)"
          label="Время"
          class="md-4"
        >
        </v-select>
      </v-col>

      <v-col cols="3">
        <v-row justify="center">
          <v-btn :color="$route.meta.theme" @click="send" x-large dark>
            Найти
          </v-btn>
        </v-row>
      </v-col>
    </v-row>

    <v-btn @click="clearForm" fab elevation="0" absolute right top>
      <v-icon>mdi-restart</v-icon>
    </v-btn>
  </v-card>
</template>

<style lang="scss" scoped>
@import "@/styles/common.scss";
@import "@/styles/views/stat.scss";
</style>

<script>
import DateTimeField from "../DateTimeForm.vue";

export default {
  name: "StatFilter",

  components: {
    DateTimeField,
  },

  data() {
    return {
      filter: {
        Город: "parent_region",
        Регион: "region",
        "Способ совершения преступления": "category",
        Освещение: "light",
        Адрес: "address",
        "Наименование органа": "organization",
        "Вид уголовного преследования": "criminal_type",
        "Кем выявлено": "employee",
        "Выявлено по оперативным данным": "is_operative",
        "Квалификация преступления": "crime_qualification",
        "пункт Квалификация преступления по УК РФ": "yk_qualification",
        Тяжесть: "severity",
        "Приготовление/покушение": "is_attempt",
        Ущерб: "damage",
        Направленность: "crime_direction",
        "Наименование наркотика": "drug_name",
      },

      filterParams: null,

      timeGroups: {
        "Все время": null,
        "2.00 - 11.00": 0,
        "11.00 - 16.00": 1,
        "16.00 - 21.00": 2,
        "21.00 - 2.00": 3,
      },

      chosedData: {
        datetime_after: null,
        datetime_before: new Date(),
        time_group: 'Все время'
      },

      loaded: false
    };
  },

  methods: {
    send() {
      this.chosedData.time_group = this.timeGroups[this.chosedData.time_group]
      this.$emit("get-data", this.chosedData);
    },

    getData() {
      this.filterParams = {...this.filter}
      Object.keys(this.filter).forEach((key) => {
        axios
          .get(
            `${this.$store.state.backendUrl}/map/get-filter-params/${this.filter[key]}/`
          )
          .then((response) => {
            this.filterParams[key] = response.data;
            this.chosedData[this.filter[key]] = null;
          });
      });
    },

    clearForm() {
      Object.keys(this.chosedData).forEach((field) => {
        this.chosedData[field] = null;
      });
    },
  },

  async created() {
    this.getData();
  },
};
</script>