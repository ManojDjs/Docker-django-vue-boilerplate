import { createWebHistory, createRouter } from "vue-router";
import Login from "@/views/Login.vue";
import Signup from "@/views/Signup.vue";
import About from "@/views/About.vue";
import RegistrationMessage from "@/views/RegistrationMessage.vue";

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
  {
    path: "/About",
    name: "About",
    component: About,
  },
  {
    path: "/RegistrationMessage",
    name: "RegistrationMessage",
    component: RegistrationMessage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;