<template>
  <v-card class="data-table mb-6" style="border-radius: 15px" elevation="0">
    <v-card-title>
      Поиск

      <v-spacer></v-spacer>

      <v-pagination
        elevation="0"
        v-model="page"
        :length="pageCount"
        :total-visible="9"
        :color="$route.meta.theme"
        circle
      ></v-pagination>

      <v-spacer></v-spacer>

      <v-text-field
        v-model.lazy="buf"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        @keyup.enter="search = buf"
      ></v-text-field>
    </v-card-title>

    <v-data-table
      :headers="tableHeaders"
      :items="tableItems"
      :search="search"
      :page.sync="page"
      :options.sync="options"
      :items-per-page="itemsPerPage"
      hide-default-footer
      @page-count="pageCount = $event"
    >
      <template v-slot:item.datetime="{ item }">
        {{ formate(item.datetime) }}
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
import { formatedDateTime } from "@/utils/helpers.js";

export default {
  name: "DataTable",
  props: {
    tableHeaders: Array,
    tableItems: Array,
  },

  data: () => ({
    search: "",
    page: 1,
    pageCount: 0,
    itemsPerPage: 10,
    options: {},
    buf: null,
  }),

  watch: {
    options: {
      handler(newm, old) {
        if (old.sortBy != undefined)
          if (newm.sortBy[0] != old.sortBy[0])
            this.$emit("get-chart", newm.sortBy[0]);
      },
      deep: true,
    },
  },

  methods: {
    formate: formatedDateTime,
  },
};
</script>