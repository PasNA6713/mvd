<template>
  <v-container class="header">
    <img class="header__img-gerb" src="@/assets/images/svg/gerb.svg" />
    <h2 class="header__h2-title">Программный комплекс поддержки принятия решений</h2>
    <h3 class="header__h3-title">Министерство внутренних дел Российской Федерации</h3>

    <div class="header__top-buttons">
      <a class="header__top-buttons__lang">Рус <img src="@/assets/images/svg/lang.svg"/></a>
      <a class="header__top-buttons__version"><img src="@/assets/images/svg/glasses.svg"/></a>
    </div>
  </v-container> 
</template>

<style lang="scss" scoped>
@import '@/styles/components/header.scss';
@import '@/styles/common.scss';
</style>