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
            <button  @click="consultingPlayerDialogStateChange(false), dialogCoverSet(false), scrollTop()">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
              </svg>
            </button>
          </div>

          <div class="val3Box1 val3Box2" style="padding: 32px 24px;">

            <div class="imgBox" style="position: relative;">
              <div class="imgBox-hidden">
                <v-img :src="consultingPlayerDialogProfileData.profile" alt="" style="
                position: relative;
                z-index: 3;
                width: 100%;
                height: 100%;
                object-fit: cover;
                "></v-img>
              </div>
                

            </div>

            <div class="defaultBox">


              <h2 class="pre-600">기본정보</h2>



              <div class="nameBox val3-inputBox">
                <h3>이름</h3>
                <input type="text" v-model="consultingPlayerDialogData.name" readonly>
              </div>

              <div class="genderBox val3-inputBox">
                <h3>성별</h3>
                <div class="genderBox">
                  <!-- gender-active를 주면 색상 변경 -->
                  <v-btn-toggle v-model="consultingPlayerDialogData.gender">
                    <v-btn class="gender-male" value="남성" style="pointer-events: none;">
                      남성
                    </v-btn>
            
                    <v-btn class="gender-woman" value="여성" style="pointer-events: none;">
                      여성
                    </v-btn>
                  </v-btn-toggle>
                </div>
              </div>

              <div class="birthBox val3-inputBox">
                <h3>생년월일</h3>
                <input type="number" v-model="consultingPlayerDialogData.birthDate" readonly>
              </div>

              <div class="tellBox val3-inputBox">
                <h3>연락처</h3>
                <input type="number" v-model="consultingPlayerDialogData.phone" readonly>
              </div>

              <div class="addressBox val3-inputBox">

                <div class="addressBox-1">
                  <h3>주소</h3>
                  <input type="text" v-model="consultingPlayerDialogData.userZip" readonly>
                </div>

                <div class="addressBox-2">
                  <div class="address-emptyBox"></div>
                  <input type="text" v-model="consultingPlayerDialogData.userAddr1" readonly>
                </div>
              
                <div class="addressBox-3">
                  <div class="address-emptyBox"></div>
                  <input type="text" v-model="consultingPlayerDialogData.userAddr2" readonly>
                </div>
                
              </div>

              <div class="guardian-nameBox val3-inputBox">
                <h3>보호자 이름</h3>
                <input type="text" v-model="consultingPlayerDialogData.guardianName" readonly>
              </div>

              <div class="guardian-tellBox val3-inputBox">
                <h3>보호자 연락처</h3>
                <input type="number" v-model="consultingPlayerDialogData.guardianNum" readonly>
              </div>

            </div>

          </div><!--e:val3Box1-->

          <div class="val3Box1 val3Box2" style="padding: 32px 24px;">

            <div class="left-emptyBox"></div>

            <div class="careerBox defaultBox">

              <h2 class="pre-600">경력사항</h2>

              <div class="val3-inputBox">
                <h3>운동종목</h3>
                <input v-model="consultingPlayerDialogData.sportType.value" readonly>
              </div>

              <div class="val3-inputBox">
                <h3>경력</h3>
                <input type="text" v-model="consultingPlayerDialogData.career" readonly>
              </div>

              <div class="val3-inputBox">
                <h3>훈련기관</h3>
                <input v-model="consultingPlayerDialogData.team.teamName" readonly>
              </div>

              <div class="val3-inputBox">
                <h3>수상경력</h3>
                <textarea name="" id="" cols="50" rows="5" v-model="consultingPlayerDialogData.awards" readonly style="
                  border-radius: 3px;
                  border: 1px solid #e1e1e1;
                  padding: 10px;
                  width: 100%;
                  ">
                </textarea>
              </div>

            </div>

          </div><!--e:val3Box2-->

          <div class="val3Box1" style="padding: 24px 24px 32px;">
            
            <div class="left-emptyBox"></div>

            <div class="personalBox defaultBox">

              <h2 class="pre-600">개인사항</h2>

              <div class="val3-inputBox">
                <h3>장애유형</h3>
                <input v-model="consultingPlayerDialogData.disabilityType.value" readonly>
              </div>

              <div class="val3-inputBox">
                <h3>장애등급</h3>
                <input v-model="consultingPlayerDialogData.disabilityGrade.value" readonly>
              </div>

              <div class="val3-inputBox">
                <h3>신장</h3>
                <input type="number" v-model="consultingPlayerDialogData.height" readonly><p class="input-right-p">cm</p>
              </div>

              <div class="val3-inputBox">
                <h3>체중</h3>
                <input type="number" v-model="consultingPlayerDialogData.weight" readonly><p class="input-right-p">kg</p>
              </div>

              <div class="val3-inputBox">
                <h3>최종학력</h3>
                <input v-model="consultingPlayerDialogData.education.value" readonly>
              </div>

              <div class="val3-inputBox">
                <h3>학교명</h3>
                <input type="text" v-model="consultingPlayerDialogData.school" readonly>
              </div>


            </div>

          </div>

          <div class="val3Box1 val3Box3" style="padding: 32px 24px 0">

            <div class="left-emptyBox"></div>

            <div class="defaultBox">

              <h2 class="pre-600">선정기업</h2>

                <div class="nameBox val3-inputBox">
                  <h3>기업명</h3>
                  <v-select
                    v-model="consultingPlayerDialogData.comID"
                    :items="companyList"
                    item-text="comName"
                    item-value="id"
                  ></v-select>
                </div>

                <div class="nameBox val3-inputBox">
                  <h3>선정상태</h3>
                  <input type="text" v-model="selectState" readonly>
                </div>

            </div>

          </div>

          <div class="update-btnBox">
            <v-btn class="update-btn1 pre-400" @click="consultingPlayerDialogStateChange(false), dialogCoverSet(false), scrollTop()">닫기</v-btn>
            <v-btn class="update-btn2 pre-400" @click="updateCompany(consultingPlayerDialogData), consultingPlayerDialogStateChange(false), dialogCoverSet(false), scrollTop()">저장하기</v-btn>
          </div>

        </div><!--e:manage-val3-wrap-->
  </div>

