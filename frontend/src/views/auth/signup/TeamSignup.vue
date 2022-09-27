<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card elevation="2">
        <v-btn class="mt-2 mr-0" absolute right icon @click="moveToPage('Login')">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-card-title class="text-h4">회원가입</v-card-title>
        <v-card-subtitle>위플레이 회원가입</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>
        <div class="mx-7">
          <v-card-text class="font-weight-medium text-h6 pb-0">
            복지관 가입정보 입력
          </v-card-text>
          <v-container>
            <!-- 기본정보 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              기본정보
            </div>
          </v-container >
          <v-container style="border: 2px solid grey;">
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  아이디<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="data.username"
                  :error-messages="err.idErrMsg"
                  hide-details="auto"
                >
                </v-text-field>
              </v-col>
              <v-col cols="2">
                <v-btn large @click="validId">중복확인</v-btn>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  비밀번호<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-text-field
                  label=" 8자 이상, 특수문자, 숫자포함 "
                  v-model="data.password"
                  type="password"
                  :error-messages="err.pwErrMsg"
                  hide-details="auto"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  비밀번호 확인<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.passwordValid"
                  type="password"
                  :error-messages="err.pwCkErrMsg"
                  hide-details="auto"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  담당자 이름<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.name"
                  hide-details="auto"
                  :error-messages="err.nameErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  기관 대표 이메일<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.email"
                  type="mail"
                  hide-details="auto"
                  :error-messages="err.emailErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>

          <v-container>
            <!-- 세부정보 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              세부정보
            </div>
          </v-container >
          <v-container style="border: 2px solid grey;">
            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  소속(복지관)<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="10">
                <v-select
                  v-model="data.team"
                  :items="teamList"
                  item-text="value"
                  item-value="id"
                  hide-details="auto"
                  :error-messages="err.emailErrMsg"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <v-card-actions>
            <v-row class="mt-10">
              <v-col>
                <v-btn
                  block
                  large
                  class="mb-7"
                  @click="back"
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
                >
                  다음으로
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
      username: "",
      password: "",
      passwordValid: "",
      email: "",
      name: "",
      userType: "3",
      team: "",
      // is_active: false // 가입시 유저 활성화 False로 세팅
    },
    err: {
      idErrMsg: "", // 서버에서 반환한 아이디 에러 메시지
      pwErrMsg: "", // 서버에서 반환한 패스워드 에러 메시지
      pwCkErrMsg: "",
      emailErrMsg: "",
      nameErrMsg: "",
      teamErrMsg: "",
    },
    idValidFlag: false, // 아이디 중복확인 여부
    teamList: [], // 복지관(훈련기관) 리스트
  }),

  watch: {
    // 아이디 바꾸면 아이디 검증 플래그 초기화
    "data.username": function() { // 아이디 체크
      this.idValidFlag = false; // 아이디 바꾸면 아이디 검증 플래그 초기화

      let check = /[a-z0-9]{5,20}/
      let checkEng_A = /[A-Z]/

      if(!this.data.username) {
        this.err.idErrMsg = "필수 정보입니다."
      }
      else if(check.test(this.data.username) == false || checkEng_A.test(this.data.username) == true) {
        this.err.idErrMsg = "5~20자의 영문 소문자, 숫자만 사용 가능합니다."
      }
      else this.err.idErrMsg = ""
    },
    "data.password": function() {// 비밀번호 체크 및 비밀번호 확인 체크
      let check = /[0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]{8,}/
      let checkNum = /[0-9]/
      let checkSpc = /[~!@#$%^&*()_+|<>?:{}]/

      if(check.test(this.data.password) == false || checkSpc.test(this.data.password) == false || checkNum.test(this.data.password) == false) {
        this.err.pwErrMsg = "8자 이상, 특수문자, 숫자를 포함하여야 합니다."
      }
      else {
        this.err.pwErrMsg = ""
      }

      if(this.data.password != this.data.passwordValid){
        this.err.pwCkErrMsg = "비밀번호가 일치하지 않습니다."
      }
      else this.err.pwCkErrMsg = ""
    },
    "data.passwordValid": function() {
      if(this.data.password != this.data.passwordValid){
        this.err.pwCkErrMsg = "비밀번호가 일치하지 않습니다."
      }
      else this.err.pwCkErrMsg = ""
    },
    "data.name": function() {
      if(!this.data.name){
        this.err.nameErrMsg = "필수 정보입니다."
      }
      else this.err.nameErrMsg = ""
    },
    "data.email": function() {
      var checkEmail = /^([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;

      if(!this.data.email) {
        this.err.emailErrMsg = "필수 정보입니다."
      }
      else if(checkEmail.test(this.data.email) == false) {
        this.err.emailErrMsg = "이메일 형식이 맞지 않습니다."
      }
      else this.err.emailErrMsg = ""
    },
    "data.team": function() {
      if(!this.data.team){
        this.err.teamErrMsg = "필수 정보입니다."
      }
      else this.err.teamErrMsg = ""
    },
  },

  async created() {
    // 복지관(훈련기관) 가져오기
    await this.$axios
      .get("datasets/api/team_list/")
      .then((res) => {
        for (const data of res.data) {
          this.teamList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });
  },

  methods: {
    // id 중복확인 함수
    validId() {
      if (!this.data.username) {
        this.err.idErrMsg = "아이디를 입력해주세요.";
      } else {
        this.$axios
          .post("users/api/regist/chk_username/", {
            username: this.data.username,
          })
          .then((res) => {
            this.idValidFlag = true;
            this.err.idErrMsg = "";
            console.log(res);
            alert(res.data.msg);
          })
          .catch((err) => {
            console.log(err.response);
            alert(err.response.data.msg);
          });
      }
    },
    // data 리셋 함수
    resetData: function() {
      Object.assign(this.$data.data, this.$options.data()["data"]);
      this.idValidFlag = false;
    },
    signup() {
      this.$axios
        .post("users/api/regist/", this.data)
        .then(() => {
          this.moveToPage('Complete');
        })
        .catch(() => {
          console.log("회원가입 실패");
          alert("정보를 정확히 입력해주세요.")
        });
    },
    moveToPage: function(val) {
      var router = this.$router;
      return router.push({ name: val });
    },
    back() {
      this.resetData();
      this.moveToPage('Signup');
    },
    next() {
      if (!this.idValidFlag) {
        alert("아이디 중복확인 필요.");
      } else {
        this.signup();
      }
    },
    totalCheck() {
      let check = null
      console.log(check)
      let checkName = /[a-z0-9]{5,20}/
      let checkEng_A = /[A-Z]/

      if(!this.data.username) {
        this.err.idErrMsg = "필수 정보입니다."
        check++
      }
      else if(checkName.test(this.data.username) == false || checkEng_A.test(this.data.username) == true) {
        this.err.idErrMsg = "5~20자의 영문 소문자, 숫자만 사용 가능합니다."
        check++
      }
      else this.err.idErrMsg = ""
    
      let checkPw = /[0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]{8,}/
      let checkNum = /[0-9]/
      let checkSpc = /[~!@#$%^&*()_+|<>?:{}]/

      if(checkPw.test(this.data.password) == false || checkSpc.test(this.data.password) == false || checkNum.test(this.data.password) == false) {
        this.err.pwErrMsg = "8자 이상, 특수문자, 숫자를 포함하여야 합니다."
        check++
      }
      else {
        this.err.pwErrMsg = ""
      }

      if(this.data.password != this.data.passwordValid){
        this.err.pwCkErrMsg = "비밀번호가 일치하지 않습니다."
        check++
      }
      else this.err.pwCkErrMsg = ""
    
      if(this.data.password != this.data.passwordValid){
        this.err.pwCkErrMsg = "비밀번호가 일치하지 않습니다."
        check++
      }
      else this.err.pwCkErrMsg = ""
    
      if(!this.data.name){
        this.err.nameErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.nameErrMsg = ""
    
      var checkEmail = /^([0-9a-zA-Z_-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/

      if(!this.data.email) {
        this.err.emailErrMsg = "필수 정보입니다."
        check++
      }
      else if(checkEmail.test(this.data.email) == false) {
        this.err.emailErrMsg = "이메일 형식이 맞지 않습니다."
        check++
      }
      else this.err.emailErrMsg = ""

      if(!this.data.team) {
        this.err.teamErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.teamErrMsg = ""
      
      return check
    },
  },
};
</script>

<style></style>
