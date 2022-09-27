<template>
  <v-container style="width:100%;">
    <v-row justify="space-between" style="align-items: center; padding: 12px 24px; margin: 0 !important; border-bottom: 0.5px solid #E1E1E1;">
      <week-num-picker
        v-on:change="inItWeekDates"
        ref="weekPicker"
        class="pre-600"
      ></week-num-picker>
      <div class="pre-600">{{this.todayTitle}}</div>
      <!-- <v-chip color="red" text-color="white" class="pre-600">미훈련</v-chip>
      <v-chip color="#FF6B00" text-color="white" class="pre-600">시간미달</v-chip>
      <v-chip color="#49ADA9" text-color="white" class="pre-600">훈련완료</v-chip> -->
      <print :formTitle="formTitle" :printData="toPrintItems" class="print-visible"></print>
      
      <v-btn  id="print-btn" class="pre-400" @click="dialogCoverSet(true), companyAttendancePrintDialogStateChange(true), getComUserList()" elevation="0">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right:10px;">
          <path d="M9.5 10C10.3284 10 11 9.32843 11 8.5C11 7.67157 10.3284 7 9.5 7C8.67157 7 8 7.67157 8 8.5C8 9.32843 8.67157 10 9.5 10Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12.8 4H9.6C5.6 4 4 5.6 4 9.6V14.4C4 18.4 5.6 20 9.6 20H14.4C18.4 20 20 18.4 20 14.4V10.4" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M15 6H19" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
          <path d="M17 8V4" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
          <path d="M5 18L8.82566 15.1435C9.4387 14.6861 10.3233 14.7379 10.8743 15.2643L11.1304 15.5146C11.7356 16.0928 12.7134 16.0928 13.3187 15.5146L16.5468 12.4337C17.1521 11.8554 18.1299 11.8554 18.7351 12.4337L20 13.6419" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        인쇄하기
      </v-btn>
    </v-row>

    <v-row justify="start" style="align-items: center; padding: 12px 24px; margin: 0 !important; border-bottom: 0.5px solid #E1E1E1;">
      <v-chip color="red" text-color="white" class="pre-600 mx-2">미훈련</v-chip>
      <v-chip color="#FF6B00" text-color="white" class="pre-600 mx-2">시간미달</v-chip>
      <v-chip color="#49ADA9" text-color="white" class="pre-600 mx-2">훈련완료</v-chip>
    </v-row>

    <!-- 마우스오버 스크롤 생성 영역 -->
    <div class="scroll-wrap" style="overflow-y:scroll; height: calc(100vh - 360px);">

      <div class="scroll-cover"></div>

      <template  v-for="(item,idx) of attUser" >
        <div
          :key="item.idx"
          v-if="attUser.length != 0"
          class="atten-card"
          @click="emitAttList(item)"
          v-bind:class="view[idx]"
        >

          <div class="atten-card-inner">

            <div class="atten-card-left">
              <div class="atten-imgBox">
                <img :src="userList[idx].profile" alt="">
              </div>
              <p>{{item.name}}</p>
            </div>

            <div class="atten-card-right">

              <div class="atten-weekBox">
                <template class="" v-for="(attState,index) of item.attState">
                  <!-- <div v-if="item.attState.length != 0"  :key="index" :class="{'now-stat' : attState.now == true, 'default-stat': attState.now == false}"> -->
                  <div v-if="item.attState.length != 0"  :key="index" class="default-stat">

                      <!--하루 일한 시간이 있으면 초록색 표시-->
                      <v-chip
                      :key="idx"
                        class="week-item"
                        color="#49ADA9"
                        label
                        text-color="white"
                        v-if="attState.stat==0"
                      >
                        {{attState.days}}
                      </v-chip>
                      <!--하루 일한 시간이 없고 시작시간이 있으면 주황색 표시-->
                      <v-chip
                      :key="idx"
                        class="week-item"
                        color="#FF6B00"
                        label
                        text-color="white"
                        v-if="attState.stat==1"
                      >
                        {{attState.days}}
                      </v-chip>
                      <!--시작시간도 없으면 빨간색 표시-->
                      <v-chip
                      :key="idx"
                        class="week-item"
                        color="red"
                        label
                        text-color="white"
                        v-if="attState.stat==2"
                      >
                        {{attState.days}}
                      </v-chip>
                      <!-- 작성대상이 아니면 회색 표시-->
                      <v-chip
                      :key="idx"
                        class="week-item"
                        color="grey"
                        label
                        text-color="white"
                        v-if="attState.stat==9"
                      >
                        {{attState.days}}
                      </v-chip>
                  </div>
                </template>
              </div>
              
              <div class="atten-timeBox">
                <p>{{item.week}}시간</p>
                <p>&nbsp;/&nbsp;</p>
                <p>{{item.monthWorkTime}}시간</p>
              </div>

              <div class="atten-gage">
                <v-progress-linear
                  v-model="item.workRatio"
                  height="14"
                  style="pointer-events: none; border-radius: 3px;"
                  color="primary500"
                >
                </v-progress-linear>
              </div>

            </div>

          </div>

        </div>
      </template>

    </div>


  </v-container>
