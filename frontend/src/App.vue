<template>
 <div id='app'>
 <Menubar :model="items" v-bind:style="{ color: black, fontSize: '25'+ 'px' }">
 <template #start>
        <h3> WBD</h3>
    </template>
    <template #end>
        <InputText placeholder="Search" type="text" />
        
    </template>
    </Menubar>
      <router-view/>

{{ token }}
</div>
</template>
<script>
import { useWindowSize } from 'vue-window-size';


export default {
  name: 'App',
  components: {
    
   

  },
  data(){
    return{
      success: null,
    
      width_window:0,
      token:'',
      visibleLeft: false,
      items: [
                {label: 'Signup', icon: 'pi pi-fw pi-user-plus', to: '/'},
                {label: 'Login', icon: 'pi pi-fw pi-sign-in', to: '/Login'},
                
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
  },
  mounted(){
    this.token=this.$store.getters.gettoken;
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
  margin-top: 60px;
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
</style>
