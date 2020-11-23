<template>
<div>
    <router-view/>
    



</div><div class="p-m-2 p-p-20">
      <Toast position="top-right" />
       
        <div class="p-grid">
         
            <div class="box p-mx-auto p-p-auto">
            <div class="p-fluid">
                
            <Fieldset legend="Logout" :toggleable="true">
               <h1>Are you sure want to Logout</h1>
               <Button type="submit"  style="width:10rem" v-on:click='logout' label="Logout" icon="pi pi-lock-open" iconPos="right" class="p-button-lg" />
            </Fieldset>
            
            </div>
            
                </div>
        </div>
</div>
  
</template>
<script>
// import axios from 'axios'
export default {


data: () => ({
  
 
}),
methods:{
    logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/Login')
        })
      }
  

},
}
</script>
<style scoped>
.p-grid{
  padding-top: 0.5in;
}
</style>