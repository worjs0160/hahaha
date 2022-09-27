<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card elevation="2">
        <v-btn class="mt-2 mr-0" absolute right icon @click="moveToLogin">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-card-title class="text-h4">아이디 찾기</v-card-title>
        <v-card-subtitle>정보관리</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>

        <div class="mx-7">
          <v-window v-model="step" touchless>
            <v-window-item :value="1">
              <v-container style="border: 2px solid grey;">
                <v-row style="border-bottom: 2px solid grey;">
                  <v-col cols="2" class="d-flex justify-center align-center content-title">
                    이름<span style="color:red; ">*</span>
                  </v-col>
                  <v-col cols="6" style="2px solid grey;">
                    <v-text-field
                      v-model="data.name"
                      :error-messages="err.nameErrMsg"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row style="border-bottom: 2px solid grey;">
                  <v-col cols="2" class="d-flex justify-center align-center content-title">
                    보호자 연락처
                  </v-col>
                  <v-col cols="6">
                    <v-text-field
                      label="( - 제외)"
                      type="number"
                      min="0"
                      v-model="data.guardianNum"
                      :error-messages="err.numErrMsg"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-btn label="인증번호받기" large @click="getSmsNumber(data.name, data.guardianNum)"
                      >인증번호받기
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="2" class="d-flex justify-center align-center content-title">
                    인증번호 입력
                  </v-col>
                  <v-col cols="6">
                    <v-text-field
                      v-model="data.authNum"
                      type="number"
                      :error-messages="err.authErrMsg"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-window-item>

            <v-window-item :value="2">
              <v-container>
                <v-alert
                  dense
                  border="left"
                  elevation="2"
                  prominent
                  type="info"
                >
                  아이디는 <strong>{{ result }}</strong> 입니다.
                </v-alert>

                <v-btn block large class="mb-7" @click="moveToLogin">
                  로그인 페이지 이동
                </v-btn>
              </v-container>
            </v-window-item>
          </v-window>

          <v-card-actions>
            <v-row>
              <v-col>
                <v-btn
                  block
                  large
                  class="mb-7"
                  @click="back"
                  :disabled="step === 2"
                >
                  이전으로
                </v-btn>
              </v-col>

              <v-col>
                <v-btn
                  block
                  large
                  class="mb-7"
                  @click="next"
                  :disabled="step === 2"
                >
                  아이디 찾기
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

export default {
  data: () => ({
    data: {
      name: "",
      guardianNum: "",
      authNum: "",
    },
    err: {
      nameErrMsg: "",
      numErrMsg: "",
      authErrMsg: "",
    },
    step: 1,
    result: "",
  }),
  watch: {
    "data.name": function() {
      if(!this.data.name) {
        this.err.nameErrMsg = "필수 정보입니다."
      }
      else this.err.nameErrMsg = ""
    },
    "data.guardianNum": function() {
      if(!this.data.guardianNum){
        this.err.guardNumErrMsg = "필수 정보입니다."
      }
      else if(this.data.guardianNum.length != 11) {
        this.err.guardNumErrMsg = "11자리 번호를 입력해주세요."
      }
      else this.err.guardNumErrMsg = ""
    },
    "data.authNum": function() {
      if(!this.data.authNum) {
        this.err.authErrMsg = "필수 정보입니다."
      }
      else this.err.authErrMsg = ""
    }
  },
  methods: {
    moveToLogin: function() {
      var router = this.$router;
      return router.push({ name: "Login" });
    },
    find_id() {
      this.$axios({
        method: "POST",
        url: "users/api/regist/find_id/",
        data: this.data,
      })
      .then((res) => {
        console.log(res);
        this.result = res.data.username;
        this.step++;
      })
      .catch((err) => {
        console.log(err.response);
        alert(err.response.data.msg);
      });
    },
    getSmsNumber(name, phoneNum) {
      // if() {

      // }
      this.$axios.get(
        "users/api/regist/?name=" + name + "&" +  "guardianNum=" + phoneNum
      )
      .then((res) => {
        console.log(res.data)
        console.log(res.data[0].name) // 선수 -> 보호자 휴대번호 인증 but 다른 유저는 자신 번호 인증
      })
      .catch((res) => {
        console.log(res)
      })
      // this.$axios.post(
      //   "users/authSms/",
      //   {"phoneNum": phoneNum}
      // )
      // .then((res)=>{
      // console.log(res)
      // alert("입력된 번호로 인증번호를 전송하였습니다.")
      // })
      // .catch((err)=>{
      //   console.log(err)
      //   alert("11자리 번호를 입력해주세요.")
      // })
    },
    // SMS 인증 번호를 인증하는 함수
    checkSmsNumber(phoneNum, authNum) {
      this.$axios({
        method: "GET",
        url:"users/authSms/",
        params :{"phoneNum": phoneNum, "authNum": authNum}
      })
      .then((res)=>{
        console.log(res.data.result)
      })
      .catch((err)=>{
        console.log(err)
        alert("4자리 인증번호를 입력해주세요.")
      })
    },
    // checkInfo(name, phoneNum) {
    //   this.$axios({
    //     method: "POST"
    //   })
    // },
    back() {
      if (this.step === 1) {
        this.moveToLogin();
      }
    },
    next() {
      this.checkSmsNumber()
      // this.find_id();
    },
  },
};
</script>

<style></style>
