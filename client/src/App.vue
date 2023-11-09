<template>
  <div id="app">
    <router-view></router-view>
  </div>
  <div v-for="user in users">
    <div class="user">
      <p>{{ getFullDataOfUser(user) }}</p>
    </div>
  </div>

</template>

<script>

import axios from "axios";

export default {
  name: 'App',
  data() {
    return {
      users: []
    }
  },
  components: {},
  created() {
    axios.get("http://localhost:3000/users")
        .then(response => {
          this.users = response.data
        })
  },
  methods: {
    getFullDataOfUser(user) {
      return `${user.name} - ${user['date-of-birth']} - ${user.sex}`
    }
  }
}
</script>


<style scoped>
.user {
  margin: 15px;
  border: 2px solid teal;
  padding: 10px;

}
</style>
