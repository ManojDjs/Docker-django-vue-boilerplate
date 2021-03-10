<template>
<div class="Demo">
    <h1>Demographic Information</h1>
    {{status }}
    <div class="p-grid" >
        <div class="p-col-12 p-md-6 p-lg-6">
            <img src="@/assets/Dash.jpeg" style="width:60%; display: block;" id="image" class="p-mr-2"/>
        </div>
        <div class="p-col-12 p-md-6 p-lg-6" v-if="status=='RS'">
        {{ status }}
        {{ demodata }}
        {{ demoquesions }}
        {{ Answers_KV }}
        <h1>Please complete the questions below:</h1>
         <div v-for='(item,index) in Answers_KV' :key='index'>
             <div v-if="item .question_no==1">
                <h2>{{ item.question }}</h2> 
                <Divider />
                <Dropdown v-model="item.answer" :options="age_band" optionLabel="name" placeholder="please indicate "/>
                <Divider />
                 </div>
                  <div v-if="item .question_no==2">
                  <h2>{{ item.question }}</h2>
                  <Divider />
                  <Dropdown v-model="item.answer" :options="e_banckground" optionLabel="name" placeholder="please indicate "/>
                  <Divider />
                 </div>
                  <div v-if="item .question_no==3">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="Gender" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                  <div v-if="item .question_no==4">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="work" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                  <div v-if="item .question_no==5">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="experience" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>

         </div>

                <Button v-on:click="submit">Submit</Button>

        </div>
         <div class="p-col-12 p-md-6 p-lg-6" v-if="status=='EDIT'">
        <h1>Please Observe carefully your answers below:</h1>

         <div v-for='(item,index) in demodata[0]["Demo"]' :key='index'>
             <div v-if="item.question_name['id']==1">
                <h2>{{ item.question_name['question'] }}</h2> 
                <Divider />
                <h3>{{ item.answer}}</h3>
                <Divider />
                 </div>
                  <div v-if="item.question_name['id']==2">
                 <h2>{{ item.question_name['question'] }}</h2> 
                  <Divider />
                  <h3>{{ item.answer}}</h3>
                  <Divider />
                 </div>
                  <div v-if="item.question_name['id']==3">
                   <h2>{{ item.question_name['question'] }}</h2> 
                   <Divider />
                  <h3>{{ item.answer}}</h3>
                   <Divider />
                 </div>
                  <div v-if="item.question_name['id']==4">
                   <h2>{{ item.question_name['question'] }}</h2> 
                   <Divider />
                   <h3>{{ item.answer}}</h3>
                   <Divider />
                 </div>
                  <div v-if="item.question_name['id']==5">
                   <h2>{{ item.question_name['question'] }}</h2> 
                   <Divider />
                   <h3>{{ item.answer}}</h3>
                   <Divider />
                 </div>

         </div>
                
                <Button v-on:click="Continue">Continue</Button>

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
            mqid:0,
            demodata:[],
            demoquesions:[],
            age_band:[
                {name:'18-24',key:"18-24"},
                {name:'24-34',key:"24-34"},
                {name:'35-44',key:"35-44"},
                {name:'45-54',key:"45-54"},
                {name:'55-64',key:"55-64"},
                {name:'65+',key:"65+"}],
            e_banckground:[
                {name:'Asian/Asian British',key:"Asian/Asian British"},
                {name:'Black/African/Caribbean/Black British',key:"Black/African/Caribbean/Black British"},
                {name:'Mixed/Multiple ethnic groups',key:"Mixed/Multiple ethnic groups"},
                {name:'White',key:"White"},
                {name:'Other ethnic group',key:"Other ethnic group"},
                ],
            Gender:[
                {name:'Female (including female transgender)',key:"Female (including female transgender)"},
                {name:'Male (including male transgender)',key:"Male (including male transgender)"},
                {name:'Gender neutral',key:"Gender neutral"},
                {name:'Non-binary',key:"Non-binary"},
                {name:'Other',key:"Other"},
                {name:'Prefer not to say',key:"Prefer not to say"}],
         work:[
                {name:'Desk based',key:"Desk based"},
                {name:'Driver',key:"Driver"},
                {name:'Educator',key:"Educator"},
                {name:'Home worker',key:"Home worker"},
                {name:'Retired',key:"Retired"},
                {name:'Studying',key:"Studying"}],
        experience:[
                {name:'No prior experience',key:"No prior experience"},
                {name:'Some prior experience',key:"Some prior experience"},
                {name:'Professional practitioner of Qigong',key:"Professional practitioner of Qigong"},
                {name:'Prior experience of Tai Chi',key:"Prior experience of Tai Chi"},
                {name:'Prior experience of other form of slow movement exercise',key:"Prior experience of other form of slow movement exercise"},
                ],
            selectedage:'',
            Answers_KV:[],
            Submisions:[]
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
            Continue(){
                this.$router.push('/Videos')
            },
            check(){
                console.log(this.token)
                const headers={'Authorization': 'Token'+' '+this.token, }
                    axios.get(this.server+this.total,{'headers':headers})
                    .then(resp => {
                    console.log(" i am at initial check")
                    console.log(resp.data)
                    this.demodata=resp.data
                    if(this.demodata.length==0){
                        console.log("no answers taken so far")
                        axios.post(this.server+this.total,{"Answered_by": this.user},{'headers':headers})
                        .then(resp => {
                            console.log(resp.data)
                            if(resp.data.length==0){
                                  this.check()
                            }
                            else{
                                this.status='RS'
                                this.check()
                            }

                        })
                        .catch(err => {
                            console.log(err)
                        })
                    }
                    else{
                        this.mqid=resp.data[0]['id']
                        
                        if(resp.data[0]['total_answers']==0){
                            console.log("i am at total answers 0 ")
                            this.status='RS'
                            this.take_demo()
                        }
                        if(resp.data[0]['total_answers']==resp.data[0]['total_questions']){
                            console.log("i am enabeling edit mode")
                            this.status='EDIT'
                            this.demodata=resp.data
                        }
                    }

                    })
                    .catch(err => {
                    console.log(err)
                    })
                    },
            take_demo(){
                 const headers={'Authorization': 'Token'+' '+this.token, }
                    axios.get(this.server+this.questionlink,{'headers':headers})
                    .then(resp => {
                    // console.log(resp.data)
                    this.demoquesions=resp.data
                    this.create_object()

                    })
                    .catch(err => {
                    console.log(err)
                    })
                    },
            submit(){
                console.log(this.Answers_KV)
                 var i;
              var checking=0;
              console.log(checking)
                
                    for(i=0;i<this.Answers_KV.length;i++){
                            try{
                                const headers={'Authorization': 'Token'+' '+this.token, }
                                axios.post(this.server+this.submission_link,{
                                            "answer": this.Answers_KV[i]['answer']['key'],
                                            "main_question_set": this.mqid,
                                            "question_name":this.Answers_KV[i]['qid'],
                                            "answer_by": this.uid},
                                            {'headers':headers}).then(resp => {
                                            console.log(resp.data)
                                        })  
                                    }
                                    catch(err){
                                        console.log(err)
                                    }
                                
                                }
                                this.check()

                        
                },
                create_object(){

                        var i;
                    // console.log(this.get_questions.data) checking questions
                    for(i=0;i<this.demoquesions.length;i++){
                    
                        
                        this.Answers_KV.push({
                            "qid":this.demoquesions[i]['id'],
                            "answer": "",
                            "question": this.demoquesions[i]['question'],
                            "question_no":this.demoquesions[i]['question_no'],
                            
                        })
                      }
                      console.log(this.Answers_KV)
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