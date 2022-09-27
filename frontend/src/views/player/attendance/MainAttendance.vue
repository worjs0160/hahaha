<template>
  <v-container class="d-flex">
    <v-col class="d-flex justify-center">
      <v-card class="home-card today-attendance-card pa-2" rounded="lg">
        <v-card-title class="pt-0 mb-6">
          {{ $store.state.userStore.name }}
        </v-card-title>
        <div class="d-flex flex-column align-center">
          <v-card-subtitle>
            {{ transformDate(todayAttendance.date) }}
          </v-card-subtitle>

          <div class="d-flex flex-column">
            <div class="d-flex mb-8">
              <!--훈련종목 영역-->
              <v-card
                cols="6"
                class="attendance-state"
                color="#C4FCD7"
                rounded="circle"
                @click="goToWork"
              >
                <v-card-title>출근</v-card-title>
                <v-card-text class="text-center"> {{ startTime }} </v-card-text>
              </v-card>
              <!--소속 영역-->
              <v-card
                cols="6"
                class="attendance-state white--text"
                color="primary"
                rounded="circle"
                @click="offWork"
              >
                <v-card-title>퇴근</v-card-title>
                <v-card-text class="text-center white--text"> {{ endTime }} </v-card-text>
              </v-card>
            </div>
            <v-card
              class="align-self-center"
              color="#C4FCD7"
              rounded="lg"
              width="fit-content"
            >
              <v-card-title class="py-2">
                {{ state }}
              </v-card-title>
            </v-card>
          </div>
        </div>
      </v-card>
    </v-col>
    <!--N째주 근무 현황-->
    <v-col class="d-flex justify-center">
      <v-card class="week-attendance-card pa-2" rounded="lg">
        <!--주 선택 -->
        <week-num-picker
          v-on:change="inItWeekDates"
          ref="weekPicker"
          class="mb-2"
        ></week-num-picker>
        <!--일주일 치 근무기록 카드 -->
        <v-row>
          <v-col cols="12">
            <attendance-card
              v-for="a in weekAttendances"
              :worktime="a"
              :key="a.date"
            >
            </attendance-card>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import AttendanceCard from "/src/components/cards/AttendanceCard";
