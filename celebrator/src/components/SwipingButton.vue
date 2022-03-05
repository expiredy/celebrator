<template>
    <div>
        <button type="button" class="swipe-button"><img src="@/assets/logo.png"></button>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';

const all_cards = document.getElementsByClassName("card-frame");

// li.card-frame:nth-of-type(1) {
//   --offset: 1;
// }
// li.card-frame:nth-of-type(2) {
//   --offset: 2;
// }
// li.card-frame:nth-of-type(3) {
//   --offset: 3;
// }
// li.card-frame:nth-of-type(4) {
//   --offset: 4;
// }
// li.card-frame:nth-of-type(5) {
//   --offset: 5;
// } 


function swipeCards()
{
    for(let card_entity in all_cards){
        // card_entity.style.offset = card_entity.style.offset 
    }
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
        height: 100%;
        z-index: 10000;
        width: 7%;
        background-color: rgba(255, 189, 197, 0.6);
        transition: background-color 0.5s ease;
    }

    .swipe-button > img{
        width: auto;
        height: auto;
    }      

    .swipe-button:hover{
            background: rgba(255, 189, 197, 0.8);
        }

    @media screen and (orientation: portrait ) {
        .swipe-button{
            height: 7%;
            width: 100%;
        }
    }
</style>