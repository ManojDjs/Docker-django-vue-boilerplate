import { createStore } from 'vuex';
import axios from 'axios'

export default createStore({

  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user : {}
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
  },
  getters:{
    gettoken:state=>state.token,
    isLoggedIn: state => !!state.token,
  authStatus: state => state.status,
    
  },
  actions: {
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
          const user = resp.data.user
          localStorage.setItem('token', token)
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
      
    
  }

  
},
  modules: { 
  }
})
