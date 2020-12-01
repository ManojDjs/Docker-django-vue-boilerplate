<template>
 <div id='app'>
   <div>
 <Menubar class='p-success'  :model="loggeditems" v-bind:style="{ color:'green', fontSize: '25'+ 'px' }" v-if="token">  
 <template #start>
       <h3>WBD</h3>
    </template>
    <template #end v-if='token'>
      <Button label="Logout" v-on:click='logout' icon="pi pi-power-off" :style="{'margin-left': '0 .5em'}"/>
        
    </template>
    </Menubar>
     <Menubar class='p-success'   :model="items" v-bind:style="{ color:'green', fontSize: '25'+ 'px' }" v-else>
 <template #start>
       <h3>WBD</h3>
    </template>
    <template #end>
    </template>
    </Menubar>
   </div>
   <div v-bind:style="{padding:padding+'px'}">
      
      <router-view/>
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
    
      width_window:0,

      visibleLeft: false,
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
         this.padding=10
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
    }
  },
  mounted(){

    
    
  },
  computed:{
    ...mapState([
      'token',
      'user'
    ])
  },
  watch:{
     windowWidth(){
       if(this.windowWidth<950){
         this.padding=10
       }
      else if(this.windowWidth>1400){
        this.padding=160
      }
       else{
         this.padding=120
       }
     }
    },
  

  
}
</script>

<style lang="scss">
$menuBorder: 1px solid #dee2e6;
$menuBg: #ffffff;
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

#tab{
  height: 0.5in;
}
.router-link{
  font-size: 1in;
}
.p-tabmenu{
  align-self: center;
}
.p-tabmenu-nav{
  align-self: center;
}
.p-tabmenuitem
{
  align-self: centre;
  font-size: 1in;
}
.p-menubar{

      position: fixed;
      width:100%;
      z-index: 102;
      

}
</style>
