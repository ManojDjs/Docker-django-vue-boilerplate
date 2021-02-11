<template>
   <div id='navbar'>
         <div class="p-d-flex p-p-3 p-shadow-5" v-if='token' style="height:100px;width:100%" id="navbar">
              <Button type="Button" label='WBD' class="p-mr-2 p-button-primary rounded p-shadow-5" icon='pi pi-heart'/>
              <Button type='Button' icon="pi pi-step-forward" @click="visibleLeft = true" class="p-mr-2 p-d-inline p-shadow-5 p-button-primary" />
              <Button type="Button" icon="pi pi-user" label="PROFILE" v-on:click='profile'  class="p-ml-auto p-button-primary p-button-rounded p-shadow-5" v-if='windowWidth>700'/>
              <Button type="Button" icon="pi pi-sign-out" label="Logout" v-on:click='logout'  class="p-ml-auto p-button-danger p-shadow-5"/>
      </div>
      <div class="p-d-flex p-p-3 card p-shadow-5" v-else style="height:100px; background-color:#ECF0F1;width:100%" id="navbar">
          <Button type="Button" label='WBD' class="p-mr-2 p-button-help p-shadow-9" icon='pi pi-heart'/>

           <Button type="Button" icon="pi pi-sign-in" label="Login" v-on:click='login'  class="p-ml-auto p-button-danger p-shadow-5"/>
      </div>

          <Sidebar v-model:visible="visibleLeft"   :baseZIndex="1000" class="p-sidebar-sm">
          <h3>Components</h3>
          
        
            <Fieldset :toggleable="true">
              
            <template #legend>
                INFORMATION
            </template>
              <Button  icon="pi pi-user" label="PROFILE" v-on:click='profile' style="width:100%" class="p-m-2 p-button-primary p-shadow-25" v-if='windowWidth<700'/>
              <Button label="Demographics"  v-on:click='dashboard' class="p-button-primary p-m-2 p-shadow-5" style="width:100%"/>
              <Button label="Data Insights" class="p-button-primary p-m-2 p-shadow-5" style="width:100%" v-on:click='dv'/>
            
            </Fieldset>
            <Fieldset :toggleable="true">
                <template #legend>
                    Initial QA
                </template>
              <Button label="ISQ" class="p-button-secondary p-m-2 p-shadow-5" style="width:100%" v-on:click="i_isq"/>
              <Button label="Well-Being-NU" class="p-button-secondary p-m-2 p-shadow-5" style="width:100%" v-on:click='i_wbmnu'/>
              <Button label="Mental-Well-Being" class="p-button-secondary p-m-2 p-shadow-5" style="width:100%" v-on:click='i_mwb'/>
            </Fieldset>
            <Fieldset :toggleable="true">
            <template #legend>
                Final QA
            </template>
              <Button label="ISQ" class="p-button-help p-m-2 p-shadow-5" style="width:100%" v-on:click='f_isq'/>
              <Button label="Well-Being-NU" class="p-button-help p-m-2 p-shadow-5" style="width:100%" v-on:click='f_wbmnu'/>
              <Button label="Mental-Well-Being" class="p-button-help p-m-2 p-shadow-5" style="width:100%" v-on:click='f_mwb'/>
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
    profile(){
       this.$router.push('/Profile')
    },
    dv(){

      this.$router.push('/DV')
    },
     login(){

      this.$router.push('/Login')
    },
    i_isq(){
      this.$router.push('I_ISQ'),
       this.set_color()
       this.Heading='Initial Immune System'
      this.visibleLeft=false;
    },
    f_isq(){
      this.$router.push('F_ISQ'),
       this.set_color()
       this.Heading='Final Immune System'
      this.visibleLeft=false;
    },
     i_mwb(){
      this.$router.push('/I_MWB'),
      this.set_color()
      this.Heading='Initial Mental Wellbeing'
      this.visibleLeft=false;
    },
     i_wbmnu(){
      this.$router.push('/I_WBMNU'),
      this.set_color()
      this.Heading='wellbeing model NU',
      this.visibleLeft=false;
    },
      f_mwb(){
      this.$router.push('/F_MWB'),
      this.set_color()
      this.Heading='Initial Mental Wellbeing'
      this.visibleLeft=false;
    },
     f_wbmnu(){
      this.$router.push('/F_WBMNU'),
      this.set_color()
      this.Heading='wellbeing model NU',
      this.visibleLeft=false;
    },
     dashboard(){
      this.$router.push('/Dashboard'),
      this.set_color()
      this.Heading='Demographics'
      this.visibleLeft=false;
    },
    
  },
}

</script>
<style scoped>

#navbar{
position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}
</style>