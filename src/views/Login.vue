<template>
  <div class="login">
    <div
      class="mt-6 max-w-screen flex align-items-center justify-content-center"
    >
      <Nav></Nav>
    </div>
    <Toast position="top-right" />
    <div class="block-content">
      <div
        class="surface-ground px-4 py-8 md:px-6 lg:px-8 flex align-items-center justify-content-center"
      >
        <div class="surface-card p-4 shadow-2 border-round w-full lg:w-6">
          <div class="text-center mb-5">
            <img
              src="images/blocks/logos/hyper.svg"
              alt="Image"
              height="50"
              class="mb-3"
            />
            <div class="text-900 text-3xl font-medium mb-3">Welcome Back</div>
            <span class="text-600 font-medium line-height-3"
              >Don't have an account?</span
            ><a
              class="font-medium no-underline ml-2 text-blue-500 cursor-pointer"
              >Create today!</a
            >
          </div>
          <div>
            <label for="email1" class="block text-900 font-medium mb-2"
              >Email</label
            ><input
              class="p-inputtext p-component w-full mb-3"
              id="email1"
              type="text"
              v-model="email"
              placeholder="Email address"
            /><label for="password1" class="block text-900 font-medium mb-2"
              >Password</label
            ><input
              class="p-inputtext p-component w-full mb-3"
              id="password1"
              type="password"
              v-model="password"
              placehoder="Password"
            />
            <div class="flex align-items-center justify-content-between mb-6">
              <div class="flex align-items-center">
                <div class="p-checkbox p-component mr-2" id="rememberme1">
                  <div class="p-hidden-accessible">
                    <input type="checkbox" class="" />
                  </div>
                  <div class="p-checkbox-box">
                    <span class="p-checkbox-icon"></span>
                  </div>
                </div>
                <label for="rememberme1">Remember me</label>
              </div>
              <a
                class="font-medium no-underline ml-2 text-blue-500 text-right cursor-pointer"
                >Forgot password?</a
              >
            </div>
            <button
              class="p-button p-component w-full"
              type="button"
              aria-label="Sign In"
            >
              <!----><span
                class="pi pi-user p-button-icon p-button-icon-left"
              ></span
              ><span class="p-button-label" v-on:click="login">Sign In</span
              ><!----><span class="p-ink" role="presentation"></span>
            </button>
          </div>
        </div>
      </div>
      <!---->
    </div>

    <Footer></Footer>
  </div>
</template>
<script>
// import axios from 'axios'
import Nav from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
export default {
  data: () => ({
    email: "",
    emailvald: "p-button-warning",
    password: "",
  }),
  components: {
    Nav,
    Footer,
  },
  methods: {
    to_login() {
      this.$router.push("/Signup");
    },
    login() {
      if ((this.email != null) & (this.password != null)) {
        let email = this.email;
        let password = this.password;
        console.log(this.email, this.password);
        this.$store
          .dispatch("login", { email, password })
          .then(() => this.$router.push("/Dashboard"))
          .catch((err) => console.log(err));
      } else {
        this.$toast.add({
          severity: "warning",
          summary: "Empty fields",
          detail: "All fields must be filled",
          life: 3000,
        });
      }
    },
    showSuccess() {
      this.$toast.add({
        severity: "error",
        summary: "Invalid credentials",
        detail: "if you dont have account try registration",
        life: 3000,
      });
      this.email = "";
      this.password = "";
    },
  },
  watch: {
    email: function (email) {
      var re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (re.test(email)) {
        console.log("matched");
        this.emailvald = "p-button-success";
      } else {
        this.emailvald = "p-button-danger";
      }
    },
  },
  created() {
    this.$store.dispatch("set_heading", "Login page");
  },
};
</script>
<style scoped>
.login {
  text-align: center;
}
#image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
#mark {
  padding-top: 30px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
}
</style>
