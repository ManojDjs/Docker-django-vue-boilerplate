<template>
<div>
    <h1>Data visualization</h1>
    <h2> immune system questionnairre</h2>
    <Chart type="radar" :data="isq_data" />

</div>
</template>
<script>
import Json from "@/assets/endpoints.json"
import axios from 'axios'
import { mapState } from 'vuex';
export default {
    data(){
        return{
            server:Json[0]['SERVER']['SERVER'],
            isq_inital:Json[0]['ISQ']['Total'],
            isq_final:Json[0]['FISQ']['Total'],
            isq_status:false,
            mwb_status:false,
            wbm_status:false,
            isq1:[],
            isq2:[],
            isq_data:{
                labels:[],
                datasets:[
                    {
						label: 'My inital dataset',
						backgroundColor: 'rgba(179,181,198,0.2)',
						borderColor: 'rgba(179,181,198,1)',
						pointBackgroundColor: 'rgba(179,181,198,1)',
						pointBorderColor: '#fff',
						pointHoverBackgroundColor: '#fff',
						pointHoverBorderColor: 'rgba(179,181,198,1)',
						data: []
					},
					{
						label: 'My final dataset',
						backgroundColor: 'rgba(255,99,132,0.2)',
						borderColor: 'rgba(255,99,132,1)',
						pointBackgroundColor: 'rgba(255,99,132,1)',
						pointBorderColor: '#fff',
						pointHoverBackgroundColor: '#fff',
						pointHoverBorderColor: 'rgba(255,99,132,1)',
						data: []
					}
                ]
            },
            mwb1:[],
            mwb2:[],
            wbm1:[],
            wbm2:[],
        }
    },
      computed:{
    ...mapState([
      'token',
      'user',
      'heading'
    ])
      },
    methods:{
        get_isq(){
            const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.get(this.server+this.isq_inital,{'headers':headers}
            ).then(resp=>{
                console.log(resp.data)
                if(resp.data[0]['ISQ']['total_answers']==resp.data[0]['ISQ']['total_questions']){
                    this.isq1=resp.data[0]['ISQ']
                    let result = this.isq1.map(a => a.answer);
                    console.log(result)
                    this.isq_data['datasets'][0]['data']=result

                }
            })
              axios.get(this.server+this.isq_final,{'headers':headers}
            ).then(resp=>{
                console.log(resp.data)
                if(resp.data[0]['FISQ']['total_answers']==resp.data[0]['FISQ']['total_questions']){
                    this.isq2=resp.data[0]['FISQ']
                    let result = this.isq2.map(a => a.answer);
                    console.log(result)
                    this.isq_data['datasets'][1]['data']=result
                    let lables=this.isq2.map(a=>a.question_name.question)
                     this.isq_data['labels']=lables

                }
            })
            
        }
    },
    created(){
        this.get_isq()
    }
}
</script>