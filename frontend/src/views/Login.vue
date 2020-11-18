<template>
<div>
    <router-view/>
    <div class="p-m-2 p-p-20">
      <Toast position="top-right" />
      
        <Button type="button" label="Registration" icon="pi pi-users" class="p-button-warning p-d-block p-mx-auto" badgeClass="p-badge-danger" /> 
        
        <div class="p-grid">
         
            <div class="box p-mx-auto p-p-auto">
            <div class="p-fluid">
              
               
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
                      <Button icon="pi pi-key" class="p-button-success"/>
                      <Password v-model="password" />
                    </div>
                    </div>
               
            <Button type="submit"  v-on:click="login" style="width:10rem" label="Log IN" icon="pi pi-chevron-circle-right" iconPos="right" class="p-button-md" />
              
           </div>
           </div>
            </div>
           </div>
</div>
  
</template>
<script>
import axios from 'axios'
export default {


data: () => ({
  email:'',
  emailvald:'p-button-warning',
  password:''
 
}),
methods:{
  login(){
    const config={
      headers:{
        'content-type':'application/json'
      }
    }
    axios.post('http://127.0.0.1:8000/api/accounts/login/',{username:this.email,password:this.password},config)
    .then(response=>{
    console.log(response.status),
    console.log(response.data),
    console.log(response.data.token)
    this.$store.getters.createToken(response.data.token)
    this.$router.push('/RegistrationMessage')})
    .catch(e=>{
      console.log(e.response.status)
     this.showSuccess();
    })
    
  },
  showSuccess() {
            this.$toast.add({severity:'error', summary: 'Invalid credentials', detail:'if you dont have account try registration', life: 3000});
            this.email='';
            this.password=''
        },

},
watch : {
               email:function(email) {
                  var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                if(re.test(email)){
                  console.log('matched')
                  this.emailvald='p-button-success'
                }
                else{
                  this.emailvald='p-button-danger'
                }
               },
}

    
}
</script>
<style scoped>
.p-grid{
  padding-top: 0.5in;
}
</style>