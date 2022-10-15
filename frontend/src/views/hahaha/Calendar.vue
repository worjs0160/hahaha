<template>
  <v-row justify="center" class="mt-5">
    <v-col cols="12" align="center">
      <div class="calendarSize main-box-wrap" style="padding: 12px 24px 24px;">
        <FullCalendar :options="calendarOptions" />
      </div>
    </v-col>
  </v-row>
</template>

<script>
import '@fullcalendar/core/vdom'
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction';

export default {
  
  components: {
    FullCalendar // <FullCalendar>태그로 캘린더 컴포넌트 사용
  },
  data: () => ({
    calendarOptions: {
      plugins: [ dayGridPlugin, interactionPlugin ],
      initialView: 'dayGridMonth', // 월간 달력
      showNonCurrentDates: false, // true하면 해당 달 이외의 날짜 전부 숫자표시
      fixedWeekCount: false, // true하면 무조건 6주로 표시
      locale : 'ko',
      editable: true, // 드래그 수정 가능
      droppable: true, //drop기능의 api 사용여부
      //eventDrop: this.scheduleUpdateDate, //드랍시 해당 이벤트의 내용을 콜백
      selectable: true, //드래그로 여러일 선택가능
      weekends: true, // 일주일에 주말까지 표시
      dayMaxEventRows: 3, // 이벤트 갯수가 4개부턴 +more 표시로 바뀜
      height: 600,
      handleWindowResize: false,
      //select: this.scheduleSelectDate, // 날짜를 드래그하여 클릭하면 해당 날짜 데이터가 들어옴(scheduleSelectDate함수 사용)
      //eventClick: this.scheduleClickData, // 이벤트 클릭하면 해당 데이터가 들어옴(scheduleClickData함수 사용)
      events: []
    },
  }),
  async created() {
    await this.getDonations();
  },
  watch: {
    // "data.name": function() {
    //   if(!this.data.name) {
    //     this.err.nameErrMsg = "필수 정보입니다."
    //   }
    //   else this.err.nameErrMsg = ""
    // },
  },
  methods: {
    async getDonations(){
      await this.$axios({
        method: "GET",
        url:"donates/api/donateInfo/"
      }).then((res) => {
        this.calendarOptions.events = []
        for(var a=0; a<res.data.length; a++){
          this.calendarOptions.events.push({
            title: res.data[a].foodName,
            start: res.data[a].startPickUp,
            end: res.data[a].endPickUp,
          })
        }
      })
    },
  },
};
</script>

