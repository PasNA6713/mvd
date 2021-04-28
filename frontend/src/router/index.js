import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    component: () => import('../views/SignIn.vue'),
    name: 'signIn',
  },
  {
    path: '/main',
    component: () => import('../views/Main.vue'),
    name: 'main',
    children: [
      {
        path: '/stat',
        component: () => import('../views/Main/Stat.vue'),
        name: 'stat',
      },
      {
        path: '/home',
        component: () => import('../views/Main/Home.vue'),
        name: 'home', 
      }  
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  linkActiveClass: 'common-is-active',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.name !== 'signIn' && store.state.token == null) next({ name: "signIn" })
  else next()
})

export default router
