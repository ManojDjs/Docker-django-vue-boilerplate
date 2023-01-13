<template>
<div class="About">
	<div
      class="mt-6 max-w-screen flex align-items-center justify-content-center"
    >
      <Nav></Nav>
    </div>
	<Footer></Footer>
</div>
</template>
<script>
import Nav from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
export default {
    data() {
		return {
            options:{
                width:1000,
                height:1000

            },
			}
	},
	components:{
		Nav,
		Footer
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

</style>