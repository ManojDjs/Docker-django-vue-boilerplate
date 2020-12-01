<template>

     <Panel header="Custom Header" class="dark-panel">
	<div class="p-grid" v-if="q_status=='NR'">
	<div class="p-col-6 p-offset-3">
        <h1 v-if="q_status=='NR'">You haven't yet started questionary!</h1>
         <Button v-if="q_status=='NR'" type="button" v-on:click="getquestions" label="Start QA" icon="pi pi-pencil" class="p-button-warning p-d-block p-mx-auto" badgeClass="p-badge-danger" /> 
    </div>
	</div>
    <div class="p-d-flex p-flex-column" v-if="q_status=='EDIT'">
        <div p-mb-2>
        <h1 v-if="q_status=='EDIT'">Start Answering the questions!</h1>
        </div>
         <div p-mb-2 >
         <div class='p-grid'>
         <div class='p-col-12 p-md-6 p-lg-6  p-mx-auto' v-for="(value,index) in questions" v-bind:key="index">
        <div class='p-pl-3' > 
                            <label for="firstname"><h1>{{ value.question_no }}.{{ value.question }}</h1></label>
                            <!-- <RadioButton v-if='value.question_type=="Options"' :id="category.key" name="category" :value="category" v-model="selectedCategory" :disabled="category.key === 'R'" /> -->
                            </div>
                            </div>
         </div>
         </div>
    
	</div>
     </Panel>
</template>
<script>
import axios from 'axios';
import { mapState,mapActions,mapMutations } from 'vuex'
export default {
    data(){
        return{
            link:'I_ISQ/',
            value:this.$store.state.user,
            questions:[],
           city: null,
            categories: [{name: 'Never', key: 'A'}, {name: 'often', key: 'M'}, {name: 'sometimes', key: 'P'}, {name: 'always', key: 'R'}],
            selectedCategory: null
        }
    },
    computed:mapState([
        'q_status',
        'user',
        'iso_data',
        'token'
    ]),
    methods:{


        generatekey(questions){
          
            for(const q in questions){
                console.log(questions[q])

            }


        },
        ...mapActions([
            'check'
        ]),
        ...mapMutations([
    'iso_status_check'

        ]
        ),
        change_status(s){
            this.iso_status_check(s)

        },
        sttaus_check(){
            this.check(this.link)
            // this.value=this.$store.getters.getiso_data;
        },
        getquestions(){
            this.change_status('EDIT')
             const config = {
        method: "GET",
        headers: {
          'content-type': 'application/json',
          'Authorization': 'Token'+' '+this.token
        }
        }
        console.log(config)
      axios.get('http://127.0.0.1:8000/QA/ISQ/',config)
      .then(response => {
       console.log(response.data),
       this.questions=response.data;
       this.generatekey(this.questions)
      
      })

        }
    },
    watch:{
        q_status:function(){
            if(this.q_status=='NR'){
console.log('nR')
            }
            
        }

    },
    created(){
        this.sttaus_check()

    }
    
    
}
</script>