</template>

<script>
import WeekNumPicker from "/src/components/pickers/WeekNumPicker";
import { Printd } from "printd";
import Print from "@/components/forms/AttendancePrint.vue";

export default {
  components: {WeekNumPicker,Print,},
  async created() {
    await this.loadingCover(true);
    await this.getComUser();
    await this.getAttDataList();
    await this.loadingCover(false);
  },
  data: () => ({
    formTitle: '선수 근태기록',
    weekFirstDate: new Date((Date.now() - 518400000) - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10).replace(/-/g, "/"), //일주일 중 첫번째인 월요일의 날짜
    weekLastDate: new Date((Date.now()) - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10).replace(/-/g, "/"), //일주일 중 마지막인 일요일의 날짜
    workRatio: 0,
    toPrintItems:[],
    attUser:[],
    userList:[],// 프로필 필요해서 유저리스트 담을 변수
    userInfoList: [],// 유저리스트 ID와 attType만 담을 변수
    view : [], //클릭 이벤트 담을 변수
  }),
  computed: {
    
    //현재 표준시간 계산하는 함수
    weekNow: function () {
      var weekNow = new Date();
      weekNow.setHours(9,0,0,0);

      return weekNow;
    },
    //일주전 날짜 반환하는 함수
    weekPre: function () {
      var d = new Date();

      const year = d.getFullYear(); // 년
      const month = d.getMonth();   // 월
      const day = d.getDate();      // 일

      var weekPre = new Date(year, month, day - 7);
      weekPre.setHours(9,0,0,0);

      return weekPre;
    },
    todayTitle: function () {
      const days = ["일", "월", "화", "수", "목", "금", "토"];
      //근태 카드에 입력된 날짜
      const inputedDate = new Date();

      const year = inputedDate.getFullYear();
      const month = inputedDate.getMonth() + 1; //근무날짜의 달
      const date = inputedDate.getDate(); //근무날짜의 일
      const day = days[inputedDate.getDay()]; //근무날짜의 요일

      return year + "년 " + month + "월 " + date + "일 " + day + "요일";
    },
  },
  methods:{
    clickViewSet(idx){
      var views = []
      var clickViews = {clickView : false, noClickView : true}
      for(var count=0; count<this.attUser.length; count++){
        if(count == idx) views.push({clickView : true, noClickView : false})
        else views.push(clickViews)
      }
      this.view = views
    },
    print() {
      const d = new Printd();
      const css = `/* 테이블 전체 디자인 */
                    #print-form {
                      width: 100%;
                      height: 100%;
                      text-align: center;
                      font-size: 10pt;
                    }
                    
                    /* 테이블 헤드의 th 디자인 */
                    #print-form thead th {
                      padding-top: 10px;
                      padding-bottom: 10px;
                    }

                    /* 테이블 바디 여백 */
                    #print-form tbody td {
                      height: 80px;
                    }

                    /* 테이블 테두리 한줄 설정 */
                    #print-form,
                    td,
                    th {
                      border: 1px solid black;
                      border-collapse: collapse;
                    }

                    .sign-img{
                      width:150px;
                      height:50px;
                    }
                    @media print {
                      .print-visible {
                        display: initial;
                      }
                      /* 헤드 첫줄 제목 디자인 */
                      #print-form thead > tr:nth-child(1) {
                        font-size: 24pt;
                      }
                      #print-form thead > tr:nth-child(2),
                      #print-form thead > tr:nth-child(3) {
                        font-size: 12pt;
                      }
                      #print-form tbody tr td:nth-child(2),
                      #print-form tbody tr td:nth-child(4){
                        width:150px;
                      }
                    }
                    /* A4 사이즈 설정 */
                    @page a4sheet {
                      size: 21cm 29.7cm;
                    }
                    .a4 {
                      page: a4sheet;
                      page-break-after: always;
                    }

                    .print-area {
                      display: flex;
                      align-items: center;
                    }`;

      const print_sheet = document.querySelector(".print-area");
      d.print(print_sheet, [css]);
    },
    
    async getAttDataList(){
      this.attUser = [] // 최종 사용될 att데이터
      this.toPrintItems = [] // 프린트용 데이터

      var dateList = [] // 선택한 주간의 모든날짜(7일)
      this.getDateRange(this.weekFirstDate, this.weekLastDate, dateList) // 주간 날짜 가져오기
      var subDateList = [] // 임시로 저장될 매칭된 날짜
      var userDateList = [] // 유저의 attType에 맞게 매칭된 날짜 

      var dayList = ["월", "화", "수", "목", "금", "토", "일"]
      var subList = [] // 유저별로 나누기 위해 임시로 저장할 att데이터
      var attList = [] // 유저별로 나눈 att데이터

      let year = new Date().getFullYear(); // 현재 년도
      let month = new Date().getMonth() + 1;  // 현재 월
      let date = new Date().getDate();  // 현재 날짜
      let todayMs = new Date(year + '/' + month + '/' + date).getTime() // 현재 날짜의 ms
      let startMs = new Date(this.weekFirstDate).getTime()-32400000 // 선택한 주간의 시작날짜 ms
      let endMs = new Date(this.weekLastDate).getTime()-32400000 // 선택한 주간의 끝날짜 ms

      var attState = [] // 상태 데이터 폼
      var attData = [] // 훈련시간 데이터 폼

      //기업에 소속된 선수의 att데이터를 전부 조회하여 유저별로 분별
      await this.$axios
        .get("attendances/api/comAtt/?onTime__range="+this.weekFirstDate+","+this.weekLastDate+"T23:59:59&comID="+this.$store.state.userStore.comID)
        .then((res) => {
          for(var i=0; i<this.userInfoList.length; i++){
            for(var j=0; j<res.data.length; j++){
              if(this.userInfoList[i].id === res.data[j].user.id){
                subList.push(res.data[j])
              }
            }
            attList.push(subList)
            subList = []
          }
        })
        .catch((err) => {
          console.log(err);
          console.log("유저 근무정보 가져오기 실패.");
        });
      //유저별 attType의 요일별로 선택한 주간의 날짜와 매칭
      for(var i=0; i<this.userInfoList.length; i++){ // 유저별로 반복
        for(var a=0; a<this.userInfoList[i].attType.days.length; a++){ // 해당 유저의 attType의 요일수만큼 반복
          for(var b=0; b<dayList.length; b++){ // 일주일 반복
            if(this.userInfoList[i].attType.days[a] === dayList[b]){ // 해당 유저의 attType의 요일과 일주일을 비교하여 선택한 주간의 날짜와 매칭
              subDateList.push({date:dateList[b], day:dayList[b]})
            }
          }
        }
        userDateList.push(subDateList)
        subDateList = []
      }
      //console.log(new Date("2022-04-02").getTime()) 이러면 9시간 빼줘야하고
      //console.log(new Date("2022-4-2").getTime()) 이러면 한국기준 정상시간으로 나옴
      //최종 att데이터 분류
      for(var i=0; i<attList.length; i++){ // 유저수만큼 반복
        var week = 0
        var attTypeOnTime = this.userInfoList[i].attType.onTime
        var attTypeOffTime = this.userInfoList[i].attType.offTime
        var monthWorkTime = this.userInfoList[i].attType.monthWorkTime
        var name = this.userInfoList[i].name
        var userId = this.userInfoList[i].id
        var attTypeId = this.userInfoList[i].attType.id

        if(todayMs >= startMs && todayMs <= endMs){ // 선택한 주간이 이번주
          for(var a=0; a<userDateList[i].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            var count = 0
            if(new Date(userDateList[i][a].date).getTime()-32400000>todayMs){ // 매칭된 날짜가 오늘 날짜보다 미래이면
              attState.push({days:userDateList[i][a].day, stat:9}) // 미래일(회색)
            }
            else if(new Date(userDateList[i][a].date).getTime()-32400000<=todayMs){ // 매칭된 날짜가 오늘 날짜보다 과거이면
              for(var b=0; b<attList[i].length; b++){
                if(attList[i][b].onTime.substr(0,10) === userDateList[i][a].date){ // 해당 유저의 attType에 매칭된 날짜와 훈련기록 날짜 비교해서 같은 날짜가 있으면
                  count = 1
                  if(attList[i][b].onType == true && attList[i][b].offType == true && Number(attList[i][b].workTime) === Number(this.userInfoList[i].attType.monthWorkTime)/this.userInfoList[i].attType.days.length){ // 그 날의 기록이 출퇴근 전부 찍혀있고, 해당 유저의 attType에 따라 훈련시간이 일치하면
                    attState.push({days:userDateList[i][a].day, stat:0}) // 정상퇴근(초록색)
                    attData.push({
                      date: attList[i][b].onTime.substr(0,10),
                      day: attList[i][b].day,
                      startTime: attList[i][b].onTime.substr(11,16),
                      endTime: attList[i][b].offTime.substr(11,16),
                      userId:userId,
                      id: attList[i][b].id,
                      idx: b,
                      mark: "훈련완료",
                      markstat: 0,
                      workTime: attList[i][b].workTime,
                      attTypeId: attTypeId,
                    })
                    week += Number(attList[i][b].workTime)
                    this.toPrintItems.push({
                      idx:b,
                      date:attList[i][b].onTime.substr(0,10)+"("+attList[i][b].day+")",
                      startTime:attList[i][b].onTime.substr(11,5), endTime:attList[i][b].offTime.substr(11,5),
                      schedule: "("+attList[i][b].attType.onTime+":00~"+attList[i][b].attType.offTime+":00"+")"
                    });
                  }
                  else{
                    attState.push({days:userDateList[i][a].day, stat:1}) // 시간미달(주황색)
                    if(attList[i][b].offType == false){ // 퇴근기록도 없는 시간미달
                      attData.push({
                        date: attList[i][b].onTime.substr(0,10),
                        day: attList[i][b].day,
                        startTime: attList[i][b].onTime.substr(11,16),
                        endTime: "기록없음",
                        userId:userId,
                        id: attList[i][b].id,
                        idx: b,
                        mark: "시간미달",
                        markstat: 1,
                        workTime: 0,
                        attTypeId: attTypeId,
                      })
                      this.toPrintItems.push({
                        idx:b,
                        date:attList[i][b].onTime.substr(0,10)+"("+attList[i][b].day+")",
                        startTime:attList[i][b].onTime.substr(11,5), endTime:"",
                        schedule: "("+attList[i][b].attType.onTime+":00~ "+" )"
                      });
                    }
                    else{ // 퇴근기록이 있는 시간미달
                      attData.push({
                        date: attList[i][b].onTime.substr(0,10),
                        day: attList[i][b].day,
                        startTime: attList[i][b].onTime.substr(11,16),
                        endTime: attList[i][b].offTime.substr(11,16),
                        userId:userId,
                        id: attList[i][b].id,
                        idx: b,
                        mark: "시간미달",
                        markstat: 1,
                        workTime: attList[i][b].workTime,
                        attTypeId: attTypeId,
                      })
                      this.toPrintItems.push({
                        idx:b,
                        date:attList[i][b].onTime.substr(0,10)+"("+attList[i][b].day+")",
                        startTime:attList[i][b].onTime.substr(11,5), endTime:attList[i][b].offTime.substr(11,5),
                        schedule: "("+attList[i][b].attType.onTime+":00~"+attList[i][b].attType.offTime+":00"+")"
                      });
                      week += Number(attList[i][b].workTime)
                    }
                  }
                }
              }
              if(count == 0){ // 훈련기록에 같은 날짜가 없으면
                attState.push({days:userDateList[i][a].day, stat:2}) // 미훈련(빨간색)
                attData.push({ // 미훈련시 빈 훈련기록 남기기
                  date: userDateList[i][a].date,
                  day: userDateList[i][a].day,
                  startTime: "기록없음",
                  endTime: "기록없음",
                  userId:userId,
                  id: "",
                  idx: b,
                  mark: "미훈련",
                  markstat: 2,
                  workTime: 0,
                  attTypeId: attTypeId,
                })
              }
            count = 0
            }
          }
        }
        else if(todayMs < startMs){ // 선택한 주간이 미래주
          for(var a=0; a<userDateList[i].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            attState.push({days:userDateList[i][a].day, stat:9}) // 미래일(회색)
          }
        }
        else if(todayMs > endMs){ // 선택한 주간이 과거주
          for(var a=0; a<userDateList[i].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            var count = 0
            for(var b=0; b<attList[i].length; b++){
              if(attList[i][b].onTime.substr(0,10) === userDateList[i][a].date){ // 해당 유저의 attType에 매칭된 날짜와 훈련기록 날짜 비교해서 같은 날짜가 있으면
                count = 1
                if(attList[i][b].onType == true && attList[i][b].offType == true && Number(attList[i][b].workTime) === Number(this.userInfoList[i].attType.monthWorkTime)/this.userInfoList[i].attType.days.length){ // 그 날의 기록이 출퇴근 전부 찍혀있고, 해당 유저의 attType에 따라 훈련시간이 일치하면
                  attState.push({days:userDateList[i][a].day, stat:0}) // 정상퇴근(초록색)
                  attData.push({
                    date: attList[i][b].onTime.substr(0,10),
                    day: attList[i][b].day,
                    startTime: attList[i][b].onTime.substr(11,16),
                    endTime: attList[i][b].offTime.substr(11,16),
                    userId:userId,
                    id: attList[i][b].id,
                    idx: b,
                    mark: "훈련완료",
                    markstat: 0,
                    workTime: attList[i][b].workTime,
                    attTypeId: attTypeId,
                  })
                  this.toPrintItems.push({
                    idx:b,
                    date:attList[i][b].onTime.substr(0,10)+"("+attList[i][b].day+")",
                    startTime:attList[i][b].onTime.substr(11,5), endTime:attList[i][b].offTime.substr(11,5),
                    schedule: "("+attList[i][b].attType.onTime+":00~"+attList[i][b].attType.offTime+":00"+")"
                  });
                  week += Number(attList[i][b].workTime)
                }
                else{
                  attState.push({days:userDateList[i][a].day, stat:1}) // 시간미달(주황색)
                  if(attList[i][b].offType == false){
                    attData.push({
                      date: attList[i][b].onTime.substr(0,10),
                      day: attList[i][b].day,
                      startTime: attList[i][b].onTime.substr(11,16),
                      endTime: "기록없음",
                      userId:userId,
                      id: attList[i][b].id,
                      idx: b,
                      mark: "시간미달",
                      markstat: 1,
                      workTime: 0,
                      attTypeId: attTypeId,
                    })
                    this.toPrintItems.push({
                      idx:b,
                      date:attList[i][b].onTime.substr(0,10)+"("+attList[i][b].day+")",
                      startTime:attList[i][b].onTime.substr(11,5), endTime:"",
                      schedule: "("+attList[i][b].attType.onTime+":00~ "+" )"
                    });
                  }
                  else{
                    attData.push({
                      date: attList[i][b].onTime.substr(0,10),
                      day: attList[i][b].day,
                      startTime: attList[i][b].onTime.substr(11,16),
                      endTime: attList[i][b].offTime.substr(11,16),
                      userId:userId,
                      id: attList[i][b].id,
                      idx: b,
                      mark: "시간미달",
                      markstat: 1,
                      workTime: attList[i][b].workTime,
                      attTypeId: attTypeId,
                    })
                    this.toPrintItems.push({
                      idx:b,
                      date:attList[i][b].onTime.substr(0,10)+"("+attList[i][b].day+")",
                      startTime:attList[i][b].onTime.substr(11,5), endTime:attList[i][b].offTime.substr(11,5),
                      schedule: "("+attList[i][b].attType.onTime+":00~"+attList[i][b].attType.offTime+":00"+")"
                    });
                    week += Number(attList[i][b].workTime)
                  }
                }
              }
            }
            if(count == 0){ // 훈련기록에 같은 날짜가 없으면
              attState.push({days:userDateList[i][a].day, stat:2}) // 미훈련(빨간색)
              attData.push({ // 미훈련시 빈 훈련기록 남기기
                date: userDateList[i][a].date,
                day: userDateList[i][a].day,
                startTime: "기록없음",
                endTime: "기록없음",
                userId:userId,
                id: "",
                idx: b,
                mark: "미훈련",
                markstat: 2,
                workTime: 0,
                attTypeId: attTypeId,
              })
            }
            count = 0
          }
        }
        this.attUser.push({ //최종 데이터 푸쉬
          attState:attState,
          attData:attData,
          attTypeOnTime:attTypeOnTime,
          attTypeOffTime:attTypeOffTime,
          monthWorkTime:monthWorkTime,
          name:name,
          week:week,
          workRatio:(week/monthWorkTime)*100
        })
        attState = []
        attData = []
        week = 0
      }
    },
    async getComUser(){
      this.userInfoList = []
      await this.$axios
      .get("users/api/employee/?comID="+ this.$store.state.userStore.comID)
      .then((res) => {
        this.userList = res.data
        for(var i=0; i< res.data.length; i++){
          this.userInfoList.push({id:res.data[i].id, attType:res.data[i].attType, name:res.data[i].name})
        }
      })
    },
    //두 날짜 사이의 날짜 배열로 가져오기
    getDateRange(startDate, endDate, listDate)
    {
      var dateMove = new Date(startDate);
      var strDate = startDate;
      if (startDate == endDate){
        var strDate = dateMove.toISOString().slice(0,10);
        listDate.push(strDate);
      }
      else{
        while (strDate < endDate)
        {
          var strDate = dateMove.toISOString().slice(0, 10);
          listDate.push(strDate);
          dateMove.setDate(dateMove.getDate() + 1);
        }
      }
      return listDate;
    },
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    async inItWeekDates(){
      await this.getWeekFirstDate();
      await this.getWeekLastDate();
      await this.getAttDataList();
      await this.emitAttList("reset");
    },
    companyUserWorkSettingDialog(state){
      this.$emit('companyUserWorkSettingDialog',state);
    },
    //월요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekFirstDate: function () {
      this.weekFirstDate = this.$refs.weekPicker.getWeekFirstDate();
    },
    //일요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekLastDate: function () {
      this.weekLastDate = this.$refs.weekPicker.getWeekLastDate();
    },
    async emitAttList(val){
      //val값이 reset이면 리스트 데이터 초기화
      await this.$emit("attList",val)
    },
    companyAttendancePrintDialogStateChange(val){
      this.$emit("companyAttendancePrintDialogStateChange", val);
    },
    dialogCoverSet(val){
      this.$emit("dialogCoverSet",val);
    },
    async getComUserList(){
      await this.$emit("getComUserList");
    },
  },
};
</script>

<style scoped>
.container {
  padding: 0 !important;
}

.print-visible {
  display: none;
}

#print-btn{
  width: 135px;
  height: 48px;
  background: #F5F5F5;
  border-radius: 10px;
  font-size: 18px;
  color: #646464;
}

.clickView{
  background: #c6c6c6;
}

.noClickView{
  border: none;
}
</style>