<template>
  <div>
    <SMdialog />
  </div>
</template>


<script>
import SMdialog from "@/components/parser/Parser.vue";

export default {
  name: "Social",
  components: {
    SMdialog,
  },
  data() {
    return {};
  },

  methods: {},
};
</script>


<style lang="scss" scoped>
@import "@/styles/common.scss";
@import "@/styles/views/stat.scss";
</style>
