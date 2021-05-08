<template>
  <div class="mb-6">
    <v-toolbar dark :style="'background: ' + $route.meta.theme">
      <v-tabs fixed-tabs>
        <v-tab :to="{ name: 'home' }"> Карта </v-tab>
        <v-tab :to="{ name: 'stat' }"> Общая статистика </v-tab>
        <v-tab :to="{ name: 'docs' }"> Документы </v-tab>
        <v-tab :to="{ name: 'parser' }"> Сбор данных </v-tab>
      </v-tabs>
    </v-toolbar>

    <div
      class="color-row"
      :style="'background: ' + $route.meta.theme"
    ></div>
  </div>
</template>


<script>
export default {
  name: "Navbar",
};
</script>


<style scoped lang="scss">
.color-row {
  height: 400px;
  width: 100%;
  position: absolute;
}
</style>