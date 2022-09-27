<template>
  <div>
    
        <!-- 작성하기 화면 시작 -->
          <v-card v-show="dialogWriteState" class="home-card pa-0" style="max-height:none;position: fixed;z-index: 11;width: 76%;height:80%; border-radius: 24px !important; overflow:hidden; " rounded="lg">
          
          <v-row class="justify-left ma-0 pa-5"  style=" box-shadow: rgb(0 0 0 / 8%) 0px 0px 0px 1px inset;width: 100%;">
            <v-col class="pa-0">
              <v-btn style=" border: 1px solid; background-color: #fff;" class="btn" @click="dialogCover(true)">작성</v-btn>
            </v-col>
            <!-- X 닫기 버튼이 들어가는 영역  -->
            <v-col class="pa-0" style="text-align: right;">
              <v-btn style=" border: 1px solid; background-color: #fff;" class="btn" @click="dialogCover(false)">닫기</v-btn>
            </v-col>
          </v-row>

          <!-- <v-row class="ma-0 pa-5"> -->
          <div class="d-flex" style="width: 100%;">
            <div class="d-flex" style=" overflow: hidden; width: 100%; ">
              <!-- 좌측 영역 시작 -->
              <v-col cols="8" class="pa-0" style="max-width: 100%; flex:none;  ">
                <!-- 상단 -->
                <div class="d-flex" style="flex-direction: column; height: calc(894px); max-height: calc(100vh - 336px);">
                  <div style="padding: 40px 40px 0px 40px;">
                    <v-card-title class="pa-0">비품신청</v-card-title>
                    <v-card-subtitle class="pa-0 mt-0" style="word-break: keep-all;">일하는 데 필요한 물품을 신청해주세요!</v-card-subtitle>
                  </div>
                  <!-- 중단 -->
                  <div style="padding: 0px 40px 40px;">
                    <v-text-field
                      id="contents"
                      placeholder="훈련 내용"
                      auto-grow
                      hide-details="auto"
                    ></v-text-field>
                    <v-text-field
                      id="contents"
                      placeholder="훈련 내용"
                      hide-details="auto"
                      auto-grow
                    ></v-text-field>
                    <v-text-field
                      id="contents"
                      placeholder="훈련 내용"
                      hide-details="auto"
                      auto-grow
                    ></v-text-field>
                    <v-text-field
                      id="contents"
                      placeholder="훈련 내용"
                      hide-details="auto"
                      auto-grow
                    ></v-text-field>
                  </div>
                </div>
                <!-- 하단 -->
                <div class="d-flex" style="width: 100%; height: 76px;box-shadow: rgb(0 0 0 / 8%) 0px 1px 0px 0px inset;align-items: center; justify-content: right;padding-left: 40px;padding-right: 40px;">
                  <v-btn style=" border: 1px solid; background-color: #fff; margin-right: 10px;" class="btn" @click="dialogCover(true)">닫기</v-btn>
                  <v-btn style=" border: 1px solid; background-color: #fff;" class="btn" @click="dialogCover(true)">보내기</v-btn>
                </div>
              </v-col>
              <!-- 좌측 영역 종료 -->
            </div>
            <div class="d-flex" style="width: 320px; flex: 0 0 320px; overflow:auto; background-color: rgba(99, 114, 131, 0.03);box-shadow: rgb(0 0 0 / 8%) 1px 0px 0px 0px inset;">
              <div>
                  <div style="padding: 40px 40px 0px 40px;">
                    <v-card-title class="pa-0">비품신청</v-card-title>
                    <v-card-subtitle class="pa-0 mt-0" style="word-break: keep-all;">일하는 데 필요한 물품을 신청해주세요!</v-card-subtitle>
                  </div>
              </div>
            </div>
          </div>
          <!-- </v-row> -->
          </v-card>
          <!-- 작성하기 화면 종료 -->
        <!-- 작성요청 화면 시작 -->
          <v-card v-show="dialogSendState" class="home-card pa-0" style="max-height:none;position: fixed;z-index: 11;width: 76%;height:80%; border-radius: 24px !important; overflow:hidden; " rounded="lg">
          
                    <v-row class="justify-left ma-0 pa-5"  style=" box-shadow: rgb(0 0 0 / 8%) 0px 0px 0px 1px inset;width: 100%;">
                      <v-col class="pa-0">
                        <v-btn style=" border: 1px solid; background-color: #fff;" class="btn" @click="dialogCover(true)">작성</v-btn>
                      </v-col>
                      <!-- X 닫기 버튼이 들어가는 영역  -->
                      <v-col class="pa-0" style="text-align: right;">
                        <v-btn style=" border: 1px solid; background-color: #fff;" class="btn" @click="dialogCover(false)">닫기</v-btn>
                      </v-col>
                    </v-row>

                    <!-- <v-row class="ma-0 pa-5"> -->
                    <div class="d-flex" style="width: 100%;">
                      <div class="d-flex" style=" overflow: hidden; width: 100%; ">
                        <!-- 좌측 영역 시작 -->
                        <v-col cols="8" class="pa-0" style="max-width: 100%; flex:none;  ">
                          <!-- 상단 -->
                          <div class="d-flex" style="flex-direction: column; height: calc(894px); max-height: calc(100vh - 336px);">
                            <div style="padding: 40px 40px 0px 40px;">
                              <v-card-title class="pa-0">비품신청</v-card-title>
                              <v-card-subtitle class="pa-0 mt-0" style="word-break: keep-all;">일하는 데 필요한 물품을 신청해주세요!</v-card-subtitle>
                            </div>
                            <!-- 중단 -->
                            <div style="padding: 0px 40px 40px;">
                              <v-text-field
                                id="contents"
                                placeholder="훈련 내용"
                                auto-grow
                                hide-details="auto"
                              ></v-text-field>
                              <v-text-field
                                id="contents"
                                placeholder="훈련 내용"
                                hide-details="auto"
                                auto-grow
                              ></v-text-field>
                              <v-text-field
                                id="contents"
                                placeholder="훈련 내용"
                                hide-details="auto"
                                auto-grow
                              ></v-text-field>
                              <v-text-field
                                id="contents"
                                placeholder="훈련 내용"
                                hide-details="auto"
                                auto-grow
                              ></v-text-field>
                            </div>
                          </div>
                          <!-- 하단 -->
                          <div class="d-flex" style="width: 100%; height: 76px;box-shadow: rgb(0 0 0 / 8%) 0px 1px 0px 0px inset;align-items: center; justify-content: right;padding-left: 40px;padding-right: 40px;">
                            <v-btn style=" border: 1px solid; background-color: #fff; margin-right: 10px;" class="btn" @click="dialogCover(true)">닫기</v-btn>
                            <v-btn style=" border: 1px solid; background-color: #fff;" class="btn" @click="dialogCover(true)">보내기</v-btn>
                          </div>
                        </v-col>
                        <!-- 좌측 영역 종료 -->
                      </div>
                      <div class="d-flex" style="width: 320px; flex: 0 0 320px; overflow:auto; background-color: rgba(99, 114, 131, 0.03);box-shadow: rgb(0 0 0 / 8%) 1px 0px 0px 0px inset;">
                        <div>
                            <div style="padding: 40px 40px 0px 40px;">
                              <v-card-title class="pa-0">비품신청</v-card-title>
                              <v-card-subtitle class="pa-0 mt-0" style="word-break: keep-all;">일하는 데 필요한 물품을 신청해주세요!</v-card-subtitle>
                            </div>
                        </div>
                      </div>
                    </div>
                    <!-- </v-row> -->
          </v-card>
          <!-- 작성요청 화면 종료 -->
    <v-container style="flex-wrap: wrap; width: 1170px;max-width: 1170px; ">
        <div v-for="(item, idx) in worklist" :key="idx" class="d-flex justify-center align-center pa-0 mx-8 mb-8" style="float: left;">
          <v-card class="home-card" style="width: 220px;height:220px; border-radius: 24px !important;    display: block; overflow:hidden;" rounded="lg">
          
                    <div class=" mb-3">
                      <v-row>
                        <v-col class="d-flex justify-left ">
                          <v-card-title style="margin-left: 24px;font-weight:1000; padding:8px;margin-top: 24px;">{{item.name}}</v-card-title>
                        </v-col>
                      </v-row>
                    </div>
                    <v-row class="justify-left mt-4" style="margin-top: 70px !important;margin-left: 30px !important; " >
                      <div>
                        <v-btn style="margin-left:0px;border: 1px solid; background-color: #fff;" class="btn px-2" @click="dialogCover(true)">작성하기</v-btn>
                        <v-btn style="margin-left:0px;border: 1px solid; background-color: #fff;" class="btn px-2 ml-2" @click="dialogCover(true)">작성요청</v-btn>
                      </div>
                    </v-row>
          </v-card>
        </div>
    </v-container>
  </div>
