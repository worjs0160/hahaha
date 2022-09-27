<template>
  <v-container style="height:100%; padding: 0; overflow: hidden;">
    <v-window v-model="step" touchless>
      <v-window-item :value="1">
        <div class="manage-val3-wrap">
          <div class="manage-val3-header">
            <h1 class="pre-400">상세정보</h1>
          </div>

          <div class="val3Box1" style="padding: 24px 24px 32px;">
            <!-- <div class="imgBox">
              <p
                class="pre-400"
                style="position: absolute; z-index:1; margin: 0;"
                v-if="!url"
              >
                사진미리보기
              </p>
              <img :src="url" alt="" style="position: relative; z-index: 3;" />
            </div> -->

            <div class="imgBox" style="
            position: relative;
            ">
              <div class="imgBox-hidden">
                <v-img :src="url" alt="" style="
                position: relative;
                z-index: 3;
                height: 100%;
                width: 100%;
                object-fit: cover;
                "></v-img>
              </div>

              <v-file-input
                v-model="profileData.profile"
                @change="preview_image()"
                accept="image/png, image/jpeg, image/bmp"
                prepend-icon="mdi-camera"
                class="detail-profile-img-input"
                label="사진 추가하기"
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
                

            </div>

            <div class="defaultBox">
              <h2 class="pre-600">기본정보</h2>

              <!-- <div class="nameBox val3-inputBox">
                <h3>이미지 추가</h3>
                <v-file-input
                  v-model="profileData.profile"
                  @change="preview_image()"
                  label="클릭하여 이미지 추가"
                  accept="image/png, image/jpeg, image/bmp"
                  prepend-icon="mdi-camera"
                  show-size
                  style="font-weight: 1000;"
                ></v-file-input>
              </div> -->

              <div class="nameBox val3-inputBox">
                <h3>이름</h3>
                <input
                  type="text"
                  placeholder="이름을 입력해 주세요"
                  v-model="data.name"
                />
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
                <!-- @@성별 select를 check로 구현 필요함 -->
                <!-- <v-select
                  v-model="data.gender"
                  :items="genderList"
                  item-text="type"
                  item-value="value"
                ></v-select> -->
              </div>

              <div class="birthBox val3-inputBox">
                <h3>생년월일</h3>
                <input
                  type="number"
                  placeholder="생년월일 8자리를 입력해 주세요 (ex.20001203)"
                  v-model="data.birthDate"
                />
              </div>

              <div class="tellBox val3-inputBox">
                <h3>연락처</h3>
                <input
                  type="number"
                  placeholder="(ex.010-1234-5678)"
                  v-model="data.phone"
                />
              </div>

              <div class="addressBox val3-inputBox">
                <div class="addressBox-1">
                  <h3>주소</h3>
                  <input
                    type="text"
                    placeholder="* 우편번호(주소검색)"
                    v-model="data.userZip"
                    readonly
                  />
                  <button class="pre-600" type="button" @click="showDaum">
                    우편번호 검색
                  </button>
                </div>

                <div class="addressBox-2">
                  <div class="address-emptyBox"></div>
                  <input
                    type="text"
                    placeholder="* 기본주소(주소검색)"
                    v-model="data.userAddr1"
                    readonly
                  />
                </div>

                <div class="addressBox-3">
                  <div class="address-emptyBox"></div>
                  <input
                    type="text"
                    placeholder="상세주소(입력해 주세요)"
                    v-model="data.userAddr2"
                  />
                </div>
              </div>

              <div class="guardian-nameBox val3-inputBox">
                <h3>보호자 이름</h3>
                <input
                  type="text"
                  placeholder="보호자 이름을 입력해 주세요"
                  v-model="data.guardianName"
                />
              </div>

              <div class="guardian-tellBox val3-inputBox">
                <h3>보호자 연락처</h3>
                <input
                  type="number"
                  placeholder="보호자 연락처를 입력해 주세요"
                  v-model="data.guardianNum"
                />
              </div>
            </div>
          </div>
          <!--e:val3Box1-->

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
                <input
                  type="text"
                  placeholder="경력을 입력해 주세요"
                  v-model="data.career"
                />
              </div>

              <div class="val3-inputBox">
                <h3>훈련기관</h3>
                <v-select
                  v-model="data.team"
                  :items="teamList"
                  item-text="teamName"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>수상경력</h3>
                <input type="text" placeholder="수상경력을 입력해 주세요" />
              </div>
            </div>
          </div>
          <!--e:val3Box2-->

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
                <input
                  type="number"
                  placeholder="ex) 173"
                  v-model="data.height"
                />
                <p class="input-right-p">cm</p>
              </div>

              <div class="val3-inputBox">
                <h3>체중</h3>
                <input
                  type="number"
                  placeholder="ex) 55"
                  v-model="data.weight"
                />
                <p class="input-right-p">kg</p>
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
                <input type="text" v-model="data.school" />
              </div>
            </div>
          </div>
        </div>
        <!--e:manage-val3-wrap-->
      </v-window-item>
      <v-window-item :value="4">
        <div class="manage-val1-wrap manage-val4-wrap" style="padding: 24px;">
          <div class="manage-val1-title">
            <p class="pre-700">기본정보</p>
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
            <p class="pre-400">선수등록이 완료되었습니다.</p>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>아이디</h2>
            <p>{{ data.username }}</p>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>이름</h2>
            <p>{{ data.name }}</p>
          </div>

          <div class="manage-val1-pw1Box manage-val1-inputBox">
            <h2>성별</h2>
            <p>{{ data.gender }}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>운동종목</h2>
            <p>{{ data.sportType }}</p>
          </div>
        </div>
        <!--e:manage-val4-wrap-->
      </v-window-item>
      <v-window-item :value="2">
        <div class="manage-val1-wrap manage-val4-wrap" style="padding: 24px;">
          <div class="manage-val1-title">
            <p class="pre-700">기본정보</p>
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
            <p class="pre-400">선수등록이 완료되었습니다.</p>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>이름</h2>
            <p class="pre-400">{{ data.name }}</p>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>성별</h2>
            <p class="pre-400">{{ data.gender }}</p>
          </div>

          <div class="manage-val1-pw1Box manage-val1-inputBox">
            <h2>운동종목</h2>
            <p class="pre-400">{{ data.sportType }}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>수상경력</h2>
            <p class="pre-400">{{ data.awards }}</p>
          </div>
        </div>
        <!--e:manage-val4-wrap-->
      </v-window-item>
    </v-window>
    <v-row class="manage-btnBox" justify="end" style="padding: 24px;">
      <v-col align="end" v-if="step == 1">
        <v-btn @click="signup()">선수등록</v-btn>
      </v-col>
      <v-col align="end" v-if="step == 2">
        <v-btn @click="backToHome()" color="success2">돌아가기</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    this.profileDataFormat = JSON.parse(JSON.stringify(this.profileData))
    this.dataSet = JSON.parse(JSON.stringify(this.data))
    this.data.createUser = this.$store.state.userStore.id; //생성자 id(선수추가)
    // 공통데이터 가져오기
    await this.$axios
      .get("datasets/api/commondata/")
      .then((res) => {
        for (const data of res.data) {
          // 1 (장애등급)
          if (data.maincategory == 1) {
            this.disabilityGradeList.push(data);
          }
          // 2 (혈액형)
          else if (data.maincategory == 2) {
            this.bloodTypeList.push(data);
          }
          // 3 (결혼여부)
          else if (data.maincategory == 3) {
            this.maritalStatusList.push(data);
          }
          // 4 (병역여부)
          else if (data.maincategory == 4) {
            this.militaryServiceList.push(data);
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
          this.teamList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });
    await this.loadingCover(false);
  },
  data: () => ({
    step:1,
    data: {
      username: "", // ID
      password: "",
      passwordValid: "",
      createUser: 0,
      modifyUser: null,
      is_superuser: false,
      gender: "",
      //email: "",
      is_staff: false,
      is_active: true,
      name: "",
      profile: "",
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
      //wheelchair: false,
      //eyesightL: "",
      //eyesightR: "",
      school: "",
      //department: "",
      guardianName: "",
      //relation: "",
      guardianNum: "",
      //guardianEmail: "",
      comID: null,
      attType: 0,
      sportType: null,
      teamID: null,
      disabilityType: null,
      disabilityGrade: null,
      //bloodType: null,
      //maritalStatus: null,
      //militaryService: null,
      education: null,
    },
    dataSet: {},
    profileData:{
      id:"",
      name:"",
      profile:null,
    },
    profileDataFormat: {},
    createId: "",
    imageFlag:"",
    genderList: [ // 성별 리스트
      { type: "남성", value: 1 },
      { type: "여성", value: 2 },
    ],
    disabilityList: [], // 장애 리스트
    disabilityGradeList: [], // 장애 등급
    educationList: [], // 최종학력 리스트
    sportTypeList: [], // 운동종목 리스트
    companyList: [], // 기업목록 리스트
    teamList: [], // 복지관(훈련기관) 리스트
  }),
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    preview_image() {
      this.url = URL.createObjectURL(this.profileData.profile)
      this.imageFlag = true
    },
    async signup() {
      //선수 등록
      await this.$axios
      .post("consultings/api/player/", this.data)
      .then((res) => {
        this.createId = res.data.id
        this.step = 2
        this.$store.dispatch("callToast", {
          msg: "성공적으로 선수를 등록하였습니다.",
          result: "success",
        });
      })
      .catch(() => {
        console.log("선수등록실패");
        alert("정보를 정확히 입력해 주세요."); // 에러 메시지 출력
      });

      if(this.imageFlag == true){//이미지 수정했을때만 실행
        var formData = new FormData();
        formData.append("profile", this.profileData.profile);
        this.$axios({
          method: "PATCH",
          url: "consultings/api/image/" + this.createId + "/",
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          data: formData,
          })
          .then(() => {});
      }
      this.imageFlag = false
      this.createId = ""
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
    backToHome(){
      this.step = 1
      this.url = ""
      this.profileData = JSON.parse(JSON.stringify(this.profileDataFormat))
      this.data = JSON.parse(JSON.stringify(this.dataSet))
    },
  },
  watch: {},
};
</script>

