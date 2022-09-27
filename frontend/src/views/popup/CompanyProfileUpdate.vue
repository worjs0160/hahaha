<template>

  <div style="padding-bottom:50px;">
      <div class="manage-val3-wrap" style="
          width: 950px;
          background: #FFFFFF;
          box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
          border-radius: 20px;
          margin: 0 auto !important;
          ">

          <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
            <h1 class="pre-400">상세정보</h1>
            <button  @click="closeProfilePopup(), updateDataFormat(), scrollTop()">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
              </svg>
            </button>
          </div>

          <div class="val3Box1" style="padding: 24px 24px 32px;">

            <div class="imgBox" style="
            position: relative;
            ">
              <div class="imgBox-hidden">
                <v-img :src="url" alt="" style="
                position: relative;
                z-index: 3;
                height: 100%;
                "></v-img>
              </div>
              <v-file-input
                v-model="profileData.profile"
                @change="preview_image()"
                accept="image/png, image/jpeg, image/bmp"
                prepend-icon="mdi-camera"
                class="detail-profile-img-input"
                label="사진 변경하기"
                style="
                box-shadow: 0px 1px 8px rgba(0, 0, 0, 0.1);
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                border-radius: 5px;
                margin-top: 15px !important;
                "
              ></v-file-input>

              <!-- <div class="profile-inputBox" style="
              width: 100%;
              position: absolute;
              bottom:-50px;
              left: 50%;
              transform: translateX(-50%);
              display: flex;
              justify-content: center;
              align-items: center;
              border-radius: 5px;
              padding: 7px 0;
              box-shadow: 0px 1px 8px rgba(0, 0, 0, 0.1);
              ">

                <v-file-input
                  v-model="profileData.profile"
                  @change="preview_image()"
                  hide-input
                  accept="image/png, image/jpeg, image/bmp"
                  prepend-icon="mdi-camera"
                  show-size
                ></v-file-input>

                <p class="pre-400 kimjinhyeok" style="
                margin: 0;
                ">
                  사진 변경하기
                </p>

              </div> -->
                

            </div>

            <div class="defaultBox">
              <div class="manage-val2-top">
                <div class="manage-val2-title">
                  <p class="pre-700">훈련일정</p>
                </div>

                <!-- <div class="manage-value2-top-inputBox">
                  <h2>훈련유형 이름</h2>
                  <input
                    class="inputBox-work-name pre-400"
                    type="text"
                    placeholder="훈련유형 이름을 입력해 주세요"
                    v-model="attData.name"
                  />
                </div> -->

                <div class="input73 manage-value2-top-inputBox">
                  <h2>훈련시간</h2>
                  <div class="times-selectBox">
                    <input
                      class="times-input pa-2"
                      type="time"
                      v-model="attData.onTime"
                    />

                    <span>~</span>

                    <input
                      class="times-input pa-2"
                      type="time"
                      v-model="attData.offTime"
                    />
                  </div>
                </div>

                <!-- <v-row>
                  <v-col cols="6">
                    <v-card-text class="px-0" style="font-weight: 700;">일 기본 휴게시간</v-card-text>
                  </v-col>
                  <v-col cols="6">
                    <v-select
                      :items="rest"
                      label="휴게시간"
                      outlined
                    ></v-select>
                  </v-col>
                </v-row> -->

                <div class="manage-value2-top-inputBox">
                  <h2>훈련일자</h2>
                  <v-btn-toggle
                    class="value-btnBox"
                    v-model="attData.workDay"
                    multiple
                  >
                    <v-btn value="24" class="px-0">월</v-btn>
                    <v-btn value="25" class="px-0">화</v-btn>
                    <v-btn value="26" class="px-0">수</v-btn>
                    <v-btn value="27" class="px-0">목</v-btn>
                    <v-btn value="28" class="px-0">금</v-btn>
                    <v-btn value="29" class="px-0">토</v-btn>
                    <v-btn value="30" class="px-0">일</v-btn>
                  </v-btn-toggle>
                </div>

                <div class="value2-errBox">
                  <p class="val2-err1">{{ err.attMessage }}</p>
                  <p class="val2-err2" v-if="attData.monthWorkTime">
                    주 {{ attData.monthWorkTime }}시간
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div class="val3Box1 val3Box2" style="padding: 32px 24px;">

            <div class="left-emptyBox"></div>

            <div class="defaultBox">

              <h2 class="pre-600">기본정보</h2>



              <div class="nameBox val3-inputBox">
                <h3>이름</h3>
                <input type="text" placeholder="이름을 입력해 주세요" v-model="data.name">
              </div>

              <div class="genderBox val3-inputBox">
                <h3>성별</h3>
                <div class="genderBox">
                  <!-- gender-active를 주면 색상 변경 -->
                  <v-btn-toggle v-model="data.gender">
                    <v-btn class="gender-male" value="남성">
                      남성
                    </v-btn>
            
                    <v-btn class="gender-woman" value="여성">
                      여성
                    </v-btn>
                  </v-btn-toggle>
                </div>
              </div>

              <div class="birthBox val3-inputBox">
                <h3>생년월일</h3>
                <input type="number" placeholder="생년월일 8자리를 입력해 주세요 (ex.20001203)" v-model="data.birthDate">
              </div>

              <div class="tellBox val3-inputBox">
                <h3>연락처</h3>
                <input type="number" placeholder="(ex.010-1234-5678)" v-model="data.phone">
              </div>

              <div class="addressBox val3-inputBox">

                <div class="addressBox-1">
                  <h3>주소</h3>
                  <input type="text" placeholder="* 우편번호(주소검색)" v-model="data.userZip" readonly>
                  <button class="pre-600" type="button" @click="showDaum">우편번호 검색</button>
                </div>

                <div class="addressBox-2">
                  <div class="address-emptyBox"></div>
                  <input type="text" placeholder="* 기본주소(주소검색)" v-model="data.userAddr1" readonly>
                </div>
              
                <div class="addressBox-3">
                  <div class="address-emptyBox"></div>
                  <input type="text" placeholder="상세주소(입력해 주세요)" v-model="data.userAddr2">
                </div>
                
              </div>

              <div class="guardian-nameBox val3-inputBox">
                <h3>보호자 이름</h3>
                <input type="text" placeholder="보호자 이름을 입력해 주세요" v-model="data.guardianName">
              </div>

              <div class="guardian-tellBox val3-inputBox">
                <h3>보호자 연락처</h3>
                <input type="number" placeholder="보호자 연락처를 입력해 주세요" v-model="data.guardianNum">
              </div>

            </div>

          </div><!--e:val3Box1-->

          <div class="val3Box1 val3Box2" style="padding: 32px 24px;">

            <div class="left-emptyBox"></div>

            <div class="careerBox defaultBox">

              <h2 class="pre-600">경력사항</h2>

              <div class="val3-inputBox">
                <h3>운동종목</h3>
                <v-select
                  v-model="data.sportType"
                  :items="sportTypeList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>경력</h3>
                <input type="text" placeholder="경력을 입력해 주세요" v-model="data.career">
              </div>

              <div class="val3-inputBox">
                <h3>훈련기관</h3>
                <v-select
                  v-model="data.teamID"
                  :items="teamList"
                  item-text="teamName"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>수상경력</h3>
                <input type="text" placeholder="수상경력을 입력해 주세요">
              </div>

            </div>

          </div><!--e:val3Box2-->

          <div class="val3Box1 val3Box3" style="padding: 32px 24px 0">
            
            <div class="left-emptyBox"></div>

            <div class="personalBox defaultBox">

              <h2 class="pre-600">개인사항</h2>

              <div class="val3-inputBox">
                <h3>장애유형</h3>
                <v-select
                  v-model="data.disabilityType"
                  :items="disabilityList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>장애등급</h3>
                <v-select
                  :items="disabilityGradeList"
                  item-text="value"
                  item-value="id"
                  v-model="data.disabilityGrade"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>신장</h3>
                <input type="number" placeholder="ex) 173" v-model="data.height"><p class="input-right-p">cm</p>
              </div>

              <div class="val3-inputBox">
                <h3>체중</h3>
                <input type="number" placeholder="ex) 55" v-model="data.weight"><p class="input-right-p">kg</p>
              </div>

              <div class="val3-inputBox">
                <h3>최종학력</h3>
                <v-select
                  v-model="data.education"
                  :items="educationList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>학교명</h3>
                <input type="text" v-model="data.school">
              </div>


            </div>

          </div>

          <div class="update-btnBox">
            <v-btn class="update-btn1 pre-400" @click="closeProfilePopup(), updateDataFormat(), scrollTop()">취소</v-btn>
            <v-btn v-if="attValidFlag" class="update-btn2 pre-400" @click="signup(), closeProfilePopup(), scrollTop()">저장하기</v-btn>
            <v-btn v-if="!attValidFlag" class="update-btn3 pre-400">저장하기</v-btn>
          </div>

        </div><!--e:manage-val3-wrap-->
  </div>

