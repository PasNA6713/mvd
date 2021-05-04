<template>
  <v-card class="data-table"
  elevation="8"
  style="border-radius: 15px;">
    <v-data-table
    :headers="tableHeaders"
    :items="tableItems"
    >
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
      tableItems: Array
    },
    data() {
      return {
        tableHeaders: [
          { text: 'Время', filterable: true, align: 'start', value: 'datetime' },
          { text: 'Регион', filterable: true, align: 'start', value: 'region' },
          { text: 'Адрес', filterable: true, align: 'start', value: 'address' },
          { text: 'Категория', filterable: true, align: 'start', value: 'category' },
          { text: 'Освещение', filterable: true, align: 'start', value: 'light' },
        ]
      }
    }
}
</script>