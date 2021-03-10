<template>
<div class="Demo">
    <h1>Base Line Questionnaire</h1>
    {{status }}
    <div class="p-grid" >
        <div class="p-col-12 p-md-6 p-lg-6">
            <img src="@/assets/Dash.jpeg" style="width:60%; display: block;" id="image" class="p-mr-2"/>
        </div>
        <div class="p-col-12 p-md-6 p-lg-6" v-if="status=='RS'">
        {{ status }}
        <!-- {{ demodata }} -->
        <!-- {{ demoquesions }} -->
        <!-- {{ Answers_KV }} -->
        {{ mqid }}
        <!-- <h1>Please complete Base Line Questionnaire:</h1> -->
         <h1>Your Physical Health in general terms:</h1>
         <div v-for='(item,index) in Answers_KV' :key='index'>
             <div v-if="item .question_no==1">
                <h2>{{ item.question }}</h2> 
                <Divider />
                <Textarea v-model="item.answer" :autoResize="true" rows="5" cols="20" />
                <Divider />
                 </div>
                  <div v-if="item .question_no==2">
                  <h2>{{ item.question }}</h2>
                  <Divider />
                   <Slider v-model="item.answer"  :step="1" :min="1" :max="100"   class="p-p-2"/>
                  <Divider />
                 </div>
                  <div v-if="item .question_no==3">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="yesno" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                  <div v-if="item .question_no==4">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="yesno" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                  <div v-if="item .question_no==5">
                <h3>Can you look at the following list. To the best of your memory can you rate your experience of each of them in roughly the last three months:</h3>
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                
                 <div v-if="item .question_no==6">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options2" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                 <div v-if="item .question_no==7">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options3" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                 <div v-if="item .question_no==8">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options4" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                 <div v-if="item .question_no==9">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options5" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                 <div v-if="item .question_no==10">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options6" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                 <div v-if="item .question_no==11">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options7" optionLabel="name" placeholder="please indicate "/>
                   <Divider />
                 </div>
                 <div v-if="item .question_no==12">
                   <h2>{{ item.question }}</h2>
                   <Divider />
                   <Dropdown v-model="item.answer" :options="options8" optionLabel="name" placeholder="please indicate "/>
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
            isq_link:Json[0]['ISQ'],
            total:Json[0]['ISQ']['Total'],
            questionlink:Json[0]['ISQ']['Questions'],
            submission_link:Json[0]['ISQ']['Answers'],
            edit:Json[0]['ISQ']['Edit'],
            sublink:'ISQ',
            status:'',
            mqid:0,
            demodata:[],
            demoquesions:[],
            pages:[1,2,3,4],
            yesno:[
                {name:'yes',key:"yes"},
                {name:'no',key:"no"},
               ],
            options:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],
                options2:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],
                options3:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],
                options4:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],
                options5:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],
                options6:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],
                options7:[
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this nearly every day at the moment',key:"I notice this nearly every day at the moment"},
                {name:'I notice this occaisionally but hard to say how often',key:"I notice this occaisionally but hard to say how often"},
                {name:'I do not experience this at all',key:"I do not experience this at all"},
                {name:'Exisitng Condition',key:"Exisitng Condition"},
                ],

            options8:[
                {name:'Less than 15 seconds',key:"Less than 15 seconds"},
                {name:'15 - 30 Seconds',key:"15 - 30 Seconds"},
                {name:'30 Seconds to a minute',key:"30 Seconds to a minute"},
                {name:'Over a minute',key:"Over a minute"},
               ],
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
              var checking=0
                console.log(this.server+this.submission_link)
                    for(i=0;i<this.Answers_KV.length;i++){
                            // try{
                                const headers={'Authorization': 'Token'+' '+this.token }
                                // const headers={'Authorization': 'Token'+' '+this.token }
                                // console.log(headers)
                                axios.post(this.server+this.submission_link,{
                                            "answer": this.Answers_KV[i]['answer']['key'],
                                            "main_question_set": this.mqid,
                                            "question_name":this.Answers_KV[i]['qid'],
                                            "answer_by": this.uid},
                                            {'headers':headers}).then(resp => {
                                            console.log(resp.data)
                                            console.log(resp.status)
                                            checking=checking+1
                                        })  
                                    // }
                                    // catch(err){
                                    //     console.log(err)
                                    // }
                                
                                }
                            if(checking==this.Answers_KV.length){
                                this.check()
                            }
                                

                        
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