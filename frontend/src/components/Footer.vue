<template>
  <footer>
    <div class="common-spacer"></div>
    <div class="footer"
    :class="{ 'theme1': themes.isTheme1, 'theme2': themes.isTheme2, 'theme3': themes.isTheme3 }" 
    > © 2021 MozhaykaTeam</div>
  </footer>
</template>

<style lang="scss" scoped>
@import '@/styles/common.scss';
@import '@/styles/components/footer.scss';
</style>

<script>
export default {
  name: "Footer",
  data() {
    return {
      color: '#55884F' 
    }
  },
  
  computed: {
    themes(){
      let route = this.$route.name
      let themes = { isTheme1: false, isTheme2: false, isTheme3: false }

      if (route == "home") {
        themes.isTheme1 = true
        themes.isTheme2 = false
        themes.isTheme3 = false
      } else if (route == "stat") {
        themes.isTheme1 = false
        themes.isTheme2 = true
        themes.isTheme3 = false
      }
      return themes
    }
  }
}
</script>