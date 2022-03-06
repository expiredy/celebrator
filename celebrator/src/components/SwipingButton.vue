<template>
    <div>
        <button type="button" class="swipe-button" :on-click="swipeCards"><img src="@/assets/logo.png"></button>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';

const cards_carousel = document.getElementById("card-carousel");

function swipeCards()
{

}

export default defineComponent({    
    name: "SwipingButton",
    props: {step_value: {default: 0, type: Number}},
    components: {},
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
        width: 10%;
        height: auto;
    }

    @media screen and (orientation: portrait ) {
        .swipe-button{
            height: 7%;
            width: 100%;
        }
        
        .swipe-button > img{
            
        }
    }
</style>