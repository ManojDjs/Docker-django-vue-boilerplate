<template>
    <div class="p-p-5 p-shadow-5" >       
    <h2>Course Page</h2>
    <h1> {{  course }}</h1>
    {{ height }}
    <Splitter layout="vertical" >
        
        <SplitterPanel style="height:500px">
            <Splitter>
                    <SplitterPanel :size="40">
                        <VC
                        width='800'
                        height='500'
                        />
                        <video
                            id=”my-player”
                            class=”video-js”
                            controls
                            preload=”auto”
                            poster=”//vjs.zencdn.net/v/oceans.png”
                            data-setup=’{}’>
                            </video>
                    </SplitterPanel>
                    <SplitterPanel>
                        <ScrollPanel style="width: 100%; height: 500px" class="custom">
                        <!-- {{course_content['Course_week']}} -->
                        <div v-for='(item,index) in course_content["Course_week"]' :key='index'>
                        <Panel :toggleable="true">
                            <template #header>
                                <h1>{{item.Week_number}}.{{ item.Week_name }}</h1>
                            </template>
                            <div v-for='(video,index) in item.Video_Week' :key='index'>
                            <Button  class="p-button-text" v-on:click="video_selected(video.Video_URL,video.Video_week,video.slug,video.Dairy_Description)">
                            {{index+1}}.{{ video.Video_Name }}
                            </Button>
                            </div>
                        </Panel>
                        </div>
                        </ScrollPanel>
                    </SplitterPanel>
            </Splitter>
        </SplitterPanel> 



        
        <SplitterPanel>
        <h1 id="course">Dairy</h1>
           {{video_link}}
            {{Dairy_text}}
            {{Dairy_link}}
        </SplitterPanel>
    </Splitter>  
    </div>
</template>
<script>
import { mapState } from 'vuex';
import VC from "@/components/VideoPlayer.vue";
import Json from "@/assets/endpoints.json"
import axios from 'axios'
export default {
    data(){
        return{
            course_link:Json[0]['Course']['LIST'],
            server:Json[0]['Course']['SERVER'],
            dairy:Json[0]['Course']['DAIRY'],
            course_content:[],
            video_link:'',
            Dairy_text:'',
            Dairy:'',
            Dairy_link:'',
            Dairy_list:[]
         
        }
    },
    components:{
        VC
    },
    methods:{
        get_course_info(){
            const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.get(this.server+this.course_link+this.course,{'headers':headers}
            ).then(resp=>{
                console.log("im in course spec")
                console.log(resp.data)
                this.course_content=resp.data
                
            })
        },
        get_dairy(dairy_slug){
            const headers={
                'Authorization': 'Token'+' '+this.token
                    }
            axios.get(this.server+this.dairy+"?Dairy_Video="+2+"&Wrote_by="+this.uid,{'headers':headers}
            ).then(resp=>{
                console.log(dairy_slug)
                console.log(resp.data)
                
            })

        },
        video_selected(video_link,vid,dairy_slug,Description){
            this.video_link=video_link,
            this.Dairy_text=Description,
            this.Dairy_link=dairy_slug,
            this.get_dairy(vid)

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
        this.get_course_info()
     }
}
</script>
<style scoped>
#course{
    text-align: center;
}
</style>