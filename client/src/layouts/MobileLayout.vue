<template>
  <div class="app">
    <header style="display: flex;  justify-content: space-between">
      <div>SportBuddy</div>
    </header>
    <main>
      <RouterView/>
    </main>

    <footer>
      <p>© 2023 My App</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'MobileLayout',

}
</script>

<style>



@media (max-width: 768px) {
  .iconMenu {
    display: none;
  }
}

@media (max-width: 768px) {
  .menu {
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

}
</style>
