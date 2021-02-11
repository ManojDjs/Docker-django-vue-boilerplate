<template>

<div class="Signup">
<Toast position="top-right" />
      <!-- <Password v-model="val" /> -->
      
<Button type="button" label="Registration" icon="pi pi-users" class=" p-button-lg p-d-block p-mx-auto p-button-text " badgeClass="p-badge-danger" /> 
<div class="p-grid">
<div class="p-col-12 p-md-6 p-lg-6">
      <img src="@/assets/WBDMAIN.jpg" style="width: 70%; display: block;" id="image"/>
</div>
            
<div class="p-col-12 p-md-6 p-lg-6">
            <div class="p-fluid">
              <div class="p-field">
                  <label for="Username">First Name</label>
                  <div class="p-inputgroup">
                  
                        <Button icon="pi pi-user" v-bind:class="fnvalid"/>
                  
           
                  <InputText id="username" v-model="firstname" type="text" />
                </div>
              </div>
                <div class="p-field">
                  <label for="Username">Last Name</label>
                  <div class="p-inputgroup">
                  
                        <Button icon="pi pi-user" v-bind:class="lnvalid"/>
                  
           
                  <InputText id="username" v-model="lastname" type="text" />
                </div>
                </div>
                <div class="p-field">
                  <label for="Username">UserName</label>
                  <div class="p-inputgroup">
                  
                        <Button icon="pi pi-id-card" v-bind:class="usernamevalid"/>
                  
           
                  <InputText id="username" v-model="username" type="text" />
                </div>
                </div>
                 <div class="p-field">
                   <label for="Email address">Email Address</label>
                  <div class="p-inputgroup">
                 
                      <!-- <i class="pi pi-envelope"></i> -->
                      <Button icon="pi pi-envelope" v-bind:class='emailvald'/>
                 
           
                  <InputText id="email" v-model="email"  type="text" />
                </div>
                </div>
                <div class="p-field">
                    <label for="Password">Password</label>
                  <div class="p-inputgroup">
                   <Button icon="pi pi-key" v-bind:class="passwordvalid1"/>
                   <Password v-model="password1" promptLabel mediumLabel />
                </div>
                </div>
                <div class="p-field">
                    <label for="Password">Confirm Password</label>
                  <div class="p-inputgroup">
                   <Button icon="pi pi-key" v-bind:class="passwordvalid2"/>
                   <Password v-model="password2" />
                </div>
                </div>
            <Button type="submit" v-on:click="register"  style="width:10rem" label="Register" icon="pi pi-user-plus" iconPos="right" class="p-button-md" />
              
           </div>
           <Button  class="p-button-text" v-on:click="to_signup">
            Already have account? click here.
            </Button>

</div>
           
          
</div>   
</div>
</template>
<script>
import axios from 'axios';
 import Json from "@/assets/endpoints.json"
export default {
data(){
  return{
        server:Json[0]['SERVER']['SERVER'],
        val: '',
        firstname:'',
        fnvalid:'p-button-warning',
        lastname:'',
        lnvalid:'p-button-warning',
        
        username:'',
        usernamevalid:'p-button-warning',
        email:'',
        emailvald:'p-button-warning',
        password1: '',
        passwordvalid1:'p-button-warning',
        password2: '',
        passwordvalid2:'p-button-warning',
        

        errors: [],
  // reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
   }
   },
methods:{
  to_signup(){
this.$router.push('/Login')
  },
  register(){
    if(this.username!=null&this.firstname!=null&this.lastname!=null&this.password1!=null&this.email!=null){
      if(this.password1==this.password2){
              const config={
                headers:{
                  'content-type':'application/json'
                }
              }
              axios.post(this.server+'api/accounts/register/',{
                username:this.username,
                email:this.email,
                password:this.password1,
                first_name:this.firstname,
                last_name:this.lastname},          
                config)
              .then(response=>{
              // console.log(response.status),
              console.log(response.data),
              console.log(response.data.token)
              // this.$store.getters.createToken(response.data.token)
              this.$router.push('/RegistrationMessage')})
              .catch(e=>{
                // console.log(e.response.status)
                console.log(e.response.data['username'])
                if(e.response.status==400){
                    this.$toast.add({severity:'error', summary: e.response.data, detail:'Try again with different username', life: 3000});
                      }
                
                    })
                }
            else{
                  this.$toast.add({severity:'error', summary: 'Invalid Email or password didn"t matched', detail:'provice valid email', life: 3000});

                  }
             }
       else{
          this.$toast.add({severity:'error', summary: 'Empty fields', detail:'All fields must be filled', life: 3000});

          }
    
        },
      validateemail(){
        var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if(re.test(this.email)){
              return true
            }
            else{
              return false
            }
          }
  
  
    
     },
watch : {
    email(email) {
              var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if(re.test(email)){
              console.log('matched')
              this.emailvald='p-button-success'
            }
            else{
              this.emailvald='p-button-danger'
            }
            },
    password2(){
            if(this.password1==this.password2){
              this.passwordvalid2='p-button-success'
            }
            else{
            this.passwordvalid2='p-button-danger'
            }
            },
    password1(){
            if(this.password1!=null){
              this.passwordvalid1='p-button-success'
            }
            else{
            this.passwordvalid1='p-button-danger'
          }
          },
    username(){

          if(this.username!=null){
            this.usernamevalid='p-button-success'
          }
          else{
          this.usernamevalid='p-button-danger'
          }
        },
    firstname(){
          if(this.firstname!=null){
            this.fnvalid='p-button-success'
          }
          else{
          this.fnvalid='p-button-danger'
        }
        },
    lastname(){
            if(this.lastname!=null){
              this.lnvalid='p-button-success'
            }
            else{
            this.lnvalid='p-button-danger'
          }
          },


   }, 
    created(){
      this.$store.dispatch("set_heading",'Signup page')
    }
        

}
</script>
<style scoped>
#n{
  width:20%;
  height: 50px;
  background-color: black;
  padding:10px;
}
.Signup{
  text-align: center;
}
#username{
  height: 0.4in;
}
/* #signup{
  border: 1px solid rgb(110, 150, 236);
} */
.p-grid{
  padding-top: 0.5in;
}
</style>