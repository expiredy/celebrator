<template>
    <ul id="example-1">
        <li v-for="card_entity in cardGenericData" :key="card_entity.main_content">
            <CongratulationFrame/>{{ item.message }}
        </li>
    </ul>
  

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CongratulationFrame from "@/components/CongratulationFrame.vue"

export default defineComponent({
    name: 'FrameViewHolder',
    props: {},
     components: {
        CongratulationFrame
    },
    data () {
        cardsGenericData: {
            
        }
    }
});
</script>
