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
            코치 가입정보 입력
          </v-card-text>
          <v-container >
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
              <v-col cols="8">
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
                  label="8자 이상, 특수문자, 숫자포함"
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

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  이름<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.name"
                  hide-details="auto"
                  :error-messages="err.nameErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  이메일
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.email"
                  type="mail"
                  hide-details="auto"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  연락처<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  label=" - 제외"
                  v-model="data.phoneNum"
                  hide-details="auto"
                  :error-messages="err.phoneErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="인증번호받기" large @click="getSmsNumber(data.phoneNum)"
                  >인증번호받기
                </v-btn>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  인증번호 입력<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="data.authNum"
                  hide-details="auto"
                  :error-messages="err.authErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="인증번호확인" large @click="checkSmsNumber(data.phoneNum, data.authNum)"
                  >인증번호확인
                </v-btn>
              </v-col>
            </v-row>
          </v-container>

          <v-container >
            <!-- 세부정보 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              세부정보
            </div>
          </v-container >

          <v-container style="border: 2px solid grey;">
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  소속(복지관)<span style="color:red; ">*</span>
              </v-col>
              <v-col style="border-right: 2px solid grey;">
                <v-select
                  v-model="data.team"
                  :items="teamList"
                  item-text="value"
                  item-value="id"
                  hide-details="auto"
                  :error-messages="err.teamErrMsg"
                ></v-select>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                  직통번호<span style="color:red; ">*</span>
              </v-col>
              <v-col>
                <v-text-field
                  label=" - 제외 "
                  v-model="data.divisionNum"
                  hide-details="auto"
                  :error-messages="err.divNumErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>

          <v-row>
            <v-col cols="2" class="d-flex justify-center align-center content-title">
                부서<span style="color:red; ">*</span>
            </v-col>
            <v-col>
              <v-text-field
                v-model="data.divisionName"
                hide-details="auto"
                :error-messages="err.divNameErrMsg"
              ></v-text-field>
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
    // "":필수, null:선택
    data: {
      username: "",
      password: "",
      passwordValid: "",
      email: "",
      name: "",
      phoneNum: "",
      authNum: "",
      userType: "1",
      team: "",
      
      divisionName: "",
      divisionNum: "",
      is_active: false // 가입시 유저 활성화 False로 세팅
    },
    err: {
      idErrMsg: "", // 서버에서 반환한 아이디 에러 메시지
      pwErrMsg: "", // 서버에서 반환한 패스워드 에러 메시지
      pwCkErrMsg: "",
      nameErrMsg: "",
      phoneErrMsg: "",
      authErrMsg: "",
      teamErrMsg: "",
      divNameErrMsg: "",
      divNumErrMsg: "",
    },
    idValidFlag: false, // 아이디 중복확인 여부
    numValidFlag: false,
    teamList: [],// 복지관(훈련기관) 리스트
  }),

  watch: {
    // 아이디 바꾸면 아이디 검증 플래그 초기화
    "data.username": function() {
      this.idValidFlag = false;

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
    "data.phoneNum": function() {
      if(!this.data.phoneNum){
        this.err.phoneErrMsg = "필수 정보입니다."
      }
      else if(this.data.phoneNum.length != 11) {
        this.err.phoneErrMsg = "11자리 번호를 입력해주세요."
      }
      else this.err.phoneErrMsg = ""
    },
    "data.authNum": function() {
      if(!this.data.authNum){
        this.err.authErrMsg = "필수 정보입니다."
      }
      else if(this.data.authNum.length != 4){
        this.err.authErrMsg = "4자리 인증번호를 입력해주세요."
      }
      else this.err.authErrMsg = ""
    },
    "data.team": function() {
      if(!this.data.team){
        this.err.teamErrMsg = "필수 정보입니다."
      }
      else this.err.teamErrMsg = ""
    },
    "data.divisionName": function() {
      if(!this.data.divisionName){
        this.err.divNameErrMsg = "필수 정보입니다."
      }
      else this.err.divNameErrMsg = ""
    },
    "data.divisionNum": function() {
      if(!this.data.divisionNum){
        this.err.divNumErrMsg = "필수 정보입니다."
      }
      else this.err.divNumErrMsg = ""
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
      this.numValidFlag = false;
    },
    // SMS 인증 번호를 받는 함수
    getSmsNumber(phoneNum) {
      this.$axios.post(
        "users/authSms/",
        {"phoneNum": phoneNum}
      )
      .then((res)=>{
      console.log(res)
      alert("입력된 번호로 인증번호를 전송하였습니다.")
      })
      .catch((err)=>{
        console.log(err)
        alert("11자리 번호를 입력해주세요.")
      })
    },
    // SMS 인증 번호를 인증하는 함수
    checkSmsNumber(phoneNum, authNum) {
      this.$axios({
        method: "GET",
        url:"users/authSms/",
        params :{"phoneNum": phoneNum, "authNum": authNum}
      })
      .then((res)=>{
        console.log(res)
        console.log(res.data.result)
        if(res.data.result) {
          this.numValidFlag = true
          alert("인증번호가 일치합니다.")
        }
        else {
          this.numValidFlag = false
          alert("인증번호가 일치하지 않습니다.")
        }
      })
      .catch((err)=>{
        console.log(err)
        alert("4자리 인증번호를 입력해주세요.")
      })
    },
    signup() {
      this.$axios
        .post("users/api/regist/", this.data)
        .then(() => {
          this.moveToPage('Complete');
        })
        .catch((err) => {
          console.log("회원가입 실패");
          console.log(err)
        });
    },
    totalCheck() {
      let check = null
      //비밀번호 빈값 체크
      if(!this.data.password){
        this.err.pwErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.pwErrMsg = ""

      //비밀번호 확인 빈값 체크
      if(!this.data.passwordValid){
        this.err.pwCkErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.pwCkErrMsg = ""

      //이름 빈값 체크
      if(!this.data.name){
        this.err.nameErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.nameErrMsg = ""

      if(!this.data.phoneNum){
        this.err.phoneErrMsg = "필수 정보입니다."
        check++
      }
      else if(this.data.phoneNum.length != 11) {
        this.err.phoneErrMsg = "11자리 번호를 입력해주세요."
        check++
      }
      else this.err.phoneErrMsg = ""


      if(!this.data.authNum){
        this.err.authErrMsg = "필수 정보입니다."
        check++
      }
      else if(this.data.authNum.length != 4){
        this.err.authErrMsg = "4자리 인증번호를 입력해주세요."
        check++
      }
      else this.err.authErrMsg = ""

      if(!this.data.team){
        this.err.teamErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.teamErrMsg = ""

      if(!this.data.divisionName){
        this.err.divNameErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.divNameErrMsg = ""

      if(!this.data.divisionNum){
        this.err.divNumErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.divNumErrMsg = ""

      return check

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
      } 
      else if(!this.numValidFlag){
        alert("보호자 휴대폰 인증번호 확인 필요")
      }
      else{
        this.data.birthDate = this.year + this.month + this.day
        if(!this.totalCheck()) {
          this.signup();
        }
        else {
          alert("정보를 정확히 입력해주세요.")
        }
      }
    },
  },
};
</script>

<style>
  .content-title{
    font-weight: 900;
    border-right: 2px solid grey;
    background-color: rgba(238, 238, 238, 0.85);
  }
</style>
