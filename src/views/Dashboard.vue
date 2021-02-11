<template>
<div class="p-grid" >
<div class="p-col-12 p-md-6 p-lg-6">
      <img src="@/assets/Dash.jpeg" style="width:60%; display: block;" id="image" class="p-mr-2"/>
</div>
<div class="p-col-12 p-md-6 p-lg-6">
                        <Card  v-if="status=='N'" class="p-mt-4 p-p-3">
                            <template #title>
                            Welcome to the Qigong Practice Research Online Platform
                            </template>
                            <template #content>
                            <h3>Now that you have created your Volunteer Account,
                            your first step is to give us some information about
                            yourself.</h3>
                            <Divider/>
                            <h3>Remember, the information you give is completely
                            confidential, and has been ethically approved
                            (Northumbria University ethics form number 23709)..</h3>
                             <Divider/>
                            <h3>Please press continue to go to the Demographic
                                    Information section</h3>
                                    <Divider/>
                            </template>
                            <template #footer>
                            <Button icon="pi pi-check" label="Continue" v-on:click="register_system" style="width:100%"/>
                            
                            </template>
                        </Card>
                        <Card  v-if="status=='R'" class="p-mt-4">
                                <template #title>
                                Welcome Back Mr/Miss {{ user_in }}
                                </template>
                                <template #content>
                                Hello, {{ user_in }}, welcome to the system. please click below button to start the courses and Base line questionnaire!
                                </template>
                                <template #footer>
                                    <Button icon="pi pi-check" label="Start" v-on:click="to_videos" style="width:100%"/>
                                
                                </template>
                        </Card>

</div>
</div>
</template>
<script>
import { mapState } from 'vuex'
import axios from 'axios'
import Json from "@/assets/endpoints.json"
export default {
    
    data(){
        return{
            server:Json[0]['Course']['SERVER'],
            register_status:Json[0]['Course']['REGISTEREDSTATUS'],
            register:Json[0]['Course']['REGISTERED'],
            check:[],
            status:'',
            path:"",
            
            user_in:''

        }
    },
    computed:{
    ...mapState([
      'token',
      'user',
      'heading',
      'height',
      
    ])
      },
      methods:{
          check_registered(){
               const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.get(this.server+this.register_status,{'headers':headers}
            ).then(resp=>{
                console.log(resp.data)
                console.log(resp.status)
                if(resp.status==200){
                    console.log(resp.data.length)
                    if(resp.data.length!=0){
                        this.status="R"
                        
                    }
                    if(resp.data.length==0){
                        this.status="N"
                        
                    }

                
                }
                })
          },
          to_videos(){
           this.$router.push('/Videos')
          },
          register_system(){
              const headers={
                'Authorization': 'Token'+' '+this.token
                    }
             axios.post(this.server+this.register,
              {"user":this.user,
                  
              },
              {'headers':headers})
            .then(resp => {
                    if(resp.status==201){
                        this.$$router.push('/Demo')             
                    }
                   })

          },
          get_user(){
              this.user_in=this.user
          },
          taketocourse(name){
              console.log(name)
              this.$store.dispatch('set_course',name)
              this.$router.push('/Course')
          },
      },
      created(){
        this.get_user()
        this.check_registered()
    }

}
</script>
<style scoped>
.div{
text-align:center
}
.Dash{
    text-align: center;
}
#image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
#mark{
	padding-top:30px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
}
</style>