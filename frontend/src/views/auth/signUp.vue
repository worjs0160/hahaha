<template>
  <v-container class="singUpinBox" style="height:100%; padding: 0; overflow: hidden;">
    <v-window v-model="step" touchless>
      <v-window-item :value="1">
        <div class="manage-val1-wrap" style="padding: 12px;">
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
            <button class="id-chk-btn pre-400" type="button" @click="validId">
              중복 확인
            </button>
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
            {{err.basicMessage}}
          </span>

          <div class="manage-val1-nameBox manage-val1-inputBox mt-7">
            <h2>대표자 성함<span class="manage-val1-errBox pre-400" style="color: red;"> *</span></h2>
            <input
              type="text"
              placeholder="성함을 입력해 주세요(필수)"
              v-model="data.storeMaster"
            />
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게이름<span class="manage-val1-errBox pre-400" style="color: red;"> *</span></h2>
            <input
              type="text"
              placeholder="가게이름을 입력해 주세요(필수)"
              v-model="data.storeName"
            />
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox mt-5">
            <h2>가게주소</h2>
            <input
              class="inputBox-id"
              type="text"
              placeholder="* 우편번호(주소검색)"
              v-model="data.userZip"
              
            />
            <button class="id-chk-btn pre-400" type="button" @click="showDaum">
              주소 검색
            </button>
          </div>

          <div class="manage-val1-pw1Box manage-val1-inputBox">
            <h2></h2>
            <input
              type="text"
              placeholder="* 기본주소(주소검색)"
              v-model="data.userAddr1"
              
            />
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox mb-5">
            <h2></h2>
            <input
              type="text"
              placeholder="상세주소(입력해 주세요)"
              v-model="data.userAddr2"
            />
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게 번호</h2>
            <input
              type="text"
              placeholder="전화번호를 입력해 주세요(-제외)"
              v-model="data.phone"
            />
          </div>
          <span class="manage-val1-errBox pre-400" style="color: red;">
            {{err.infoMessage}}
          </span>
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
            <p class="pre-400">{{data.username}}</p>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게이름</h2>
            <p class="pre-400">{{data.storeName}}</p>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>가게이름</h2>
            <p class="pre-400">{{data.storeName}}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>대표자</h2>
            <p>{{data.storeMaster}}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>연락처</h2>
            <p>{{data.phone}}</p>
          </div>
        </div>
        <!--e:manage-val4-wrap-->
      </v-window-item>
    </v-window>
    <v-row class="manage-btnBox" justify="end" style="width:500px; padding: 24px; margin:0;">
      <v-col align="start" v-if="step == 1">
        <v-btn @click="backToHome()">이전</v-btn>
      </v-col>
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
        passwordValid : "",
        storeName : "",
        userZip : "",
        userAddr1 : "",
        userAddr2 : "",
        storeMaster : "",
        phone : "",
        userType : "1",
      },
      err: {
        basicMessage: null,
        infoMessage: null,
      },
      idValidFlag: false,
      validFlag: false,
      infoValidFlag: false,
    };
  },
  methods: {
    signup() {
      if(this.idValidFlag && this.validFlag && this.infoValidFlag){
        this.$axios({
            method: 'POST',
            url: "users/api/userRegist/",
            data: this.data
          })
          .then(() => {
            this.step = 2;
            this.$store.dispatch("callToast", {
              msg: "성공적으로 계정을 생성하였습니다.",
              result: "success",
            });
          })
          .catch(() => {
            this.$store.dispatch("callToast", {
              msg: "정보입력의 유형이 올바르지 않습니다. 정확히 입력해 주세요.",
              result: "error",
            });
          });
      }
      else {
        this.basicValid()
        this.infoValid()
      }
    },
    // router 이용하여 이동할 페이지 선언
    backToHome: function() {
      var router = this.$router;
      return router.push({ name: "Login" });
    },
    validId() {
      let check = /[a-z0-9]{5,20}/;
      let checkEng_A = /[A-Z]/;
      if (!this.data.username) {
        this.err.basicMessage = "* 아이디는 필수 정보입니다.";
      } else if (
        check.test(this.data.username) == false ||
        checkEng_A.test(this.data.username) == true
      ) {
        this.err.basicMessage =
          "* 아이디는 5~20자의 영문 소문자, 숫자만 사용 가능합니다.";
      } else {
        this.$axios
          .post("users/api/userRegist/chk_username/", {
            username: this.data.username,
          })
          .then((res) => {
            this.idValidFlag = true;
            this.basicValid();
            alert(res.data.msg);
          })
          .catch((err) => {
            console.log(err.response);
            alert(err.response.data.msg);
          });
      }
    },
    basicValid() {
      //아이디부터 비밀번호까지 순서대로 유효성 체크하는 함수
      this.validFlag = false; // 각 데이터의 내용을 바꾸면 검증 플래그 초기화
      let check = /[a-z0-9]{5,20}/;
      let checkEng_A = /[A-Z]/;
      let checkNum1 = /[0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]{8,}/;
      let checkNum2 = /[0-9]/;
      let checkSpc = /[~!@#$%^&*()_+|<>?:{}]/;
      if (!this.data.username) {
        this.err.basicMessage = "* 아이디는 필수 정보입니다.";
      } else if (
        check.test(this.data.username) == false ||
        checkEng_A.test(this.data.username) == true
      ) {
        this.err.basicMessage =
          "* 아이디는 5~20자의 영문 소문자, 숫자만 사용 가능합니다.";
      } else if (!this.data.password) {
        this.err.basicMessage = "* 비밀번호는 필수 정보입니다.";
      } else if (
        checkNum1.test(this.data.password) == false ||
        checkSpc.test(this.data.password) == false ||
        checkNum2.test(this.data.password) == false
      ) {
        this.err.basicMessage =
          "* 비밀번호는 8자 이상, 특수문자, 숫자를 포함하여야 합니다.";
      } else if (!this.data.passwordValid) {
        this.err.basicMessage = "* 비밀번호 확인이 필요합니다.";
      } else if (this.data.password != this.data.passwordValid) {
        this.err.basicMessage = "* 비밀번호가 일치하지 않습니다.";
      } else if (this.idValidFlag == false)
        this.err.basicMessage = "* 아이디 중복검사가 필요합니다.";
      else if (
        this.data.username &&
        this.data.password &&
        this.data.passwordValid &&
        this.idValidFlag
      ) {
        this.err.basicMessage = "";
        this.validFlag = true;
      }
    },
    infoValid(){
      //필수기입란 검사
      this.infoValidFlag = false
      if(!this.data.storeMaster){
        this.err.infoMessage = "* 대표자 성함은 필수 정보입니다.";
      }
      else if(!this.data.storeName){
        this.err.infoMessage = "* 가게이름은 필수 정보입니다.";
      }
      else if(this.data.storeMaster && this.data.storeName){
        this.err.infoMessage = "";
        this.infoValidFlag = true;
      }
    },
    showDaum() {
      new window.daum.Postcode({
        oncomplete: (data) => {
          // 팝업에서 검색결과 항목 클릭했을 때 실행할 코드를 작성하는 부분
          // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
          // 변수의 값이 없는 경우엔 공백('')값 가지므로, 이를 이용하여 분기
          let fullRoadAddr = data.roadAddress; // 도로명 주소 변수
          let extraRoadAddr = ""; // 도로명 조합형 주소 변수
          // 법정동명이 있을경우 추가한다. (법정리는 제외)
          // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
          if (data.bname !== "" && /[동|로|가]$/g.test(data.bname)) {
            extraRoadAddr += data.bname;
          }
          // 건물명이 있고, 공동주택일 경우 추가한다.
          if (data.buildingName !== "" && data.apartment === "Y") {
            extraRoadAddr +=
              extraRoadAddr !== ""
                ? ", " + data.buildingName
                : data.buildingName;
          }
          // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
          if (extraRoadAddr !== "") {
            extraRoadAddr = " (" + extraRoadAddr + ")";
          }
          // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
          if (fullRoadAddr !== "") {
            fullRoadAddr += extraRoadAddr;
          }
          // 우편번호와 주소 정보를 해당 필드에 넣는다.
          this.data.userZip = data.zonecode;
          this.data.userAddr1 = fullRoadAddr;
        },
      }).open();
    },
  },
  watch: {
    "data.username": function() {
      // 아이디 체크
      this.idValidFlag = false; // 아이디 바꾸면 아이디 중복검증 플래그 초기화
      this.basicValid();
    },
    "data.name": function() {
      this.basicValid();
    },
    "data.password": function() {
      // 비밀번호 체크 및 비밀번호 확인 체크
      this.basicValid();
    },
    "passwordValid": function() {
      this.basicValid();
    },
    "data.storeMaster": function() {
      this.infoValid();
    },
    "data.storeName": function() {
      this.infoValid();
    },
  },
};
</script>

