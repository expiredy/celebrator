<template>
  <div class="home">
      <FrameCarousel/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FrameCarousel from "@/components/FrameCarousel.vue"

export default defineComponent({
  name: 'HomeView',
  components: {
    FrameCarousel,
  },
});
</script>   
