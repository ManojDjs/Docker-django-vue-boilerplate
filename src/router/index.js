import { createWebHistory, createRouter } from "vue-router";
import Login from "@/views/Login.vue";
import LogOut from "@/views/LogOut.vue";
import Signup from "@/views/Signup.vue";
import About from "@/views/About.vue";
import NavBar from "@/views/NavBar.vue";
import Dashboard from "@/views/Dashboard.vue";
import RegistrationMessage from "@/views/RegistrationMessage.vue";
import I_ISQ from "@/components/I_ISQ.vue";
import F_ISQ from "@/components/F_ISQ.vue";
import I_MWB from "@/components/I_MWB.vue";
import I_WBMNU from "@/components/I_WBMNU.vue";
import F_MWB from "@/components/F_MWB.vue";
import F_WBMNU from "@/components/F_WBMNU.vue";
import Profile from "@/components/Profile.vue";
import DV from "@/components/DV.vue";

const routes = [
  {
    path: "/DV",
    name: "DV",
    component: DV,
  },
  {
    path: "/Profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/F_WBMNU",
    name: "F_WBMNU",
    component: F_WBMNU,
  },
  {
    path: "/F_MWB",
    name: "F_MWB",
    component: F_MWB,
  },
  {
    path: "/I_WBMNU",
    name: "I_WBMNU",
    component: I_WBMNU,
  },
  {
    path: "/I_MWB",
    name: "I_MWB",
    component: I_MWB,
  },
  {
    path: "/NavBar",
    name: "NavBar",
    component: NavBar,
  },
  {
    path: "/F_ISQ",
    name: "F_ISQ",
    component: F_ISQ,
  },
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