import WeekNumPicker from "/src/components/pickers/WeekNumPicker";
export default {
  components: {
    WeekNumPicker,
    AttendanceCard,
  },
  data: () => ({
    weekAttendances: [], //일주일 치 근태기록 리스트
    todayAttendance: {}, //오늘날짜의 근태기록 객체
    weekFirstDate: "", //일주일 중 첫번째인 월요일의 날짜
    weekLastDate: "", //일주일 중 마지막인 일요일의 날짜
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString(), //현재 시간
    todayId:"", // 오늘 만들어진 근태기록 아이디
    todayStartTime:"", // 오늘 만들어진 출근 시간
    startTime:"", // 화면에 표시할 출근 시간
    todayEndTime:"", // 오늘 만들어진 퇴근 시간
    endTime:"", // 화면에 표시할 퇴근 시간
    state:"출근전", // 화면에 표시할 근태 상태(출근전, 출근중, 정상 퇴근)
  }),

  async created() {
    await this.loadingCover(true);
    await this.getTodayStartTime();
    await this.getTodayAttendance();
    await this.loadingCover(false);
  },

  computed: {},
  watch:{
    "todayStartTime": function(){
      let time = this.todayStartTime
      const date = new Date(time);
      let hour = date.getHours();
      var minute;
      //10분 미만일땐 0붙혀서 보이게(ex. 7분 -> 07분)
      if(date.getMinutes()<10) minute = "0" + date.getMinutes();
      else minute = date.getMinutes();
      this.state = "출근중"
      this.startTime = hour + " : " + minute;
    },
    "todayEndTime": function(){
      let time = this.todayEndTime
      const date = new Date(time);
      let hour = date.getHours();
      var minute;
      //10분 미만일땐 0붙혀서 보이게(ex. 7분 -> 07분)
      if(date.getMinutes()<10) minute = "0" + date.getMinutes();
      else minute = date.getMinutes();
      this.state = "정상 퇴근"
      this.endTime = hour + " : " + minute;
    },
  },
  methods: {
    inItWeekDates: function () {
      this.getWeekFirstDate();
      this.getWeekLastDate();
      this.getWeekAttendances();
    },
    //월요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekFirstDate: function () {
      this.weekFirstDate = this.$refs.weekPicker.getWeekFirstDate();
    },
    //일요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekLastDate: function () {
      this.weekLastDate = this.$refs.weekPicker.getWeekLastDate();
    },
    //일주일치 근무기록을 가져오는 함수
    getWeekAttendances: function () {
      this.$axios({
        method: "POST",
        url:
          "attendances/work_time_week/" +
          this.$store.state.userStore.id +
          "_" +
          this.weekFirstDate +
          "/",
      })
        .then((res) => {
          this.weekAttendances = [];

          for (var i = 0; i < res.data.length; i++) {
            const attendance = res.data[i];
            //출근기록이 없는 경우 데이터에 포함시키지 않음
            if (attendance.attendanceState === -1) {
              continue;
            }
            this.weekAttendances.push(attendance);
          }
        })
        .catch((err) => {
          console.log("Failed to request =>", err);
        });
    },
    //오늘날짜의 근태기록 가져오기
    async getTodayAttendance() {
      await this.loadingCover(true);
      await this.$axios({
        method: "POST",
        url:
          "attendances/get_work_time/" +
          this.$store.state.userStore.id +
          "_" +
          this.$store.state.userStore.serverDate +
          "/",
      })
      .then((res) => {
        this.todayAttendance = {};
        this.todayAttendance = res.data;
        if(res.data.attendanceState=="-1"){
          this.state = "출근전"
        }
        else if(res.data.attendanceState=="0"){
          this.startTime = res.data.startWorkTime.substr(11,5)
          this.state = "출근중"
        }
        else if(res.data.attendanceState=="1"){
          this.endTime = res.data.finishWorkTime.substr(11,5)
          this.state = "정상 퇴근"
        }
      })
      .catch((err) => {
        console.log("Failed to request =>", err);
      });
      await this.loadingCover(false);
    },
    //datepicker에 출력되는 일 형식 설정
    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },
    //화면에 보여줄 날짜 형식 m월 d일 x요일로 변환
    transformDate: function (dateFormat) {
      const days = ["일", "월", "화", "수", "목", "금", "토"];
      //근태 카드에 입력된 날짜
      const inputedDate = new Date(dateFormat);

      const year = inputedDate.getFullYear();
      const month = inputedDate.getMonth() + 1; //근무날짜의 달
      const date = inputedDate.getDate(); //근무날짜의 일
      const day = days[inputedDate.getDay()]; //근무날짜의 요일

      return year + "년 " + month + "월 " + date + "일 " + day + "요일";
    },
        // -------- 출근 기록 함수 --------
    async goToWork() {
      if(!this.$store.state.userStore.company && !this.$store.state.userStore.team){
        this.$store.dispatch("callToast", {
            msg: "소속된 기업이나 복지관이 없어 출근기록을 할 수 없습니다.",
            result: "fail",
          });
        return false
      }
      if(this.todayId){
        this.$store.dispatch("callToast", {
            msg: "금일은 이미 출근하셨습니다.",
            result: "fail",
          });
        return false
      }
      this.todayStartTime = this.today.substr(0, 10) +" "+ this.today.substr(11, 8)
      await this.$axios({
        method: "POST",
        url: "attendances/api/att_list/",
        data: {
          user: this.$store.state.userStore.id,
          startWorkTime: this.todayStartTime,
          finishWorkTime: "",
          workPlace: this.$store.state.userStore.team.value,
          memo: "",
          id: null,
        }
      })
      .catch((err) => {
        console.log(err.response);
      });
      await this.$store.dispatch("callToast", {
        msg: "금일 출근처리 되었습니다.",
        result: "success",
      });
      await this.getTodayStartTime(); // 저장된 오늘의 근태리스트로부터 ID값과 시작시간 가져오기(퇴근시간을 찍기 위해)
      this.inItWeekDates(); // 출근 시간이 기록될 때, 주차별 근태리스트의 시간도 갱신
    },
    // -------- 퇴근 기록 함수 --------
    offWork: function () {
      if(!this.todayStartTime){
        this.$store.dispatch("callToast", {
            msg: "금일은 아직 출근하지 않으셨습니다.",
            result: "fail",
          });
        return false
      }
      if(this.todayId && this.todayEndTime){
        this.$store.dispatch("callToast", {
            msg: "금일은 이미 퇴근하셨습니다.",
            result: "fail",
          });
        return false
      }
      this.todayEndTime = this.today.substr(0, 10) +" "+ this.today.substr(11, 8)
      this.$axios
        .post("attendances/api/att_list/todayOffWork/", {
          user: this.todayId,
          data: {
          user: this.$store.state.userStore.id,
          startWorkTime: this.todayStartTime,
          finishWorkTime: this.todayEndTime,
          workPlace: this.$store.state.userStore.team.value,
          memo: "",
          id: null,
        },
      })
      .catch((err) => {
        console.log(err.response);
      });
      this.$store.dispatch("callToast", {
            msg: "금일 퇴근처리 되었습니다.",
            result: "success",
      });
      this.inItWeekDates(); // 퇴근 시간이 기록될 때, 주차별 근태리스트의 시간도 갱신
    },
    async loadingCover(val){
      await this.$emit('coverSetChild',val);
    },
    async getTodayStartTime(){
      await this.$axios({
        method: "GET",
        url: "attendances/api/att_list/?user="+this.$store.state.userStore.id+"&startWorkTime="+this.today.substr(0, 10),
      })
      .then((res) => {
        if(res.data){
          this.todayStartTime = res.data[0].startWorkTime
          this.todayId = res.data[0].id
        }
      })
      .catch((err) => {
        return err;
      });
    },
    setting(){
      
    }
  },
};
</script>

<style scoped>
.home-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 480px;
  width: 360px;
}

.today-attendance-card {
  justify-content: start;
}

.month-attendance-card {
  justify-content: start;
}

.week-attendance-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 480px;
  width: 360px;
}

.attendance-state {
  margin: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 150px;
  width: 150px;
}
</style>