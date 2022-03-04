<template>
    <article class="card" ref="main">
        <div class="content"> 
            <h2>Здесь могла быть ваша реклама</h2>
            <p>Check out these top 10 beaches this summer.</p>
        </div>
    </article>
</template>

<script lang="ts">
import { defineComponent, handleError } from 'vue';


const THRESHOLD = 15;
const ORIENTATION_LIMIT = 45;

function startSystem (card: any, motion_match_media: MediaQueryList) {
    
    function handleHover(event: any) {
        const { clientX, clientY, currentTarget } = event;
        const { clientWidth, clientHeight, offsetLeft, offsetTop } = currentTarget;

        var horizontal = (clientX - offsetLeft) / clientWidth;
        var vertical = (clientY - offsetTop) / clientHeight;
        var rotateX = (THRESHOLD / 2 - horizontal * THRESHOLD).toFixed(2);
        var rotateY = (vertical * THRESHOLD - THRESHOLD / 2).toFixed(2);

        if (card){
            card.style.transform = 'perspective(' + clientWidth + 'px) rotateX(' + rotateY + 'deg) rotateY(' + rotateX + 'deg) scale3d(1, 1, 1)';
        }
    }

    function resetStyles(event: any) {
        if (card){
            card.style.transform = 'perspective(' + event.currentTarget.clientWidth + 'px) rotateX(0deg) rotateY(0deg)';
        }
    }
    
    if (!motion_match_media.matches) {
        card.addEventListener("mousemove", handleHover);
        // card.addEventListener("deviceorientation", function(event: any) {
        //     let position = Math.round(event.gamma);
        //     if (Math.abs(position) > ORIENTATION_LIMIT) {
        //         if (position > ORIENTATION_LIMIT) {
        //                 position = ORIENTATION_LIMIT;
        //             } else {
        //                 position = -ORIENTATION_LIMIT;
        //                 }
        //             }
        //     position = position / -100;
        //     let style = "rotateY(" + position + "deg)";
        //     card.style.transform = style;
        //     });
        card.addEventListener("mouseleave", resetStyles);

    }   
}



export default defineComponent({
    name: 'CongratulationFrame',              
    props: {main_content: {default: 'Здесь могла быть ваша реклама', type: String},
            signature: {default: 'Вдохновитель', type: String}},    

    mounted() {
        var card: any = this.$refs.main;
        var motion_match_media = window.matchMedia("(prefers-reduced-motion)");
        startSystem(card, motion_match_media);
    },

});
</script>


<style>

body {
    font-family: Arial, Helvetica, sans-serif;
}


.card {
    margin: auto;
    height: auto;
    position: relative;
    color: #E6B98B;
    background-color: #13083D;
    transition: transform 0.1s ease;
    padding: 20vw 10vw 20vw 10vw;
    transform-style: preserve-3d;
    will-change: transform;
    }

.card::before {    
    content: "";
    background: rgba(0, 0, 0, 0.4);
    position: absolute;
    height: 100%;
    width: 100%;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
}

.card:hover .content {
    transform: translateZ(12px);
} 

.content {
    position: relative;
    z-index: 1;
    transition: transform 0.3s ease;
}
</style>