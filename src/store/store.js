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
    uid: localStorage.getItem('uid') || '',
    mqid: localStorage.getItem('mqid') || ''
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, token, user,uid){
      state.status = 'success'
      state.token = token
      state.user = user
      state.uid=uid
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
    get_qa(state,qa,mqid){
      state.question_answers=qa
      state.mqid=mqid
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
                  //  console.log(headers)
        axios.get('http://127.0.0.1:8000/'+link,{'headers':headers})
        .then(resp => {
          console.log(resp.data)
          if(resp.data.length==0){
            commit('check_q_status','NR')  //for no records found status

          }
          else{
            if(resp.data[0]['total_answers']==resp.data[0]['total_questions']){
              const mqid=resp.data[0].id
              localStorage.setItem('mqid', mqid)
              console.log(mqid)
              commit('check_q_status','EDIT') //for records found status
              commit('get_qa',resp.data,mqid)
            }
            else{
              const mqid=resp.data[0].id
              localStorage.setItem('mqid', mqid)
              console.log(mqid)
              commit('check_q_status','RF') //for records found status
              commit('get_qa',resp.data,mqid)
  
            }
           
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
                //  console.log(headers)
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
                //  console.log(headers)
      axios.get('http://127.0.0.1:8000/'+link,{'headers':headers})
      .then(resp => {
        console.log(resp.data)
        if(resp.data.length==0){
          commit('check_q_status','ERQ')

        }
        else{
          commit('get_questions',resp.data)
          commit('check_q_status','RS')

        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  submitanswers({commit},subparam){
            console.log(subparam)
            commit('check_q_status','RS')
            const headers={
                
              'Authorization': 'Token'+' '+this.state.token,

                      }
            console.log(headers)
            var i
            var check=0
            for(i=0;i<subparam.submisiondata.length;i++){
              console.log(subparam.submisiondata[i]['answer'])
              console.log( this.state.uid )
              console.log( this.state.mqid )
              
            axios.post('http://127.0.0.1:8000/'+subparam.link,
              {
            "answer": subparam.submisiondata[i]['answer'],
            "main_question_set": localStorage.getItem('mqid') ,
            "question_name": subparam.submisiondata[i]['qid'],
            "answer_by": this.state.uid
                  
              },
              {'headers':headers})
            .then(resp => {
                    console.log(resp.data)
                    if(resp.data.length==0){
                      check=check+1
                    }
                    else{
                    console.log(resp.data)

                    }
                    
                  })

                }
                if(check==0){
                  commit('check_q_status','EDIT')
                }

  },
 save({commit},subparam){
          console.log(subparam)
          // commit('check_q_status','RS')
          const headers={
              
            'Authorization': 'Token'+' '+this.state.token,

                    }
          console.log(headers)
          var i
          var check=0
          for(i=0;i<subparam.submisiondata.length;i++){
            console.log(subparam.submisiondata[i]['answer'])
            console.log( this.state.uid )
            console.log( this.state.mqid )
            
          axios.put('http://127.0.0.1:8000/'+subparam.link+subparam.submisiondata[i]['editid'],
            {
              "id":subparam.submisiondata[i]['editid'],
          "answer": subparam.submisiondata[i]['answer'],
          "main_question_set": localStorage.getItem('mqid') ,
          "question_name": subparam.submisiondata[i]['qid'],
          "answer_by": this.state.uid
                
            },
            {'headers':headers})
          .then(resp => {
                  console.log(resp.data)
                  if(resp.data.length==0){
                    check=check+1
                  }
                  else{
                  console.log(resp.data)
                  commit('check_q_status','EDIT')

                  }
                  
                })

              }
              if(check==0){
                commit('check_q_status','EDIT')
              }

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
          const uid=resp.data.id
          console.log(user)
          localStorage.setItem('token', token)
          localStorage.setItem('user', user)
          localStorage.setItem('uid', uid)
          console.log(uid),
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', token, user,uid)
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
