<template>
    <article class="card" ref="main">
        <div class="content"> 
            <h2>{{main_content}}</h2>
            <p>{{signature}}</p>
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
        var rotateX = (THRESHOLD / 2 - horizontal * THRESHOLD).toFixed(1);
        var rotateY = (vertical * THRESHOLD - THRESHOLD / 2).toFixed();

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
        card.addEventListener("mouseleave", resetStyles);
    }   
}

export default defineComponent({
    name: 'CongratulationFrame',              
    props: {offset_index: {default: 1, type: Number},
            main_content: {default: 'Здесь могла быть ваша реклама', type: String},
            signature: {default: 'Вдохновитель', type: String}},    

    started(){
    },
    
    mounted() {
        
        var card: any = this.$refs.main;
        var motion_match_media = window.matchMedia("(prefers-reduced-motion)");
        card.parentElement.style.setProperty("--offset", this.offset_index);
        startSystem(card.parentElement, motion_match_media);
    }

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