<template>
    <v-container style="height:100%;">
      <v-row class="d-flex justify-center" style="height:100%;">
        <v-col class="d-flex justify-center align-center pa-0" cols="4">
          <v-card class="home-card" rounded="lg">
            <today-attendance
              :goToWorkPlayer="goToWorkPlayer"
              :noWorkPlayer="noWorkPlayer"
              :offWorkPlayer="offWorkPlayer"
            ></today-attendance>
          </v-card>
        </v-col>
        <v-col class="pa-0" cols="8">
        <!-- 선수 카드 목록 영역 -->
          <v-slide-group show-arrows style="width:95%; height: 100%;" center-active>
            <div
              v-if="noData"
              class="text-center align-self-center"
              style="width: 100%"
            >
              <h1>등록된 선수가 없습니다.</h1>
            </div>
            <v-slide-item class="my-auto" v-for="user in users" :key="user.id">
              <!-- 유저 카드 -->

              <user-card v-bind:user="user" v-if="isRender(user)">
                <div class="d-flex flex-column">
                  <v-date-picker
                    v-model="today"
                    color="primary"
                    :day-format="setDayFormat"
                    :events="user.attendanceState"
                    locale="ko-kr"
                    width="auto"
                    no-title
                    readonly
                    style="width: 100%"
                  >
                  </v-date-picker>
                </div>
                <v-container>
                  <v-row>
                    <v-col class="d-flex justify-center align-center" cols="6">
                      <div class="green-circle ma-2"></div><div style="font-weight:1000;">: 정상 퇴근</div>
                    </v-col>
                    <v-col class="d-flex justify-center align-center" cols="6">
                      <div class="yellow-circle ma-2"></div><div style="font-weight:1000;">: 출근중</div>
                    </v-col>
                  </v-row>
                </v-container>
              </user-card>
            </v-slide-item>
          </v-slide-group>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import TodayAttendance from "/src/views/team/home/TodayAttendance";
import UserCard from "/src/components/cards/UserCard";
import eventBus from "/src/main.js";

export default {
  data: () => ({
    noData: false,
    users: [],
    search: "",
    offWorkPlayer: [],
    goToWorkPlayer: [],
    noWorkPlayer: [],
  }),
  components: {
    TodayAttendance,
    UserCard
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