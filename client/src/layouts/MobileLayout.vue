<template>
  <div class="app">
    <header style="display: flex;  justify-content: space-between">
      <div>SportBuddy</div>
      <div class="profile-additions">
        <div>+ friends</div>
        <div>new post</div>
        <div>notifications</div>
      </div>
    </header>

    <nav>
      <div class="navigation">
        <router-link to="/">Home</router-link>
        <router-link to="/maps">Maps</router-link>
        <router-link to="/communities">Communities</router-link>
        <router-link to="/profile">Profile</router-link>
      </div>

    </nav>

    <!-- Основное содержимое -->
    <main>
      <RouterView/>
    </main>

    <!-- Подвал приложения -->
    <footer>
      <p>© 2023 My App</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'MobileLayout'
}
</script>

<style>


.profile-additions {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  gap: 20px;
}

.navigation {
  border-top: 1px solid #d7ffff;
  padding: 10px;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #014646;
  z-index: 2;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-self: flex-end;
}
@media (min-width: 768px) {
  .navigation {

  }
}
</style>
