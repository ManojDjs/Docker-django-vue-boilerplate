<template>
<div class="course">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/uOtgJmJIsio" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</div>
</template>
<script>
// import LazyYoutubeVideo from 'vue-lazy-youtube-video'
export default {
    props:['width','height','link'],
    
}
</script>
<style scoped>
.course{
    text-align: center;
}
</style>