<template>
  <Menubar
    class="fixed w-full z-2 bg-indigo-700 text-primary-50"
    :model="afteritems"
    id="menu"
    v-if="token"
  >
    <template #start>
      <span
        class="inline-flex border-circle align-items-center justify-content-center bg-yellow-50 m-3"
        style="width: 30px; height: 30px"
        ><i
          class="pi pi-cog pi-spin text-indigo-900"
          style="font-size: 1.5rem"
        ></i></span
      ><span class="font-bold text-3xl md:text-2xl">EDUMOON</span>
    </template>

    <template #end>
      <Avatar
        image="https://avatars.githubusercontent.com/u/22208973?v=4"
        size="large"
        shape="circle"
        class="border-cyan-50 surface-overlay border-1 border-circle"
      />
    </template>
  </Menubar>
  <Menubar
    class="fixed w-full z-2 bg-surface-0 text-primary-50"
    :model="beforeitems"
    id="menu"
    v-else
  >
    <template #start>
      <span
        class="inline-flex border-circle align-items-center justify-content-center bg-yellow-50 m-3"
        style="width: 30px; height: 30px"
        ><i
          class="pi pi-cog pi-spin text-indigo-900"
          style="font-size: 1.5rem"
        ></i></span
      ><span class="font-bold text-3xl md:text-2xl">EDUMOON</span>
    </template>

    <template #end>
      <Avatar
        image="https://avatars.githubusercontent.com/u/22208973?v=4"
        size="large"
        shape="circle"
        class="border-cyan-50 surface-overlay border-1 border-circle"
      />
    </template>
  </Menubar>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      beforeitems: [
        {
          label: "Home",
          icon: "pi pi-fw pi-home",
          to: "/",
        },
        {
          label: "Login",
          icon: "pi pi-sign-in",
          to: "/Login",
        },

        {
          label: "Signup",
          icon: "pi pi-user-plus",
          to: "/Signup",
        },
      ],
      afteritems: [
        {
          label: "Dashboard",
          icon: "pi pi-fw pi-home",
          to: "/Dashboard",
        },
        {
          label: "Aggregator",
          icon: "pi pi-fw pi-briefcase",
          to: "/Demo",
        },

        {
          label: "Projects",
          icon: "pi pi-fw pi-bolt",
          to: "/Signup",
        },
      ],
    };
  },
  computed: {
    ...mapState(["token", "user", "heading"]),
  },
};
</script>
<style lang="scss" scoped>
/* .menu-utilisateur {
  background-color: white;
  height: 30px;
} */

.p-menubar {
  background-color: #4511b5;
  padding: 20px;
  align-items: center;
}

.p-menubar .p-menubar-root-list > .p-menuitem > .p-menuitem-link {
  color: #168554 !important;
}

.p-menubar .p-menuitem-link {
  color: #168554 !important;
}
.p-menubar .p-menuitem {
  color: #168554 !important;
}
.p-menubar .p-menuitem-content {
  color: #168554 !important;
}
</style>
