<template>
    <article class="card" ref="main">
        <div class="content">
            <img :src="logo_url" @error="this.src='@/assets/plag.jpg'" alt="logo"/> 
            <p>{{main_content}}</p>
            <a :href="signature_url">{{signature}}</a>
        </div>
    </article>
</template>

<script lang="ts">
import { defineComponent, handleError } from 'vue';


const THRESHOLD = 15;
const ORIENTATION_LIMIT = 45;


function startSystem (card: any, motion_match_media: MediaQueryList, offset_index: string) {


    function resetStyles(event: any) {
        if (card){
            card.style.transform = '';
        }
    }

    
    function handleHover(event: any) {
        var { clientX, clientY, currentTarget } = event;
        const { clientWidth, clientHeight, offsetLeft, offsetTop } = currentTarget;

        var horizontal = (clientX - offsetLeft) / clientWidth;
        var vertical = (clientY - offsetTop) / clientHeight;
        var rotateX = (THRESHOLD / 2 - horizontal * THRESHOLD).toFixed(1);
        var rotateY = (vertical * THRESHOLD - THRESHOLD / 2).toFixed();

        if (card){
            card.style.transform = 'perspective(' + clientWidth + 'px) rotateX(' + rotateY + 'deg) rotateY(' + rotateX + 'deg) scale3d(1, 1, 1)';
        }else{
            resetStyles(event);
        }
    }

    // function handelGyroscopeChanges(event: any) {
    //     this.gyroscope_y = event.beta;
    //     this.gyroscope_x = event.gamma;
    // }

    if (!motion_match_media.matches) {
        card.addEventListener("mousemove", handleHover);
        card.addEventListener("mouseleave", resetStyles);
        // window.addEventListener("deviceorientation", handelGyroscopeChanges);
    }   
}

export default defineComponent({
    name: 'CongratulationFrame',       
    data( ) {
        return {
            gyroscope_y: 0,
            gyroscope_x: 0,
            gyroscope_z: 0
        }
    },

    props: {offset_index: {default: "1", type: String},
            main_content: {default: "Здесь могла быть ваша реклама", type: String},
            signature: {default: 'Вдохновитель', type: String},
            signature_url: {default: 'https://t.me/expiredy', type: String},
            logo_url: {default: "@/assets/plag.jpg", type: String}},    

    mounted() {
        var card: any = this.$refs.main;
        var motion_match_media = window.matchMedia("(prefers-reduced-motion)");
        card.parentElement.style.setProperty("--offset", this.offset_index);
        startSystem(card.parentElement, motion_match_media, this.offset_index);
    }

});
</script>


<style>

body {
    font-family: Arial, Helvetica, sans-serif;
}


.card {
    margin: 10%;
    height: 10%;
    position: relative;
    color: #E6B98B;
    background-color: #13083D;
    transition: transform 0.1s ease;
    padding: 3vw 3vw 3vw 3vw;
    transform-style: preserve-3d;
    will-change: transform;
    }

.card::before {    
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

.content a{
    color: #E6B98B;
}

/* .content img {
    width: 30%;
    height: 30%;
} */

</style>