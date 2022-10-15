import Vue from "vue";
import App from "./App.vue";
import router from "./router.js";
import vuetify from "./plugins/vuetify";
import { store } from "./store/store.js"; // Vuex의 store파일 등록
import axios from "./api/index";

import Restaurant from "./views/hahaha/Restaurant";
import Calendar from "./views/hahaha/Calendar";
import Donations from "./views/hahaha/Donations";

import VueApexCharts from "vue-apexcharts";
import 'chart.js' //chart.js 관련
import 'hchs-vue-charts' //chart.js 관련

// import "./plugins/socketPlugin";
// import Directives from "./plugins/directives.vue"; // chat 관련
// import "./plugins/socketPlugin"; // chat 관련

Vue.use(window.VueCharts) //chart.js 관련
const EventBus = new Vue();
export default EventBus;

// Vue.use(Directives); // chat 관련
Vue.component("apexchart", VueApexCharts); // 그래프 관련

Vue.component("Restaurant", Restaurant);
Vue.component("Calendar", Calendar);
Vue.component("Donations", Donations);

// Vue와 Django의 CSRF토큰 이름 동기화
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

new Vue({
  components: {
    apexchart: VueApexCharts,
  },
  vuetify,
  router,
  store: store,
  render: (h) => h(App),
}).$mount("#app");
