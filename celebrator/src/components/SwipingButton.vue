<template>
    <div>
        <button type="button" class="swipe-button" @click="swipeCards()"><img src="@/assets/logo.png"></button>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';


function swipeCards()
{
    const cards_carousel = document.getElementById("card-carousel");
    var new_position: Number = (+cards_carousel.style.getPropertyValue("--position")) + this.step_value
    if (cards_carousel !== null && (1 <= new_position) && (new_position <= 6) ){
        cards_carousel.style.setProperty("--position",  ""+new_position);
    }
    
}

export default defineComponent({    
    name: "SwipingButton",
    props: {step_value: {default: 0, type: Number}},
    components: {},
    methods: {swipeCards}
})
</script>


<style>
    .swipe-button{
        position: fixed;
        height: 99%;
        z-index: 10000;
        width: 7%;
        background-color: rgba(255, 189, 197, 0.2);
        transition: background-color 0.5s ease;
    }

    .swipe-button > img{
        width: 100%;
        height: auto;
        transition: 0.5s ease;
    }      

    .swipe-button:hover{
        background-color: rgba(255, 189, 197, 0.8);
    }

    .swipe-button:active > img{
        width: 50%;
        height: auto;
    }

    @media screen and (orientation: portrait ) {
        .swipe-button{
            height: 7%;
            width: 100%;
        }
        
        .swipe-button > img{
            height: 100%;
            width: auto;
        }

        .swipe-button:active > img{
            height: 50%;
            width: auto;
        }
    }
</style>