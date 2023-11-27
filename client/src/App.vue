<template>
  <VApp theme="dark" >
    <div id="app">
      <router-view></router-view>
    </div>
  </VApp>
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
