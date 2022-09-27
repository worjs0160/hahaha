<template>
  <v-container style="padding:0;" class="paddingtop30">
    <div class="user-home-wrap">
      
      <div class="width870 height632 main-box-wrap" style="padding: 12px 24px 24px;">
        <FullCalendar :options="calendarOptions" />
        <!-- <div class="calendarWrap">

          <div class="header">
            <div class="monthBox">

              <button type="button" class="prevBtn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 11.5C9.00588 11.717 9.08227 11.903 9.24094 12.0705L13.8129 16.7892C13.9481 16.9256 14.1068 17 14.3007 17C14.6944 17 15 16.6776 15 16.2621C15 16.0637 14.9236 15.8777 14.7884 15.7351L10.6748 11.5L14.7884 7.26494C14.9236 7.12232 15 6.9425 15 6.73788C15 6.32244 14.6944 6 14.3007 6C14.1126 6 13.9481 6.07441 13.8129 6.21082L9.24094 10.9357C9.0764 11.097 9 11.283 9 11.5Z" fill="#2E2E2E" stroke="#2E2E2E" stroke-width="0.5"/>
                </svg>
              </button>

              <div class="monthBox-inner">
                <p class="pre-400">
                  12월
                  <button type="button" class="month-selectBtn" @click="test()">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 14C12.1381 13.9961 12.2565 13.9452 12.363 13.8394L15.3658 10.7914C15.4526 10.7013 15.5 10.5955 15.5 10.4662C15.5 10.2037 15.2948 10 15.0304 10C14.9042 10 14.7858 10.0509 14.695 10.141L12 12.8834L9.30496 10.141C9.21421 10.0509 9.09977 10 8.96956 10C8.70519 10 8.5 10.2037 8.5 10.4662C8.5 10.5916 8.54735 10.7013 8.63416 10.7914L11.6409 13.8394C11.7435 13.9491 11.8619 14 12 14Z" fill="#2E2E2E"/>
                    </svg>
                  </button>
                </p>



                <div class="monthBox-innerBox main-box-wrap" style="
                width: 559px;
                height: 249px;
                padding: 18px;
                position: absolute;
                left:0;
                box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.2);
                "
                v-if="monthModalChk == 2">

                  <div class="header">

                    <div class="monthBox">
                      <button type="button" class="prevBtn">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M9 11.5C9.00588 11.717 9.08227 11.903 9.24094 12.0705L13.8129 16.7892C13.9481 16.9256 14.1068 17 14.3007 17C14.6944 17 15 16.6776 15 16.2621C15 16.0637 14.9236 15.8777 14.7884 15.7351L10.6748 11.5L14.7884 7.26494C14.9236 7.12232 15 6.9425 15 6.73788C15 6.32244 14.6944 6 14.3007 6C14.1126 6 13.9481 6.07441 13.8129 6.21082L9.24094 10.9357C9.0764 11.097 9 11.283 9 11.5Z" fill="#2E2E2E" stroke="#2E2E2E" stroke-width="0.5"/>
                        </svg>
                      </button>

                      <p class="pre-400">2022년</p>

                      <button type="button" class="nextBtn">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M15 11.5C14.9941 11.283 14.9177 11.097 14.7591 10.9295L10.1871 6.21082C10.0519 6.07441 9.89324 6 9.69931 6C9.30558 6 9 6.32244 9 6.73788C9 6.9363 9.0764 7.12232 9.21156 7.26494L13.3252 11.5L9.21156 15.7351C9.0764 15.8777 9 16.0575 9 16.2621C9 16.6776 9.30558 17 9.69931 17C9.88737 17 10.0519 16.9256 10.1871 16.7892L14.7591 12.0643C14.9236 11.903 15 11.717 15 11.5Z" fill="#2E2E2E" stroke="#2E2E2E" stroke-width="0.5"/>
                        </svg>
                      </button>
                    </div>

                    <button type="button" class="month-select-exit" @click="test2()">
                      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M7.18849 19.0509C6.81935 19.4201 6.80177 20.0792 7.19728 20.466C7.58399 20.8527 8.24317 20.8439 8.61231 20.4747L13.9912 15.087L19.3789 20.4747C19.7568 20.8527 20.4072 20.8527 20.794 20.466C21.1719 20.0704 21.1807 19.4288 20.794 19.0509L15.415 13.6632L20.794 8.28431C21.1807 7.90638 21.1807 7.25599 20.794 6.86927C20.3984 6.49134 19.7568 6.48255 19.3789 6.86048L13.9912 12.2482L8.61231 6.86048C8.24317 6.49134 7.5752 6.47376 7.19728 6.86927C6.81056 7.25599 6.81935 7.91517 7.18849 8.28431L12.5762 13.6632L7.18849 19.0509Z" fill="#646464"/>
                      </svg>
                    </button>

                  </div>

                  <table class="yearsBox">
                    <tr>
                      <td>1월</td>
                      <td>2월</td>
                      <td>3월</td>
                    </tr>
                    <tr>
                      <td>4월</td>
                      <td>5월</td>
                      <td>6월</td>
                    </tr>
                    <tr>
                      <td>7월</td>
                      <td>8월</td>
                      <td>9월</td>
                    </tr>
                    <tr>
                      <td>10월</td>
                      <td>11월</td>
                      <td>12월</td>
                    </tr>
                  </table>

                </div>



              </div>

              <button type="button" class="nextBtn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15 11.5C14.9941 11.283 14.9177 11.097 14.7591 10.9295L10.1871 6.21082C10.0519 6.07441 9.89324 6 9.69931 6C9.30558 6 9 6.32244 9 6.73788C9 6.9363 9.0764 7.12232 9.21156 7.26494L13.3252 11.5L9.21156 15.7351C9.0764 15.8777 9 16.0575 9 16.2621C9 16.6776 9.30558 17 9.69931 17C9.88737 17 10.0519 16.9256 10.1871 16.7892L14.7591 12.0643C14.9236 11.903 15 11.717 15 11.5Z" fill="#2E2E2E" stroke="#2E2E2E" stroke-width="0.5"/>
                </svg>
              </button>

            </div>

            <div class="todayBox">
              <button type="button" class="todayBtn pre-400">오늘</button>
            </div>
          </div>

          <table class="calendar">

            <thead>
              <tr>
                <th>일</th>
                <th>월</th>
                <th>화</th>
                <th>수</th>
                <th>목</th>
                <th>금</th>
                <th>토</th>
              </tr>
            </thead>

            <tbody>

              <tr>
                <td>
                  <div class="noMonth">
                    <span>28</span>
                  </div>
                </td>
                <td>
                  <div class="noMonth">
                    <span>29</span>
                  </div>
                </td>
                <td>
                  <div class="noMonth">
                    <span>30</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>1</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>2</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>3</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>4</span>
                  </div>
                </td>
              </tr>


              <tr>
                <td>
                  <div>
                    <span>5</span>
                    <p><em class="circle-1"></em>출근일</p>
                    <p><em class="circle-1"></em>업무일지</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>6</span>
                    <p><em class="circle-1"></em>출근일</p>
                    <p><em class="circle-1"></em>업무일지</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span class="today">7</span>
                    <p><em class="circle-1"></em>출근일</p>
                    <p><em class="circle-1"></em>업무일지</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>8</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>9</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>10</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>11</span>
                  </div>
                </td>
              </tr>

              <tr>
                <td>
                  <div>
                    <span>12</span>
                    <p><em class="circle-1"></em>출근일</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>13</span>
                    <p><em class="circle-1"></em>출근일</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>14</span>
                    <p><em class="circle-1"></em>출근일</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>15</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>16</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>17</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>18</span>
                  </div>
                </td>
              </tr>

              <tr>
                <td>
                  <div>
                    <span>19</span>
                    <p><em class="circle-1"></em>출근일</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>20</span>
                    <p><em class="circle-1"></em>출근일</p>
                  </div>
                </td>
                <td>
                  <div class="holiday">
                    <span>21</span>
                    <p>공휴일</p>
                  </div>
                </td>
                <td>
                  <div>
                    <span>22</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>23</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>24</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>25</span>
                  </div>
                </td>
              </tr>

              <tr>
                <td>
                  <div>
                    <span>26</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>27</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>28</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>29</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>30</span>
                  </div>
                </td>
                <td>
                  <div>
                    <span>31</span>
                  </div>
                </td>
                <td>
                  <div class="noMonth">
                    <span>1</span>
                  </div>
                </td>
              </tr>

            </tbody>

          </table>

        </div> -->

      </div>



      <div class="width270 height632" style="
      display:flex;
      flex-direction: column;
      justify-content: space-between;
      ">

        <div class="user-main-rightCard main-box-wrap">

          <h1>오늘의 훈련 기록</h1>

          <div class="h2Box">
            <h2 v-if="!myOnTime">오늘은 아직 훈련기록이 없네요</h2>
            <h2 v-if="myOnTime && !myOffTime">오늘은 훈련중이에요</h2>
            <h2 v-if="myOnTime && myOffTime">오늘은 훈련종료하셨어요</h2>
          </div>

          <div class="timeBox">
            <p v-if="myOnTime">{{ myOnTime.substr(0,5) }} ~ {{ myOffTime.substr(0,5) }}</p>
          </div>

          <div class="btnBox">
            <button style="background: #61C0BD;" type="button" @click="goToWork" v-if="checkAtt == 0"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 10V15C22 20 20 22 15 22H9C4 22 2 20 2 15V9C2 4 4 2 9 2H14" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M22 10H18C15 10 14 9 14 6V2L22 10Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 13H13" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 17H11" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            훈련시작하기</button>
            <button style="background: #61C0BD;" type="button" @click="offWork" v-if="checkAtt == 1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 10V15C22 20 20 22 15 22H9C4 22 2 20 2 15V9C2 4 4 2 9 2H14" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M22 10H18C15 10 14 9 14 6V2L22 10Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 13H13" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 17H11" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            훈련종료하기</button>
            <button style="background: #E1E1E1;" type="button" v-if="checkAtt == 2"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 10V15C22 20 20 22 15 22H9C4 22 2 20 2 15V9C2 4 4 2 9 2H14" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M22 10H18C15 10 14 9 14 6V2L22 10Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 13H13" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 17H11" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            훈련종료</button>
          </div>

        </div>


        <div class="user-main-companyBox main-box-wrap py-0">

          <div class="comtop">
            <h2>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 22H22" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M17 2H7C4 2 3 3.79 3 6V22H21V6C21 3.79 20 2 17 2Z" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M7 16.5H10" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M14 16.5H17" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M7 12H10" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M14 12H17" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M7 7.5H10" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M14 7.5H17" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              {{ comData.comName }}
            </h2>
            <p class="num">{{ comData.comNum }}</p>
            <p class="address">{{ comData.comAddr1 }}</p>
          </div>

          <div class="comtop comtop2">
            <h2>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 22H22" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2.94995 21.9993L2.99995 9.96926C2.99995 9.35926 3.28995 8.77931 3.76995 8.39931L10.77 2.9493C11.49 2.3893 12.4999 2.3893 13.2299 2.9493L20.23 8.3893C20.72 8.7693 21 9.34926 21 9.96926V21.9993" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linejoin="round"/>
                <path d="M13 17H11C10.17 17 9.5 17.67 9.5 18.5V22H14.5V18.5C14.5 17.67 13.83 17 13 17Z" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linejoin="round"/>
                <path d="M9.5 13.75H7.5C6.95 13.75 6.5 13.3 6.5 12.75V11.25C6.5 10.7 6.95 10.25 7.5 10.25H9.5C10.05 10.25 10.5 10.7 10.5 11.25V12.75C10.5 13.3 10.05 13.75 9.5 13.75Z" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linejoin="round"/>
                <path d="M16.5 13.75H14.5C13.95 13.75 13.5 13.3 13.5 12.75V11.25C13.5 10.7 13.95 10.25 14.5 10.25H16.5C17.05 10.25 17.5 10.7 17.5 11.25V12.75C17.5 13.3 17.05 13.75 16.5 13.75Z" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linejoin="round"/>
                <path d="M19.0001 7L18.9701 4H14.5701" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              {{ teamData.teamName }}
            </h2>
            <p class="num">{{ teamData.teamNum }}</p>
            <p class="address">{{ teamData.teamAddr1 }}</p>
          </div>

        </div>

      </div>

    </div>
  </v-container>
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
  data(){
    return{
      calendarOptions: {
        plugins: [ dayGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth', // 월간 달력
        showNonCurrentDates: false, // true하면 해당 달 이외의 날짜 전부 숫자표시
        fixedWeekCount: false, // true하면 무조건 6주로 표시
        locale : 'ko',
        editable: true, // 드래그 수정 가능
        droppable: true, //drop기능의 api 사용여부
        eventDrop: this.scheduleUpdateDate, //드랍시 해당 이벤트의 내용을 콜백
        selectable: true, //드래그로 여러일 선택가능
        weekends: true, // 일주일에 주말까지 표시
        dayMaxEventRows: 3, // 이벤트 갯수가 4개부턴 +more 표시로 바뀜
        height: 600,
        handleWindowResize: false,
        select: this.scheduleSelectDate, // 날짜를 드래그하여 클릭하면 해당 날짜 데이터가 들어옴(scheduleSelectDate함수 사용)
        eventClick: this.scheduleClickData, // 이벤트 클릭하면 해당 데이터가 들어옴(scheduleClickData함수 사용)
        events: [ // 데이터는 이런식으로 들어가면 됨
          { title: 'event 1', start:'2022-02-01T13:00', end:'2022-02-02T00:01', startEditable:true}, // 띠 형식의 일정표시
          { title: 'event 2', date: '2022-02-02' } // 점 + 날짜로 일정표시
        ]
      },
      monthModalChk: 1,
      type: "month",
      typeToLabel: {
        month: "Month",
        week: "Week",
        day: "Day",
        "4day": "4 Days",
      },
      today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString(), //현재 시간, 여기서 변수만들고 오늘날짜 가져오려면 지금처럼 해야함
      tomorrow: new Date(Date.now() + 86400000 - new Date().getTimezoneOffset() * 60000).toISOString(), //현재 시간
      checkAtt: 0,
      myOnTime: "",
      myOffTime: "",
      workDays: [],
      week: ["일", "월", "화", "수", "목", "금", "토"], //근무 유형이랑 비교하기 위한 날짜
      attType: {},
      comData: {},
      teamData: {},
      dialog:false,
      myIp: "",
      myAttDate:"",
      ipCheck: false,
    }
  },
  async created() {
    await this.loadingCover(true);
    await this.getAttType();
    await this.getComInfo();
    await this.getTeamInfo();
    await this.checkMyAtt();
    await this.getMySchedule();
    await this.loadingCover(false);
  },
  watch: {
    checkAtt: function() {
      this.checkMyAtt();
    },
    events: function() {
      console.log(1)
    },
  },
  mounted() {},
  methods: {
    scheduleClickData(info){
      this.$axios({
        method: "GET",
        url:"calendars/api/calendar/" + info.event._def.publicId
      })
      .then((res) => {
        this.$emit("scheduleClickData", true, res.data)
      })
    },
    scheduleSelectDate(info){
      var date = new Date(new Date(info.end).setSeconds(new Date(info.end).getSeconds() - 1))
      var year = date.getFullYear();
      var month = ('0' + (date.getMonth() + 1)).slice(-2);
      var day = ('0' + date.getDate()).slice(-2);
      var hours = ('0' + date.getHours()).slice(-2); 
      var minutes = ('0' + date.getMinutes()).slice(-2);
      var seconds = ('0' + date.getSeconds()).slice(-2); 

      var endTime = year+"-"+month+"-"+day+"T"+hours+":"+minutes+":"+seconds
      this.$emit("scheduleSelectDate", true, this.$store.state.userStore.id, info.startStr+"T00:00:00", endTime, this.$store.state.userStore.name)
    },
    scheduleUpdateDate(info){
      this.$axios({
        method: "PATCH",
        url:"calendars/api/calendar/" + info.event._def.publicId + "/",
        data: {
          id: info.event._def.publicId,
          title: info.event._def.title,
          start: info.event.startStr.substr(0,19),
          end: info.event.endStr.substr(0,19),
          contents: info.event._def.extendedProps.contents,
          startEditable: true,
        },
      })
      .then(() => {
        this.$store.dispatch("callToast", {
          msg: "일정시간이 변경되었습니다.",
          result: "success",
        });
      })
    },
    loadingCover(val) {
      this.$emit("coverSetChild", val);
    },
    async goToWork() {
      //.toISOString()사용하려면 시간 오프셋 해줘야함
      var nowTime = new Date(Date.now() - new Date().getTimezoneOffset() * 60000);
      var now = new Date(Date.now())
      var month= now.getMonth() +1;  
      var day  = now.getDate();  
      var year = now.getFullYear();

      // await this.$axios.get("users/getIP/")
      // .then((res) => {
      //   //현재 접속한 PC의 IP가 소속된 훈련기관의 허용IP인지 비교, 일단 3바이트까지만 비교함
      //   if(res.data.ip.substr(0,9)==this.$store.state.userStore.teamAllowedIP.substr(0,9)){
      //     this.ipCheck = true
      //   }
      //   else {this.ipCheck = false}
      //   this.myIp = res.data.ip
      // })
      // .catch((err) => {
      //   console.log(err)
      // })

      // //내 ip가 허용ip가 아니면 훈련시작 불가
      // if(!this.ipCheck){
      //   this.$store.dispatch("callToast", {
      //     msg: "IP확인 결과 현재 위치가 훈련기관의 위치와 다릅니다.",
      //     // msg: "훈련기관 위치 : "+this.$store.state.userStore.teamAllowedIP,
      //     // msg: "내 위치 : "+this.myIp,
      //     result: "fail",
      //   });
      //   return false;
      // }

      //근무시간 기록하기 전에 오늘 요일이 유저의 근무 유형의 요일인지 체크
      for (var count = 0; this.workDays[count]; count++) {
        if (this.workDays.indexOf(this.week[new Date(Date.now()).getDay()]) == -1){
          this.$store.dispatch("callToast", {
            msg: "오늘은 훈련일이 아니네요. 집에서 쉬시는게 어떨까요? ^^",
            result: "fail",
          });
          return false;
        }
      }

      //출근시간은 자신의 근무유형의 퇴근시간보다 늦으면 출근 불가능
      if(new Date(Date.now()).getTime() > new Date(year + '-' + month + '-' + day + '-' + this.attType.offTime).getTime()){
        this.$store.dispatch("callToast", {
          msg: "오늘 훈련을 시작하기엔 시간이 너무 늦네요 ㅜㅜ",
          result: "fail",
        });
        return false;
      }

      //근무시간 기록
      await this.$axios({
        method: "POST",
        url: "attendances/api/empAtt/",
        data: {
          user: this.$store.state.userStore.id,
          onTime: nowTime.toISOString().substr(0, 19),
          onType: true,
          offTime: null,
          offType: false,
          place: "",
          memo: "",
          id: null,
          attType: this.attType.id,
        },
      }).catch((err) => {
        console.log(err.response);
      });
      this.$store.dispatch("callToast", {
        msg: "오늘 훈련이 시작되었습니다.",
        result: "success",
      });
      this.checkAtt = 1;
    },
    async offWork() {
      if((new Date(this.myAttDate+"T23:59:59").getTime()) < (new Date(Date.now()).getTime())){ // 퇴근버튼 누른 시점이 다음날일 경우
        var nowTime = this.myAttDate+"T23:59:59"
      }
      else{
        var nowTime = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 19);
      }
      var now = new Date(Date.now())
      var month= now.getMonth() +1;  
      var day  = now.getDate();  
      var year = now.getFullYear();
      var checkStartTime = 0
      var checkEndTime = 0
      var workTime = 0

      if(new Date(this.myStartTime).getTime() >= new Date(year + '-' + month + '-' + day + '-' + this.attType.onTime).getTime()){
        //내 출근시간이 근무유형의 시간보다 늦으면 내 출근 시간으로 체크
        checkStartTime = new Date(this.myStartTime).getTime() //근무시간 계산용 출근 시간
      }
      else if(new Date(this.myStartTime).getTime() < new Date(year + '-' + month + '-' + day + '-' + this.attType.onTime).getTime()){
        //내 출근시간이 근무유형의 시간보다 빠르면 근무유형 출근 시간으로 체크
        checkStartTime = new Date(year + '-' + month + '-' + day + '-' + this.attType.onTime).getTime()
      }

      if(new Date(Date.now()).getTime() >= new Date(year + '-' + month + '-' + day + '-' + this.attType.offTime).getTime()){
        //내 퇴근시간이 근무유형의 시간보다 늦으면 근무유형 퇴근 시간으로 체크
        checkEndTime = new Date(year + '-' + month + '-' + day + '-' + this.attType.offTime).getTime() //근무시간 계산용 퇴근 시간
      }
      else if(new Date(Date.now()).getTime() < new Date(year + '-' + month + '-' + day + '-' + this.attType.offTime).getTime()){
        //내 퇴근시간이 근무유형의 시간보다 빠르면 내 퇴근 시간으로 체크
        checkEndTime = new Date(Date.now()).getTime()
      }
      if(Math.floor((checkEndTime - checkStartTime) / 1000 / 3600) > 0){
        workTime = Math.floor((checkEndTime - checkStartTime) / 1000 / 3600);
      }
      else if(Math.floor((checkEndTime - checkStartTime) / 1000 / 3600) < 0){
        workTime = 0;
      }

      await this.$axios({
        method: "PATCH",
        url: "attendances/api/empAtt/" + this.attId + "/",
        data: {
          user: this.$store.state.userStore.id,
          offTime: nowTime,
          offType: true,
          workTime: workTime,
        },
      }).catch((err) => {
        console.log(err.response);
      });
      this.$store.dispatch("callToast", {
        msg: "오늘 훈련이 종료되었습니다. 고생하셨어요",
        result: "success",
      });
      this.checkAtt = 2;
    },
    async getMySchedule() {
      await this.$axios({
        method: "GET",
        url: "calendars/api/calendar/?user=" + this.$store.state.userStore.id
      })
      .then((res) => {
        this.calendarOptions.events = res.data
      })
      .catch((err) => {
        console.log(err);
      });
    },
    async checkMyAtt() {
      await this.$axios({
        method: "GET",
        url:
          "attendances/api/empAtt/?user_id=" +
          this.$store.state.userStore.id +
          "&onTime__range=" +
          this.today.substr(0, 10) +
          "," +
          this.tomorrow.substr(0, 10),
      })
        .then((res) => {
          this.attId = res.data[0].id;
          if (res.data[0].onType) {
            this.myOnTime = res.data[0].onTime.substr(11, 8);
            this.myAttDate = res.data[0].onTime.substr(0,10);
            this.myStartTime = new Date(res.data[0].onTime); //근무시간 계산용
            this.checkAtt = 1;
          }
          if (res.data[0].offType) {
            this.myOffTime = res.data[0].offTime.substr(11, 8);
            this.checkAtt = 2;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getAttType() {
      await this.$axios({
        method: "GET",
        url:
          "attendances/api/userAttType/" + this.$store.state.userStore.id + "/",
      })
        .then((res) => {
          this.attType = res.data.attType;
          this.workDays = res.data.days;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getComInfo() {
      await this.$axios({
        method: "GET",
        url:"datasets/api/company_list/"+ this.$store.state.userStore.comID +"/",
      })
        .then((res) => {
          this.comData = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getTeamInfo() {
      await this.$axios({
        method: "GET",
        url: "users/api/employee/" + this.$store.state.userStore.id,
      })
        .then((res) => {
          this.teamData = res.data.teamID;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
  .user-home-wrap {
    display: flex;
    justify-content: space-between;
  }
  .width870 {
    width:870px;
  }
  .width270 {
    width: 270px;
  }
  .paddingtop30 {
    padding-top: 30px !important;
  }
  .height632 {
    height: 632px;
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
