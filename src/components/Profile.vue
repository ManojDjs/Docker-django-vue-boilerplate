<template>
<div class="profile">
	<h2 class="p-m-2"> PROFILE INFORMATION</h2>
	<hr style="height:20px">
	<Toast position="center" />
    <Dialog header="Change Password" v-model:visible="display" style="height:600px;width:500px" modal='true'>
		<div class="p-col-6 p-offset-3 " style="text-align:center">
		<h1>Old Password:</h1>
		<Password v-model="value" class="p-invalid" />
			</div>
			<div class="p-col-6 p-offset-3 "  style="text-align:center">
				<h1>New Password:</h1>
		<Password v-model="value" class="p-invalid" v-tooltip.focus="'Enter your username'" />
			</div>
			<div class="p-col-6 p-offset-3 "  style="text-align:center">
		<Button label="Change" icon="pi pi-key"  class="p-button-lg p-m-3" v-on:click='openpassword' style="width:100%" />
			</div>
		<p>
		At least one lowercase,
		At least one uppercase,
		At least one numeric,
		Minimum 8 characters
		</p>
   </Dialog>
<div class="p-grid p-d-none p-d-lg-inline-flex "> 
<div class="p-col-6 p-offset-3 ">
    <div class="p-grid p-mt-5">
			<div class="p-col-fixed p-mr-5" style="width:200px">
				<Avatar v-bind:label="get_user_name" class=" p-m-2" size="large" style="background-color:#2196F3; color: #ffffff; height:75px;width:75px" shape="circle"/>
				<h2 class="p-m-3">{{ username.toUpperCase() }}</h2>
				
					<Button label="INFO" icon="pi pi-info-circle" class="p-button-lg p-m-3" v-on:click='get_details' style="width:100%"/>
					
					<Button label="EDIT" icon="pi pi-user-edit"  class="p-button-lg p-m-3" v-on:click='edit_user' style="width:100%" />
					<Button label="PASSWORD" icon="pi pi-key"  class="p-button-lg p-m-3" v-on:click='openpassword' style="width:100%" />
			</div>
					<div class="p-col p-mt-10">
										<div class="p-grid p-pt-5" v-if="info" >
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>USERNAME</h2>
													<Divider :type='solid' />
													<h2>{{ username }}</h2>
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>FIRSTNAME</h2>
														<Divider :type='solid' />
													<h2>{{ first_name }}</h2>
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>LASTNAME</h2>
													<Divider :type='solid' />
													<h2>{{ last_name}}</h2>
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>EMAIL-ID</h2>
													<Divider :type='solid' />
													<h2>{{ email }}</h2>
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>DATE-JOINED</h2>
													<Divider :type='solid' />
													<h2>{{ date_joined }}</h2>
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>LASTLOGIN</h2>
													<Divider :type='solid' />
													<h2>{{ last_login }}</h2>	
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>IS-STAFF</h2>
													<Divider :type='solid' />
													<h2>{{ is_staff }}</h2>
													</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>IS-SUPERUSER</h2>
													<Divider :type='solid' />
													<h2>{{ is_superuser }}</h2>
												</div>
											</div>
											
									</div>
					
					<!-- edit -->
						<div class="p-grid p-pt-5" v-if="edit" >
										<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>USERNAME</h2>
													<h3>{{ username }}</h3>
													<Divider :type='solid' />
												</div>
										</div>
										<div class="p-col-12 p-md-6 p-lg-6">
											<div class="box "> 
												<h2>EMAIL-ID</h2>
												<h3>{{ email }}</h3>
												<Divider :type='solid' />
												
											</div>
										</div>
										<div class="p-col-12 p-md-6 p-lg-6">
											<div class="box "> 
												<h2>FIRSTNAME</h2>
												<h3>{{ first_name }}</h3>
												<InputText type="text" class="p-inputtext-md p-invalid" v-model="first_name"  placeholder="Large" />
												<Divider :type='solid' />
												
											</div>
										</div>
										<div class="p-col-12 p-md-6 p-lg-6">
											<div class="box "> 
												<h2>LASTNAME</h2>
												<h3>{{ last_name}}</h3>
												<InputText type="text" class="p-inputtext-md p-invalid" v-model="last_name"  placeholder="Large" />
												<Divider :type='solid' />
											</div>
										</div>
										
										<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>DATE-JOINED</h2>
													<h3>{{ date_joined }}</h3>
													<Divider :type='solid' />
												</div>
										</div>
										<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>LASTLOGIN</h2>
													<h3>{{ last_login }}</h3>
													<Divider :type='solid' />
													
												</div>
										</div>
										<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>IS-STAFF</h2>
													<h3>{{ is_staff }}</h3>
													<Divider :type='solid' />
												</div>
										</div>
										<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>IS-SUPERUSER</h2>
													<h3>{{ is_superuser }}</h3>
													<Divider :type='solid' />
												
												</div>
										</div>
											
										<div class="p-col-6 p-offset-3 " style="text-align:center">
											
												<Button label="save" icon="pi pi-check"  style="width:100%" class="p-button-success p-button-lg " iconPos="right" v-on:click='save'/>
											
										</div>
						</div>

						
				</div>
		
		
	</div>
</div>
</div>

