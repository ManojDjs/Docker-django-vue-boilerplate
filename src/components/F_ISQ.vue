<template>
<div>
    <h1>IMMUNE SYSTEM QUESTIONARY</h1>
<!-- <ScrollPanel style="width: 100%; height: 600px" class="custombar1"> -->
    <w-app class="block">
     <w-card title="Terms and conditions">
  Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rem dolore delectus,
  quisquam ipsa laudantium esse consequatur itaque similique et eligendi eum voluptas
  odit dolor labore eveniet at vel sequi nostrum.

  <template #actions>
    <div class="spacer"></div>
    <w-button bg-color="error" class="mr2">I disagree</w-button>
    <w-button bg-color="success">I agree</w-button>
  </template>
</w-card>
    </w-app>
    
   <div class="p-fluid p-formgrid p-grid" v-for='(item,index) in Answers_KV' :key='index'>
    
    <div class="p-field p-col" >
            <h3>{{ item.question_name }}</h3>
            <div class="demo-container p-pl-6 p-pr-6">

            <Dropdown v-model="item.answer" :options="oprions" optionLabel="name" placeholder="please indicate " v-if='item.question_type=="Options"'/>
            <Slider v-model="item.answer" v-if="item.question_type=='Slider'" class="p-p-2"/>
            
            <SelectButton v-model="item.answer" :options="yesno" v-if="item.question_type=='YESNO'" />
            </div>
    </div>
</div>
 
<!-- </ScrollPanel> -->
<div class="demo-container p-p-2">
        <Button type="button" label="Submit" class=" p-pr-5 p-pl-5" />
    </div>

</div>
</template>
<script>
import { mapGetters } from 'vuex'
 import Json from "@/assets/endpoints.json"
export default {
    data(){
        return{
            isq_link:Json[0]['ISQ'],
            total:Json[0]['ISQ']['Total'],
            questionlink:Json[0]['ISQ']['Questions'],
            status:this.$store.getters.get_q_status,
            value: [0],
            Answers_KV:[],
            yesno: ['YES', 'NO'],
            oprions: [
			{name: 'Never', code: 1},
			{name: 'sometimes', code: 2},
			{name: 'Regularly', code: 3},
			{name: 'Often', code: 4},
			{name: 'Almost Always', code: 5}
		]    
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
         register(){
             let link=this.total
             console.log(link)

         },
         create_object(){

             var i;
                console.log(this.get_questions.data)
            for(i=0;i<this.get_questions.length;i++){
               
                   
                this.Answers_KV.push({
                    "answer": 0,
                    "main_question_set":this.getuser,
                    "question_name": this.get_questions[i]['question'],
                    "question_type":this.get_questions[i]['question_type'],
                    "answer_by": this.getuser
                })
            }
        console.log(this.Answers_KV)


         }

        },
         watch:{
            get_q_status(){
                if(this.get_q_status=='NR'){
                    this.$store.dispatch('registeruser',this.total)
                }
                if(this.get_q_status=="RS"){
                    this.$store.dispatch('questions_taker',this.questionlink)
                }
            },
            get_qa(){
                if(this.get_qa[0]['total_answers']=='0'){
                    this.$store.dispatch('questions_taker',this.questionlink)
                    
                }
                
            },
            get_questions(){
                console.log('i triggered len')
                if(this.get_questions.length>1){
                    this.create_object()
                }
            }

        },
        created(){
            this.check()
            // this.create_object()

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