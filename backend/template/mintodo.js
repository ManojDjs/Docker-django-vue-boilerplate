Vue.component('click-btn',{
  template:'<button type="button" class="btn btn-secondary btn-lg btn-block" @click="count++">{{count}}</button>',
  data(){
    return {count:0}
  }
})
Vue.component('plan-picker',{
  template:'#plan-picker-template',
  data(){
    return {goals: ['college','job','food cooking'],
    isselected:null}
  },
  methods:{
    selected(plan){
      this.isselected=plan,
      console.log(plan)
    }
  }

})



Vue.component('plan',{
  template:'#plan-template',
  props:{name:{ type:String,
                required:true}},
  data(){
    return {
      selected:false
    }
  },
  methods:{
    select(){
      this.$emit('select',this.name)
      this.selected=true
    }
  }
})
var app=new Vue({
  el:"#app",
  data:
  {
    plansmain: ['college','job','food cooking'],
  }
})