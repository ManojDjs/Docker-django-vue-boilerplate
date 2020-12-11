<template>
<div class="Dashboard">
     <Toast position="top-right" />
    <Panel header="Message" v-if="get_q_status=='NR'">
	<h1> No Reocrds found for you</h1>
     <div class="p-m-2"> <h3>click below button to start questionnaire</h3></div>
     <Button type="button" v-on:click='register_user_qa' label="Start" class="p-button-success"/>
   </Panel>
    <div v-if="get_q_status=='RS'">
        
         <div class="p-fluid p-formgrid" v-for='(item,index) in Answers_KV' :key='index' >
             {{ item.question_type }}
            <div class="p-field p-col" > 
                    <h3>{{ item.question_name }}</h3>
                    <div  v-if="item.question_name=='Age'">
                       <InputNumber id="horizontal" v-model="item.answer" showButtons buttonLayout="horizontal" :step="1"
                        decrementButtonClass="p-button-danger" incrementButtonClass="p-button-success" incrementButtonIcon="pi pi-plus" decrementButtonIcon="pi pi-minus"  prefix='I am ' suffix=" years" />
                    </div>
                    <div v-if="item.question_name=='Gender'">
                          <div class="demo-container p-p-4">
                                <div class="p-field-radiobutton" >
                                        <RadioButton id="city1" name="city" value="Male" v-model="item.answer" />
                                        <label for="city1">Male</label>
                                    </div>
                                    <div class="p-field-radiobutton">
                                        <RadioButton id="city2" name="city" value="Female " v-model="item.answer" />
                                        <label for="city2">Female</label>
                                    </div>
                          </div>
                    </div>
                       <div v-else >
                        <InputText type="text" class="p-inputtext" />
                        
                        </div>
             </div>
            </div>
                    
     <Button type="button" v-on:click='submit' label="Submit" class="p-button-success p-button-lg"/>   
   </div>
 {{ get_q_status }}
 {{ get_qa }}
   <!-- {{ Json}} -->
</div>
</template>
<script>
import { mapGetters } from 'vuex'
import Json from "@/assets/endpoints.json"
export default {
    
            data(){
                return{
                    isq_link:Json[0]['DEMO'],
                    total:Json[0]['DEMO']['Total'],
                    questionlink:Json[0]['DEMO']['Questions'],
                    submission_link:Json[0]['DEMO']['Answers'],
                    edit:Json[0]['DEMO']['DEMO'],
                    status:this.$store.getters.get_q_status,
                    value: [0],
                    Answers_KV:[],
                    Submisions:[],
                     countries: [
                    {name: 'Australia', code: 'AU'},
                    {name: 'Brazil', code: 'BR'},
                    {name: 'China', code: 'CN'},
                    {name: 'Egypt', code: 'EG'},
                    {name: 'France', code: 'FR'},
                    {name: 'Germany', code: 'DE'},
                    {name: 'India', code: 'IN'},
                    {name: 'Japan', code: 'JP'},
                    {name: 'Spain', code: 'ES'},
                    {name: 'United States', code: 'US'}
            ]
                        }
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
                 create_object:function(){

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
                    console.log('These are loaded')
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
            
            created(){
                this.check()

            }
}

</script>
<style lang='scss' scoped>
.p-multiselect {
    min-width: 15rem;
}

::v-deep(.multiselect-custom) {
    .p-multiselect-label:not(.p-placeholder) {
        padding-top: .25rem;
        padding-bottom: .25rem;
    }

    .country-item-value {
        padding: .25rem .5rem;
        border-radius: 3px;
        display: inline-flex;
        margin-right: .5rem;
        background-color: var(--primary-color);
        color: var(--primary-color-text);

        img.flag {
            width: 17px;
        }
    }
}
</style>
