<template>
  <v-card class="data-table"
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
      tableHeaders: Array,
      tableItems: Array
    },
}
</script>