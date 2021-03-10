<template>
 <div  id='app' :style="fontstyle">

      <div v-if="windowWidth>780">
      <div class="p-d-flex p-p-3 p-shadow-5" v-if='token' style="height:100px;width:100%" id="navbar">
              <!-- <Button type="Button" label='WBD' class="p-mr-2 p-button-primary rounded p-shadow-5" icon='pi pi-heart'/> -->
              <Button type='Button' icon="pi pi-step-forward" @click="visibleLeft = true" class="p-mr-2 p-d-inline p-shadow-5 p-button-primary" />
              <Button type="Button" icon="pi pi-user" label="PROFILE" v-on:click='profile'  class="p-ml-auto p-button-primary p-button-rounded p-shadow-5" v-if='windowWidth>700'/>
              <Button type="Button" icon="pi pi-sign-out" label="Logout" v-on:click='logout'  class="p-ml-auto p-button-danger p-shadow-5"/>
      </div>
      <div class="p-d-flex p-p-3 card p-shadow-5" v-else style="height:100px; background-color:#ECF0F1;width:100%" id="navbar">
        <!-- <Button type="Button" label='WBD' class="p-mr-2 p-button-help p-shadow-9" icon='pi pi-heart'/> -->

           <!-- <Button type="Button" icon="pi pi-sign-in" label="Login" v-on:click='login'  class="p-ml-auto p-button-danger p-shadow-5"/> -->
      </div>

          <Sidebar v-model:visible="visibleLeft"   :baseZIndex="1000" class="p-sidebar-sm">
          <h3>Components</h3>
          
        
            <Fieldset :toggleable="true">
              
            <template #legend>
                INFORMATION
            </template>
              <Button  icon="pi pi-user" label="Profile" v-on:click='profile' style="width:100%" class="p-m-2 p-button-primary p-shadow-25" />
              <Button icon="pi pi-book" label="Demographics"  v-on:click='demo' class="p-button-primary p-m-2 p-shadow-5" style="width:100%"/>
              <Button icon="pi pi-book" label="Dairy"  v-on:click='dashboard' class="p-button-primary p-m-2 p-shadow-5" style="width:100%"/>
              <Button icon="pi pi-video" label="Videos" class="p-button-primary p-m-2 p-shadow-5" style="width:100%" v-on:click='videos'/>
              <Button type="Button" icon="pi pi-sign-out" label="Logout" v-on:click='logout' style="width:100%"  class="p-m-2  p-button-danger p-shadow-5"/>
            </Fieldset>      
          </Sidebar>
           <div class="p-p-5">
    <ScrollPanel :style=style class="custombar1">
    
       <router-view/>
       </ScrollPanel>
  </div>
      </div>
      <div v-else>
        <div class="p-m-3" id='navbtn'>
        <Button type='Button'   icon="pi pi-step-forward" @click="visibleLeft = true" class="p-m-8 p-shadow-25 p-button-primary" style=" height:70px;width:70px;"/>
        </div>
         <Sidebar v-model:visible="visibleLeft"   :baseZIndex="1000" class="p-sidebar-sm">
          <h3>Components</h3>
            <Fieldset :toggleable="true">
              
            <template #legend>
                INFORMATION
            </template>
            <Button  icon="pi pi-user" label="Profile" v-on:click='profile' style="width:100%" class="p-m-2 p-button-primary p-shadow-25" />
            <Button icon="pi pi-book" label="Demographics"  v-on:click='demo' class="p-button-primary p-m-2 p-shadow-5" style="width:100%"/>
              <Button icon="pi pi-book" label="Dairy"  v-on:click='dashboard' class="p-button-primary p-m-2 p-shadow-5" style="width:100%"/>
              <Button icon="pi pi-video" label="Video" class="p-button-primary p-m-2 p-shadow-5" style="width:100%" v-on:click='videos'/>
              <Button type="Button" icon="pi pi-sign-out" label="Logout" v-on:click='logout' style="width:100%"  class="p-m-2  p-button-danger p-shadow-5"/>
           
            </Fieldset>
            
          
          </Sidebar>
          <router-view/>
      </div>
  
</div>
</template>
<script>
import { useWindowSize } from 'vue-window-size';
import { mapState } from 'vuex';
// import Navbar from "@/views/NavBar.vue";

export default {
  name: 'App',
  components: {
    
  },
  data(){
    return{
      success: null,
      padding:null,
      visibleLeft: false,
      listcolors:['orange','Tomato','DodgerBlue','MediumSeaGreen','SlateBlue','Violet'],
      hcolor:'',
      Heading:'',
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
    this.set_color()
  
  },
  methods:{
    
    set_color(){
      this.hcolor=this.listcolors[Math.floor(Math.random() * this.listcolors.length)]
      this.height=this.windowWidth;
      // console.log(this.hcolor)
    },
     logout(){

      this.$router.push('/Logout')
      this.visibleLeft=false;
    },
    profile(){
      this.$router.push('/Profile')
      this.visibleLeft=false;
    },
    videos(){

      this.$router.push('/Videos')
      this.visibleLeft=false;
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
      this.$router.push('/Dairy'),
      this.set_color()
      this.visibleLeft=false;
      
    },
     demo(){
      this.$router.push('/Demo'),
      this.set_color()
      this.visibleLeft=false;
      
    },
    
  },
  mounted(){

    
    
  },
  computed:{
    ...mapState([
      'token',
      'user',
      'heading',
      'height'
    ]),
    style(){
      return{
      // "padding-top":this.padding+'px'
      "width":this.windowWidth-50+'px',
      "height":this.windowHeight-200+'px',
      }
    },
    fontstyle(){
      return{
        "font-size":'20px'
      }
    },
    headingstyle(){

      return{
      "background-color":this.hcolor,
      "border-radius": "5px",
      "padding":"5px",
      "color":"black"
      }
    },
  
    
  },

  watch:{
    
     token(){
       if(this.token==''){
         this.$router.push('/')
       }
       else{
         this.$router.push("/Dashboard")
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
  font-size:20px;
  // background-color: #f0e6eb;

}
html {
    font-size: 16px;
}
::v-deep(.p-scrollpanel) {
    p {
        padding: .5rem;
        line-height: 1.5;
        margin: 0;
    }

    &.custombar1 {
        .p-scrollpanel-wrapper {
            border-right: 9px solid var(--surface-b);
        }

        .p-scrollpanel-bar {
            background-color: var(--primary-color);
            opacity: 1;
            transition: background-color .2s;

            &:hover {
                background-color: #007ad9;
            }
        }
    }

    &.custombar2 {
        .p-scrollpanel-wrapper {
            border-right: 9px solid var(--surface-b);
            border-bottom: 9px solid var(--surface-b);
        }

        .p-scrollpanel-bar {
            background-color: var(--surface-d);
            border-radius: 0;
            opacity: 1;
            transition: background-color .2s;
        }
    }  
}
#navbtn{
position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}
</style>
