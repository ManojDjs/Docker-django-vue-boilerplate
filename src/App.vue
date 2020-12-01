<template>
 <div class="p-d-flex p-flex-column" style="height:150px" id='app'>
      <div>
          <div class="p-d-flex p-p-3 card p-shadow-5" v-if='token' style="height:80px; background-color:#ECF0F1;position:fixed;width:100% ">
          <Button type="Button" label='WBD' class="p-mr-2 p-button-success p-shadow-5" icon='pi pi-heart'/>
          
          <Button type='Button' icon="pi pi-sliders-h" @click="visibleLeft = true" class="p-mr-2 p-d-inline p-shadow-5 p-button-success" />
          <Button type="Button" icon="pi pi-sign-out" label="Logout" v-on:click='logout'  class="p-ml-auto p-button-danger p-shadow-5"/>
        </div>




        <div class="p-d-flex p-p-3 card p-shadow-5" v-else style="height:80px; background-color:#ECF0F1;position:fixed;width:100%,">
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

   <div v-bind:style="style" class="p-shadow-20" style="height:100%">
       <Panel>
      <router-view></router-view>
       </Panel>
   </div>
  


</div>
</template>
<script>
import { useWindowSize } from 'vue-window-size';
import { mapState } from 'vuex';

export default {
  name: 'App',
  components: {
  },
  data(){
    return{
      success: null,
      padding:null,
      visibleLeft: false,
      
      width_window:0,

      
      iitems:null,
      items: [
                {label: 'Signup', icon: 'pi pi-fw pi-user-plus', to: '/'},
                {label: 'Login', icon: 'pi pi-fw pi-sign-in', to: '/Login'},
                
            ],
      loggeditems:[
        {label: 'Initia-QA', icon: 'pi pi-fw pi-user-plus',class:"p-button-success", to: '/Dashboard'},
        {label: 'Analysis', icon: 'pi pi-fw pi-chart-line',class:"p-button-success", to: '/About'},

      ]
  }
  },
  setup() {
    const { width, height } = useWindowSize();
    return {
      windowWidth: width, 
      windowHeight: height,
    };
  },
  created(){
    const { width } = useWindowSize();
    this.width_window=width;
    if(this.width_window<950){
         this.padding=100
       }
      else if(this.width_window>1400){
        this.padding=120
      }
       else{
         this.padding=120
       }
     

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
  mounted(){

    
    
  },
  computed:{
    ...mapState([
      'token',
      'user'
    ]),
    style(){
      return{
      "padding-top":this.padding+'px'
    }
    }
  },
  watch:{
     windowWidth(){
       if(this.windowWidth<950){
         this.padding=100
       }
      else if(this.windowWidth>1400){
        this.padding=100
      }
       else{
         this.padding=120
       }
     }
    },
  

  
}
</script>

<style lang="scss">

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center; 
  // background-color: #263539;

}
</style>
