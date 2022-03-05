<template>
    <ul id="card-carousel">
        <li class='card-frame' v-for="cardEntityIndex in this.lengthOfGenericData" :key="cardEntityIndex">
            <CongratulationFrame :main_context="this.cardsGenericData[cardEntityIndex]" :signature="this.cardsGenericData[cardEntityIndex]"/>
        </li>
    </ul>
  

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CongratulationFrame from "@/components/CongratulationFrame.vue";
const cards_generic_data = [{main_content: 'Здесь могла быть ваша ', signature: "Абоба"},
                            {main_content: 'Здесь тоже', signature: "генерал Гавс"},
                            {main_content: 'А здесь?', signature: "ФФФФ"}]



export default defineComponent({
    name: 'FrameCarousel',
    props: {},
    components: {
        CongratulationFrame
    },
    data () {
        return{
            cardsGenericData: cards_generic_data,
            lengthOfGenericData: cards_generic_data.length}
    }
});
</script>

<style>

ul#card-carousel {
  height: 100vw;
  display: flex;
  justify-content: center;
  overflow: hidden;
  transform-style: preserve-3d;
  perspective: 30vw;
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
    translateX(calc(-30vw * var(--r)));
    /* filter: drop-shadow(0 0 100px rgba(255, 255, 255, 0.25)); */
    z-index: calc((var(--position) - var(--abs)));
} 

@media screen and (orientation: portrait ) {
    ul#card-carousel {
        padding: 25%;
        display: block;
    }

    li.card-frame {
        position: absolute;
        --r: calc(var(--position) - var(--offset));
        --abs: max(calc(var(--r) * -1), var(--r));
        transition: all 0.25s linear;
        transform: rotateX(calc(10deg * var(--r)))
            translateY(calc(-30vw * var(--r)));
        z-index: calc((var(--position) - var(--abs)));
    } 
}
</style>