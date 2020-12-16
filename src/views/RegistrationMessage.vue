<template>
<div class="p-m-2 p-p-20">
      <Toast position="top-right" />
        <Button type="button" label="Account verification" icon="pi pi-users" class="p-button-warning p-d-block p-mx-auto" badgeClass="p-badge-danger" /> 
        
        <div class="p-grid">
         
            <div class="box p-mx-auto p-p-auto">
            <div class="p-fluid">
              <br>
                <h1>Registration successfull</h1>
                <br>
            <Fieldset legend="Congratulations" :toggleable="true">
                <p>Email has been sent to the address you provided while Registration,you can click on the link to verify you account</p>
                     <Button type="submit"  style="width:10rem" v-on:click='back_to_login' label="Goto LOGIN" icon="pi pi-backward" iconPos="left" class="p-button-md" />
                <h4>OR</h4>
                <p>Copy paste token in below token box for activation!</p>

            </Fieldset>
             <div class="p-field">
                   <label for="Email address">Enter Token to validate</label>
                  <div class="p-inputgroup">
                 
                      <!-- <i class="pi pi-envelope"></i> -->
                      <Button icon="pi pi-money-bill" v-bind:class='tokenvalid'/>
           
                  <InputText id="email" v-model="token"  type="text" />
                
                </div>
            </div>
            </div>
            <Button type="submit"  style="width:10rem" v-on:click='validate' label="validate token" icon="pi pi-lock-open" iconPos="right" class="p-button-md" />
                </div>
        </div>
</div>
</template>
<script>
import axios from 'axios'
export default {
    data: () => ({
  
  token:null,
  tokenvalid:'p-button-warning',

  errors: [],
  // reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
 
}),
methods:{
     validate(){
    if(this.token!=null){
        const config={
          headers:{
            'content-type':'application/json'
          }
        }
        axios.get('http://127.0.0.1:8000/api/accounts/activate/NA/'+this.token,          
          config)
        .then(response=>{
        console.log(response.status),
        console.log(response.data),
        this.$router.push('/Login')})
        .catch(e=>{
          console.log(e.response.status)
          if(e.response.status==400){
              this.$toast.add({severity:'error', summary: e.response.data, detail:'invalid token', life: 3000});
          }
          
        })
     
    }
    else{
       this.$toast.add({severity:'error', summary: 'Empty fields', detail:'Token must be provided ', life: 3000});

    }
    
  },
  back_to_login(){
      this.$router.push('/Login')

  }
},
watch:{
     token:function(){
      if(this.token!=null){
        this.tokenvalid='p-button-success'
      }
      else{
      this.tokenvalid='p-button-danger'
    }
    },
}
    
}
</script>