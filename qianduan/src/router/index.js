import Vue from 'vue'
import Router from 'vue-router'
import reg from '@/components/reg'
import login from '@/components/login'
import addA from '@/components/addA'
import main from '@/components/main'
import showdetails from '@/components/showdetails'
import my from '@/components/MyArticles'
import xiugai from '@/components/xiugai'
import wel from '@/components/wel'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'wel', // 设置路由名称为 'reg'
      component: wel
    },
    {
      path: '/reg',
      name: 'reg',
      component: reg
    },
    {
      path: '/login',
      name: 'login', 
      component: login
    },
    {
      path: '/addA',
      name: 'addA', 
      component: addA
    },
    {
      path: '/main',
      name: 'main', 
      component: main
    },
    {
      path: '/showdetails/:id',
      name: 'showdetails', 
      component: showdetails
    },
    {
      path: '/my',
      name: 'my',
      component: my, // 将新组件添加到路由
    },
    {
      path: '/xiugai/:id',
      name: 'xiugai',
      component: xiugai, // 将新组件添加到路由
    },

  ]
})
