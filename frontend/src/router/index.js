import { createWebHistory, createRouter } from "vue-router";
import Login from "@/views/Login.vue";
import Signup from "@/views/Signup.vue";

const routes = [
  {
    path: "/",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;