</template>


<script>
export default {
  async created() {
    await this.loadingCover(true);
    // 공통데이터 가져오기
    await this.$axios
      .get("datasets/api/commondata/")
      .then((res) => {
        for (const data of res.data) {
          // 1 (장애등급)
          if (data.maincategory == 1) {
            this.disabilityGradeList.push(data);
          }
          // 5 (최종학력)
          else if (data.maincategory == 5) {
            this.educationList.push(data);
          }
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 장애유형 가져오기
    await this.$axios
      .get("datasets/api/disability_type/")
      .then((res) => {
        for (const data of res.data) {
          this.disabilityList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 운동종목 가져오기
    await this.$axios
      .get("datasets/api/sport_type/")
      .then((res) => {
        for (const data of res.data) {
          this.sportTypeList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 기업목록 가져오기
    await this.$axios
      .get("datasets/api/company_list/")
      .then((res) => {
        for (const data of res.data) {
          this.companyList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 복지관(훈련기관) 가져오기
    await this.$axios
      .get("datasets/api/team_list/")
      .then((res) => {
        for (const data of res.data) {
          this.teamList.push( data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });
    await this.timeSet()
    await this.loadingCover(false);
  },
  data: () => ({
    step: 1,
    times:[],
    userID: '',
    //rest:['없음', '30분', '1시간', '1시간 30분', '2시간'],
    selectWorkTime: [],
    dataFormat: {},
    data: {
      id:'',
      username: "", // ID
      password: "",
      createUser: 0,
      modifyUser: null,
      is_superuser: false,
      gender: "",
      is_staff: false,
      is_active: true,
      name: "",
      //profile: "",
      userType: 1,
      birthDate: "",
      phone: "",
      userZip: "", //우편번호
      userAddr1: "",
      userAddr2: "",
      career: null, //운동경력
      awards: "", //수상경력
      height: "",
      weight: "",
      school: "",
      guardianName: "",
      guardianNum: "",
      comID: null,
      attType: 1,
      sportType: null,
      teamID: null,
      disabilityType: null,
      disabilityGrade: null,
      education: null,
    },
    profileDataFormat:{},
    url:"", // 미리보기용 url
    profileData:{
      id:"",
      name:"",
      profile:"",
    },
    genderList: [ // 성별 리스트
      { type: "남성", value: 1 },
      { type: "여성", value: 2 },
    ],
    attData: {
      name:"",
      onTime:"",
      offTime:"",
      monthWorkTime:"",
      workDay:[],
    },
    onTime:0,
    offTime:0,
    err: {
      basicMessage: null,
      attMessage: null,
      onTimeErrMsg: null,
      offTimeErrMsg: null,
      workTimeErrMsg: null,
    },
    disabilityList: [], // 장애 리스트
    disabilityGradeList: [], // 장애 등급
    sportTypeList: [], // 운동종목 리스트
    companyList: [], // 기업목록 리스트
    teamList: [], // 복지관(훈련기관) 리스트
    educationList:[], //최종학력
    attValidFlag: true,
  }),
  methods: {
    loadingCover(val) {
      this.$emit("coverSetChild", val);
    },
    scrollTop(){
      document.getElementById('companyProfile').scrollTo(0,0)
    },
    preview_image() {
      this.url = URL.createObjectURL(this.profileData.profile)
    },
    async settingAccount(id){
      //계정 정보 세팅
      await this.$axios
        .get("users/api/employee/"+id+"/")
        .then((res) => {
          this.data = res.data
          if(res.data)this.data.id = res.data.id
          if(res.data.sportType)this.data.sportType = res.data.sportType.id
          if(res.data.teamID)this.data.teamID = res.data.teamID.id
          if(res.data.disabilityType)this.data.disabilityType = res.data.disabilityType.id
          if(res.data.disabilityGrade)this.data.disabilityGrade = res.data.disabilityGrade.id
          delete this.data.profile

          //선택한 선수의 훈련일정 가져오기
          this.$axios
          .get("attendances/api/attType/"+res.data.attType.id+"/")
          .then((attRes) => {
            if(attRes)this.data.attType = attRes.data.id
            var formatDay = []
            this.timeSet()
            this.attData = attRes.data
            for(var i in this.attData.workDay){
              formatDay.push(String(this.attData.workDay[i]))
            }
            this.attData.workDay = formatDay
            this.attValidFlag = true
          })
      });
      await this.$axios
        .get("users/api/image/"+id+"/")
        .then((res) => {
          this.profileData = res.data
          this.url = res.data.profile
        });
      this.dataFormat = JSON.parse(JSON.stringify(this.data))
      this.profileDataFormat = JSON.parse(JSON.stringify(this.profileData))
    },
    updateDataFormat(){
      this.data = JSON.parse(JSON.stringify(this.dataFormat))
      this.profileData = JSON.parse(JSON.stringify(this.profileDataFormat))
      this.imageFlag = false
    },
    closeProfilePopup(){
      this.$emit("closeProfilePopup");
    },
    updateCompanyProfile(){
      this.$emit("updateCompanyProfile");
    },
    attValid() {
      //훈련시간 유효성 체크
      this.attValidFlag = false;
      if (!this.attData.onTime)
        this.err.attMessage = "* 출근시간은 필수입니다.";
      else if (!this.attData.offTime)
        this.err.attMessage = "* 퇴근시간은 필수입니다.";
      else if (!this.attData.workDay)
        this.err.attMessage = "* 근무 요일을 선택해주세요";
      else if ((this.offTime - this.onTime) * this.attData.workDay.length <= 0){
        this.err.attMessage = "* 출퇴근 시간과 근무요일을 확인해주세요";
      }
      else if (
        this.attData.onTime &&
        this.attData.offTime &&
        this.attData.workDay &&
        this.attData.monthWorkTime
      ) {
        this.err.attMessage = "";
        this.attValidFlag = true;
      }
    },
    back() {
      this.step--;
    },
    next() {
      this.step++;
    },
    timeSet(){
      for(var i=1; i<25; i++){
        if(i<10){
          var num = "0"+i;
          this.times.push(num+":00");
        }
        else{
          this.times.push(i+":00");
        }
      }
    },
    async signup() {
      //계정 수정
      await this.$axios({
          method: "PATCH",
          url: "attendances/api/attType/"+this.attData.id+"/",
          data: this.attData,
        })
        .then(() => {
          console.log(1)
          this.$store.dispatch("callToast", {
            msg: this.data.name+"님의 상세정보를 수정하였습니다.",
            result: "success",
          });
        });

      await this.$axios({
          method: "PATCH",
          url: "users/api/employee/"+this.data.id+"/",
          data: this.data,
        })
        .then(() => {
          this.updateCompanyProfile()
          this.$store.dispatch("callToast", {
            msg: this.data.name+"님의 상세정보를 수정하였습니다.",
            result: "success",
          });
        });

      if(this.imageFlag == true){//이미지 수정했을때만 실행
        var formData = new FormData();
        formData.append("profile", this.profileData.profile);
        await this.$axios({
          method: "PATCH",
          url: "users/api/image/" + this.data.id + "/",
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          data: formData,
          })
          .then(() => {
            this.updateCompanyProfile()
          });
      }

      this.dataFormat = JSON.parse(JSON.stringify(this.data))
      this.profileDataFormat = JSON.parse(JSON.stringify(this.profileData))
      this.imageFlag = false
    },
    workTimeSet(){
      if(this.onTime && this.offTime && (this.attData.workDay.length)>0){
        this.attData.monthWorkTime = (this.offTime - this.onTime)*this.attData.workDay.length
      }
    },
    // 주소 가져오는 함수
    /* eslint-disable */
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
    "profileData.profile": function(){
      this.imageFlag = true
    },
    "attData.onTime": function() {
      this.onTime = Number(this.attData.onTime.substr(0, 2));
      this.workTimeSet();
      this.attValid();
    },
    "attData.offTime": function() {
      this.offTime = Number(this.attData.offTime.substr(0, 2));
      this.workTimeSet();
      this.attValid();
    },
    "attData.workDay": function() {
      this.workTimeSet();
      this.attValid();
    },
  },
};
</script>

<style>
  .background{
    background-color:rgba(240, 240, 240);
    border-radius: 10px;
  }
  .update-btnBox {
    display: flex;
    justify-content: center;
    align-content: center;
  }
  .update-btnBox button {
    margin: 64px 0 24px;
    font-size: 18px !important;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 10px !important;
    box-shadow: none;
  }
  .update-btnBox .update-btn1 {
    color: #646464;
    background: #F5F5F5 !important;
    width: 126px;
    height: 48px !important;
    margin-right: 10px;
  }
  .update-btnBox .update-btn2 {
    color: #fff;
    background: #61C0BD !important;
    width: 252px;
    height: 48px !important;
  }
  .update-btnBox .update-btn3 {
    color: #fff;
    background: rgb(216, 216, 215) !important;
    width: 252px;
    height: 48px !important;
  }
  .v-application--is-ltr .v-input__prepend-outer {
    margin: 0;
  }
</style>
