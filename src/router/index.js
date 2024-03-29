import { createWebHistory, createRouter } from "vue-router";
import Login from "@/views/Login.vue";
import LogOut from "@/views/LogOut.vue";
import Signup from "@/views/Signup.vue";
import sample from "@/views/sample.vue";
import Course from "@/views/Course.vue";
import About from "@/views/About.vue";
import NavBar from "@/components/NavBar.vue";
import Dashboard from "@/views/Dashboard.vue";
import RegistrationMessage from "@/views/RegistrationMessage.vue";
import ISQ from "@/components/ISQ.vue";
import F_ISQ from "@/components/F_ISQ.vue";
import I_MWB from "@/components/I_MWB.vue";
import I_WBMNU from "@/components/I_WBMNU.vue";
import F_MWB from "@/components/F_MWB.vue";
import F_WBMNU from "@/components/F_WBMNU.vue";
import Profile from "@/components/Profile.vue";
import DV from "@/components/DV.vue";
import Videos from "@/views/Videos.vue";
import Demo from "@/views/Demo.vue";
import Dairy from "@/views/Dairy.vue";

const routes = [
  {
    path: "/sample",
    name: "sample",
    component: sample,
  },
  {
    path: "/Videos",
    name: "Videos",
    component: Videos,
  },
  {
    path: "/Dairy",
    name: "Dairy",
    component: Dairy,
  },
  {
    path: "/Demo",
    name: "Demo",
    component: Demo,
  },
  {
    path: "/DV",
    name: "DV",
    component: DV,
  },
  {
    path: "/Course",
    name: "Course",
    component: Course,
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
    path: "/ISQ",
    name: "ISQ",
    component: ISQ,
  },
  {
    path: "/Signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/Dashboard",
    name: "Dashboard",
    component: Dashboard,
    props: true,
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
  {
    path: "/",
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
