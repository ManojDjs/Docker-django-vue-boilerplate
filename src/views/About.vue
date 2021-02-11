<template>
<div class="About p-shadow-5">
	<div class="p-grid">
			<div class="p-col-12 p-md-6 p-lg-6">
			<img src="@/assets/WBDMAIN.jpg" style="width: 70%; display: block;" id="image" />
			</div>
			<div class="p-col-12 p-md-6 p-lg-6">
				<div class="demo-container p-p-4" id="mark" >
			<h1 class="p-d-block p-mx-auto" >Qigong Practice Research Project</h1>
				</div>
			</div>
	</div>
			<Divider/>
	<div class="p-grid">
			<div class="p-col-12 p-md-6 p-lg-6">

			<Button label="Log In" icon="pi pi-check" class="p-button-lg p-d-block p-mx-auto" v-on:click="login" />
			<Divider/>
			<Button label="Create Account" icon="pi pi-check" class="p-button-lg p-d-block p-mx-auto"  v-on:click="signup"  />

			</div>
			<div class="p-col-12 p-md-6 p-lg-6 ">
			<div class="demo-container p-p-4">
			<h3 class="p-d-block p-mx-auto" id="mark">
			No Account yet? Click ‘Create Account’ and type in your details
			</h3>
			</div>
	</div>
	<Divider/>
</div>
</div>
</template>
<script>
export default {
    data() {
		return {
            options:{
                width:1000,
                height:1000

            },
			}
	},
	methods:{
		login(){

      this.$router.push('/Login')
    },
	signup(){

      this.$router.push('/Signup')
    },
	}
}
</script>

<style >
.About{
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