<template>
    <ul id="card-carousel">
        <li class='card-frame' v-for="cardEntityIndex in cardsGenericData.length" :key="cardEntityIndex">
            <CongratulationFrame main_content={{cardsGenericData[cardEntityIndex].main_content}} />
        </li>
    </ul>
  

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CongratulationFrame from "@/components/CongratulationFrame.vue";

export default defineComponent({
    name: 'FrameCarousel',
    props: {},
    components: {
        CongratulationFrame
    },
    data () {
        return{
            cardsGenericData: [{main_context: 'Здесь могла быть ваша реклама'}, {main_context: 'Здесь тоже'}, {main_context: 'А здесь?'} ]}
    }
});
</script>

<style>

ul#card-carousel {
  height: 50vw;
  display: flex;
  justify-content: center;
  overflow: hidden;
  transform-style: preserve-3d;
  perspective: 400px;
  --card-frames: 5;
  --middle: 3;
  --position: 1;
  list-style-type: none;
}
 
li.card-frame {
  position: absolute;
  --r: calc(var(--position) - var(--offset));
  --abs: max(calc(var(--r) * -1), var(--r));
  transition: all 0.25s linear;
  transform: rotateY(calc(-10deg * var(--r)))
    translateX(calc(-300px * var(--r)));
  z-index: calc((var(--position) - var(--abs)));
} 

li.card-frame:nth-of-type(1) {
  --offset: 1;
}
li.card-frame:nth-of-type(2) {
  --offset: 2;
}
li.card-frame:nth-of-type(3) {
  --offset: 3;
}
li.card-frame:nth-of-type(4) {
  --offset: 4;
}
li.card-frame:nth-of-type(5) {
  --offset: 5;
} 


@media screen and (orientation: portrait ) {
    ul#card-carousel {
      display: block;
    }
}
</style>