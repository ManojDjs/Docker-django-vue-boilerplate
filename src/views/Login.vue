<template>
<div class="login"> 
<Toast position="top-right"/>
   
<Divider/>
<div class="p-grid">
<div class="p-col-12 p-md-6 p-lg-6">
      <img src="@/assets/WBDMAIN.jpg" style="width: 70%; display: block;" id="image"/>
</div>
<div class="p-col-12 p-md-6 p-lg-6">
          <div class="demo-container p-p-4" >
          <div class="p-grid" id="mark" >
                
            <div class="p-field">
                              <label for="Email address">Email Address</label>
                              <div class="p-inputgroup">
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
<Button  class="p-button-text" v-on:click="to_login">
Dont have account? click here.
</Button>
</div>
</div>
<Divider/>
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
  to_login(){
   this.$router.push('/Signup')
  },
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
},
created(){
   this.$store.dispatch("set_heading",'Login page')
}

    
}
</script>
<style scoped>
.login{
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