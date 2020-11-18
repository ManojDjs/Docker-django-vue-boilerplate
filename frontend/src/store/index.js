import { createStore } from 'vuex'

export default createStore({
  state: {
    'token':''
  },
  mutations: {
    settoken(state,payload){
      state.token=payload;


    }
  },
  getters:{
    gettoken:state=>state.token,
    createToken:state=>(arg)=>{
      state.token=arg
      return state.token
    }

  },
  actions: {
  },
  modules: { 
  }
})
