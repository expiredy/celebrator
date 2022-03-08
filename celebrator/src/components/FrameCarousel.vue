<template>
    <ul id="card-carousel">
        <li class='card-frame' v-for="cardEntityIndex in this.lengthOfGenericData" :key="cardEntityIndex">
                <h1>{{typeof  this.cardsGenericData[cardEntityIndex]}}</h1>
                <h2>{{this.cardsGenericData[cardEntityIndex]}}</h2>
                <CongratulationFrame :offset_index="cardEntityIndex" main_context="{{this.cardsGenericData[cardEntityIndex]}}" signature="{{this.cardsGenericData[cardEntityIndex]}}"/>
        </li>
    </ul>
  

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CongratulationFrame from "@/components/CongratulationFrame.vue";
const start_position = 1;

const cards_generic_data = [{main_context: "Здесь могла быть ваша", signature: "Абоба"},
                            {main_context: "Здесь тоже", signature: "генерал Гавс"},
                            {main_context: "А здесь?", signature: "ФФФФ"}]

const generic_data_length = cards_generic_data.length;



export default defineComponent({
    name: 'FrameCarousel',
    props: {},
    components: {
        CongratulationFrame
    },
    data () {
        return{
            cardsGenericData: cards_generic_data,
            lengthOfGenericData: generic_data_length}
    },
    mounted(){
        var styling_object = document!.getElementById("card-carousel");
        if (styling_object){
            styling_object.style.setProperty("--card-frame", ""+generic_data_length);
            styling_object.style.setProperty("--position", ""+start_position)
        }
    }
});
</script>

<style>

ul#card-carousel {
    height: 100vw;
    width: auto;
    display: flex;
    justify-content: center;
    overflow: hidden;
    transform-style: preserve-3d;
    perspective: 30vw;
    list-style-type: none;
}

li.card-frame {
    position: absolute;
    --radius: calc(var(--position) - var(--offset));
    --abs: max(calc(var(--radius) * -1), var(--radius));
    transition: all 0.25s linear;
    transform: rotateY(calc(-10deg * var(--radius)))
    translateX(calc(-30vw * var(--radius)));
    filter: drop-shadow(0 0 2vw rgba(7, 7, 7, 0.25));
    z-index: calc((var(--position) - var(--abs)));
} 


@media screen and (orientation: portrait ) {
    ul#card-carousel {
        padding: 25%;
        display: block;
    }

    li.card-frame {
        position: absolute;
        --radius: calc(var(--position) - var(--offset));
        --abs: max(calc(var(--radius) * -1), var(--radius));
        transition: all 0.35s linear;
        transform: rotateX(calc(10deg * var(--radius)))
            translateY(calc(-30vw * var(--radius)));
        z-index: calc((var(--position) - var(--abs)));
    } 
}
</style>