import { createStore } from "vuex";
import axios from "axios";
import Json from "@/assets/endpoints.json";
export default createStore({
  state: {
    server: Json[0]["SERVER"]["SERVER"],
    status: "",
    token: localStorage.getItem("token") || "",
    user: localStorage.getItem("user") || "",
    uid: localStorage.getItem("uid") || "",
    course: localStorage.getItem("course") || "",
    current_course: localStorage.getItem("current_course") || "",
  },
  mutations: {
    set_course(state, course) {
      state.course = course;
    },
    set_current_course(state, current_course) {
      state.current_course = current_course;
    },
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, token, user, uid) {
      state.status = "success";
      state.token = token;
      state.user = user;
      state.uid = uid;
    },
    auth_error(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
    },
  },
  getters: {
    gettoken: (state) => state.token,
    getuser: (state) => state.user,
    isLoggedIn: (state) => !!state.token,
    authStatus: (state) => state.status,
    get_course: (state) => state.course,
    get_current_course: (state) => state.current_course,
  },
  actions: {
    // set_heading({ commit }, heading) {
    //   commit("set_heading", heading);
    // },
    set_course({ commit }, course) {
      commit("set_course", course);
      localStorage.setItem("course", course);
    },
    current_course({ commit }, current_course) {
      // commit("set_course", current_course);
      localStorage.setItem("current_course", current_course);
      commit("set_current_course", current_course);
    },

    // authentication modules

    login({ commit }, user) {
      console.log(user);
      const config = {
        headers: {
          "content-type": "application/json",
        },
      };
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios
          .post(
            this.state.server + "api/accounts/login/",
            { username: user.email, password: user.password },
            config
          )
          .then((resp) => {
            console.log(resp.data);
            const token = resp.data.token;
            const user = resp.data.username;
            const uid = resp.data.id;
            console.log(user);
            localStorage.setItem("token", token);
            localStorage.setItem("user", user);
            localStorage.setItem("uid", uid);
            console.log(uid),
              (axios.defaults.headers.common["Authorization"] = token);
            commit("auth_success", token, user, uid);
            resolve(resp);
          })
          .catch((err) => {
            commit("auth_error");
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    logout({ commit }) {
      commit("logout");
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
    },
  },
  modules: {},
});
