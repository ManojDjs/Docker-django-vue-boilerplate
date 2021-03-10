<template>
    <div class="Dairy">
        <h1>Diary</h1>
        <Toast position="center" />
        <div class="p-p-3 card">
    <Button type="Button" icon="pi pi-book" label="Add Dairy" v-on:click="edit_mode_off" class="p-mr-2" />
    <Button type="Button" icon="pi pi-pencil" label="Exisitng Dairy" v-on:click="edit_mode"  class="p-button-danger"/>
        </div>
        <div class=" p-shadow-5" v-if="edit=='OFF'">
            <div v-for='(item,index) in Dairy_Answers' :key='index'>
            <Card style="width:100%">
            <template #header>
            </template>
            <template #title>
              <h5>  {{ item.Text }} </h5>
            </template>
            <template subtitle>
            </template>
            <template #content>
                <Textarea v-model="item.answer" :autoResize="true" rows="5" cols="50" />
            </template>
            <template #footer>
                <Button icon="pi pi-check" label="Save" v-on:click="submit_dairy(item.id,item.answer)" />
               
            </template>
            </Card>
            </div>
        </div>
        <div class=" p-shadow-5" v-if="edit=='ON'">
        <ScrollPanel style="width: 100%; height: 900%">
            <div v-for='(item,index) in Exisitng_dairy' :key='index'>
            <Card style="width:100%">
            <template #header>
            </template>
            <template #title>
                {{ item.Date }}
            </template>
            <template subtitle>
                <h1>manoj</h1>
            </template>
            <template #content>
                <p>{{item.Dairy_Text }}</p>
            </template>
            <template #footer>
                <Button icon="pi pi-check" label="Edit" v-on:click="update_dairy(item.id,item.Dairy_label,item.Dairy_Text)"/>
                <Button icon="pi pi-trash" label="Delete" v-on:click="delete_dairy(item.id)" class="p-button-secondary" style="margin-left: .5em" />
            </template>
            </Card>
         </div>
        </ScrollPanel>
            <Dialog header="Edit Below Dairy" v-model:visible="display" style="width:90%">
                <h1>Question</h1>
                 {{ editqsn}}
                <h1>Your dairy</h1>
                <Textarea v-model="edittext" :autoResize="true" rows="5" cols="50" />
                <Divider/>
                <Button icon="pi pi-save" label="Submit" class="p-button-secondary" style="margin-left: .5em" v-on:click="finalupdate" />
          </Dialog>

        </div>
        
    </div>
</template>
<script>
import { mapState } from 'vuex';
import Json from "@/assets/endpoints.json"
import axios from 'axios'
export default {
     data(){
        return{
            
            dairy_label_link:Json[0]['Course']['DAIRYLABLE'],
            dairy_link:Json[0]['Course']['DAIRY'],
            server:Json[0]['Course']['SERVER'],
            dairy_update_link:Json[0]['Course']['DAIRYUPDATE'],
            course_content:[],
            video_link:'',
            Dairy_text:'',
            Dairy:'',
            Dairy_labels:[],
            Dairy_Answers:[],
            Exisitng_dairy:[],
            edit:"OFF",
            display:false,
            edittext:"",
            editqsn:"",
            editid:null
            
         
        }
    },
    methods:{
        delete_dairy(id){
            const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.delete(this.server+this.dairy_update_link+id,{'headers':headers}
            ).then(resp=>{
                console.log(resp.status)
                this.get_existing_dairy()
                 
                
            })
        },
         create_object(){
                     var i;
                // console.log(this.get_questions.data) checking questions
                    for(i=0;i<this.Dairy_labels.length;i++){
                    
                        
                        this.Dairy_Answers.push({
                            "id":this.Dairy_labels[i]['id'],
                            "answer": "",
                            
                            "Text": this.Dairy_labels[i]['Text'],
                            "DairyNumber":this.Dairy_labels[i]['DairyNumber'],
                            
                        })
                      }
                    //   console.log(this.Dairy_Answers)
                      },
        get_dairy_labels(){
             const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.get(this.server+this.dairy_label_link,{'headers':headers}
            ).then(resp=>{
                // console.log("im in dairy labels")
                // console.log(resp.data)
                this.Dairy_labels=resp.data
                this.create_object()
                
            })
        },
        get_existing_dairy(){
            const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.get(this.server+this.dairy_link,{'headers':headers}
            ).then(resp=>{
                this.Exisitng_dairy=resp.data
                
            })
        },
        submit_dairy(id,text){
            const headers={
                'Authorization': 'Token'+' '+this.token
                    }
             axios.post(this.server+this.dairy_link,
              {"Dairy_label":id,
                "Dairy_Text": text,
                "Wrote_by": this.uid
                  
              },
              {'headers':headers})
            .then(resp => {
                    if(resp.status==201){
                        
                        this.$toast.add({severity:'success', summary: 'Dairy submited ', detail:'successfully , submitted your dairy', life: 3000}),
                        this.get_existing_dairy()
                        this.edit='ON'
                        

                    }
                   })
        },
       
        update_dairy(id,qsn,txt){
            this.display=true
            this.edittext=txt
            this.editqsn=qsn
            this.editid=id

        },
        finalupdate(){
             const headers={
                'Authorization': 'Token'+' '+this.token
                    }
             axios.put(this.server+this.dairy_update_link+this.editid,
            {
                "id":this.editid,
                "Dairy_label":this.editqsn,
                "Dairy_Text": this.edittext,
                "Wrote_by": this.uid
                
            },{'headers':headers})
          .then(resp => {
              if(resp.status==200){
                  this.$toast.add({severity:'success', summary: 'updated ', detail:'successfully , updated your dairy', life: 3000})
                 this.edittext="",
                 this.editqsn="",
                 this.editid=null,

                 this.get_existing_dairy()
                 this.display=false
              }
          })

        },
        edit_mode(){
            this.edit="ON"

        },
        edit_mode_off(){
            this.edit="OFF"
            this.Dairy_labels=[]
            this.Dairy_Answers=[]
            this.get_dairy_labels()
            

        }
    },
    computed:{
    ...mapState([
      'token',
      'user',
      'uid',
      'heading',
      'height',
      'course',
    ])
     },
     created(){
         this.get_dairy_labels()
         this.get_existing_dairy()
     }
    
}
</script>

<style scoped>
.Dairy{
    text-align:center;
}
</style>