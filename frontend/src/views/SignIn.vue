<template>
  <div>
    <v-row class="sign-in">
      <v-col cols="6" class="sign-in__column">
        <v-card class="sign-in-form">
          <p class="sign-in-form__text">Авторизация</p>
          <v-text-field
            v-model="username"
            label="Имя пользователя"
            type="username"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Пароль"
            type="password"
            required
          ></v-text-field>

          <v-btn
            color="#27646A"
            style="color: white"
            @click="signIn"
            class="sign-in-form__button"
            block
            large
          >
            Войти
          </v-btn>
          <br>
          <v-alert
            type="warning"
            v-if="isFalseLogin"
            color="#ff0000"
          >Некорректно введены данные!</v-alert>
        </v-card>
      </v-col> 

      <v-col cols="6" class="sign-in-form__image">
      </v-col>
    </v-row>
  </div>
</template>

<script>
  export default {
    data: () => ({
      isFalseLogin: false,
      password: "",
      username: ""
    }),
    
    methods: {
      async signIn() {
        try {
          await axios.post(`${this.$store.state.backendUrl}/auth/token/login/`, 
          {
              'Content-Type': 'application/json',
              'username': this.username,
              'password': this.password
          }
        ).then(response => {
              this.$store.dispatch('setToken', response.data.auth_token) 
              this.$router.push({ name: 'home' })
          })
        } catch (Error) {
          this.isFalseLogin = true
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
@import '@/styles/common.scss';
@import '@/styles/views/signIn.scss';
</style>