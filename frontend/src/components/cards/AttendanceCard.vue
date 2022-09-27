<template>
  <v-card class="px-4 py-0 mx-0 mb-2" rounded="lg" width="320" style="pointer-events: none;">
    <!--날짜 및 요일 / 근무 시간 영역 -->
    <div class="date-and-time">
      <v-card-title class="px-0 text-subtitle-2">
        {{ transformDate }}
      </v-card-title>
      <span id="worktime">
        <v-card-title class="px-0 text-subtitle-2">
          {{ transformWorktime }}
        </v-card-title>
        <v-card-subtitle class="px-0 pb-2 text-caption red--text">
          {{ transformRemainTime }}
        </v-card-subtitle>
      </span>
    </div>
    <!--진행사항 Bar 표시 영역 -->
    <div id="progressbar">
      <v-progress-linear
        v-model="proportions"
        color="primary"
        height="18"
      ></v-progress-linear>
      <div class="d-flex justify-space-between">
        <span v-if="worktime.startWorkTime">{{worktime.startWorkTime.substr(11, 5)}}</span>
        <span v-if="!worktime.startWorkTime">미출근</span>
        <span v-if="worktime.finishWorkTime">{{worktime.finishWorkTime.substr(11, 5)}}</span>
        <span v-if="!worktime.finishWorkTime">미퇴근</span>
      </div>
    </div>
  </v-card>
</template>

<script>
export default {
  props: {
    worktime: Object,
  },
  data: () => ({
    remainWorkTime: "",
    totalHour: 4,
    totalMinute: 0,
  }),
  async created() {
    await this.getRemainWorkTime();
  },
  computed: {
    //정해진 하루 근무 시간 중 내 근무시간이 차지하는 비율
    proportions: function () {
      //출근X or 근무중
      if (this.worktime.attendanceState !== "1") {
        return 0;
      }
      const totalWorkTime = 60 * this.totalHour + this.totalMinute;

      const worktime = this.worktime.worktime;

      const hour = worktime.split(":")[0];
      const minute = worktime.split(":")[1];

      const myWorkTime = parseInt(hour, 10) * 60 + parseInt(minute, 10);

      return (myWorkTime / totalWorkTime) * 100;
    },

    //화면에 보여줄 날짜 형식 m월 d일 x요일로 변환
    transformDate: function () {
      const days = ["일", "월", "화", "수", "목", "금", "토"];
      //근태 카드에 입력된 날짜
      const inputedDate = new Date(this.worktime.date);

      const month = inputedDate.getMonth() + 1; //근무날짜의 달
      const date = inputedDate.getDate(); //근무날짜의 일
      const day = days[inputedDate.getDay()]; //근무날짜의 일

      return month + "월 " + date + "일 " + day + "요일";
    },

    ////화면에 보여줄 날짜 형식 h시간 m분으로 변환
    transformWorktime: function () {
      //출근X 상태값: -1
      if (this.worktime.attendanceState === "-1") {
        return "결근";
      }
      //근무중 상태값: 0
      else if (this.worktime.attendanceState === "0") {
        return "근무중";
      }
      //근무완료 상태값: 1
      const worktime = this.worktime.worktime;

      const hour = worktime.split(":")[0];
      const minute = worktime.split(":")[1];

      return hour + "시간 " + minute + "분";
    },
    ////화면에 보여줄 날짜 형식 h시간 m분 미달/초과 으로 변환
    transformRemainTime: function () {
      if (this.worktime.attendanceState !== "1") {
        return "";
      }
      const worktime = this.remainWorkTime;

      let hour = parseInt(worktime.split(":")[0], 10);
      let minute = parseInt(worktime.split(":")[1], 10);

      return hour + "시간 " + minute + "분 미달";
    },
  },
  methods: {
    //정해진 하루 근무시간 중 남은 근무시간
    getRemainWorkTime: function () {
      if (this.worktime.attendanceState !== "1") {
        return;
      }
      const totalWorkTime = 60 * this.totalHour + this.totalMinute;

      const worktime = this.worktime.worktime;

      const hour = worktime.split(":")[0];
      const minute = worktime.split(":")[1];

      const myWorkTime = parseInt(hour, 10) * 60 + parseInt(minute, 10);

      let remainTime = totalWorkTime - myWorkTime;

      const remainHour = parseInt(remainTime / 60, 10);

      const remainMinute = remainTime - remainHour * 60;

      this.remainWorkTime = remainHour + ":" + remainMinute;
    },
  },
};
</script>

<style>
.date-and-time {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin: 0;
}

#progressbar {
  margin-bottom: 8px;
}

#worktime {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
</style>