<style>
.background {
  background-color: rgba(240, 240, 240);
  border-radius: 10px;
}
.manage-val1-wrap {
}
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
  font-family: "Pretendard-SemiBold";
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
  font-family: "Pretendard-Regular";
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
  background: #eff9f8;
  border-radius: 3px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 107px;
  margin-left: 6px;
  transition: all 0.3s;
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
.manage-btnBox .col {
}
.manage-btnBox button {
  width: 126px !important;
  height: 48px !important;
  background-color: #eff9f8 !important;
  border-radius: 10px;
  box-shadow: none;
  padding: 0 !important;
  transition: all 0.5s;
}
.manage-btnBox button:hover {
  background: #49ada9 !important;
}
.manage-btnBox button:hover span {
  color: #fff !important;
}
.manage-btnBox button span {
  font-family: "Pretendard-Regular";
  font-size: 18px;
  color: #49ada9;
  transition: all 0.5s;
}
.manage-btnBox button span svg {
  transition: all 0.5s;
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
  background: #f5f5f5;
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
  font-family: "Pretendard-Regular";
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
.times-selectBox fieldset {
  display: none;
}
.times-selectBox label {
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
.manage-value2-top-inputBox .value-btnBox {
}
.manage-value2-top-inputBox .value-btnBox button {
  margin-right: 6px;
  width: 34px !important;
  min-width: auto !important;
  height: 32px !important;
  border-radius: 6px !important;
  background-color: #b4b4b4 !important;
  border: 0 !important;
}
.manage-value2-top-inputBox .value-btnBox span {
  color: #fff;
  font-family: "Pretendard-Regular";
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
  font-family: "Pretendard-Regular";
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
  background-color: #e4f2f9;
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
.v-text-field--outlined .v-label--active,
.v-text-field .v-label--active {
  transform: unset;
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
  font-family: "Pretendard-Regular";
  font-size: 15px;
}
.theme--light.v-input--switch .v-input--switch__track {
  /* background-color: #008bd6; */
}
.v-input--switch:not(.v-input--switch--flat):not(.v-input--switch--inset)
  .v-input--switch__thumb {
  color: #fff !important;
}
.v-application--is-ltr .v-text-field .v-label {
  font-family: "Pretendard-Regular";
}
.manage-val3-wrap {}
.manage-val3-wrap .manage-val3-header {
  width: 100%;
  height: 72px;
  border-bottom: 0.5px solid #b4b4b4;
  display: flex;
  align-items: center;
  padding: 0 24px;
}
.manage-val3-wrap h1 {
  font-size: 20px;
  color: #2e2e2e;
  font-weight: 600;
}
.manage-val3-wrap .left-emptyBox {
  width: 200px;
  height: 200px;
  margin-right: 32px;
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
  font-family: "Pretendard-Regular";
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
  font-family: "Pretendard-Regular";
  font-weight: 500;
}
.defaultBox .val3-inputBox input::placeholder {
  color: #989898;
}
.defaultBox .val3-inputBox input:focus,
.addressBox-1 button:focus,
input:focus {
  outline-color: #49ada9 !important;
}
.genderBox {
  display: flex;
  align-items: center;
}
.genderBox {
  font-size: 16px;
  color: #fff;
  font-family: "Pretendard-Regular";
  cursor: pointer;
}
.genderBox > div {
  transition: all 0.5s;
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
  transition: all 0.5s;
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
  border-bottom: 0.5px solid #b4b4b4;
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
  font-family: "Pretendard-Regular";
  font-size: 16px;
}
.val3Box1
  .v-text-field.v-input--is-focused
  > .v-input__control
  > .v-input__slot:after {
  display: none;
}
.val3-inputBox .input-right-p {
  position: relative;
  left: 10px;
  top: 7px;
  font-family: "Pretendard-Regular";
  font-size: 16px;
}
.times-selectBox .v-select__selection--comma {
  left: 60px;
}
.manage-val4-wrap p {
  margin: 0;
}
.detail-profile-img-input {
  padding: 5px 10px !important;
}
.detail-profile-img-input div,
.detail-profile-img-input label,
.detail-profile-img-input {
  cursor: pointer !important;
}
.detail-profile-img-input label {
  font-weight: 600;
  font-size: 14.5px !important;
  left: 35px !important;
}
.detail-profile-img-input button {
  margin-right: 0 !important;
  font-size: 20px !important;
}
.detail-profile-img-input .v-input__prepend-outer button {
  position: relative;
  left: 30px;
}
.detail-profile-img-input .v-input__icon--clear,
.detail-profile-img-input .v-file-input__text {
  /* opacity: 0;
  cursor: none;
  position: absolute;
  z-index: -9999; */
}
.detail-profile-img-input .v-file-input__text {
  /* opacity: 0; */
  /* cursor: none; */
  /* position: absolute; */
  background: rgba(255,255,255,.6);
  position: relative;
  z-index: 9990;
  display: none;
  top: 2px;
  left: -10px;
  font-family: 'Pretendard-Regular';
  font-weight: 600;
  overflow: hidden;
  width: 128px;
  height: 32px;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.detail-profile-img-input .v-label--active + .v-file-input__text {
  display: block;
}
</style>