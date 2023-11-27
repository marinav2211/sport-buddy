<template>
  <v-layout class="h-full">
    <Header @open-menu="drawer = !drawer" />
    <v-navigation-drawer class="!bg-[#014646]" v-model="drawer" location="left">
      <v-list>
        <router-link :to="item.value" v-for="item in items">
          <v-list-item :value="item.value">{{ item.title }} </v-list-item>
        </router-link>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-layout>
</template>

<script>
import Header from '../components/Header.vue'

export default {
  name: 'DesktopLayout',
  data: () => ({
    drawer: false,
    group: null,
    items: [
      {
        title: 'Home',
        value: '/',
      },
      {
        title: 'Maps',
        value: 'maps',
      },
      {
        title: 'Communities',
        value: 'communities',
      },
      {
        title: 'Profile',
        value: 'profile',
      },
    ],
  }),
  components: {
    Header,
  },
}
</script>

<style scoped></style>
