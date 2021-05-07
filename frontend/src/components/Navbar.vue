<template>
  <nav class="navbar" 
  :class="{ 'theme1': themes.isTheme1, 'theme2': themes.isTheme2, 'theme3': themes.isTheme3, 'theme4': themes.isTheme4 }">  
    <v-row class='navbar__row'>
      <router-link :to="{name: 'home'}" class='navbar__row__btn'>Главная</router-link>
      <router-link :to="{name: 'stat'}" class='navbar__row__btn'>Статистика</router-link>
      <router-link :to="{name: 'parser'}" class='navbar__row__btn'>Сбор данных</router-link>
      <router-link :to="{name: 'about'}" class='navbar__row__btn'>О проекте</router-link>
    </v-row>
    <p class="navbar__text">Исправить может только такое средство, которое заставит виновного осознать, что он поступил плохо, что надо жить и поступать иначе. Розга же действует лишь короткое время; когда дети подрастают и перестают бояться ее, вместе с ней исчезает и совесть</p>
    <p class="navbar__text-author">(Феликс Эдмундович Дзержинский)</p>
  </nav>
</template>

<style scoped lang="scss">
@import '@/styles/components/navbar.scss';
@import '@/styles/common.scss';
</style>

<script>
export default {
  name: 'Navbar',
  data: () => ({
    color: '#55884F'
  }),
  
  computed: {
    themes(){
      let route = this.$route.name
      let themes = { isTheme1: false, isTheme2: false, isTheme3: false }

      if (route == "home") {
        themes.isTheme1 = true
        themes.isTheme2 = false
        themes.isTheme3 = false
        themes.isTheme4 = false
      } else if (route == "stat") {
        themes.isTheme1 = false
        themes.isTheme2 = true
        themes.isTheme3 = false
        themes.isTheme4 = false
      } else if (route == "about") {
        themes.isTheme1 = false
        themes.isTheme2 = false
        themes.isTheme3 = true
        themes.isTheme4 = false
      } else if (route == "parser") {
        themes.isTheme1 = false
        themes.isTheme2 = false
        themes.isTheme3 = false
        themes.isTheme4 = true
      }
      return themes
    }
  }
}
</script>