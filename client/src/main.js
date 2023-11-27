import {createApp} from 'vue'
import './index.css'
import App from './App.vue'
import {createRouter, createWebHistory} from 'vue-router';
import Home from './components/Home.vue';
import Communities from "./components/Communities.vue";
import Maps from "./components/Maps.vue";
import Profile from "./components/Profile.vue";
import Layout from "./layouts/Layout.vue";
import vuetify from "../plugins/vuetify.js";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Layout,
      children: [
        {path: '', component: Home},
        {path: 'communities', component: Communities},
        {path: 'maps', component: Maps},
        {path: 'profile', component: Profile}
      ]
    }
  ]
})


createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