<style>
  .user-home-wrap {
    display: flex;
    justify-content: space-between;
  }
  .calendarSize {
    width:870px;
    height:631px;
  }
  .width270 {
    width: 270px;
  }
  .paddingtop30 {
    padding-top: 30px !important;
  }
  .calendarWrap .header {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 22px;
  }
  .calendarWrap .monthBox {
    display: flex;
    align-items: center;
  }
  .calendarWrap .monthBox button {
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all .3s;
    border-radius: 50%;
  }
  .calendarWrap .monthBox button:hover {
    background: #f5f5f5;
  }
  .calendarWrap .monthBox p {
    font-size: 20px;
    color: #2e2e2e;
    display: flex;
    align-items: center;
    margin: 0;
    margin: 0 33px;
  }
  .main-box-wrap {
    background: #FFFFFF;
    box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
    border-radius: 20px;
  }
  .todayBox {}
  .todayBox .todayBtn {
    font-size: 18px;
    color: #646464;
    width: 108px;
    height: 48px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #f5f5f5;
    border-radius: 10px;
    transition: all .3s;
  }
  .todayBox .todayBtn:hover {
    background: #61C0BD;
    color: #fff;
  }
  .holiday span,
  .holiday p {
    color: #EC0000 !important;
  }
  .circle-1 {
    display: block;
    background: #0081C7;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    margin-right: 5px;
  }
  .noMonth {
    background: #F5F5F5;
  }
  .noMonth span {
    color: #989898 !important; 
  }
  .calendar {
    border-collapse: collapse;
    width: 822px;
  }
  .calendar tbody {
    border-radius: 10px;
    border-style: hidden;
    box-shadow: 0 0 0 .5px #e4e4e4;
  }
  .calendar th {
    font-size: 14px;
    color: #989898;
    font-family: 'Pretendard-Regular';
    width: 117px;
    text-align: center;
    padding-bottom: 8px;
  }
  .calendar td {
    font-size: 12px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    width: 120px;
  }
  .calendar td span {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    cursor: pointer;
  }
  .today {
    color: #49ada9;
    background: #e4f2f9;
  }
  .calendar td div {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 97px;
    padding-top: 8px;
  }
  .calendar td {
      border-top: .5px solid #e4e4e4;
      border-left: .5px solid #e4e4e4;
      overflow: hidden;
  }
  .calendar td:last-child {
    border-right: .5px solid #e4e4e4;
  }
  .calendar p {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    padding-left: 8px;
    margin: 0;
    margin-top: 4px;
    cursor: pointer;
  }
  .calendar div p:nth-of-type(1) {
    margin-top: 14px;
  }
  .calendar tbody tr:first-child td:last-child {
    border-top-right-radius: 10px !important;
  }
  .calendar tbody tr:first-child td:first-child {
    border-top-left-radius: 10px !important;
  }
  .calendar tbody tr:last-child td:last-child {
    border-bottom-right-radius: 10px !important;
  }
  .calendar tbody tr:last-child td:first-child {
    border-bottom-left-radius: 10px !important;
  }
  .user-main-rightCard {
    width: 100%;
    height: 301px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .user-main-rightCard h1 {
    font-size: 20px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
  }
  .user-main-rightCard .h2Box h2 {
    font-size: 16px;
    color: #b4b4b4;
    font-family: 'Pretendard-Regular';
    font-weight: 400;
  }
  .user-main-rightCard .timeBox p {
    font-size: 24px;
    color: #2e2e2e;
    font-family: 'Pretendard-SemiBold';
  }
  .user-main-rightCard .btnBox button {
    width: 222px;
    height: 64px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 16px;
    font-size: 20px;
    color: #fff;
    font-family: 'Pretendard-Regular';
    transition: all .3s;
  }
  .user-main-rightCard .btnBox button svg {
    margin-right: 20px;
  }
  .user-main-companyBox {
    width: 100%;
    height: 301px;
    padding: 24px;
  }
  .comtop {
    height: 50%;
    border-bottom: 0.5px solid #B4B4B4;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .comtop2 {
    border-bottom: 0;
  }
  .comtop h2 {
    font-size: 20px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    display: flex;
    align-items: center;
    margin: 0;
  }
  .comtop h2 svg {
    margin-right: 8px;
  }
  .comtop .num {
    font-size: 16px;
    color: #008bd6;
    font-family: 'Pretendard-Regular';
    margin: 0;
    margin: 16px 0 6px;
  }
  .comtop .address {
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    margin: 0;
  }
  .monthBox-inner {
    position: relative;
  }
  .yearsBox {
    width: 100%;
    border: 1px solid #E1E1E1;
  }
  .yearsBox td {
    cursor: pointer;
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    transition: all .3s;
    text-align: center;
    padding: 7px 0;
    border-right: 1px solid #F5F5F5;
    border-bottom: 1px solid #F5F5F5;
    border-collapse: collapse;
  }
  .yearsBox tr td:last-child {
    border-right: none;
  }
  .yearsBox tr:last-child td {
    border-bottom: none;
  }
  .yearsBox td:hover {
    background: #EFF9F8;
    color: #49ADA9;
  }
  .fc .fc-toolbar-title,
  .fc .fc-col-header-cell-cushion,
  .fc .fc-daygrid-day-number,
  .fc-h-event .fc-event-main-frame,
  .fc-direction-ltr .fc-daygrid-event.fc-event-end,
  .fc-direction-rtl .fc-daygrid-event.fc-event-start,
  .fc .fc-button-primary:disabled {
    font-family: 'Pretendard-Regular';
    color: #2e2e2e;
  }
  .fc-h-event .fc-event-main-frame {
    padding: 0 10px;
    color: #fff;
  }
  .fc-direction-ltr .fc-daygrid-event.fc-event-end {
    color: #3788d8;
  }
  .fc-direction-ltr .fc-daygrid-event .fc-event-time {
    font-weight: 500;
    margin-right: 5px;
  }
  .fc .fc-toolbar-title {
    font-size: 22px;
  }
  .fc-icon-chevron-left:before,
  .fc-icon-chevron-right:before {
    position: relative;
    top: -4px;
  }
  .fc .fc-button:disabled,
  .fc .fc-button:not(:disabled) {
    width: 108px;
    height: 43px;
    background: #E1E1E1;
    border-radius: 10px;
    color: #646464;
    border: 0;
    transition: all .3s;
  }
  .fc .fc-button:not(:disabled) {
    background-color: #2C3E50;
    color: #fff;
  }
  .fc-direction-ltr .fc-button-group > .fc-button:not(:last-child),
  .fc-direction-ltr .fc-button-group > .fc-button:not(:first-child) {
    width: 50px;
  }
  .fc .fc-toolbar.fc-header-toolbar {
    /* padding: 0 15px; */
  }
  .fc-day-sat a { color:#0000FF !important; } /* 토요일 */
  .fc-day-sun a { color:#FF0000 !important; } /* 일요일 */
  .fc-event-time { display: none; }
  .fc-event-title-container { text-overflow:ellipsis; }
  .fc-event-title { text-overflow:ellipsis; }
</style>