<style>
  .singUpinBox {
    width: 50% !important;
    margin: 120px auto;
  }
  .background{
    background-color:rgba(240, 240, 240);
    border-radius: 10px;
  }
  .manage-val1-wrap {}
  .manage-val1-wrap .manage-val1-title {
    margin-bottom: 32px;
  }
  .manage-val1-wrap .manage-val1-title p {
    font-size: 18px;
    color: #2e2e2e;
    margin: 0;
  }
  .manage-val1-wrap .manage-val1-inputBox {
    display: flex;
    align-items: center;
    height: 39px;
    margin-bottom: 8px;
  }
  .manage-val1-wrap .manage-val1-inputBox h2 {
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-SemiBold';
    width: 90px;
    margin-right: 28px;
  }
  .manage-val1-wrap .manage-val1-inputBox input {
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    height: 100%;
    width: 370px;
    padding: 0 12px;
    font-size: 16px;
    color: #000;
    font-family: 'Pretendard-Regular';
  }
  .manage-val1-wrap .manage-val1-inputBox input::placeholder {
    color: #b4b4b4;
  }
  .manage-val1-wrap .manage-val1-inputBox input:focus,
  .manage-val1-wrap .manage-val1-inputBox button:focus {
    outline-color: #49ada9;
  }
  .manage-val1-wrap .manage-val1-inputBox .inputBox-id {
    width: 257px;
  }
  .manage-val1-wrap .manage-val1-inputBox .id-chk-btn {
    font-size: 13px;
    color: #49ada9;
    background: #EFF9F8;
    border-radius: 3px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 107px;
    margin-left: 6px;
    transition: all .3s;
  }
  .manage-val1-wrap .manage-val1-inputBox .id-chk-btn:hover {
    background: #49ada9;
    color: #fff;
  }
  .manage-value1-errBox {
    font-size: 13px;
    color: red;
  }
  .manage-btnBox {
    width: 100%;
    margin-top: 44px;
  }
  .manage-btnBox .col {}
  .manage-btnBox button {
    width: 126px !important;
    height: 48px !important;
    background-color: #EFF9F8 !important;
    border-radius: 10px;
    box-shadow: none;
    padding: 0 !important;
    transition: all .5s;
  }
  .manage-btnBox button:hover {
    background: #49ada9 !important;
  }
  .manage-btnBox button:hover span {
    color: #fff !important;
  }
  .manage-btnBox button span {
    font-family: 'Pretendard-Regular';
    font-size: 18px;
    color: #49ada9;
    transition: all .5s;
  }
  .manage-btnBox button span svg {
    transition: all .5s;
  }
  .manage-btnBox .nextBtn span svg {
    margin-left: 14px;
  }
  .manage-btnBox button:hover span svg,
  .manage-btnBox button:focus span svg {
    fill: #fff !important;
  }
  .manage-btnBox .preBtn span svg {
    margin-right: 14px;
  }
  .manage-btnBox .buttonsuccess {
    background-color: #49ada9 !important;
  }
  .manage-btnBox .buttonsuccess span {
    color: #fff !important;
  }
  .manage-btnBox .buttonsuccess span svg {
    fill: #fff !important;
  }
  .manage-btnBox .buttonerrer {
    background: #F5F5F5;
  }
  .manage-btnBox .buttonerrer span {
    color: #646464;
  }
  .manage-btnBox .buttonerrer:hover {
    background-color: rgb(242, 95, 95) !important;
  }

  .manage-val2-top {
    display: flex;
    flex-direction: column;
  }
  .manage-val2-title {
    margin-bottom: 32px;
  }
  .manage-val2-title2 {
    margin-bottom: 12px;
  }
  .manage-val2-title p {
    font-size: 18px;
    color: #2e2e2e;
    margin: 0;
  }
  .manage-value2-top-inputBox {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  .manage-value2-top-inputBox h2 {
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    width: 97px;
    margin-right: 28px;
    font-weight: 500;
  }
  .inputBox-work-name {
    width: 370px;
    height: 39px;
    padding: 0 12px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    color: #000;
    
  }
  .value2-selectBox {
    width: 172px;
    height: 39px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
  }
  .value2-selectBox .v-input__slot {
    height: 39px !important;
    min-height: auto !important;
  }
  .inputBox-work-name::placeholder {
    color: #989898;
  }
  .inputBox-work-name:focus,
  .value2-selectBox:focus {
    outline-color: #49ada9;
  }
  .times-selectBox {
    display: flex;
    align-items: center;
  }
  .times-selectBox span {
    display: block;
    margin: 0 8px;
  }
  .times-input {
    width: 130px;
    height: 39px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
  }
  .times-selectBox fieldset {
    display: none;
  }
  .input_label_position_transform  .times-selectBox label {
    position: unset !important;
  }
  .v-select__slot {
    display: flex;
    align-items: center;
  }
  .v-application--is-ltr .v-text-field .v-input__append-inner {
    margin: 0;
    align-self: unset;
  }
  .manage-value2-top-inputBox .value-btnBox {}
  .manage-value2-top-inputBox .value-btnBox button {
    margin-right: 6px;
    width: 34px !important;
    min-width: auto !important;
    height: 32px !important;
    border-radius: 6px !important;
    background-color: #B4B4B4 !important;
    border: 0 !important;
  }
  .manage-value2-top-inputBox .value-btnBox span {
    color: #fff;
    font-family: 'Pretendard-Regular';
    font-size: 20px;
    font-weight: 400 !important; 
  }
  .v-btn-toggle > .v-btn.v-btn--active {
    background-color: #0081C7 !important;
    color: #fff !important;
  }
  .value2-errBox {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Pretendard-Regular';
    margin-bottom: 30px;
    width: 540px;
  }
  .value2-errBox .val2-err1 {
    color: red;
  }
  .value2-errBox .val2-err2 {
    color: #2e2e2e;
    background-color: #49ada9;
    border-radius: 5px;
    padding: 5px 10px;
    color: #fff;
    margin: 0;
  }
  .manage-val2-btm-info {
    background-color: #E4F2F9;
    display: flex;
    align-items: center;
    padding: 8px;
    border-radius: 3px;
    margin-bottom: 32px;
    width: 495px;
  }
  .manage-val2-btm-info svg {
    margin-right: 8px;
  }
  .manage-val2-btm-info p {
    color: #0081c7;
    font-size: 14px;
    margin: 0;
  }
  .manage-value2-top-inputBox .v-text-field--rounded {
    border-radius: 3px;
    width: 370px;
    height: 39px;
  }
  .val2-btm-selectBox {
    width: 370px;
    height: 39px;
  }
  .val2-btm-selectBox .v-input__slot {
    height: 39px !important;
    min-height: auto !important;
  }
  .manage-value2-top-inputBox {
    width: 495px !important;
  }
  .v-text-field--rounded > .v-input__control > .v-input__slot {
    padding: 0 12px;
  }
  .input_label_position_transform .v-text-field--outlined .v-label--active,
  .input_label_position_transform .v-text-field .v-label--active {
    transform:unset;
    font-size: 12px;
    margin-right: 10px;
  }
  .v-input--selection-controls {
    margin-top: 16px;
    padding-top: 0;
  }
  .v-input__slot {
    margin-bottom: 0;
  }
  .v-input--switch__track {
    border-radius: 16px;
    width: 46px;
    height: 26px;
    left: -3px;
    position: absolute;
    opacity: 0.6;
    right: 2px;
    top: calc(50% - 13px);
  }
  .v-application--is-ltr .v-input--selection-controls__input {
    margin-right: 15px;
  }
  .v-input--selection-controls .v-input__slot > .v-label {
    font-family: 'Pretendard-Regular';
    font-size: 15px;
  }
  .theme--light.v-input--switch .v-input--switch__track {
    /* background-color: #008bd6; */
  }
  .v-input--switch:not(.v-input--switch--flat):not(.v-input--switch--inset) .v-input--switch__thumb {
    color: #fff !important;
  }
  .v-application--is-ltr .v-text-field .v-label {
    font-family: 'Pretendard-Regular';
  }
  .manage-val3-wrap {}
  .manage-val3-wrap .manage-val3-header {
    width: 100%;
    height: 72px;
    border-bottom: .5px solid #b4b4b4;
    display: flex;
    align-items: center;
    padding: 0 24px;
  }
  .manage-val3-wrap h1 {
    font-size: 20px;
    color: #2e2e2e;
    font-weight: 600;
  }
  .manage-val3-wrap .imgBox {
    width: 200px;
    height: 200px;
    margin-right: 32px;
  }
  .manage-val3-wrap .imgBox-hidden {
    width: 200px;
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 6px;
    overflow: hidden;
  }
  .manage-val3-wrap .left-emptyBox {
    width: 200px;
    height: 200px;
    margin-right: 32px;
  }
  .manage-val3-wrap .imgBox img {
    width: 100%;
  }
  .manage-val3-wrap .imgBox .v-input {
    flex: none !important;
  }
  .manage-val3-wrap .imgBox .v-input button {
    margin-right: 20px;
  }
  .manage-val3-wrap .val3Box1 {
    display: flex;
  }
  .defaultBox h2 {
    font-size: 18px;
    color: #2e2e2e;
    margin-bottom: 32px;
  }
  .defaultBox .val3-inputBox {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  .defaultBox .val3-inputBox h3 {
    font-size: 16px;
    color: #000;
    font-family: 'Pretendard-Regular';
    font-weight: 500;
    width: 90px;
    margin-right: 10px;
  }
  .defaultBox .val3-inputBox input {
    width: 370px;
    height: 39px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    font-size: 16px;
    color: #000;
    padding: 0 12px;
    font-family: 'Pretendard-Regular';
    font-weight: 500;
  }
  .defaultBox .val3-inputBox input::placeholder {
    color: #989898;
  }
   .defaultBox .val3-inputBox input:focus,
   .addressBox-1 button:focus,
   input:focus,
   textarea:focus {
    outline-color: #49ada9 !important;
  }
  .genderBox {
    display: flex;
    align-items: center;
  }
  .genderBox {
    font-size: 16px;
    color: #fff;
    font-family: 'Pretendard-Regular';
    cursor: pointer;
  }
  .genderBox button {
    transition: all .5s;
  }
  .gender-male {
    border-radius: 3px 0px 0px 3px;
    width: 185px;
    height: 39px;
    border: 1px solid #e1e1e1;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #989898;
  }
  .gender-woman {
    border-radius: 0px 3px 3px 0px;
    width: 185px;
    height: 39px;
    border: 1px solid #e1e1e1;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #989898;
  }
  /* .gender-male:hover,
  .gender-woman:hover {
    background: #47a7da !important;
    border: 1px solid #47a7da !important;
    color: #fff !important;
  } */
  .gender-active {
    background: #0081c7 !important;
    border: 1px solid #0081c7 !important;
    color: #fff !important;
  }
  .addressBox {
    display: flex;
    flex-direction: column;
    margin-bottom: 0 !important;
  }
  .addressBox > div {
    display: flex;
    width: 100%;
    margin-bottom: 10px;
  }
  .addressBox-1 {
    align-items: center;
  }
  .addressBox-1 input {
    width: 257px !important;
  }
  .addressBox-1 button {
    width: 107px;
    height: 39px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #eff9f8;
    border-radius: 3px;
    font-size: 13px;
    color: #49ada9;
    margin-left: 6px;
    transition: all .5s;
  }
  .addressBox-1 button:hover {
    background-color: #49ada9;
    color: #fff;
  }
  .address-emptyBox {
    width: 90px;
    margin-right: 10px;
  }
  .val3Box1 {
    border-bottom: .5px solid #b4b4b4;
  }
  .val3Box3 {
    border-bottom: 0;
  }
  .v-input {
    margin: 0 !important;
    padding: 0 !important;
  }
  .v-input input {
    max-height: unset !important;
  }
  .val3Box1 .v-text-field__details {
    display: none;
  }
  .v-select__selection--comma {
    position: absolute;
    left: 12px;
    font-family: 'Pretendard-Regular';
    font-size: 16px;
  }
  .val3Box1 .v-text-field.v-input--is-focused > .v-input__control > .v-input__slot:after {
    display: none;
  }
  .val3-inputBox .input-right-p {
    position: relative;
    left: 10px;
    top: 7px;
    font-family: 'Pretendard-Regular';
    font-size: 16px;
  }
  .input73 .times-selectBox .v-select__selection--comma {
    left: 73px;
  }
  .manage-val4-wrap p {
    margin: 0;
  }
  .areaColor {
    background: #F5F5F5;
    padding: 10px;
    border-radius: 6px;
  }
  .new-player-val2-input-agency {
    border: 1px solid #e1e1e1;
  }
  .new-player-val2-input-agency div {
    background: none !important;
  }
  .new-player-val2-input-ip {
    background: rgba(0, 0, 0, 0.06);
    border: 0 !important;
  }
  .print-h2 {
    font-size: 18px !important;
  }
</style>
