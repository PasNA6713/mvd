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
        meta: { theme: '#55884F' }
      },
      {
        path: '/home',
        component: () => import('../views/Main/Home.vue'),
        name: 'home',
        meta: { theme: '#544F88' }
      },  
      {
        path: '/parser',
        component: () => import('../views/Main/Social.vue'),
        name: 'parser',
        meta: { theme: '#37889A' }
      },  
      {
        path: '/docs',
        component: () => import('../views/Main/Docs.vue'),
        name: 'docs',
        meta: { theme: '#374D9A' }
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
