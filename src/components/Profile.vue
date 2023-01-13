<template>
  <div class="profile">
    <div
      class="mt-6 max-w-screen flex align-items-center justify-content-center"
    >
      <Nav></Nav>
    </div>
    <br />
    <br />
    <div class="grid">
      <div class="col-12 md:col-6 lg:col-6">
        <Card class="bg-white p-5">
          <template #header>
            <div class="uppercase text-yellow-700 font-medium text-xl mb-3">
              Profile Information
            </div>
            <div
              class="flex align-items-center justify-content-center flex-column md:flex-row"
            >
              <img :src="Image" class="" style="width: 90px; height: 90px" />
            </div>
          </template>
          <template #title>
            <span class="uppercase text-indigo-900 font-medium text-3xl"
              >{{ first_name }} {{ last_name }}</span
            >
          </template>
          <template #content>
            <div class="flex justify-content-center flex-wrap text-lm">
              <div class="mr-5 mt-3">
                <span class="font-medium text-100">USER NAME</span>
                <div class="text-purple-700 mt-2">{{ username }}</div>
              </div>
              <div class="mr-5 mt-3">
                <span class="font-medium text-100">PROJECTS</span>
                <div class="text-purple-700 mt-2">26</div>
              </div>
              <div class="mr-5 mt-3">
                <span class="font-medium text-100">ACTIVE</span>
                <div class="text-purple-700 mt-2" v-if="is_active">
                  <i class="pi pi-check" style="font-size: 1rem"></i>
                </div>
                <div class="text-purple-700 mt-2" v-else>
                  <i class="pi pi-times" style="font-size: 1rem"></i>
                </div>
              </div>
              <div class="mt-3">
                <span class="font-medium text-100">EMAIL</span>
                <div class="text-purple-700 mt-2">{{ email }}</div>
              </div>
            </div>
          </template>
          <template #footer>
            <Button icon="pi pi-check" label="Save" />
            <Button
              icon="pi pi-times"
              label="Cancel"
              class="p-button-secondary"
              style="margin-left: 0.5em"
            />
          </template>
        </Card>
      </div>

      <div class="col-12 md:col-6 lg:col-6">
        <div class="bg-white p-5">
          <div>
            <div class="uppercase text-yellow-500 font-medium text-xl mb-3">
              Profile
            </div>
            <div class="bg-white p-4 shadow-2 border-round">
              <div class="grid formgrid p-fluid">
                <div class="field mb-4 col-12">
                  <label for="nickname" class="font-medium">User Name</label
                  ><input
                    class="p-inputtext p-component"
                    id="nickname"
                    type="text"
                    v-model="username"
                  />
                </div>
                <div class="surface-100 mb-3 col-12" style="height: 2px"></div>
                <div class="field mb-4 col-12 md:col-6">
                  <label for="bio" class="font-medium">First Name</label
                  ><input
                    class="p-inputtext p-component"
                    id="nickname"
                    type="text"
                    v-model="first_name"
                  />
                </div>
                <div class="field mb-4 col-12 md:col-6">
                  <label for="bio" class="font-medium">Last Name</label
                  ><input
                    class="p-inputtext p-component"
                    id="nickname"
                    type="text"
                    v-model="last_name"
                  />
                </div>
                <div class="field mb-4 col-12 md:col-6">
                  <label for="avatar" class="font-medium">Avatar</label>
                  <div class="flex align-items-center">
                    <img
                      :src="Image"
                      class="mr-1"
                      style="width: 60px; height: 60px"
                    />
                    <div class="p-fileupload p-fileupload-basic p-component">
                      <span
                        class="p-button p-component p-fileupload-choose p-button-outlined p-button-plain"
                        tabindex="0"
                        ><span
                          class="p-button-icon p-button-icon-left pi pi-upload"
                        ></span
                        ><span class="p-button-label">Upload Image</span
                        ><input type="file" accept="image/*" /><span
                          class="p-ink"
                          role="presentation"
                        ></span
                      ></span>
                    </div>
                  </div>
                </div>
                <div class="field mb-4 col-12">
                  <label for="email" class="font-medium">Email</label
                  ><input
                    class="p-inputtext p-component"
                    id="email"
                    v-model="email"
                  />
                </div>
                <div class="col-12">
                  <button
                    class="p-button p-component w-auto mt-3"
                    type="button"
                    aria-label="Save Changes"
                  >
                    <!----><!----><span class="p-button-label"
                      >Save Changes</span
                    ><!----><span class="p-ink" role="presentation"></span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <Footer></Footer>
  </div>
</template>
<script>
import Json from "@/assets/endpoints.json";
import axios from "axios";
import { mapState } from "vuex";
import Nav from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
export default {
  data() {
    return {
      server: Json[0]["SERVER"],
      main: Json[0]["USER"],
      detailslink: Json[0]["USER"]["DETAILS"],
      editlink: Json[0]["USER"]["EDIT"],
      value1: null,
      options: ["info", "edit"],
      info: true,
      edit: null,
      udetails: [],
      last_name: "",
      first_name: "",
      username: "",
      email: "",
      date_joined: "",
      is_superuser: "",
      is_staff: "",
      last_login: "",
      fid: "",
      is_active: false,
      display: false,
      Image: "",
    };
  },
  components: {
    Nav,
    Footer,
  },
  computed: {
    ...mapState(["token", "user", "heading", "uid"]),
    get_user_name() {
      return this.username.charAt(0).toLocaleUpperCase();
    },
  },

  methods: {
    openpassword() {
      this.display = true;
    },
    get_details() {
      (this.edit = false), (this.info = true);
      var link = this.server["SERVER"] + this.detailslink;
      const headers = {
        Authorization: "Token" + " " + this.token,
      };
      console.log(link);
      axios.get(link, { headers: headers }).then((resp) => {
        console.log(resp.data);

        this.last_name = resp.data[0]["last_name"];
        this.first_name = resp.data[0]["first_name"];
        this.username = resp.data[0]["username"];
        this.email = resp.data[0]["email"];
        this.date_joined = resp.data[0]["date_joined"];
        this.is_superuser = resp.data[0]["is_superuser"];
        this.is_active = resp.data[0]["is_active"];
        this.is_staff = resp.data[0]["is_staff"];
        this.last_login = resp.data[0]["last_login"];
        this.fid = resp.data[0]["id"];
        this.Image = resp.data[0]["Image"];
      });
    },
    edit_user() {
      this.info = false;
      this.edit = true;
    },
    save() {
      const headers = {
        Authorization: "Token" + " " + this.token,
      };
      var link = this.server["SERVER"] + this.editlink + "/" + this.fid;
      axios
        .put(
          link,
          {
            username: this.username,
            first_name: this.first_name,
            last_name: this.last_name,
          },
          { headers: headers }
        )
        .then((resp) => {
          console.log(resp.data);
          this.$toast.add({
            severity: "success",
            summary: "Details updated",
            detail: "successfully , Updated user details",
            life: 3000,
          }),
            (this.edit = false),
            this.get_details();
        });
    },
  },
  mounted() {
    this.get_details();
  },
};
</script>
<style scoped></style>
