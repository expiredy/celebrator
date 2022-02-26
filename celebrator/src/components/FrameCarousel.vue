<template>
    <ul id="card-carousel">
        <li id='card-frame' v-for="cardEntity in cardsGenericData"  :key="cardEntity.main_content">
            <CongratulationFrame main_content=cardEntity />
        </li>
    </ul>
  

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CongratulationFrame from "@/components/CongratulationFrame.vue"

export default defineComponent({
    name: 'FrameCarousel',
    props: {},
     components: {
        CongratulationFrame
    },
    data () {
        return{
            cardsGenericData: [{main_context: 'Здесь могла быть ваша реклама'}, {main_context: 'Здесь тоже'}]}
    }
});
</script>

<style>
    #card-carousel{
        display: inline;
    }

    #card-frame{
        position: flex;
    }
</style>