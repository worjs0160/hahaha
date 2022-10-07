<template>
  <!--전체 화면 정렬을 위한 row-->
  <v-row justify="center">
    <v-col>
      <!--로그인 카드 영역-->
      <v-card class="login-wrap">
        <!-- 로그인 헤더 영역 -->
        <div class="login-wrap-header">
          <p class="pre-600">로그인</p>
        </div>
        <!--로그인 카드 인풋 영역-->
        <div class="login-inputBox">
          <v-row align="center" justify="center">
            <v-col cols="5">
              <!-- 로그인 로고 영역 -->
              <img :src="require('@/views/auth/hahaha.png')" style="width:100%; height:100%;">
            </v-col>
            <v-col cols="7">
              <div>
                <v-text-field
                  class="login-input login-input-id"
                  style="margin-bottom: 8px !important;"
                  v-model="data.username"
                  hide-details="auto"
                  placeholder="아이디를 입력해주세요"
                  @keyup.enter="login()"
                ></v-text-field>
                <v-text-field
                  class="login-input login-input-pw"
                  v-model="data.password"
                  hide-details="auto"
                  type="password"
                  placeholder="패스워드를 입력해주세요"
                  @keyup.enter="login()"
                ></v-text-field>
              </div>

              <!-- 아이디 / 비밀번호 찾기-->
              <div class="login-findBox">
                <!-- <v-btn text @click="moveToFindID()">아이디 찾기</v-btn>
                <span class="login-bar"></span>
                <v-btn text @click="moveToFindPW()">비밀번호 찾기</v-btn> -->
              </div>
              <!-- 로그인 버튼 col 영역 비율 4 차지-->
              <button class="loginButton" type="button" @click="moveToHome(1)">
                기부자 로그인
              </button>
              <button class="loginButton mt-3" type="button" @click="moveToHome(0)">
                관리자 로그인
              </button>
              <button class="loginButton mt-3" type="button" @click="moveToHome(2)">
                회원가입
              </button>
            </v-col>
          </v-row>
        </div>
        <div class="signupButton">
          <!-- <v-btn text @click="moveToSignup()">아직 회원이 아니신가요?</v-btn> -->
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data: () => {
    return {
      data: {
        username: "",
        password: "",
      },
    };
  },
  created() {
    // this.$axios({
    //   method: "GET",
    //   url: "https://api.ip.pe.kr/",
    // })
    //   .then((res) => {
    //     console.log(res);
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   });
  },
  // created() {
  //   this.$axios.get("users/getIP/")
  //   .then((res) => {
  //     console.log(res)
  //   })
  //   .catch((err) => {
  //     console.log(err)
  //   })
  // },
  methods: {
    // router 이용하여 이동할 페이지 선언
    moveToSignup: function() {
      var router = this.$router;

      return router.push({ name: "Signup" });
    },
    moveToFindID: function() {
      var router = this.$router;

      return router.push({ name: "FindIDType" });
    },
    moveToFindPW: function() {
      var router = this.$router;

      return router.push({ name: "FindPW" });
    },
    moveToHome: function(val) {
      var router = this.$router;
      if(val==0){
        return router.push({ name: "Manager" });
      }
      else if(val==1){
        return router.push({ name: "Contributor" });
      }
      else if(val==2){
        return router.push({ name: "signUp" });
      }
      //return router.push({ name: "Home" });
    },
    // 폼에 있는 데이터 삭제하는 함수
    clearPW: function() {
      this.data.password = "";
    },
    // 로그인 함수 정의
    login() {
      this.moveToHome();
      // this.$axios({
      //   method: "POST",
      //   url: "users/login/",
      //   data: this.data,
      // })
      //   .then((res) => {
      //     // 요청 성공시 실행
      //     // console.log(res);
      //     this.$store.commit("setToken", res.data.tokens);
      //     this.$store.commit("setId", res.data.user_id);
      //     this.moveToHome();
      //   })
      //   .catch((err) => {
      //     // 요청 실패시 실행
      //     console.log(err.response);
      //     alert(err.response.data.msg);
      //     this.clearPW(); // 기존에 입력되어 있던 데이터 삭제
      //   });
    },
    getIP() {
      this.$axios({
        method: "GET",
        url: "https://api.ip.pe.kr/",
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.login-wrap {
  width: 870px;
  height: 580px;
  margin: 0 auto;
  background: #fff;
  border-radius: 20px !important;
  box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06) !important;
}
.login-wrap-header {
  widows: 100%;
  height: 72px;
  display: flex;
  align-items: center;
  border-bottom: 0.5px solid #b4b4b4;
}
.login-wrap-header p {
  font-size: 20px;
  line-height: 24px;
  margin: 0 !important;
  margin-left: 24px !important;
}
.login-wrap-logoBox {
  widows: 100%;
  display: flex;
  justify-content: center;
  margin: 34px 0 60px;
}
.login-inputBox {
  width: 570px !important;
  margin: 120px auto;
}
.login-input {
  margin: 0 !important;
  padding: 0 !important;
  font-family: "Pretendard-Regular";
}
.login-input-id {
  margin-bottom: 8px !important;
}
.login-input-pw {
  margin-bottom: 13px !important;
}
.login-input input {
  height: 39px !important;
  max-height: none !important;
  border: 1px solid #e1e1e1;
  border-radius: 3px;
  font-size: 16px !important;
  padding: 10px 12px !important;
}
.theme--light.v-text-field > .v-input__control > .v-input__slot:before {
  display: none;
}
.login-findBox {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
.login-findBox button {
  padding: 0 !important;
  font-size: 13px;
  font-family: "Pretendard-Regular";
  color: #646464 !important;
}
.login-bar {
  background: #989898;
  display: block;
  width: 1px;
  height: 19px;
  margin: 0 6px;
}
.loginButton {
  width: 320px;
  height: 38px;
  margin: 0 auto;
  background: #fbbb31;
  border-radius: 10px;
  font-size: 18px;
  color: #fff !important;
  font-family: "Pretendard-Regular";
  transition: all 0.3s;
}
.loginButton:hover {
  background: #ffd06a;
}
.signupButton {
  display: flex;
  justify-content: center;
}
.signupButton button {
  font-size: 13px !important;
  font-family: "Pretendard-Regular";
  color: #49ada9 !important;
  margin-top: 25px;
}
</style>
