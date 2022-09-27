import Vue from "vue";
import VueRouter from "vue-router";
import Login from "./views/auth/Login";
import FindID from "./views/auth/FindID";

import PlayerFindID from "./views/auth/FindID/Player";
import FindIDType from "./views/auth/FindID/FindID";
import ExceptUser from "./views/auth/FindID/ExceptUser";

import FindPW from "./views/auth/FindPW";
import Signup from "./views/auth/signup/Signup";
import TeamSignup from "./views/auth/signup/TeamSignup";
import CoachSignup from "./views/auth/signup/CoachSignup";
import PlayerSignup from "./views/auth/signup/PlayerSignup";
import CompanySignup from "./views/auth/signup/CompanySignup";
import AdminSignup from "./views/auth/signup/AdminSignup";
import Complete from "./views/auth/signup/Complete";
import ChatRoom from "./views/chat/ChatRoom.vue";
import MainLayout from "./components/layout/MainLayout";
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
        // 회원가입 페이지 (/auth/signup)
        path: "signup/",
        name: "Signup",
        component: Signup,
      },
      {
        // 훈련기관 회원가입 페이지 (/auth/team)
        path: "team/",
        name: "Team",
        component: TeamSignup,
      },
      {
        // 코치 회원가입 페이지 (/auth/coach)
        path: "coach/",
        name: "Coach",
        component: CoachSignup,
      },
      {
        // 선수 회원가입 페이지 (/auth/player)
        path: "player/",
        name: "Player",
        component: PlayerSignup,
      },
      {
        // 기업 회원가입 페이지 (/auth/company)
        path: "company/",
        name: "Company",
        component: CompanySignup,
      },
      {
        // 위플레이 회원가입 페이지 (/auth/admin)
        path: "admin/",
        name: "Admin",
        component: AdminSignup,
      },
      {
        // 회원가입 완료 페이지 (/auth/complete)
        path: "complete/",
        name: "Complete",
        component: Complete,
      },
      {
        // 아이디 찾기 페이지 (/auth/FindID)
        path: "FindID/",
        name: "FindID",
        component: FindID,
      },
      {
        // 아이디 찾기 유형 선택 페이지 (/auth/FindID)
        path: "FindID/Type/",
        name: "FindIDType",
        component: FindIDType,
      },
      {
        // 선수 아이디 찾기 페이지 (/auth/FindID/Player)
        path: "FindID/Player/",
        name: "PlayerFindID",
        component: PlayerFindID,
      },
      {
        path: "FindID/Except/",
        name: "ExceptFindID",
        component: ExceptUser,
      },

      // {
      //   // 아이디 찾기 페이지 (/auth/FindID/User)
      //   path: "FindID/User/",
      //   name: "FindID",
      //   component: FindID,
      // },
      {
        // 비밀번호 찾기 페이지 (/auth/FindPW)
        path: "FindPW/",
        name: "FindPW",
        component: FindPW,
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
    //플랫폼 최상단 레이아웃
    path: "/Home",
    name: "Home",
    component: MainLayout,
    beforeEnter: requireAuth(),
  },
  {
    path: '/chat-room/:username',
    name: 'ChatRoom',
    component: ChatRoom,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
