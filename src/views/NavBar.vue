<template>
   <div>
          <div class="p-d-flex p-p-3 card p-shadow-5" v-if='token' style="height:80px; background-color:#ECF0F1;width:100% ">
          <Button type="Button" label='WBD' class="p-mr-2 p-button-success p-shadow-5" icon='pi pi-heart'/>
          
          <Button type='Button' icon="pi pi-sliders-h" @click="visibleLeft = true" class="p-mr-2 p-d-inline p-shadow-5 p-button-success" />
          <Button type="Button" icon="pi pi-sign-out" label="Logout" v-on:click='logout'  class="p-ml-auto p-button-danger p-shadow-5"/>
        </div>




        <div class="p-d-flex p-p-3 card p-shadow-5" v-else style="height:80px; background-color:#ECF0F1;width:100%,">
          <Button type="Button" label='WBD' class="p-mr-2 p-button-success p-shadow-9" icon='pi pi-heart'/>
        </div>

          <Sidebar v-model:visible="visibleLeft"   :baseZIndex="1000" class="p-sidebar-sm">
          <h3>Components</h3>
        
            <Fieldset :toggleable="true">
                <template #legend>
                    Initial QA
                </template>
              <Button label="ISQ" class="p-button-secondary p-m-2 p-shadow-5" style="width:100%" v-on:click="i_isq"/>
              <Button label="Well-Being-NU" class="p-button-secondary p-m-2 p-shadow-5" style="width:100%"/>
              <Button label="Mental-Well-Being" class="p-button-secondary p-m-2 p-shadow-5" style="width:100%"/>
            </Fieldset>
            <Fieldset :toggleable="true">
            <template #legend>
                Final QA
            </template>
              <Button label="ISQ" class="p-button-help p-m-2 p-shadow-5" style="width:100%"/>
              <Button label="Well-Being-NU" class="p-button-help p-m-2 p-shadow-5" style="width:100%"/>
              <Button label="Mental-Well-Being" class="p-button-help p-m-2 p-shadow-5" style="width:100%"/>
        </Fieldset>
         
          </Sidebar>
   </div>
</template>
<script>
import { mapState } from 'vuex';
export default {
   data(){
     return{
        visibleLeft: false,
      
     }
   },
    computed:{
    ...mapState([
      'token',
      'user'
    ]),
    },
   methods:{
    logout(){

      this.$router.push('/Logout')
    },
    i_isq(){
      this.$router.push('I_ISQ'),
      this.visibleLeft=false;
    }
    
  },
}

</script>