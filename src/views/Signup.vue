<template>
  <div class="Signup bg-indigo-50">
    <div
      class="mt-6 max-w-screen flex align-items-center justify-content-center"
    >
      <Nav></Nav>
    </div>

    <Toast position="top-right" />
    <!-- <Password v-model="val" /> -->

    <div class="surface-section">
      <div class="grid grid-nogutter">
        <div
          class="col-12 md:col-6 bg-no-repeat bg-cover p-8"
          style="background-image: url('images/blocks/contact/contact-2.jpg')"
        >
          <div class="text-2xl text-yellow-300 font-medium mb-6">
            Sign Up Today!
          </div>
          <div class="text-gray-300 line-height-3 mb-6">
            Signup today to see our quality products and work. Our Education
            platform is completely secured and supervised.
          </div>
          <a
            class="inline-flex align-items-center text-blue-300 font-bold no-underline cursor-pointer"
            ><span class="mr-3">View Address on Google Maps</span
            ><i class="pi pi-arrow-right"></i
          ></a>
          <ul class="list-none p-0 m-0 mt-6 text-white">
            <li class="flex align-items-center mb-3">
              <i class="pi pi-phone mr-2"></i><span>+123456789</span>
            </li>
            <li class="flex align-items-center mb-3">
              <i class="pi pi-twitter mr-2"></i><span>@prime_ng</span>
            </li>
            <li class="flex align-items-center">
              <i class="pi pi-inbox mr-2"></i
              ><span>contact@primetek.com.tr</span>
            </li>
          </ul>
        </div>
        <div class="col-12 md:col-6">
          <div class="p-fluid formgrid grid px-4 py-8 md:px-6 lg:px-8">
            <div class="field col-12 lg:col-6 mb-4">
              <input
                class="p-inputtext p-component py-3 px-2 text-lg"
                id="firstname"
                type="text"
                v-model="firstname"
                placeholder="First Name"
              />
            </div>
            <div class="field col-12 lg:col-6 mb-4">
              <input
                class="p-inputtext p-component py-3 px-2 text-lg"
                id="lastname"
                type="text"
                v-model="lastname"
                placeholder="Last Name"
              />
            </div>
            <div class="field col-12 mb-4">
              <input
                class="p-inputtext p-component py-3 px-2 text-lg"
                id="username"
                type="text"
                v-model="username"
                placeholder="User Name"
              />
            </div>
            <div class="field col-12 mb-4">
              <input
                class="p-inputtext p-component py-3 px-2 text-lg"
                id="email"
                type="email"
                v-model="email"
                placeholder="Email"
                :style="emailStyle"
              />
            </div>
            <div class="field col-12 lg:col-6 mb-4">
              <div class="p-float-label">
                <Password v-model="password">
                  <template #header>
                    <h6>Password Strength</h6>
                  </template>
                  <template #footer>
                    <Divider />
                    <p class="mt-2">Suggestions</p>
                    <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                      <li>At least one lowercase</li>
                      <li>At least one uppercase</li>
                      <li>At least one numeric</li>
                      <li>Minimum 8 characters</li>
                    </ul>
                  </template>
                </Password>
                <label for="password">Password</label>
              </div>
            </div>
            <div class="field col-12 lg:col-6 mb-4">
              <div class="p-float-label">
                <Password v-model="password2">
                  <template #header>
                    <h6>Password Strength</h6>
                  </template>
                  <template #footer>
                    <Divider />
                    <p class="mt-2">Suggestions</p>
                    <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                      <li>At least one lowercase</li>
                      <li>At least one uppercase</li>
                      <li>At least one numeric</li>
                      <li>Minimum 8 characters</li>
                    </ul>
                  </template>
                </Password>
                <label for="password">Confirm</label>
              </div>
            </div>
            <div class="col-12 text-right">
              <button
                class="p-button bg-green-700 p-component px-5 py-3 w-auto"
                type="button"
                aria-label="Submit"
                v-on:click="register"
              >
                <!----><span
                  class="pi pi-sign-in p-button-icon p-button-icon-left"
                ></span
                ><span class="p-button-label">Sign Up</span
                ><!----><span class="p-ink" role="presentation"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <Footer></Footer>
  </div>
</template>
<script>
import axios from "axios";
import Json from "@/assets/endpoints.json";
import Nav from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
export default {
  data() {
    return {
      server: Json[0]["SERVER"]["SERVER"],
      val: "",
      firstname: "",
      lastname: "",
      username: "",
      email: "",
      password: "",
      password2: "",
      emailStyle:
        "box-shadow: 0 2px 1px -1px rgba(0,0,0,.2), 0 1px 1px 0 rgba(0,0,0,.14), 0 1px 3px 0 rgba(0,0,0,.12);",

      errors: [],
      // reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
    };
  },
  components: {
    Nav,
    Footer,
  },
  methods: {
    to_signup() {
      this.$router.push("/Login");
    },
    register() {
      if (
        (this.username != null) &
        (this.firstname != null) &
        (this.lastname != null) &
        (this.password != null) &
        (this.email != null)
      ) {
        if (this.password == this.password2) {
          const config = {
            headers: {
              "content-type": "application/json",
            },
          };
          axios
            .post(
              this.server + "api/accounts/register/",
              {
                username: this.username,
                email: this.email,
                password: this.password,
                first_name: this.firstname,
                last_name: this.lastname,
              },
              config
            )
            .then((response) => {
              // console.log(response.status),
              console.log(response.data), console.log(response.data.token);
              // this.$store.getters.createToken(response.data.token)
              this.$router.push("/RegistrationMessage");
            })
            .catch((e) => {
              // console.log(e.response.status)
              console.log(e.response.data["username"]);
              if (e.response.status == 400) {
                this.$toast.add({
                  severity: "error",
                  summary: e.response.data,
                  detail: "Try again with different username",
                  life: 3000,
                });
              }
            });
        } else {
          this.$toast.add({
            severity: "error",
            summary: 'Invalid Email or password didn"t matched',
            detail: "provice valid email",
            life: 3000,
          });
        }
      } else {
        this.$toast.add({
          severity: "error",
          summary: "Empty fields",
          detail: "All fields must be filled",
          life: 3000,
        });
      }
    },
    validateemail() {
      var re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (re.test(this.email)) {
        return true;
      } else {
        return false;
      }
    },
  },
  watch: {
    email(email) {
      var re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (re.test(email)) {
        console.log(email);
        this.emailStyle =
          "box-shadow: 0 2px 1px -1px rgba(0,0,0,.2), 0 1px 1px 0 rgba(0,0,0,.14), 0 1px 3px 0 rgba(0,0,0,.12);";
      } else {
        this.emailStyle =
          "box-shadow: 0 2px 1px -1px rgba(0,0,0,.2), 0 1px 1px 0 rgba(0,0,0,.14), 0 1px 3px 0 rgba(0,0,0,.12);background-color: var(--red-500);";
      }
    },
  },
  created() {
    this.$store.dispatch("set_heading", "Signup page");
  },
};
</script>
<style scoped>
#n {
  width: 20%;
  height: 50px;
  background-color: black;
  padding: 10px;
}
.Signup {
  text-align: center;
}
#username {
  height: 0.4in;
}
/* #signup{
  border: 1px solid rgb(110, 150, 236);
} */
.p-grid {
  padding-top: 0.5in;
}
</style>
