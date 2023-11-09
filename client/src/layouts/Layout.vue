<script>
import {useMediaQueries} from "../composables/useMediaQueries.js";

import DesktopLayout from "./DesktopLayout.vue";
import MobileLayout from "./MobileLayout.vue";


export default {
  name: "Layout",
  components: {
    DesktopLayout,
    MobileLayout
  },
  setup() {
    const {isDesktop} = useMediaQueries()

    return {
      isDesktop
    }
  }
}
</script>

<template>
<div>
  <DesktopLayout v-if="isDesktop" />
  <MobileLayout v-else/>
</div>
</template>

<style scoped>

</style>