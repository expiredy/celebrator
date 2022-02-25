<template>
  <div class="home">
      <FrameViewHolder/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FrameViewHolder from "@/components/FrameViewHolder.vue"

export default defineComponent({
  name: 'HomeView',
  components: {
    FrameViewHolder,
  },
});
</script>   
