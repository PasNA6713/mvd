<template>
  <v-card class="data-table"
  style="border-radius: 15px;">
    <v-data-table
    :headers="tableHeaders"
    :items="tableItems"
    >
      <template v-slot:header.datetime>
        <button @click="drawChart('datetime')">Время</button>
      </template>
      <template v-slot:header.parent_region>
        <button @click="drawChart('parent_region')">Город</button>
      </template>
      <template v-slot:header.region>
        <button @click="drawChart('region')">Регион</button>
      </template>
      <template v-slot:header.address>
        <button @click="drawChart('address')">Адрес</button>
      </template>
      <template v-slot:header.category>
        <button @click="drawChart('category')">Категория</button>
      </template>
      <template v-slot:header.organization>
        <button @click="drawChart('organization')">Организация</button>
      </template>
      <template v-slot:header.criminal_type>
        <button @click="drawChart('criminal_type')">Тип преследования</button>
      </template>
      <template v-slot:header.employee>
        <button @click="drawChart('employee')">Работник</button>
      </template>
      <template v-slot:header.crime_qualification>
        <button @click="drawChart('crime_qualification')">Квалификация преступления</button>
      </template>
      <template v-slot:header.yk_qualification>
        <button @click="drawChart('yk_qualification')">Квалификация по УК</button>
      </template>
      <template v-slot:header.severity>
        <button @click="drawChart('severity')">Строгость</button>
      </template>
      <template v-slot:header.crime_direction>
        <button @click="drawChart('crime_direction')">Направление преступления</button>
      </template>
      <template v-slot:header.damage>
        <button @click="drawChart('damage')">Ущерб</button>
      </template>
      <template v-slot:header.money>
        <button @click="drawChart('money')">Деньги</button>
      </template>
      <template v-slot:header.drug_name>
        <button @click="drawChart('drug_name')">Наркотики</button>
      </template>
      <template v-slot:header.drug_weight>
        <button @click="drawChart('drug_weight')">Масса наркотиков</button>
      </template>
      <template v-slot:header.victim_number>
        <button @click="drawChart('victim_number')">Количество пострадавших</button>
      </template>
      <template v-slot:header.dead_num>
        <button @click="drawChart('dead_num')">Количество погибших</button>
      </template>
      <template v-slot:header.is_operative>
        <button @click="drawChart('is_operative')">В процессе</button>
      </template>
      <template v-slot:header.is_attempt>
        <button @click="drawChart('is_attempt')">Это попытка</button>
      </template>
      <template v-slot:header.light>
        <button @click="drawChart('light')">Освещение</button>
      </template>
    </v-data-table>
  </v-card>
</template>

<style lang="scss" scoped>
.data-table {
  margin-top: 20px;
  padding: 30px;
}
</style>

<script>
export default {
    name: "DataTable",
    props: {
      tableHeaders: Array,
      tableItems: Array
    },

    methods: {
      drawChart(val) {
        this.$emit('get-chart', val)
      }
    }
}
</script>