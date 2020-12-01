import { createStore } from 'vuex';
import axios from 'axios'

export default createStore({

  state: {
    status:'',
    token: localStorage.getItem('token') || '',
    user : localStorage.getItem('user') || '',
    q_status:null,
    demo:'',
    questions:[],
    f_questions:[],
    edit_status:null,
    question_answers:[],
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, token, user){
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_error(state){
      state.status = 'error'
    },
    logout(state){
      state.status = ''
      state.token = ''
    },
    check_q_status(state,status){
      state.q_status=status
    },
    get_qa(state,qa){
      state.question_answers=qa
    },
    get_questions(state,qu){
      state.questions=qu
    }
   
  },
  getters:{
    gettoken:state=>state.token,
    getuser:state=>state.user,
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    get_q_status: state => state.q_status,
    get_questions:state=>state.questions,
    get_f_questions:state=>state.f_questions,
    get_edit_status: state=>state.edit_status,
    get_qa:state=>state.question_answers

    
  },
  actions: {
    //  questions
    check_q_status({commit},link){
      console.log(this.state.token)
      
       const headers={
         
          'Authorization': 'Token'+' '+this.state.token,

                  }
                   console.log(headers)
        axios.get('http://127.0.0.1:8000/'+link,{'headers':headers})
        .then(resp => {
          console.log(resp.data)
          if(resp.data.length==0){
            commit('check_q_status','NR')

          }
          else{
            commit('check_q_status','RF')
            commit('get_qa',resp.data)

          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    registeruser({commit},link){
      const headers={
         
        'Authorization': 'Token'+' '+this.state.token,

                }
                 console.log(headers)
      axios.post('http://127.0.0.1:8000/'+link,
        {
        "Answered_by": this.state.user
        },
        {'headers':headers})
      .then(resp => {
        console.log(resp.data)
        if(resp.data.length==0){
          commit('check_q_status','ER')

        }
        else{
          commit('check_q_status','RS')
          commit('get_qa',resp.data)

        }

      })
      .catch(err => {
        console.log(err)
      })
    },
    questions_taker({commit},link){
      const headers={
         
        'Authorization': 'Token'+' '+this.state.token,

                }
                 console.log(headers)
      axios.get('http://127.0.0.1:8000/'+link,{'headers':headers})
      .then(resp => {
        console.log(resp.data)
        if(resp.data.length==0){
          commit('check_q_status','ERQ')

        }
        else{
          commit('get_questions',resp.data)

        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  


    // authentication modules

    login({commit}, user){
      console.log(user)
      const config={
        headers:{
          'content-type':'application/json'
                  }
                   }
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.post('http://127.0.0.1:8000/api/accounts/login/',{username:user.email,password:user.password},config)
        .then(resp => {
          console.log(resp.data)
          const token = resp.data.token
          const user = resp.data.username
          console.log(user)
          localStorage.setItem('token', token)
          localStorage.setItem('user', user)

          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', token, user)
          resolve(resp)
        })
        .catch(err => {
          commit('auth_error')
          localStorage.removeItem('token')
          reject(err)
        })
      })
  },
  logout({commit}){
    
      commit('logout')
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
      
    
  },
  
},
  modules: { 
  }
})
