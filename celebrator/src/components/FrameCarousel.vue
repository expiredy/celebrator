<template>
    <ul id="card-carousel">
        <li class='card-frame' v-for="cardEntityIndex in this.lengthOfGenericData" :key="cardEntityIndex">
            <CongratulationFrame :offset_index="cardEntityIndex" :main_context="this.cardsGenericData[cardEntityIndex]" :signature="this.cardsGenericData[cardEntityIndex]"/>
        </li>
    </ul>
  

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CongratulationFrame from "@/components/CongratulationFrame.vue";
const start_position = 1;

const cards_generic_data = [{main_content: 'Здесь могла быть ваша ', signature: "Абоба"},
                            {main_content: 'Здесь тоже', signature: "генерал Гавс"},
                            {main_content: 'А здесь?', signature: "ФФФФ"}]
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
    height: 50vw;
    display: flex;
    justify-content: center;
    overflow: hidden;
    transform-style: preserve-3d;
    perspective: 30vw;
    list-style-type: none;
}

li.card-frame {
    position: absolute;
    --r: calc(var(--position) - var(--offset));
    --abs: max(calc(var(--r) * -1), var(--r));
    transition: all 0.25s linear;
    transform: rotateY(calc(-10deg * var(--r)))
    translateX(calc(-30vw * var(--r)));
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
        --r: calc(var(--position) - var(--offset));
        --abs: max(calc(var(--r) * -1), var(--r));
        transition: all 0.25s linear;
        transform: rotateX(calc(10deg * var(--r)))
            translateY(calc(-30vw * var(--r)));
        z-index: calc((var(--position) - var(--abs)));
    } 
}
</style>