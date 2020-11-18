<template>
<div class="p-m-2 p-p-20">
      <Toast position="top-right" />
        <Button type="button" label="Account verification" icon="pi pi-users" class="p-button-warning p-d-block p-mx-auto" badgeClass="p-badge-danger" /> 
        
        <div class="p-grid">
         
            <div class="box p-mx-auto p-p-auto">
            <div class="p-fluid">
                <h1>Registration successfull</h1>
            <Fieldset legend="Congratulations" :toggleable="true">
                <p>Email has been sent to the address you provided while Registration,you can click on the link to verify you account</p>

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
            <Button type="submit"  style="width:10rem" label="validate token" icon="pi pi-lock-open" iconPos="right" class="p-button-md" />
                </div>
        </div>
</div>
</template>
<script>
export default {
    data: () => ({
  
  token:'',
  tokenvalid:'p-button-warning',

  errors: [],
  // reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
 
}),
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