import Vue from "vue";
import VueRouter from "vue-router";
import Login from "./views/auth/Login";

import Contributor from "./components/layout/Contributor";
import Manager from "./components/layout/Manager";
import signUp from "./views/auth/signUp";

import NoDashBoardLayout from "./components/layout/NoDashBoardLayout";
import store from "./store/store";

Vue.use(VueRouter);


// 토큰이 없는 유저 로그인 페이지로 리다이렉트 하는 함수
const requireAuth = () => (to, from, next) => {
  if (store.state.authStore.access_token !== "") {
    return next();
  }
  next("auth/login/");
};

const routes = [
  {
    //인증관련 최상단 레이아웃
    path: "/auth",
    component: NoDashBoardLayout,
    children: [
      {
        // 로그인 페이지 (/auth/login)
        path: "login/",
        name: "Login",
        component: Login,
      },
      {
        // hahaha 회원가입 페이지 (/auth/signup)
        path: "signUp/",
        name: "signUp",
        component: signUp,
      },
    ],
  },
  {
    //기본 도메인 접속 시 로그인 페이지(/auth/login)으로 리다이렉트
    path: "/",
    name: "Index",
    redirect: "/auth/login",
  },
  {
    //기부자 화면
    path: "/Contributor",
    name: "Contributor",
    component: Contributor,
    beforeEnter: requireAuth(),
  },
  {
    //관리자 화면
    path: "/Manager",
    name: "Manager",
    component: Manager,
    beforeEnter: requireAuth(),
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
