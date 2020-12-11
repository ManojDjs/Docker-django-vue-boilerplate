<template>
<div>
    <Toast position="top-right" />
    <Panel header="Message" v-if="get_q_status=='NR'">
	<h1> No Reocrds found for you</h1>
     <div class="p-m-2"> <h3>click below button to start questionnaire</h3></div>
     <Button type="button" v-on:click='register_user_qa' label="Start" class="p-button-success"/>

   </Panel>
   <div v-if="get_q_status=='RS'">
        <div class="p-fluid p-formgrid p-grid" v-for='(item,index) in Answers_KV' :key='index' >
            
            <div class="p-field p-col" >
                    <h3>{{ item.question_name }}</h3>
                    <div class="demo-container p-pl-6 p-pr-6">

                    <Dropdown v-model="item.answer" :options="oprions" optionLabel="name" placeholder="please indicate " v-if='item.question_type=="Options"'/>
                    <h3 v-if="item.question_type=='Slider'">Please Drage between [0,10] {{ item.answer }}</h3>
                    <Slider v-model="item.answer" v-if="item.question_type=='Slider'" :step="1" :min="1" :max="10"   class="p-p-2"/>
                    
                    <SelectButton class='p-button-primary' v-model="item.answer" :options="yesno" v-if="item.question_type=='YESNO'" />
                    </div>
            </div>
         </div>
           <Button type="button" v-on:click='submit' label="Submit" class="p-button-success p-button-lg"/>
   </div>
    <div v-if="localedit">
        {{ get_qa }}
        <div class="p-fluid p-formgrid p-grid" v-for='(item,index) in Answers_KV' :key='index' >
            
            <div class="p-field p-col" >
                    <h3>{{ item.question_name }}</h3>
                    <div class="demo-container p-pl-6 p-pr-6">

                    <Dropdown v-model="item.answer" :options="oprions" optionLabel="name" placeholder="please indicate " v-if='item.question_type=="Options"'/>
                    <h3 v-if="item.question_type=='Slider'">Please Drage between [0,10] {{ item.answer }}</h3>
                    <Slider v-model="item.answer" v-if="item.question_type=='Slider'" :step="1" :min="1" :max="10"   class="p-p-2"/>
                    
                    <SelectButton class='p-button-primary' v-model="item.answer" :options="yesno" v-if="item.question_type=='YESNO'" />
                    </div>
            </div>
         </div>
         <Button type="button" v-on:click='submit' label="Save" class="p-button-success p-button-lg"/>
          
   </div>
 {{ get_q_status }}
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
            isq_link:Json[0]['ISQ'],
            total:Json[0]['ISQ']['Total'],
            questionlink:Json[0]['ISQ']['Questions'],
            submission_link:Json[0]['ISQ']['Answers'],
            edit:Json[0]['ISQ']['Edit'],
            status:this.$store.getters.get_q_status,
            value: [0],
            Answers_KV:[],
            Submisions:[],
            yesno: ['YES', 'NO'],
            yesnoanswer:null,
            selected:null,
            oprions: [
			{name: 'Never', value: 1},
			{name: 'sometimes', value: 2},
			{name: 'Regularly', value: 3},
			{name: 'Often', value: 4},
            {name: 'Almost Always', value: 5}
            
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
                }
         },
         submit(){
              var i;
              var checking=0;
              console.log(checking)
                // console.log(this.get_questions.data) checking questions
                    for(i=0;i<this.Answers_KV.length;i++){
                    
                        if(this.Answers_KV[i]['question_type']=='Options'){
                            try{
                                if(this.Answers_KV[i]['answer']){
                            //    this.Answers_KV[i]['answer']=this.Answers_KV[i]['answer']['value']
                            this.Submisions.push(
                                {
                                    'answer':this.Answers_KV[i]['answer']['value'],
                                    'editid':this.Answers_KV[i]['editid'],
                                        'qid':this.Answers_KV[i]['qid'],
                                    'question_name':this.Answers_KV[i]['question_name'],
                                    'question_type':this.Answers_KV[i]['question_type']
                                }
                            )
                            console.log(this.Answers_KV[i])
                                }
                                if(!this.Answers_KV[i]['answer'])
                                {
                                        // this.$toast.add({severity:'error', summary: 'Empty fields', detail:'please fill your Answer for '+this.Answers_KV[i]['question_name'], life: 5000});
                                    checking=checking+1
                                }
                            }
                            catch(err){
                                console.log(err)
                            }
                            
                        }
                            if(this.Answers_KV[i]['question_type']=='Slider'){
                            try{
                                if(this.Answers_KV[i]['answer']){
                            //    this.Answers_KV[i]['answer']=this.Answers_KV[i]['answer']['value']
                                                                this.Submisions.push(
                                                                {
                                                                    'answer':this.Answers_KV[i]['answer'],
                                                                    'editid':this.Answers_KV[i]['editid'],
                                                                    'qid':this.Answers_KV[i]['qid'],
                                                                    'question_name':this.Answers_KV[i]['question_name'],
                                                                    'question_type':this.Answers_KV[i]['question_type']
                                                                })
                                                                console.log(this.Answers_KV[i])
                                }
                                if(!this.Answers_KV[i]['Slider'])
                                {
                                        // this.$toast.add({severity:'error', summary: 'Empty fields', detail:'please fill your Answer for '+this.Answers_KV[i]['question_name'], life: 5000});
                                    checking=checking+1
                                }
                                    }
                            catch(err){
                                console.log(err)
                            }
                            
                        }
                        if(this.Answers_KV[i]['question_type']=='YESNO'){
                            try{
                                if(this.Answers_KV[i]['answer']){
                                    if(this.Answers_KV[i]['answer']=='YES')
                                    {
                                                        this.Submisions.push(
                                                        {
                                                    'answer':1,
                                                    'editid':this.Answers_KV[i]['editid'],
                                                    'qid':this.Answers_KV[i]['qid'],
                                                    'question_name':this.Answers_KV[i]['question_name'],
                                                    'question_type':this.Answers_KV[i]['question_type']
                                                    })

                                    }
                                    else{
                                                                this.Submisions.push(
                                                        {
                                                            'answer':0,
                                                            'editid':this.Answers_KV[i]['editid'],
                                                            'qid':this.Answers_KV[i]['qid'],
                                                            'question_name':this.Answers_KV[i]['question_name'],
                                                            'question_type':this.Answers_KV[i]['question_type']
                                                        })
                                    }
                                }
                                if(!this.Answers_KV[i]['Slider'])
                                {
                                        
                                    checking=checking+1
                                }
                            }
                            catch(err){
                                console.log(err)
                            }
                            
                        }
                        
                        
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
                                this.Answers_KV=[]
                                this.$store.dispatch('submitanswers',{link,submisiondata})
                            }
                    }
                    if(this.get_q_status=='EDIT'){
                        console.log(this.Submisions)
                        console.log('no empty fields')
                                console.log('I am calling store for save')
                                console.log(this.Submisions)
                                let link=this.edit
                                let submisiondata=this.Submisions
                                this.Answers_KV=[]
                                this.$store.dispatch('save',{link,submisiondata})
                        this.Submisions=[]
                        this.Answers_KV=[]
                    }
         },

         create_object(){

             var i;
                // console.log(this.get_questions.data) checking questions
            for(i=0;i<this.get_questions.length;i++){
               
                   
                this.Answers_KV.push({
                    "qid":this.get_questions[i]['id'],
                    "answer": 0,
                    // "main_question_set":this.getuser,
                    "question_name": this.get_questions[i]['question'],
                    "question_type":this.get_questions[i]['question_type'],
                    // "answer_by": this.getuser
                })
            }
        console.log(this.Answers_KV)


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
                        
                    }
                }
                if(this.get_q_status=='EDIT'){
                this.localedit=true
                var i;
                // console.log(this.get_questions.data) checking questions
                 for(i=0;i<this.get_qa[0]['ISQ'].length;i++){
                     if(this.get_qa[0]['ISQ'][i]['question_name']['question_type']=='Options'){
                         if(this.get_qa[0]['ISQ'][i]['answer']=='1'){
                                 this.get_qa[0]['ISQ'][i]['answer']={name: 'Never', value: 1}

                         }
                         if(this.get_qa[0]['ISQ'][i]['answer']=='2'){
                                 this.get_qa[0]['ISQ'][i]['answer']={name: 'sometimes', value: 2}

                         }
                         if(this.get_qa[0]['ISQ'][i]['answer']=='3'){
                                 this.get_qa[0]['ISQ'][i]['answer']={name: 'Regularly', value: 3}

                         }
                         if(this.get_qa[0]['ISQ'][i]['answer']=='4'){
                                 this.get_qa[0]['ISQ'][i]['answer']={name: 'Often', value: 4}

                         }
                         if(this.get_qa[0]['ISQ'][i]['answer']=='5'){
                                 this.get_qa[0]['ISQ'][i]['answer']={name: 'Almost Always', value: 5}

                         }
                     }
                     if(this.get_qa[0]['ISQ'][i]['question_name']['question_type']=='YESNO'){
                          if(this.get_qa[0]['ISQ'][i]['answer']=='1'){
                                 this.get_qa[0]['ISQ'][i]['answer']='YES'

                         }
                          if(this.get_qa[0]['ISQ'][i]['answer']=='0'){
                                 this.get_qa[0]['ISQ'][i]['answer']='NO'

                         }
                     }

                        this.Answers_KV.push({
                            "editid":this.get_qa[0]['ISQ'][i]['id'],
                            "qid":this.get_qa[0]['ISQ'][i]['question_name']['id'],
                            "answer": this.get_qa[0]['ISQ'][i]['answer'],
                            // "main_question_set":this.getuser,
                            "question_name": this.get_qa[0]['ISQ'][i]['question_name']['question'],
                            "question_type":this.get_qa[0]['ISQ'][i]['question_name']['question_type'],
                            // "answer_by": this.getuser
                        })
                        }
                    console.log('i am here')
                    console.log(this.Answers_KV)


                    }



                }
            },
            get_qa(){

                if(this.get_qa[0]['total_answers']=='0'){
                    this.$store.dispatch('questions_taker',this.questionlink)
                    this.get_q_status=='RS'
                    
                }
                
            },
            get_questions(){
                console.log('i triggered len')
                if(this.get_questions.length>1){
                    console.log("fuck")
                }
            },
        created(){
            this.check()
           if(this.get_q_status=='EDIT'){
               this.localedit=true
           }
           else{
               this.localedit=false
           }

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