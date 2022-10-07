import Vue from "vue";
import App from "./App.vue";
import router from "./router.js";
import vuetify from "./plugins/vuetify";
import { store } from "./store/store.js"; // Vuex의 store파일 등록
import axios from "./api/index";

import Restaurant from "./views/hahaha/Restaurant";
import Calendar from "./views/hahaha/Calendar";
import Donations from "./views/hahaha/Donations";

import CoachHome from "./views/coach/home/CoachHome";
import CoachAttendance from "./views/coach/attendance/MainAttendance";
import CoachTraining from "./views/coach/training/MainTraining";
import CoachCalendar from "./views/coach/calendar/MainCalendar";
import CoachMessage from "./views/coach/message/MainMessage";

import PlayerHome from "./views/player/home/PlayerHome";
import PlayerAttendance from "./views/player/attendance/MainAttendance";
import PlayerTraining from "./views/player/training/MainTraining";
import PlayerCalendar from "./views/player/calendar/MainCalendar";
import PlayerMessage from "./views/player/message/MainMessage";

import TeamHome from "./views/team/home/TeamHome";
import TeamAttendance from "./views/team/attendance/MainAttendance";
import TeamTraining from "./views/team/training/MainTraining";
import TeamUserManage from "./views/team/user_management/layout";
import TeamCompanyInfo from "./views/team/company_info/MainCompanyInfo";
import TeamMessage from "./views/team/message/MainMessage";

import Test_UserHome from "./views/test_user/home/TestHome";
import Test_UserAttendance from "./views/test_user/attendance/TestAttendance";
import Test_UserWork from "./views/test_user/work/TestWork";
import Test_UserInfo from "./views/test_user/info/TestInfo";
import Test_UserApproval from "./views/test_user/approval/TestApproval";
import Test_UserPay from "./views/test_user/pay/TestPay";

import Test_CompanyHome from "./views/test_company/home/TestHome";
import Test_CompanyInfo from "./views/test_company/info/TestInfo";
import Test_CompanyManage from "./views/test_company/manage/TestManage";

import ConsultingHome from "./views/consulting/home/ConsultingHome";
import ConsultingAddition from "./views/consulting/addition/ConsultingAddition";

import CompanyHome from "./views/company/home/CompanyHome";
import CompanyPlayer from "./views/company/player/MainPlayer";

import SailorHome from "./views/sailor//home/SailorHome";

import UserInfo from "./views/UserInfo.vue";

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

Vue.component("CoachHome", CoachHome);
Vue.component("CoachAttendance", CoachAttendance);
Vue.component("CoachTraining", CoachTraining);
Vue.component("CoachCalendar", CoachCalendar);
Vue.component("CoachMessage", CoachMessage);

Vue.component("PlayerHome", PlayerHome);
Vue.component("PlayerAttendance", PlayerAttendance);
Vue.component("PlayerTraining", PlayerTraining);
Vue.component("PlayerCalendar", PlayerCalendar);
Vue.component("PlayerMessage", PlayerMessage);

Vue.component("TeamHome", TeamHome);
Vue.component("TeamAttendance", TeamAttendance);
Vue.component("TeamTraining", TeamTraining);
Vue.component("TeamUserManage", TeamUserManage);
Vue.component("TeamCompanyInfo", TeamCompanyInfo);
Vue.component("TeamMessage", TeamMessage);


Vue.component("Test_UserHome", Test_UserHome);
Vue.component("Test_UserAttendance", Test_UserAttendance);
Vue.component("Test_UserWork", Test_UserWork);
Vue.component("Test_UserPay", Test_UserPay);
Vue.component("Test_UserApproval", Test_UserApproval);
Vue.component("Test_UserInfo", Test_UserInfo);

Vue.component("Test_CompanyHome", Test_CompanyHome);
Vue.component("Test_CompanyInfo", Test_CompanyInfo);
Vue.component("Test_CompanyManage", Test_CompanyManage);

Vue.component("ConsultingHome", ConsultingHome);
Vue.component("ConsultingAddition", ConsultingAddition);

Vue.component("CompanyHome", CompanyHome);
Vue.component("CompanyPlayer", CompanyPlayer);

Vue.component("SailorHome", SailorHome);

Vue.component("UserInfo", UserInfo);


// Vue와 Django의 CSRF토큰 이름 동기화
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

new Vue({
  components: {
    CoachHome,
    CoachAttendance,
    CoachTraining,
    CoachCalendar,
    CoachMessage,

    PlayerHome,
    PlayerAttendance,
    PlayerTraining,
    PlayerCalendar,
    PlayerMessage,

    TeamHome,
    TeamAttendance,
    TeamTraining,
    TeamUserManage,
    TeamCompanyInfo,
    TeamMessage,

    CompanyHome,
    CompanyPlayer,

    SailorHome,

    UserInfo,
    apexchart: VueApexCharts,
  },
  vuetify,
  router,
  store: store,
  render: (h) => h(App),
}).$mount("#app");
