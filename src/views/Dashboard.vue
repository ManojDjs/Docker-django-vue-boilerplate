<template>
<div>
    <!-- {{ localstatus }} -->

    <!-- initial record check -->
    <Toast position="center" />
    <Panel header="Message" v-if="get_q_status=='NR'">
	<h1> No Reocrds found for you</h1>
     <div class="p-m-2"> <h3>click below button to start questionnaire</h3></div>
     <Button type="button" v-on:click='register_user_qa' label="Start" class="p-button-success"/>
   </Panel>
   <!-- Record settting -->
   <div v-if="get_q_status=='RS'">
        <div class="p-fluid p-formgrid p-grid" v-for='(item,index) in Answers_KV' :key='index' >
            
            <div class="p-field p-col" >
                    <h3>{{ item.question_name }}</h3>
                    <div class="demo-container p-pl-6 p-pr-6">

                    <Dropdown v-model="item.answer" :options="oprions" optionLabel="name" placeholder="please indicate " v-if='item.question_type=="Options"'/>
                     <InputNumber id="expiry" v-model="item.answer" prefix="I am " suffix="-years" v-if='item.question_type=="Number"'/>
                    <!-- <h3 v-if="item.question_type=='Slider'">Please Drage between [0,10] {{ item.answer }}</h3> -->
                    <!-- <Slider v-model="item.answer" v-if="item.question_type=='Slider'" :step="1" :min="1" :max="10"   class="p-p-2"/> -->
                    <InputText id="username" type="text" v-model="item.answer" v-if='item.question_type=="TEXT"' />
                     <SelectButton class='p-button-primary' v-model="item.answer" :options="gender" v-if="item.question_type=='Gender'" />
                    <SelectButton class='p-button-primary' v-model="item.answer" :options="yesno" v-if="item.question_type=='YESNO'" />
                    </div>
            </div>
         </div>
           <Button type="button" v-on:click='submit' label="Submit" class="p-button-success p-button-lg"/>
   </div>

   <!-- Editing question -->
   <div v-if="get_q_status=='EDIT'">
            <Panel  v-if="localedit==false" header="You Already have you answers">
            <template #icons>
                    <Button type="button" v-on:click='edit_questions' label="EDIT" class="p-button-success p-button-lg"/>
                
            </template>
            <div class="p-fluid p-formgrid p-grid" v-for='(item,index) in get_qa[0]["Demo"]' :key='index' >
                         <Divider align="center" :type='dashed'/>
                          <h3>{{ item.question_name.question }}</h3>
                          <div class="demo-container p-pl-6 p-pr-6">
                          <h3> Answer:  <Badge :value="item.answer"  severity="success"></Badge></h3>
                          </div>

                        

                         
            </div>
            </Panel>
            <div v-if="localedit==true">
                
                <div class="p-fluid p-formgrid p-grid" v-for='(item,index) in Answers_KV' :key='index' >
                         <Divider align="center" :type='dashed'>
                            <span class="p-tag">{{ index +1}} </span>
                        </Divider>
                    <div class="p-field p-col p-p-2" >
                       
                            <h3>{{ item.question_name }}</h3>
                            <div class="demo-container p-pl-6 p-pr-6">

                            <Dropdown v-model="item.answer" :options="oprions" optionLabel="name" placeholder="please indicate " v-if='item.question_type=="Options"'/>
                           
                             <InputNumber id="expiry" v-model="item.answer" prefix="I am " suffix="-years" v-if='item.question_type=="Number"'/>
                    <!-- <h3 v-if="item.question_type=='Slider'">Please Drage between [0,10] {{ item.answer }}</h3> -->
                    <!-- <Slider v-model="item.answer" v-if="item.question_type=='Slider'" :step="1" :min="1" :max="10"   class="p-p-2"/> -->
                    <InputText id="username" type="text" v-model="item.answer" v-if='item.question_type=="TEXT"' />
                     <SelectButton class='p-button-primary' v-model="item.answer" :options="gender" v-if="item.question_type=='Gender'" />
                    <SelectButton class='p-button-primary' v-model="item.answer" :options="yesno" v-if="item.question_type=='YESNO'" />
                            
                           
                            </div>
                    </div>
                      
                </div>
                <Button type="button" v-on:click='save' label="Save" class="p-button-success p-button-lg"/>
              
                
        </div>
   </div>

 <!-- {{ get_qa[0]['total_answers'] }} -->
</div>
</template>
<script>
import { mapGetters } from 'vuex'
 import Json from "@/assets/endpoints.json"
