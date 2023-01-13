<template>
  <div class="app relative" id="app">
    <router-view />
  </div>
</template>

<script>
// import Nav from "@/components/NavBar.vue";
export default {
  data() {
    return {
      myStyle: {
        backgroundColor: "#00000",
      },
    };
  },
  components: {
    // Nav,
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #155494;
  padding: 0%;
}
</style>