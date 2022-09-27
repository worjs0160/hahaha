<template>
  <div class="d-flex flex-column align-center">
    <div class="d-flex align-center mb-1" style="width:270px">
      <!--이전 주 버튼-->
      <v-btn icon @click="prev"><v-icon>mdi-chevron-left</v-icon></v-btn>
      <v-card-subtitle class="mx-1 pa-0" style="text-align:center; font-size:16px !important; font-weight:bold;">
        {{year}}년
      </v-card-subtitle>
      <v-card-subtitle class="mx-1 pa-0" style="width:270px !important; text-align:center;">
        {{ weekMonday }} ~ {{ weekSunday }}
      </v-card-subtitle>
      <!--다음 주 버튼-->
      <v-btn icon @click="next"><v-icon>mdi-chevron-right</v-icon></v-btn>
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  data: () => ({
    year: "", //선택된 날짜의 년도
    month: "", //선택된 날짜의 달
    weekNum: "", //선택된 날짜의 달의 주차
    selectedDate: "", //선택된 날짜
    weekFirstDate: "", //선택된 날짜가 포함된 주의 월요일 날짜
    weekLastDate: "", //선택된 날짜가 포함된 주의 일요일 날짜
  }),
  async created() {
    //당일 날짜로 date 초기화
    this.selectedDate = new Date(Date.now()).toISOString().substr(0,10).replace(/-/g, "/")
    //당일 날짜의 주차
    await this.getWeekNum(this.selectedDate);
    await this.MondayOfWeek(this.selectedDate);
    await this.SundayOfWeek(this.selectedDate);
  },

  watch: {
    //
    selectedDate() {
      this.getWeekNum(this.selectedDate);
      this.MondayOfWeek(this.selectedDate);
      this.SundayOfWeek(this.selectedDate);
      this.$emit("change");
    },
  },

  computed: {
    //date가 속한 주의 일요일
    weekMonday: {
      get() {
        const tempDate = new Date(this.weekFirstDate);
        const month = tempDate.getMonth() + 1;
        const date = tempDate.getDate();

        return month + "." + date;
      },
    },

    //date가 속한 주의 일요일
    weekSunday: {
      get() {
        const tempDate = new Date(this.weekLastDate);
        const month = tempDate.getMonth() + 1;
        const date = tempDate.getDate();

        return month + "." + date;
      },
    },
  },

  methods: {
    getDate: function () {
      return this.selectedDate;
    },
    getWeekFirstDate: function () {
      return this.weekFirstDate;
    },
    getWeekLastDate: function () {
      return this.weekLastDate;
    },

    //dateFormat이 속한 주의 월요일의 일 날짜
    MondayOfWeek: function (dateFormat) {
      const inputDate = new Date(dateFormat);
      //console.log(inputDate)
      let year = inputDate.getFullYear();
      let month = inputDate.getMonth();
      let date = inputDate.getDate();

      const day = (6 + inputDate.getDay()) % 7; //getDay의 결과(일:0 월:1 화:2 수:3 목:4 금:5 토:6)

      let newDate = new Date(year, month, date);
      newDate.setDate(newDate.getDate() - day);

      year = newDate.getFullYear();

      month = newDate.getMonth() + 1;
      month = ("0" + month).slice(-2);

      date = newDate.getDate();
      date = ("0" + date).slice(-2);

      this.weekFirstDate = year + "-" + month + "-" + date;
    },

    //dateFormat이 속한 주의 일요일의 일 날짜
    SundayOfWeek: function (dateFormat) {
      const inputDate = new Date(dateFormat);

      let year = inputDate.getFullYear();
      let month = inputDate.getMonth();
      let date = inputDate.getDate();

      const day = (7 - inputDate.getDay()) % 7; //getDay의 결과(일:0 월:1 화:2 수:3 목:4 금:5 토:6)

      let newDate = new Date(year, month, date);
      newDate.setDate(newDate.getDate() + day);

      year = newDate.getFullYear();

      month = newDate.getMonth() + 1;
      month = ("0" + month).slice(-2);

      date = newDate.getDate();
      date = ("0" + date).slice(-2);

      this.weekLastDate = year + "-" + month + "-" + date;
    },

    //dateFormat가 속한 달의 주 차수
    getWeekNum: function (dateFormat) {
      const inputDate = new Date(dateFormat);

      //입력받은 날짜의 년, 월, 일
      let year = inputDate.getFullYear();
      let month = inputDate.getMonth() + 1;
      //let date = inputDate.getDate();

      const weekNumberByThurFnc = (paramDate) => {
        const year = paramDate.getFullYear();
        const month = paramDate.getMonth();
        const date = paramDate.getDate();

        // 인풋한 달의 첫 날과 마지막 날의 요일
        const firstDate = new Date(year, month, 1);
        const lastDate = new Date(year, month + 1, 0);
        const firstDayOfWeek =
          firstDate.getDay() === 0 ? 7 : firstDate.getDay();
        const lastDayOfweek = lastDate.getDay();

        // 인풋한 달의 마지막 일
        const lastDay = lastDate.getDate();

        // 첫 날의 요일이 금, 토, 일요일 이라면 true
        const firstWeekCheck =
          firstDayOfWeek === 5 || firstDayOfWeek === 6 || firstDayOfWeek === 7;
        // 마지막 날의 요일이 월, 화, 수라면 true
        const lastWeekCheck =
          lastDayOfweek === 1 || lastDayOfweek === 2 || lastDayOfweek === 3;

        // 해당 달이 총 몇주까지 있는지
        const lastWeekNo = Math.ceil((firstDayOfWeek - 1 + lastDay) / 7);

        // 날짜 기준으로 몇주차 인지
        let weekNo = Math.ceil((firstDayOfWeek - 1 + date) / 7);

        // 인풋한 날짜가 첫 주에 있고 첫 날이 월, 화, 수로 시작한다면 'prev'(전달 마지막 주)
        if (weekNo === 1 && firstWeekCheck) weekNo = "prev";
        // 인풋한 날짜가 마지막 주에 있고 마지막 날이 월, 화, 수로 끝난다면 'next'(다음달 첫 주)
        else if (weekNo === lastWeekNo && lastWeekCheck) weekNo = "next";
        // 인풋한 날짜의 첫 주는 아니지만 첫날이 월, 화 수로 시작하면 -1;
        else if (firstWeekCheck) weekNo = weekNo - 1;

        return weekNo;
      };

      // 목요일 기준의 주차
      let weekNo = weekNumberByThurFnc(inputDate);

      // 이전달의 마지막 주차일 떄
      if (weekNo === "prev") {
        // 이전 달의 마지막날
        const afterDate = new Date(year, month - 1, 0);
        year = month === 1 ? year - 1 : year;
        month = month === 1 ? 12 : month - 1;
        weekNo = weekNumberByThurFnc(afterDate);
      }
      // 다음달의 첫 주차일 때
      if (weekNo === "next") {
        year = month === 12 ? year + 1 : year;
        month = month === 12 ? 1 : month + 1;
        weekNo = 1;
      }

      this.year = year;
      this.month = month;
      this.weekNum = weekNo;
    },

    // 이전 버튼을 눌렀을 때 동작함수
    prev: function () {
      let currentDate = new Date(this.selectedDate);

      //현재 선택된 날짜의 년, 월, 일
      let year = currentDate.getFullYear();
      let month = currentDate.getMonth();

      let date = currentDate.getDate();

      const prevDate = new Date(year, month, date);
      prevDate.setDate(prevDate.getDate() - 7);

      year = prevDate.getFullYear();
      month = prevDate.getMonth() + 1;
      date = prevDate.getDate();

      this.selectedDate = year + "/" + month + "/" + date;
    },

    // 다음 버튼을 눌렀을 때 동작함수
    next: function () {
      let currentdate = new Date(this.selectedDate);

      //현재 선택된 날짜의 년, 월, 일
      let year = currentdate.getFullYear();
      let month = currentdate.getMonth();
      let date = currentdate.getDate();

      const nextDate = new Date(year, month, date);
      nextDate.setDate(nextDate.getDate() + 7);

      year = nextDate.getFullYear();
      month = nextDate.getMonth() + 1;
      date = nextDate.getDate();

      this.selectedDate = year + "/" + month + "/" + date;
    },

    //알람 날짜
    alarmDate(date){
      this.selectedDate = new Date(date).toISOString().substr(0,10).replace(/-/g, "/")
      this.getWeekNum(this.selectedDate);
      this.MondayOfWeek(this.selectedDate);
      this.SundayOfWeek(this.selectedDate);
    },
  },
};
</script>

<style>
</style>