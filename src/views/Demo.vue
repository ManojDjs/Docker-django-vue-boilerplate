<template>
<div class="Demo">
    <h1>Demographic Information</h1>
    {{status }}
    <div class="p-grid" >
<div class="p-col-12 p-md-6 p-lg-6">
      <img src="@/assets/Dash.jpeg" style="width:60%; display: block;" id="image" class="p-mr-2"/>
</div>
<div class="p-col-12 p-md-6 p-lg-6">
{{ localstatus }}
 {{ status }}
    <!-- initial record check -->
    <div v-if="status=='NR'">
    <Toast position="center" />
    <Panel header="Message" >
     <div class="p-m-2"> <h3>click below button to start filling Demographics</h3></div>
     <Divider/>
      <Button icon="pi pi-check" label="Continue" v-on:click="register_user_demo" style="width:100%"/>
   </Panel>
   </div>
   <div v-if="status=='RS'">
    <Toast position="center" />
    <Panel header="Message" >
     <div class="p-m-2"> <h3>Please complete the questions below:</h3></div>
     <Divider/>
      <div v-for="age of age_band" :key="age.key" class="p-field-radiobutton">
            <RadioButton :id="age.key" name="category" :value="category" v-model="selectedCategory" :disabled="age.key === 'R'" />
            <label :for="age.key">{{age.name}}</label>
        </div>
     <Divider/>
      <Button icon="pi pi-check" label="Continue" v-on:click="Submit" style="width:100%"/>
   </Panel>
   </div>
</div>
</div>

</div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'
 import Json from "@/assets/endpoints.json"
 import axios from 'axios'
// import { computed } from 'vue'
export default {
    data(){
        return{
            server:Json[0]['SERVER']['SERVER'],
            isq_link:Json[0]['DEMO'],
            total:Json[0]['DEMO']['Total'],
            questionlink:Json[0]['DEMO']['Questions'],
            submission_link:Json[0]['DEMO']['Answers'],
            edit:Json[0]['DEMO']['Edit'],
            sublink:'Demo',
            status:'',
            mqid:'',
            age_band:[
                {name:'18-24',key:"18-24"},
                {name:'24-34',key:"24-34"},
                {name:'35-44',key:"35-44"},
                {name:'45-54',key:"45-54"},
                {name:'55-64',key:"55-64"},
                {name:'65+',key:"65+"}],
            selectedage:''
        }
        },
        computed:{
            ...mapGetters([
                'get_questions',
                'get_q_status',
                'get_qa',
                'getuser'
            ]),
            ...mapState([
                'token',
                'uid',
                'user'
            ])
           
        },
        methods:{
            check(){
                console.log(this.token)
                const headers={
         
          'Authorization': 'Token'+' '+this.token,

                  }
                  //  console.log(headers)
                    axios.get(this.server+this.total,{'headers':headers})
                    .then(resp => {
                    console.log(resp.data)
                    if(resp.data.length==0){
                    this.status='NR'
                    }
                    else{
                        if(resp.data[0]['total_answers']==resp.data[0]['total_questions']){
                        const mqid=resp.data[0].id
                        this.mqid=mqid
                        console.log(resp.data)
                        }
                        else if(resp.data[0]['total_answers']==0){
                            this.status='RS'

                        }
                        else{
                        const mqid=resp.data[0].id
                        this.mqid=mqid
                        console.log(mqid)
                        this.status='RF'//for records found status
                        }
                    
                    }
                    })
                    .catch(err => {
                    console.log(err)
                    })

            },
            register_user_demo(){
                const headers={
         
                    'Authorization': 'Token'+' '+this.token,

                            }
                            //  console.log(headers)
                axios.post(this.server+this.total,
                    {
                    "Answered_by": this.user
                    },
                    {'headers':headers})
                .then(resp => {
                    console.log(resp.data)
                    if(resp.data.length==0){
                    this.status='ER'

                    }
                    else{
                    this.status='RS'
                    

                    }

                })
                .catch(err => {
                    console.log(err)
                })
                
            }

        },
        watch:{
            localedit(){
                this.check()
            },
            submitstatus(){
                this.check()
            }

        },
        created(){
            this.check()
            this.selectedage=this.a[1]

            
        }

    
}
</script>
<style lang='scss' scoped>
::v-deep(.p-scrollpanel) {
    p {
        padding: .5rem;
        line-height: 1.5;
        margin: 0;
    }
    & .button{
         .p-selectbutton {
             background:green;

    }
    }
    &.custombar1 {
        .p-scrollpanel-wrapper {
            border-right: 9px solid var(--surface-b);
        }

        .p-scrollpanel-bar {
            background-color: var(--primary-color);
            opacity: 1;
            transition: background-color .2s;

            &:hover {
                background-color: #007ad9;
            }
        }
    }

    &.custombar2 {
        .p-scrollpanel-wrapper {
            border-right: 9px solid var(--surface-b);
            border-bottom: 9px solid var(--surface-b);
        }

        .p-scrollpanel-bar {
            background-color: var(--surface-d);
            border-radius: 0;
            opacity: 1;
            transition: background-color .2s;
        }
    }  
}
.Demo{
    text-align: center;
}
</style>