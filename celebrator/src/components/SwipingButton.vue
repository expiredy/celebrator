<template>
    <div>
        <button type="button" class="swipe-button">A</button>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';

function swipeCards()
{
    
}

export default defineComponent({    
    name: "SwipingButton",
    props: {coefficient: {default: "0", type: String}},
    components: {}
})
</script>


<style>
    .swipe-button{
        position: fixed;
        height: 100%;
        z-index: 10;
        width: 100%;
    }
</style>