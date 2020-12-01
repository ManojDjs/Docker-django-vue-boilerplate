<template>
<div class="Dashboard">
    
    <span class="p-buttonset">
    <Button label="IMMUNE_SYS" icon="pi pi-check" v-on:click='activateisq' class="p-button-lg p-button-success"/>
    <Button label="QBD" icon="pi pi-check" v-on:click='activateqbd' class="p-button-lg p-button-success"/>
    <Button label="MW" icon="pi pi-check" v-on:click='activatemw' class="p-button-lg p-button-success"/>
</span>
<div v-if='isq'><isq/></div>
<h1 v-if='qbd'>qbd</h1>
<h1 v-if='mw'>mw</h1>
</div>
</template>
<script>
import isq from '@/components/ISQ.vue';
export default {
    components:{
       isq
    },
    data(){
        return{
            isq:true,
            qbd:false,
            mw:false
        }
    },
    methods:{
        activateisq(){
            this.isq=true,
            this.qbd=false,
            this.mw=false
        },
        activateqbd(){
            this.isq=false;
            this.qbd=true;
            this.mw=false
        },
        activatemw(){
            this.isq=false;
            this.qbd=false;
            this.mw=true
        }


    }
}
</script>
<style scoped>

</style>
