```<template>
    <div class="container">
      <article class="card" ref="main">
        <div class="content"> 
          <h2>The Best Bitches</h2>
          <p>Check out these top 10 beaches this summer.</p>
          <button type="button">Explore</button>
        </div>
      </article>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';


const THRESHOLD = 10;
var card_active: any;

function handleHover(event: any) {
    const { clientX, clientY, currentTarget } = event;
    const { clientWidth, clientHeight, offsetLeft, offsetTop } = currentTarget;

    var horizontal = (clientX - offsetLeft) / clientWidth;
    var vertical = (clientY - offsetTop) / clientHeight;
    var rotateX = (THRESHOLD / 2 - horizontal * THRESHOLD).toFixed(2);
    var rotateY = (vertical * THRESHOLD - THRESHOLD / 2).toFixed(2);

    if (card_active){
        card_active.style.transform = 'perspective(${clientWidth}px) rotateX(${rotateY}deg) rotateY(${rotateX}deg) scale3d(1, 1, 1)';
    }else{
        console.log(card_active);
    }
}

function resetStyles(event: any) {
  if (card_active){
    card_active.style.transform = 'perspective(${event.currentTarget.clientWidth}px) rotateX(0deg) rotateY(0deg)';
  }
}
function startSystem (card: any, motion_match_media: MediaQueryList) {
    if (!motion_match_media.matches) {
        card_active = card;
        card_active.addEventListener("mousemove", handleHover);
        card_active.addEventListener("mouseleave", resetStyles);
    }
}



export default defineComponent({
    name: 'CongratulationFrame',              
    props: {},    
    mounted : function() {
        var card = this.$refs.main;
        var motion_match_media = window.matchMedia("(prefers-reduced-motion)");
        startSystem(card, motion_match_media);
    },

});
</script>


<style>
* {
    box-sizing: border-box;
}

body {
    font-family: Arial, Helvetica, sans-serif;
}

p {
    margin-top: 0;
    font-size: 20px;
}

a {
    text-decoration: none;
}

h2 {
    font-size: 42px;
    margin-bottom: 15px;
}   

button {
    background: #e85757;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    display: block;
    font-size: 18px;
    font-weight: 700;
    padding: 16px;
    width: 120px;
    color: #fff;
}

.card {
    /* background: url("src/card-bg.jpg") no-repeat; */
    background-size: cover;
    max-width: 500px;
    margin: auto;
    height: auto;
    padding: 40px;
    position: relative;
    color: #fff;
    transition: transform 0.1s ease;
    transform-style: preserve-3d;
    will-change: transform;
    }

.card::before {    content: "";
    background: rgba(0, 0, 0, 0.4);
    position: absolute;
    height: 100%;
    width: 100%;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
}

/* Slight parallax effect on hover */
.card:hover .content {
    transform: translateZ(12px);
}

.content {
    position: relative;
    z-index: 1;
    transition: transform 0.3s ease;
}

/* Demo only */
.container {
    margin-top: 100px;
}

.photo-cred {
    position: absolute;
    bottom: 20px;
    right: 20px;
}

</style>