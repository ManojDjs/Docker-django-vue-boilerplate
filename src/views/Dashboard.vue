<template>
  <div>
    <div
      class="mt-6 max-w-screen flex align-items-center justify-content-center"
    >
      <Nav></Nav>
    </div>
    <div class="block-content mt-5">
      <div
        class="bg-indigo-10 px-4 py-5 md:px-6 lg:px-8 flex justify-content-start flex-wrap"
      >
        <div
          class="text-900 text-3xl font-medium mb-3 flex-column md:flex-row align-items-center"
        >
          Courses
          <span class="text-700 ml-3 text-base font-normal"
            >{{ count }} Active</span
          >
          <i
            class="pi pi-circle-fill ml-3 text-green-300"
            style="font-size: 1rem"
          ></i>
          <span class="p-input-icon-left m-3"
            ><i class="pi pi-search"></i
            ><input
              class="p-inputtext p-component"
              type="text"
              placeholder="Search"
              style="border-radius: 20px"
          /></span>
          <Dropdown
            class="inline-flex py-2 px-3 align-items-center transition-colors border-round transition-duration-150 mb-3 md:mb-0 mr-0 md:mr-3 p-ripple"
            v-model="selectedCategory"
            :options="categories"
            optionLabel="name"
            placeholder="Select a Category"
          />
        </div>
      </div>
    </div>

    <!---->

    <div class="bg-white px-4 py-4 md:px-6 lg:px-4">
      <div class="bg-white-100">
        <div class="grid md:px-8">
          <div
            class="col-12 md:col-6 xl:col-3 p-3"
            :key="item"
            v-for="item in course_content"
          >
            <div class="bg-indigo-700 shadow-6 border-round p-4">
              <div
                class="flex flex-column align-items-center border-bottom-1 surface-border pb-3"
              >
                <img :src="item.image" class="mb-3 w-9" /><span
                  class="text-xl text-900 font-medium mb-2 text-overflow-ellipsis"
                  style="height: 50px"
                  >{{ item.Name }}</span
                ><span class="text-600 font-medium mb-3">{{
                  item.Category
                }}</span
                ><span class="text-2xl text-800 block mb-3 font-semibold"
                  >{{ item.price }} ₹</span
                >
              </div>
              <div class="flex pt-3 justify-content-between align-items-center">
                <button
                  class="p-button p-component p-button-text bg-yellow-500"
                  type="button"
                  aria-label="Buy Now"
                  v-tooltip="'Compare with other platforms before you buy'"
                >
                  <!----><span
                    class="pi pi-chart-bar p-button-icon p-button-icon-left text-white"
                  ></span
                  ><span
                    class="p-button-label text-white"
                    v-on:click="load_aggregator(item)"
                    >Compare Now</span
                  ><!----><span
                    class="p-ink"
                    role="presentation"
                  ></span></button
                ><button
                  class="p-button p-component p-button-icon-only p-button-text p-button-secondary"
                  type="button"
                >
                  <!----><span class="pi pi-heart p-button-icon"></span
                  ><span class="p-button-label">&nbsp;</span
                  ><!----><span class="p-ink" role="presentation"></span>
                </button>
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
import { mapState } from "vuex";
import axios from "axios";
import Json from "@/assets/endpoints.json";
import Nav from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
export default {
  data() {
    return {
      server: Json[0]["Course"]["SERVER"],
      course: Json[0]["Course"]["Course"],
      register: Json[0]["Course"]["REGISTERED"],
      course_content: [],
      count: 0,
      all_course: [],

      user_in: "",
      categories: [
        { name: "New York" },
        { name: "Rome" },
        { name: "London" },
        { name: "Istanbul" },
        { name: "Paris" },
      ],
      selectedCategory: null,
    };
  },
  components: {
    Nav,
    Footer,
  },
  computed: {
    ...mapState(["token", "user", "heading", "height"]),
  },
  methods: {
    get_categories(cat) {
      var json_arr = [];
      var cat_g = {};
      for (let i = 0; i < cat.length; i++) {
        json_arr.push({ name: cat[i] });
      }

      console.log(json_arr);
      return json_arr;
    },
    get_course_info() {
      const headers = {
        Authorization: "Token" + " " + this.token,
      };
      axios
        .get(this.server + this.course, { headers: headers })
        .then((resp) => {
          console.log("im in course spec");
          console.log(resp.data);
          this.count = resp.data.length;
          // this.cities = [...new Set(resp.data.map((item) => item.Category))];
          console.log([...new Set(resp.data.map((item) => item.Category))]);
          this.categories = this.get_categories([
            ...new Set(resp.data.map((item) => item.Category)),
          ]);
          this.all_course = resp.data;
          this.course_content = resp.data;
        });
    },
    load_aggregator(item) {
      console.log(item);
      this.$store
        .dispatch("current_course", { item })
        .then(() => this.$router.push("/Demo"))
        .catch((err) => console.log(err));
    },
    get_user() {
      console.log(this.user);
      this.user_in = this.user;
    },
    filter_course() {
      console.log("prompted from watcher");
      console.log(this.selectedCategory.name);
      console.log(this.all_course.length);
      var s = this.selectedCategory.name;
      var newList = [];

      for (var i = 0; i < this.all_course.length; i++) {
        if (this.all_course[i].Category === s) {
          newList.push(this.all_course[i]);
        }
        this.course_content = newList;
        this.count = this.course_content.length;
      }
      console.log(newList);
    },
  },
  created() {
    this.get_user();
    this.get_course_info();
  },
  watch: {
    selectedCategory() {
      if (this.selectedCategory == null) {
        console.log("cat is emplty");
        this.course_content = this.all_course;
      } else {
        console.log("cat is not emplty");
        this.filter_course();
      }
    },
  },
};
</script>
<style scoped>
.div {
  text-align: center;
}
.Dash {
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
