<template>
  <v-container class="singUpinBox" style="height:100%; padding: 0; overflow: hidden;">
    <v-window v-model="step" touchless>
      <v-window-item :value="1">
        <div class="manage-val1-wrap" style="padding: 24px;">
          <div class="manage-val1-title">
            <p class="pre-700">기본정보</p>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>아이디</h2>
            <input
              class="inputBox-id"
              type="text"
              placeholder="아이디를 입력해 주세요"
              v-model="data.username"
            />
            <!-- <button class="id-chk-btn pre-400" type="button" @click="validId">
              중복 확인
            </button> -->
          </div>

          <div class="manage-val1-pw1Box manage-val1-inputBox">
            <h2>비밀번호</h2>
            <input
              type="password"
              placeholder="비밀번호를 입력해 주세요"
              v-model="data.password"
            />
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>비밀번호 확인</h2>
            <input
              type="password"
              placeholder="비밀번호를 한번 더 입력해 주세요"
              v-model="data.passwordValid"
            />
          </div>
          <span class="manage-val1-errBox pre-400" style="color: red;">
            오류 메세지 위치
          </span>

          <div class="manage-val1-nameBox manage-val1-inputBox mt-7">
            <h2>대표자 성함</h2>
            <input
              type="text"
              placeholder="성함을 입력해 주세요"
              v-model="data.name"
            />
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게이름</h2>
            <input
              type="text"
              placeholder="가게이름을 입력해 주세요"
              v-model="data.restaurantName"
            />
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게 주소</h2>
            <input
              type="text"
              placeholder="주소를 입력해 주세요"
              v-model="data.addr"
            />
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게 번호</h2>
            <input
              type="text"
              placeholder="전화번호를 입력해 주세요(-제외)"
              v-model="data.number"
            />
          </div>
        </div>
        <!--e:manage-val1-wrap-->
      </v-window-item>
      <v-window-item :value="2">
        <div class="manage-val1-wrap manage-val4-wrap" style="padding: 24px;">
          <div class="manage-val1-title">
            <p class="pre-700">입력정보 확인</p>
          </div>

          <div class="manage-val2-btm-info">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM11.25 8C11.25 7.59 11.59 7.25 12 7.25C12.41 7.25 12.75 7.59 12.75 8V13C12.75 13.41 12.41 13.75 12 13.75C11.59 13.75 11.25 13.41 11.25 13V8ZM12.92 16.38C12.87 16.51 12.8 16.61 12.71 16.71C12.61 16.8 12.5 16.87 12.38 16.92C12.26 16.97 12.13 17 12 17C11.87 17 11.74 16.97 11.62 16.92C11.5 16.87 11.39 16.8 11.29 16.71C11.2 16.61 11.13 16.51 11.08 16.38C11.03 16.26 11 16.13 11 16C11 15.87 11.03 15.74 11.08 15.62C11.13 15.5 11.2 15.39 11.29 15.29C11.39 15.2 11.5 15.13 11.62 15.08C11.86 14.98 12.14 14.98 12.38 15.08C12.5 15.13 12.61 15.2 12.71 15.29C12.8 15.39 12.87 15.5 12.92 15.62C12.97 15.74 13 15.87 13 16C13 16.13 12.97 16.26 12.92 16.38Z"
                fill="#0081C7"
              />
            </svg>
            <p class="pre-400">회원가입이 완료되었습니다.</p>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>아이디</h2>
            <p class="pre-400">아이디예시</p>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게이름</h2>
            <p class="pre-400">이름예시</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>주소</h2>
            <p>주소예시</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>대표자</h2>
            <p>대표자예시</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>연락처</h2>
            <p>연락처 예시</p>
          </div>
        </div>
        <!--e:manage-val4-wrap-->
      </v-window-item>
    </v-window>
    <v-row class="manage-btnBox" justify="end" style="width:500px; padding: 24px; margin:0;">
      <v-col align="start" v-if="step > 0">
        <v-btn class="preBtn" @click="backToHome()" color="buttonerrer" v-if="step == 1">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="#646464"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M9 12C9.00588 12.217 9.08227 12.403 9.24094 12.5705L13.8129 17.2892C13.9481 17.4256 14.1068 17.5 14.3007 17.5C14.6944 17.5 15 17.1776 15 16.7621C15 16.5637 14.9236 16.3777 14.7884 16.2351L10.6748 12L14.7884 7.76494C14.9236 7.62232 15 7.4425 15 7.23788C15 6.82244 14.6944 6.5 14.3007 6.5C14.1126 6.5 13.9481 6.57441 13.8129 6.71082L9.24094 11.4357C9.0764 11.597 9 11.783 9 12Z"
              stroke-width="0.5"
            />
          </svg>
          이전
        </v-btn>
      </v-col>
      <!-- <v-col align="end" v-if="step == 2 && attValidFlag == true">
        <v-btn class="nextBtn" @click="next" color="buttonsuccess">
          다음
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="#49ADA9"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M15 12C14.9941 11.783 14.9177 11.597 14.7591 11.4295L10.1871 6.71082C10.0519 6.57441 9.89324 6.5 9.69931 6.5C9.30558 6.5 9 6.82244 9 7.23788C9 7.4363 9.0764 7.62232 9.21156 7.76494L13.3252 12L9.21156 16.2351C9.0764 16.3777 9 16.5575 9 16.7621C9 17.1776 9.30558 17.5 9.69931 17.5C9.88737 17.5 10.0519 17.4256 10.1871 17.2892L14.7591 12.5643C14.9236 12.403 15 12.217 15 12Z"
              stroke-width="0.5"
            />
          </svg>
        </v-btn>
      </v-col> -->

      <!--테스트용 다음버튼-->
      <!-- <v-col align="end">
        <v-btn @click="next" color="gray">다음</v-btn>
      </v-col> -->

      <v-col align="end" v-if="step == 1">
        <v-btn @click="signup()">계정 생성</v-btn>
      </v-col>
      <v-col align="end" v-if="step == 2">
        <v-btn @click="backToHome()" color="success2">돌아가기</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => {
    return {
      step: 1,
      data:{
        username : "",
        password : "",
        restaurantName : "",
        addr : "",
        name : "",
        number : "",
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
  methods: {
    signup() {
      this.step = 2
      console.log("생성완료")
      //계정 생성
      // await this.$axios({
      //     method: 'POST',
      //     url: "users/api/empRegist/",
      //     data: this.data
      //   })
      //   .then(async (res) => {
      //     this.createId = res.data.id
      //     if (this.allowedIP) {
      //       this.pushIP(this.allowedIP, res.data.id);
      //     }
      //     this.data.allowedIP = []; //계정 생성후 다음 계정 생성을 위해 허용IP 리스트 비워주기
      //     this.step = 4;
      //     this.$store.dispatch("callToast", {
      //       msg: "성공적으로 선수를 등록하였습니다.",
      //       result: "success",
      //     });
      //   })
      //   .catch(() => {
      //     this.$store.dispatch("callToast", {
      //       msg: "정보입력의 유형이 올바르지 않습니다. 정확히 입력해 주세요.",
      //       result: "error",
      //     });
      //   });
    },
    // router 이용하여 이동할 페이지 선언
    backToHome: function() {
      var router = this.$router;
      return router.push({ name: "Login" });
    },
  },
};
</script>

<style>
  .singUpinBox {
      width: 50% !important;
      margin: 120px auto;
    }
</style>
