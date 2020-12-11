<template>
<div>
    
      <Toast position="top-right" />
      
        <Button type="button" label="Login" icon="pi pi-users" class="p-button-warning p-d-block p-mx-auto" badgeClass="p-badge-danger" />        
            <div>
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
  
</template>
<script>
// import axios from 'axios'
export default {


data: () => ({
  email:'',
  emailvald:'p-button-warning',
  password:''
 
}),
methods:{
  login(){
    if(this.email!=null &this.password!=null){
    let email = this.email
        let password = this.password
        this.$store.dispatch('login', { email, password })
       .then(() => this.$router.push('/Dashboard'))
       .catch(err => console.log(err))
    }
    else{
       this.$toast.add({severity:'warning', summary: 'Empty fields', detail:'All fields must be filled', life: 3000});
    }
    
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

</style>