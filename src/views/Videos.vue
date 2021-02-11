<template>
    <div class="Video">
        <h1> Welcome to Qigong Practice Videos and Practice Diary</h1>
                <div class="p-grid nested-grid p-shadow-6">  
                    <div class="p-col-4">
                        <h2 class="poster">
                        Use the first three videos below to learn the
                        three sections of the Qigong Lung
                        Strengthening Exercise.

                        The last video contains the whole sequence,
                        so you can skip the earlier videos once
                        you’re familiar with the sequence.

                        Try to practice the whole sequence at least
                        once a week plus of the parts as a shorter
                        practice at least another two times per week.

                        Ideally, we recommend that you practice
                        every day.
                        </h2>
                </div>
                <div class="p-col-8">
                    <div id='Player'>
                           <iframe v-if="selected==0"  width="800" height="500" src="https://www.youtube-nocookie.com/embed/nJVaQ6ORkoA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                           <iframe v-if="selected==1"  width="800" height="500" src="https://www.youtube-nocookie.com/embed/rILma2T1NBs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                           <iframe  v-if="selected==2"  width="800" height="500" src="https://www.youtube-nocookie.com/embed/HiLmost762M" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                           <iframe v-if="selected==3" width="800" height="500" src="https://www.youtube-nocookie.com/embed/9tmfBwyaQPA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>                      
                            </div>
                            <div class="flex-container">
                            <div v-for='(item,index) in videos' :key='index'>
                                
                                    <Button  class="p-button"  v-on:click="select_video(index)">
                                        Video {{ index+1 }}
                                    </Button>
                                </div>
                            </div>
                                                            
                
                </div>
                </div>
    </div>
</template>
<script>

export default {
    data(){
        return{
            selected:0,
            videos:[1,2,3,4]

        }
    },
    methods:{
        select_video(index){
            this.selected=index
        }
    }
     
    
}
</script>
<style scoped>
.Video{
    text-align: center;
}
.flex-container {
  display: flex;
}

.flex-container > div {
  background-color: #f1f1f1;
  margin: 10px;
  padding: 20px;
  font-size: 30px;
}
.poster{
    line-height: 50px;
}
#Player{

}
</style>