// import { computed } from 'vue'
export default {
    data(){
        return{
            isq_link:Json[0]['DEMO'],
            total:Json[0]['DEMO']['Total'],
            questionlink:Json[0]['DEMO']['Questions'],
            submission_link:Json[0]['DEMO']['Answers'],
            edit:Json[0]['DEMO']['Edit'],
            sublink:'Demo',
            status:this.$store.getters.get_q_status,
            value: [0],
            localstatus:'',
            Answers_KV:[],
            Submisions:[],
            submitstatus:false,
            yesno: ['YES', 'NO'],
            gender:['Male','Female'],
            yesnoanswer:null,
            selected:null,
            oprions: [
			{name: 'None of the time', value: 1},
			{name: 'Rarely', value: 2},
			{name: 'Some of the time', value: 3},
			{name: 'Often', value: 4},
            {name: 'All of the Time', value: 5}
            
        ],
        take_questions:false,
        localedit:false
        }
        },
        computed:{
            ...mapGetters([
                'get_questions',
                'get_q_status',
                'get_qa',
                'getuser'
            ]),
           
        },
        methods:{
            check(){
                    let link=this.total
                    this.$store.dispatch('check_q_status',link)

                    },
           register_user_qa(){
                            console.log("you clicked")
                            if(this.get_q_status=='NR'){
                                    this.$store.dispatch('registeruser',this.total)
                                    this.$router.go()
                                }
                              },
          create_object(){

                     var i;
                // console.log(this.get_questions.data) checking questions
                    for(i=0;i<this.get_questions.length;i++){
                    
                        
                        this.Answers_KV.push({
                            "qid":this.get_questions[i]['id'],
                            "answer": '',
                            // "main_question_set":this.getuser,
                            "question_name": this.get_questions[i]['question'],
                            "question_type":this.get_questions[i]['question_type'],
                            "question_field":this.get_questions[i]['question_field']
                            // "answer_by": this.getuser
                        })
                      }
                      console.log(this.Answers_KV)
                      },
        submit(){
           var i;
              var checking=0;
              console.log(checking)
                // console.log(this.get_questions.data) checking questions
                    for(i=0;i<this.Answers_KV.length;i++){
                    
                                    this.Submisions.push(
                                                        {
                                                    'answer':this.Answers_KV[i]['answer'],
                                                    'editid':this.Answers_KV[i]['editid'],
                                                    'qid':this.Answers_KV[i]['qid'],
                                                    'question_name':this.Answers_KV[i]['question_name'],
                                                    'question_type':this.Answers_KV[i]['question_type']
                                                    })

                                  
                        
                    }
            // console.log(this.Submisions)
                    if(this.get_q_status=='RS'){
                            if(this.Submisions.length!=this.Answers_KV.length){
                                var q=this.Answers_KV.length
                                var b=this.Submisions.length
                                var len=q-b
                                    this.$toast.add({severity:'error', summary: 'Empty fields', detail:'there are  '+len+'empty fields', life: 5000});
                                    this.Submisions=[]
                                }
                            else{
                                console.log('no empty fields')
                                console.log('I am calling store ')
                                console.log(this.Submisions)
                                let link=this.submission_link
                                let submisiondata=this.Submisions
                                console.log("iam checking length")
                                 console.log(this.Submisions.length)
                                
                                this.$store.dispatch('submitanswers',{link,submisiondata})
                                .then(() =>  this.$toast.add({severity:'success', summary: 'Answers submitted', detail:'submitted your answers , absorb below', life: 3000},
                                this.check(),
                                this.localedit=true,
                                ))
                                
                                .catch(err => console.log(err))
                                
                                // this.$router.go()
                                this.Submisions=[]
                                 }
                    }

            },
            edit_questions(){
                
                var i
                this.Answers_KV=[]
                this.Submisions=[]
                for(i=0;i<this.get_qa[0][this.sublink].length;i++){
                                                this.Answers_KV.push({
                                                    "editid":this.get_qa[0][this.sublink][i]['id'],
                                                    "qid":this.get_qa[0][this.sublink][i]['question_name']['id'],
                                                    "answer": this.get_qa[0][this.sublink][i]['answer'],
                                                    // "main_question_set":this.getuser,
                                                    "question_name": this.get_qa[0][this.sublink][i]['question_name']['question'],
                                                    "question_type":this.get_qa[0][this.sublink][i]['question_name']['question_type'],
                                                    // "answer_by": this.getuser
                                                })
                                                }
                            console.log('after creating edit answers')
                            console.log(this.Answers_KV)
                            this.localedit=true

                    },
            save(){
              var i;
                this.Submisions=[]
                console.log(" i am here after save button")
                console.log(this.Answers_KV)
                    for(i=0;i<this.Answers_KV.length;i++){
                    
                       
                            this.Submisions.push(
                                {
                                    'answer':this.Answers_KV[i]['answer'],
                                    'editid':this.Answers_KV[i]['editid'],
                                    'qid':this.Answers_KV[i]['qid'],
                                    'question_name':this.Answers_KV[i]['question_name'],
                                    'question_type':this.Answers_KV[i]['question_type']
                                }
                            )
                           
                        
                        
                    }
            // console.log(this.Submisions)
               
                    if(this.get_q_status=='EDIT'){
                        console.log(this.Submisions)
                        console.log('no empty fields')
                                console.log('I am calling store for save')
                                console.log(this.Submisions)
                                let link=this.edit
                                let submisiondata=this.Submisions
                        
                                this.$store.dispatch('save',{link,submisiondata})
                                .then(() =>  this.$toast.add({severity:'success', summary: 'Answers updated', detail:'updated your answers , absorb below', life: 3000}))
                                .catch(err => console.log(err))
                        this.Submisions=[]
                        this.Answers_KV=[]
                        this.localedit=false
                        this.check()

                    }

            }

        },
        watch:{
            get_q_status(){
                if(this.get_q_status=='NR'){
                    this.take_questions=true
                }
                if(this.get_q_status=="RS"){
                    this.$store.dispatch('questions_taker',this.questionlink)
                    this.create_object()
                }
                if(this.get_q_status=='RF'){
                    console.log(' iam here')
                    if(this.get_qa[0]['total_answers']=='0'){
                        this.$store.dispatch('questions_taker',this.questionlink)
                        this.localstatus='0 answers so far',
                        this.get_q_status=='RS'
                        
                    }
                }
            },
            localedit(){
                this.check()
            },
            submitstatus(){
                this.check()
            }

        },
        created(){
            this.$store.dispatch("set_heading",'Dashboard')
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

</style>