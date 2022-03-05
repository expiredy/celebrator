<template>
  <div class="home">
      <SwipingButton id="left-position" class="swipe-button-holder" :step_value="1"/>
      <FrameCarousel/>
      <SwipingButton id="right-position" class="swipe-button-holder" :step_value="-1"/>
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

<style>
    .swipe-button-holder {
        position: absolute;
        z-index: 10001;
        border: none;        
    }

    #left-position{
        top: 0;
        left: 0;
    }

    #right-position{
        top: 0;
        left: 86%;
        right: 0;
    }

    @media screen and (orientation: portrait){
        #left-position{
            top: 0;
            left: 0;
            bottom: 95%;
            padding: 0;
            margin: 0;
        }
        #right-position{
            left: 0;
            right: 0;
            top: 95%;
            bottom: 5%;
        }
    }

</style>
