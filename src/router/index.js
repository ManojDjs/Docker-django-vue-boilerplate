import { createWebHistory, createRouter } from "vue-router";
import Login from "@/views/Login.vue";
import LogOut from "@/views/LogOut.vue";
import Signup from "@/views/Signup.vue";
import About from "@/views/About.vue";
import Dashboard from "@/views/Dashboard.vue";
import RegistrationMessage from "@/views/RegistrationMessage.vue";
import I_ISQ from "@/components/I_ISQ.vue";

const routes = [
  {
    path: "/I_ISQ",
    name: "I_ISQ",
    component: I_ISQ,
  },
  {
    path: "/",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/Dashboard",
    name: "Dashboard",
    component: Dashboard,
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
    path: "/LogOut",
    name: "LogOut",
    component: LogOut,
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