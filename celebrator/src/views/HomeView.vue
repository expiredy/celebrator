<template>
  <div class="home">
      <SwipingButton coefficient="1"/>
      <FrameCarousel/>
      <SwipingButton coefficient="-1"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FrameCarousel from "@/components/FrameCarousel.vue";
import SwipingButton from "@/components/SwipingButton.vue";

export default defineComponent({
  name: 'HomeView',
  components: {
    FrameCarousel,
    SwipingButton
  },
});
</script>   
