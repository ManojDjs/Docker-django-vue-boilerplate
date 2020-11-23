<template>
 <div id='app'>
 <Menubar  :model="loggeditems" v-bind:style="{ color:'#00000', fontSize: '25'+ 'px' }" v-if="token">  
 <template #start>
       <h3>WBD</h3>
    </template>
    <template #end v-if='token'>
      <Button label="Logout" v-on:click='logout' icon="pi pi-power-off" :style="{'margin-left': '0 .5em'}"/>
        
    </template>
    </Menubar>
     <Menubar  :model="items" v-bind:style="{ color:'#00000', fontSize: '25'+ 'px' }" v-else>
 <template #start>
       <h3>WBD</h3>
    </template>
    <template #end>
         
        
    </template>
    </Menubar>
      <router-view/>


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
    
      width_window:0,

      visibleLeft: false,
      items: [
                {label: 'Signup', icon: 'pi pi-fw pi-user-plus', to: '/'},
                {label: 'Login', icon: 'pi pi-fw pi-sign-in', to: '/Login'},
                
            ],
      loggeditems:[
        {label: 'My programs', icon: 'pi pi-fw pi-user-plus', to: '/Dashboard'},
        {label: 'Profile', icon: 'pi pi-fw pi-sign-in', to: '/About'},

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
      'token'
    ])
  },
  watch:{

    }

  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 6px;
}
#page{
  padding:1in;
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
  color: black;

}
</style>
