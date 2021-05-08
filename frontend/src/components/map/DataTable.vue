<template>
  <v-card class="data-table" elevation="0" style="border-radius: 15px">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          fab
          elevation="0"
          :color="$route.meta.theme"
          small
          dark
          v-bind="attrs"
          v-on="on"
          absolute
          top
          right
          style="margin-top: 20px;"
        >
          <v-icon>mdi-download</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in ['json', 'csv', 'xlsx']"
          :key="index"
        >
          <v-list-item-title>
            <v-btn text @click="$emit('download', item)">{{ item }}</v-btn>
          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-data-table :headers="tableHeaders" :items="tableItems"> </v-data-table>
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
    tableItems: Array,
  },
};
</script>