</template>

<script>
// import TodayAttendance from "/src/views/team/home/TodayAttendance";
// import UserCard from "/src/components/cards/UserCard";
import eventBus from "/src/main.js";

export default {
  data: () => ({
    noData: false,
    users: [],
    search: "",
    offWorkPlayer: [],
    goToWorkPlayer: [],
    noWorkPlayer: [],
    dialogWriteState: false,
    dialogSendState: false,
    worklist: [{name:"연차"},{name:"주간업무보고"},{name:"월간업무보고"},{name:"대회참가"},{name:"대회결과보고"},{name:"공단서류제출"}]
  }),
  components: {
    // TodayAttendance,
    // UserCard
  },
  async created() {
    await this.loadingCover(true);
    await this.$axios({
      method: "GET",
      url:
        "/attendances/api/att_user/?is_active=true&coach=" + this.$store.state.userStore.id,
    })
      .then((res) => {
        for (var i = 0; i < res.data.length; i++) {
          this.$set(this.users, i, res.data[i]); //코치로 받아온 유저데이터 users에 복사
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      })
      .finally(() => {
        if (this.users.length === 0) {
          this.noData = true;
        } else {
          this.noData = false;

          this.setAttendanceState();
        }
      });

      this.$axios({
      method: "POST",
      url:
        "attendances/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.id+"_"+ this.today +"/",
    })
      .then((res) => {
        //근무중, 미출근, 퇴근 선수 분류
        for(var i=0; i < res.data.length; i++){
          if(res.data[i].state=="1"){
            this.offWorkPlayer.push(res.data[i].user)
          }
          else if(res.data[i].state=="0"){
            this.goToWorkPlayer.push(res.data[i].user)
          }
          else
            this.noWorkPlayer.push(res.data[i].user)
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });

    //SearchBar로부터 검색어 데이터를 받아옴
    eventBus.$on(
      "searchEvent",
      function (value) {
        this.search = value;
      }.bind(this)
    );
    await this.loadingCover(false);
  },
  computed: {
    //당일 날짜 반환하는 함수
    today: function () {
      var date = new Date();
      var year = date.getFullYear();
      var month = ("0" + (1 + date.getMonth())).slice(-2);
      var day = ("0" + date.getDate()).slice(-2);

      return year + "-" + month + "-" + day;
    },
  },
  methods: {
    //date-picker 일 출력 형식 변환 (ex) 3일 => 3
    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },

    //유저마다 attendanceState 속성 추가
    setAttendanceState: function () {
      for (let i = 0; i < this.users.length; i++) {
        //출퇴근 상태값 계산 후 추가
        let user = this.users[i];
        this.$set(user, "attendanceState", {});
        for (let j = 0; j < user["attendances"].length; j++) {
          let key = user["attendances"][j]["startWorkTime"].split(" ")[0];
          let val = this.getState(user["attendances"][j]);
          user["attendanceState"][key] = val;
        }
      }
    },

    //출퇴근 값에 따라 유저의 출퇴근 상태값 얻기
    getState: function (attendance) {
      let start = attendance["startWorkTime"];
      let end = attendance["finishWorkTime"];

      //해당 date의 출근기록이 있고 퇴근기록 또한 존재하는 경우
      if (start !== undefined && end.length !== 0) {
        return "green";
      }
      //해당 date의 출근기록이 있고 퇴근기록이 없는 경우
      else if (start !== undefined && end.length == 0) {
        return "yellow";
      }
    },
    searchByName: function (name) {
      if (this.search === null) {
        return true;
      } else if (name.includes(this.search)) {
        return true;
      } else {
        return false;
      }
    },
    isRender(user) {
      //선수 이름검색이 된경우
      if (this.searchByName(user.name)) {
        return true;
      }
      return false;
    },
    //MainAttendance로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    
    dialogCover(val){
      this.$emit('dialogCoverSetChild',val);
      this.dialogWriteState = val;
    },
  },
};
</script>

<style>
.border {
  border: solid 2px black;
}

.border-bottom {
  border-bottom: solid 2px black;
}

@media screen and (max-width:350px) {
  .v-slide-group__next{
    display:none;
  }

  .v-slide-group__next--disabled{
    display:none;
  }

  .v-slide-group__prev{
    display:none;
  }
  
  .v-slide-group__prev--disabled{
    display:none;
  }
}

.home-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 520px;
  width: 360px;
}

.green-circle{
  width : 17px;
  height : 17px;
  border-radius: 50%;
  background-color: green;
  margin: auto;
}

.yellow-circle{
  width : 17px;
  height : 17px;
  border-radius: 50%;
  background-color: yellow;
  margin: auto;
}

</style>