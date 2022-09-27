import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

// 사용할 모듈들 임포트
import authStore from "./modules/authStore";
import tabStore from "./modules/tabStore";
import userStore from "./modules/userStore";
import selectedUser from "./modules/selectedUserStore";
import toast from "./modules/toast";
// import socket from './modules/socket'

const debug = process.env.NODE_ENV !== "production";

export const store = new Vuex.Store({
  modules: {
    authStore: authStore, // authStore 모듈 가져오기
    tabStore: tabStore, // tabStore 모듈 가져오기
    userStore, // userStore 모듈 가져오기
    selectedUser,
    toast,
    // socket,
  },
  strict: debug,
  // plugins: debug ? [createLogger()] : []
  plugins: [
    /*
    createPersistedState({
      // path에 쓴 모듈만 로컬스토리지에 저장
      paths: [authStore],
    }),
    */

    createPersistedState({
      storage: window.sessionStorage,
    }),
  ],
});

export default store;
