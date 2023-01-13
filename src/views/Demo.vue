<template>
  <div class="bg-indigo-50">
    <div
      class="mt-6 max-w-screen flex align-items-center justify-content-center"
    >
      <Nav></Nav>
    </div>
    <br />
    <br />
    <br />

    <div class="card">
      <div
        class="flex justify-content-between flex-wrap card-container purple-container"
      >
        <div
          class="flex align-items-center justify-content-center font-bold text-indigo-700 border-round m-2"
        >
          <p class="text-center text-4xl uppercase">Price Aggregator</p>
        </div>
        <div
          class="flex align-items-center justify-content-center font-bold text-white border-round m-2"
        >
          <p class="text-indigo-600 text-center font-medium text-2xl">
            Other Sites
          </p>
        </div>
        <div
          class="flex align-items-center justify-content-center font-bold text-indigo-700 border-round m-2"
        >
          <h5 id="single" class="text-xl pr-3">Aggregator</h5>
          <SelectButton
            class="bg-orange-500"
            v-model="value1"
            :options="options"
            aria-labelledby="single"
          />
        </div>
      </div>
    </div>
    <div class="grid m-1">
      <div class="col-12 md:col-4 lg:col-4 mb-0">
        <Card class="border-round-md bg-indigo-700">
          <template #header>
            <img alt="user header" :src="course_now.item.image" />
          </template>
          <template #title>
            <div class="flex align-items-center justify-content-between mb-4">
              <span
                class="uppercase text-left text-4xl font-medium text-900 mr-5"
              >
                Course Name : {{ course_now.item.Name }}</span
              ><span class="text-3xl font-medium text-900"
                >₹{{ course_now.item.price }}</span
              >
            </div>
          </template>
          <template #content>
            <p class="p-0 mt-0 mb-5 line-height-3 text-700 text-left">
              {{ course_now.item.Description }}
            </p>
          </template>
          <template #footer>
            <ul class="list-none p-0 m-0 text-sm px-1 text-600">
              <li class="flex align-items-center mb-3">
                <i class="pi pi-credit-card mr-2"></i
                ><span>Pay in 21 days</span>
              </li>
              <li class="flex align-items-center mb-3">
                <i class="pi pi-send mr-2"></i><span>Free Cancellation</span>
              </li>
              <li class="flex align-items-center">
                <i class="pi pi-refresh mr-2"></i
                ><span>Price on {{ course_now.item.Date }}</span>
              </li>
            </ul>
            <Button
              label="Buy Now"
              icon="pi pi-shopping-cart"
              class="py-3 my-3"
            />
          </template>
        </Card>
      </div>
      <div class="col-12 md:col-8 lg:col-8">
        <div class="mt-0">
          <ul
            class="list-none m-0 p-0 bg-indigo-700 border-round mb-2"
            :key="item"
            v-for="item in course_now.item.User_Course"
            v-if="value1 === 'Off'"
          >
            <li class="py-5 border-top-1 surface-border">
              <div class="flex align-items-center justify-content-between mb-3">
                <div class="flex align-items-center">
                  <img
                    :src="course_now.item.image"
                    class="w-4rem h-4rem flex-shrink-0 m-3 border-round shadow-7 border-orange-500 border-1 m-2"
                  />
                  <div class="flex flex-column">
                    <span class="text-left text-900 font-medium mb-1">
                      Plat Form: {{ item.Site }}</span
                    >
                    <span class="text-left text-900 font-medium mb-1">
                      Course Name : {{ course_now.item.Name }}</span
                    ><span class="text-left text-500 font-medium text-sm"
                      >Price on {{ course_now.item.Date }}</span
                    >
                  </div>
                </div>
                <div class="flex align-items-center">
                  <span class="font-medium text-2xl text-white mr-6"
                    >{{ item.Price }} ₹</span
                  >
                </div>
              </div>
              <p class="text-600 p-0 m-0 line-height-3 text-left m-4">
                {{ course_now.item.Description }}
              </p>
            </li>
          </ul>
        </div>
        <div class="col-12 lg:col-12 p-3" v-if="value1 === 'On'">
          <div class="card">
            <h5>Compare Prices from our top competators</h5>
            <Chart type="bar" :data="basicData" :options="horizontalOptions" />
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
      course_now: {},
      value1: "Off",

      options: ["Off", "On"],
      horizontalOptions: {
        responsive: true,
        indexAxis: "y",
        plugins: {
          showDatapoints: true,
          datalabels: {
            anchor: "end",
            align: "right",
            formatter: Math.round,
            font: {
              weight: "bold",
            },
          },
          legend: {
            labels: {
              color: "#495057",
              font: {
                size: 24,
              },
            },
          },
        },
        scales: {
          x: {
            ticks: {
              color: "#495057",
              callback: function (value, index, ticks) {
                return "₹" + value;
              },
              scaleLabel: {
                display: true,
              },
            },
            grid: {
              color: "#591BDF",
            },
          },
          y: {
            ticks: {
              color: "#495057",
              //   mirror: true, //Show y-axis labels inside horizontal bars
            },
            grid: {
              color: "#ebedef",
            },
            gridLines: {
              drawOnChartArea: false,
            },
          },
        },
      },
      basicData: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "My First dataset",
            backgroundColor: "#DF711B",
            barThickness: 25,
            padding: {
              top: 5,
            },
            data: [650, 59, 80, 81, 56, 55, 40],
          },
          //   {
          //     label: "Line Dataset",
          //     backgroundColor: "#42A5F5",
          //     data: [500, 500, 500, 500, 500, 500, 500, 500],
          //     type: "line",
          //     // this dataset is drawn on top
          //     order: 1,
          //   },
        ],
      },
    };
  },
  components: {
    Nav,
    Footer,
  },
  computed: {
    ...mapState(["token", "user", "current_course"]),
  },
  methods: {
    get_course_info() {
      this.course_now = JSON.parse(localStorage.current_course);
      //   console.log("at initital load", this.current_course);
      console.log("loaded from local storage");
      console.log(JSON.parse(localStorage.current_course));
      //   this.course_now = this.current_course;
    },
    scroll(id) {
      document.getElementById(id).scrollIntoView({
        behavior: "smooth",
      });
    },
    load_data() {
      this.course_now;

      const data_vals = [];
      data_vals.push(this.course_now.item.price);
      const sites = [];
      sites.push("Edumoon");
      for (var j = 0; j < this.course_now.item.User_Course.length; j++) {
        data_vals.push(
          Math.floor(this.course_now.item.User_Course[j].Price / 10) * 10
        );
        sites.push(this.course_now.item.User_Course[j].Site);
      }
      this.basicData.datasets[0].label =
        this.course_now.item.Name + "Course -Price Variation";
      this.basicData.datasets[0].data = data_vals;
      this.basicData.labels = sites;
    },
  },

  created() {
    this.get_course_info();
    this.load_data();
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
