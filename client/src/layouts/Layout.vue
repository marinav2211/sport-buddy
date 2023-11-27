<script>
import { useMediaQueries } from '../composables/useMediaQueries.js'
import DesktopLayout from './DesktopLayout.vue'
import MobileLayout from './MobileLayout.vue'
import NavigationBar from '../components/NovigationBar.vue'

export default {
  name: 'Layout',
  components: {
    DesktopLayout,
    MobileLayout,
    NavigationBar,
  },
  setup() {
    const { isDesktop } = useMediaQueries()
    return {
      isDesktop,
    }
  },
}
</script>

<template>
  <div class="h-[100vh] layout">
    <NavigationBar />
    <DesktopLayout v-if="isDesktop" />
    <MobileLayout v-else />
  </div>
</template>

<style scoped>
.layout {
  background-color: #014646;
}
</style>