<div class="p-d-lg-none">
<span class=" p-m-3">
		<Avatar v-bind:label="get_user_name" class="p-m-5" size="large" style="background-color:#2196F3; color: #ffffff; height:75px;width:75px" shape="circle"  v-if='info'/>
		<Avatar v-bind:label="get_user_name" class="p-m-5" size="large" style="background-color:#2196F3; color: #ffffff ;height:75px;width:75px" shape="circle"  v-if='edit'/>
		</span>
		
			
			<br>
		<span class="p-buttonset p-m-3">
			<Button  icon="pi pi-info-circle" class="p-button-lg" v-on:click='get_details'/>
			<Button  icon="pi pi-user-edit"  class="p-button-lg" v-on:click='edit_user'/>
		
		</span>
		<div class="p-grid p-pt-5" v-if="info" >
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>USERNAME</h2>
													<Divider :type='solid' />
													<h2>{{ username }}</h2>
													
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>FIRSTNAME</h2>
														<Divider :type='solid' />
													<h2>{{ first_name }}</h2>
												
													
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>LASTNAME</h2>
													<Divider :type='solid' />
													<h2>{{ last_name}}</h2>
													
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>EMAIL-ID</h2>
													<Divider :type='solid' />
													<h2>{{ email }}</h2>
													
													
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>DATE-JOINED</h2>
													<Divider :type='solid' />
													<h2>{{ date_joined }}</h2>
													
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>LASTLOGIN</h2>
													<Divider :type='solid' />
													<h2>{{ last_login }}</h2>
													
													
												</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>IS-STAFF</h2>
													<Divider :type='solid' />
												
													<h2>{{ is_staff }}</h2>
													</div>
											</div>
											<div class="p-col-12 p-md-6 p-lg-6">
												<div class="box "> 
													<h2>IS-SUPERUSER</h2>
													<Divider :type='solid' />
													<h2>{{ is_superuser }}</h2>
													
												
												</div>
											</div>
		</div>
		<!-- edit -->
		<div class="p-grid p-m-5" v-if="edit"  style="text-align:center">
			
					<div class="p-col-12 p-md-6 p-lg-6">
						<div class="box "> 
							<h2>FIRSTNAME</h2>
							<h3>{{ first_name }}</h3>
							<InputText type="text" class="p-inputtext-lg" v-model="first_name"  placeholder="Large" />
							<Divider :type='solid' />
							
						</div>
					</div>
					<div class="p-col-12 p-md-6 p-lg-6">
						<div class="box "> 
							<h2>LASTNAME</h2>
							<h3>{{ last_name}}</h3>
							<InputText type="text" class="p-inputtext-lg" v-model="last_name"  placeholder="Large" />
							<Divider :type='solid' />
						</div>
					</div>
						<div class="p-col-6 p-offset-3 " style="text-align:center">
											
												<Button label="save" icon="pi pi-check"  style="width:100%" class="p-button-success p-button-lg " iconPos="right" v-on:click='save'/>
											
						</div>
		</div>
</div>	
</div>
</template>
<script>
 import Json from "@/assets/endpoints.json"
 import axios from 'axios';
 import { mapState } from 'vuex';
export default {
	data(){
		return{
			server:Json[0]['SERVER'],
			main:Json[0]['USER'],
			detailslink:Json[0]['USER']['DETAILS'],
			editlink:Json[0]['USER']['EDIT'],
			value1:null,
			options:['info','edit'],
			info:true,
			edit:null,
			udetails:[],
			last_name:'',
			first_name:'',
			username:'',
			email:'',
			date_joined:'',
			is_superuser:'',
			is_staff:'',
			last_login:'',
			fid:'',
			display: false
			}
		
		},
		computed:{
    ...mapState([
		'token',
		'user',
		'heading',
		'uid'
		]),
		get_user_name(){
			return this.username.charAt(0).toLocaleUpperCase();
		}
		},

	methods:{
		openpassword() {
            this.display = true;
        },
			get_details(){
				this.edit=false,
				this.info=true
				var link=this.server['SERVER']+this.detailslink
				const headers={
                'Authorization': 'Token'+' '+this.token
                    }
				console.log(link)
				axios.get(link,{'headers':headers})
				.then(resp=>{
					console.log(resp.data)

			this.last_name=resp.data[0]['last_name']
			this.first_name=resp.data[0]['first_name']
			this.username=resp.data[0]['username']
			this.email=resp.data[0]['email']
			this.date_joined=resp.data[0]['date_joined']
			this.is_superuser=resp.data[0]['is_superuser']
			this.is_staff=resp.data[0]['is_staff']
			this.last_login=resp.data[0]['last_login']
			this.fid=resp.data[0]['id']
				})
				


			},
			edit_user(){
				this.info=false
				this.edit=true

				

			},
			save(){
				const headers={
                'Authorization': 'Token'+' '+this.token
					}
				var link=this.server['SERVER']+this.editlink+'/'+this.fid
				axios.put(link,
            {
				"username": this.username,
                    "first_name": this.first_name,
                    "last_name": this.last_name
            },
			{'headers':headers})
			.then(resp => {
				console.log(resp.data)
				this.$toast.add({severity:'success', summary: 'Details updated', detail:'successfully , Updated user details', life: 3000}),
				this.edit=false,
				this.get_details()
				})
				}

		},
		mounted(){
			this.get_details()
		}
}
</script>
<style scoped>
.profile{
	text-align: center;
}
</style>