</template>


<script>
export default {
  async created() {
    await this.loadingCover(true);
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
    await this.loadingCover(false);
  },
  data: () => ({
    companyList: [], // 기업목록 리스트
    selectState: "미지정",
  }),
  methods: {
    loadingCover(val) {
      this.$emit("coverSetChild", val);
    },
    scrollTop(){
      document.getElementById('consultingProfile').scrollTo(0,0)
    },
    dialogCoverSet(val){
      this.$emit("dialogCoverSet",val);
    },
    consultingPlayerDialogStateChange(val){
      this.$emit("consultingPlayerDialogStateChange", val);
    },
    updateProfile(){
      this.$emit("updateProfile");
    },
    updateCompany(profileData) {      
      this.$axios({
        method: "PATCH",
        url: "consultings/api/player/"+profileData.id+"/",
        data: {'comID':profileData.comID},
      })
      .then(() => {
        this.updateProfile()
        this.$store.dispatch("callToast", {
          msg: profileData.name+"님의 선정기업을 수정하였습니다.",
          result: "success",
        });
      });
    },
    async selectStateUpdate(val){
      var compareData = []
      if(val.comID.id){
        await this.$axios
          .get("users/api/employee/?comID="+val.comID.id)
          .then((res) => {
            compareData = res.data
          })
          .catch((err) => {
            console.log(err.response);
          });
      }
      if(!val.comID.id){
        this.selectState = "미지정"
      }
      else if(val.comID.id && compareData.findIndex(data=>data.name===val.name) == -1){
        this.selectState = "계정 없음"
      }
      else if(val.comID.id && compareData.findIndex(data=>data.name===val.name) != -1){
        this.selectState = "선정 완료"
      }
    },
  },
  props:['consultingPlayerDialogData', 'consultingPlayerDialogProfileData'],
  watch: {},
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
  .v-application--is-ltr .v-input__prepend-outer {
    margin: 0;
  }
</style>