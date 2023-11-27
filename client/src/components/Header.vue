<template>
  <v-app-bar style="background-color: #012626" rounded>
    <template v-slot:append>
      <v-btn icon="mdi-bell-outline"></v-btn>
      <v-btn icon="mdi-web"></v-btn>
      <v-btn icon="mdi-account-circle"></v-btn>
      <v-btn icon="mdi-cog-outline"></v-btn>
    </template>

    <template v-slot:prepend>
      <v-btn @click="$emit('open-menu')" color="white" icon="mdi-menu"></v-btn>
      <div>SportBuddy</div>
    </template>

    <div class="w-full px-4 flex items-center">
      <v-text-field label="Search" variant="underlined"></v-text-field>
      <v-btn class="m-4">
        <v-icon>mdi-plus</v-icon>
        <span class="">Create</span>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
export default {}
</script>

<style scoped></style>
