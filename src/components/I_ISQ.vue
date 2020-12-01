<template>
<div>
    <h1>IMMUNE SYSTEM QUESTIONARY</h1>
    <Timeline :value="get_questions"  align="alternate">
		<template #content="slotProps">
			{{slotProps.item.question}}
            <!-- <Slider v-model="value"  :range='true' class='p-p-20'/> -->
		</template>
	</Timeline>
<ScrollPanel style="width: 100%; height: 100%" >
    {{ get_q_status }}
    <!-- {{ get_questions }}
    {{ get_qa }}
	<h5>Alternate Align</h5> -->

</ScrollPanel>
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
            value: [0]
           
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
                
            }

        },
        created(){
            this.check()

        }
       
    

    
}
</script>
<style scoped>

.custom .p-scrollpanel-wrapper {
    border-right: 9px solid #f4f4f4;
}

.custom .p-scrollpanel-bar {
    background-color: #1976d2;
    opacity: 1;
    transition: background-color .3s;
}

.custom .p-scrollpanel-bar:hover {
    background-color: #135ba1;
}
</style>