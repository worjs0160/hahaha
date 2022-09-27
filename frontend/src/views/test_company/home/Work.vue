<template>
  <v-container style="width:100%;">
    <v-row justify="space-between" style="position:relative; z-index:2; align-items: center; padding: 12px 24px; margin: 0 !important; border-bottom: 0.5px solid #E1E1E1;">
      <week-num-picker
        v-on:change="inItWeekDates"
        ref="weekPicker"
        class="pre-600"
      ></week-num-picker>
      <div class="pre-600">{{this.todayTitle}}</div>

      <print :formTitle="formTitle" :printData="toPrintItems" class="print-visible"></print>

      <v-btn  id="print-btn" class="pre-400" @click="dialogCoverSet(true), companyWorkPrintDialogStateChange(true), getComUserList()" elevation="0">
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
      <v-chip color="red" text-color="white" class="pre-600 mx-2">미작성</v-chip>
      <v-chip color="#FF6B00" text-color="white" class="pre-600 mx-2">미승인</v-chip>
      <v-chip color="#49ADA9" text-color="white" class="pre-600 mx-2">승인완료</v-chip>
    </v-row>

    <!-- 마우스오버 스크롤 생성 영역 -->
    <div class="scroll-wrap" style="overflow-y:scroll; height: calc(100vh - 360px);">

      <div class="scroll-cover"></div>

      <div class="atten-card" v-for="(item,widx) of workUser" :key="widx" @click="emitWork(item.workData)">
      
      
        <div class="atten-card-inner">
          
          <div class="atten-card-left">
            <div class="atten-imgBox">
              <img :src="userList[widx].profile" alt="">
            </div>
            <p>{{item.name}}</p>
          </div><!--atten-card-left-->

          <div class="atten-card-right">

            <div class="atten-weekBox">
              <!-- <div v-for="attState of item.attState[0]" :key="attState.index" :class="{'now-stat' : attState.now == true, 'default-stat': attState.now == false}"> -->
              <div v-for="attState of item.attState[0]" :key="attState.index" class="default-stat">
                <!-- 훈련 승인 초록색 표시-->
                <v-chip
                  class="week-item"
                  color="#49ADA9"
                  label
                  text-color="white"
                  v-if="attState.stat==0"
                >
                  {{attState.days}}
                </v-chip>

                <!--훈련 승인 보류 / 미승인 주황색 표시-->
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
                <!--작성기록이 없으면 빨간색 표시-->
                <v-chip
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
                  class="week-item"
                  color="grey"
                  label
                  text-color="white"
                  v-if="attState.stat==9"
                >
                  {{attState.days}}
                </v-chip>
              </div>
            </div>

            <div class="atten-timeBox">
              <p>{{item.week}}</p>
              <p>&nbsp;/&nbsp;</p>
              <p>{{item.weekWork}}개</p>
            </div>

            <div class="atten-gage">
              <v-progress-linear
                v-model="item.workRatio"
                height="14"
                style="border-radius: 3px; pointer-events: none;"
                color="primary500"
              >
              </v-progress-linear>
            </div>

          </div><!--e:"atten-card-right-->

        </div><!--e:atten-card-inner-->
        
      </div>
    </div>

  </v-container>
</template>

<script>
import WeekNumPicker from "/src/components/pickers/WeekNumPicker";
import { Printd } from "printd";
import Print from "@/components/forms/WorkPrint";

export default {
  components: {WeekNumPicker,Print,},
  async created() {
    await this.loadingCover(true);
    await this.getComUser();
    await this.inItWeekDates();
    await this.loadingCover(false);
  },
  data: () => ({
    formTitle: ("0" + (1 + new Date().getMonth())).slice(-2) + '월 업무일지',
    formContent: '수영',
    formUser: '담당자명',
    formDate: new Date(new Date().getFullYear(),(1+new Date().getMonth()), 0).getDate(),
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString(), //현재 시간
    weekFirstDate: new Date((Date.now() - 518400000) - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10).replace(/-/g, "/"), //일주일 중 첫번째인 월요일의 날짜
    weekLastDate: new Date((Date.now()) - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10).replace(/-/g, "/"), //일주일 중 마지막인 일요일의 날짜
    workRatio: 0,
    toPrintItems:[],
    workUser:[],
    userList:[], // 프로필 필요해서 유저리스트 담을 변수
    userInfoList:[], // 유저리스트 ID와 attType만 담을 변수
    alarmState: false, // 알림의 바로가기를 통해 접근했을경우 true값을 가져 created에서 api 실행을 막음
    userIdx:0,
  }),
  computed:{
    
    
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
    //현재 표준시간 계산하는 함수
    weekNow: function () {
      var weekNow = new Date();
      weekNow.setHours(9,0,0,0);

      return weekNow;
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
    print() {
      const d = new Printd();
      //console.log(this.toPrintItems)
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
    async getTrainingDataList(){
      this.workUser = [] // 최종 사용될 trainings데이터
      this.toPrintItems = [] // 프린트용 데이터

      var dateList = [] // 선택한 주간의 모든날짜(7일)
      this.getDateRange(this.weekFirstDate, this.weekLastDate, dateList) // 주간 날짜 가져오기
      var subDateList = [] // 임시로 저장될 매칭된 날짜
      var userDateList = [] // 유저의 attType에 맞게 매칭된 날짜 

      var dayList = ["월", "화", "수", "목", "금", "토", "일"]
      var subList = [] // 유저별로 나누기 위해 임시로 저장할 trainings데이터
      var trainingsList = [] // 유저별로 나눈 trainings데이터

      let year = new Date().getFullYear(); // 현재 년도
      let month = new Date().getMonth() + 1;  // 현재 월
      let date = new Date().getDate();  // 현재 날짜
      let todayMs = new Date(year + '/' + month + '/' + date).getTime() // 현재 날짜의 ms
      let startMs = new Date(this.weekFirstDate).getTime()-32400000 // 선택한 주간의 시작날짜 ms
      let endMs = new Date(this.weekLastDate).getTime()-32400000 // 선택한 주간의 끝날짜 ms

      var att = [] // 폼 맞추기위한 배열 껍데기
      var attState = [] // 상태 데이터 폼
      var trainingsData = [] // 훈련일지 데이터 폼
      
      //기업에 소속된 선수의 att데이터를 전부 조회하여 유저별로 분별
      await this.$axios
        .get("trainings/api/CCUserTrainings/?&workDate__range="+this.weekFirstDate+","+this.weekLastDate+"T23:59:59&comID="+this.$store.state.userStore.comID)
        .then((res) => {
          for(var i=0; i<this.userInfoList.length; i++){
            for(var j=0; j<res.data.length; j++){
              if(this.userInfoList[i].id === res.data[j].user){
                subList.push(res.data[j])
              }
            }
            trainingsList.push(subList)
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
      //최종 trainings데이터 분류
      for(i=0; i<trainingsList.length; i++){ // 유저수만큼 반복
        var week = 0 // 일지 작성갯수
        var weekWork = this.userInfoList[i].attType.workDay.length // 총 훈련해야하는 요일수
        var name = this.userInfoList[i].name
        var images = []

        if(todayMs >= startMs && todayMs <= endMs){ // 선택한 주간이 이번주
          for(a=0; a<userDateList[i].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            var count = 0
            if(new Date(userDateList[i][a].date).getTime()-32400000>todayMs){ // 매칭된 날짜가 오늘 날짜보다 미래이면
              att.push({days:userDateList[i][a].day, stat:9, index:a}) // 미래일(회색)
            }
            else if(new Date(userDateList[i][a].date).getTime()-32400000<=todayMs){ // 매칭된 날짜가 오늘 날짜보다 과거이면
              for(b=0; b<trainingsList[i].length; b++){
                if(trainingsList[i][b].workDate.substr(0,10) === userDateList[i][a].date){ // 해당 유저의 attType에 매칭된 날짜와 훈련일지 날짜 비교해서 같은 날짜가 있으면
                  count = 1
                  if(trainingsList[i][b].state == 1){ // 훈련일지 상태가 1번이면 승인완료
                    att.push({days:userDateList[i][a].day, stat:0, index:a}) // 승인완료(초록색)
                    for(var c=0; c<trainingsList[i][b].images.length; c++){
                      images.push(trainingsList[i][b].images[c].images)
                    }
                    trainingsData.push({
                      contents: trainingsList[i][b].contents,
                      date: trainingsList[i][b].workDate.substr(0,10),
                      datetime: trainingsList[i][b].workDate.substr(0,19),
                      day: trainingsList[i][b].day,
                      id: trainingsList[i][b].id,
                      idx: b,
                      images: images,
                      name: name,
                      state: true,
                      stateCode: 1,
                      title: trainingsList[i][b].title,
                      reason: trainingsList[i][b].reason,
                      createdTime: trainingsList[i][b].createdTime,
                      modifiedTime: trainingsList[i][b].modifiedTime,
                      rejectedReason: trainingsList[i][b].rejectedReason,
                      rejectedTime: trainingsList[i][b].rejectedTime,
                    })
                    images = []
                    week++
                    this.toPrintItems.push({
                      idx:b,
                      date:trainingsList[i][b].workDate.substr(2,2)+"/"+String(Number(trainingsList[i][b].workDate.substr(8,2))) +"("+trainingsList[i][b].day+")", 
                      contents:trainingsList[i][b].contents
                    })
                  }
                  else if(trainingsList[i][b].state == 2){
                    att.push({days:userDateList[i][a].day, stat:1, index:a}) // 승인반려(주황색)
                    for(c=0; c<trainingsList[i][b].images.length; c++){
                      images.push(trainingsList[i][b].images[c].images)
                    }
                    trainingsData.push({
                      contents: trainingsList[i][b].contents,
                      date: trainingsList[i][b].workDate.substr(0,10),
                      datetime: trainingsList[i][b].workDate.substr(0,19),
                      day: trainingsList[i][b].day,
                      id: trainingsList[i][b].id,
                      idx: b,
                      images: images,
                      name: name,
                      state: false,
                      stateCode: 2,
                      title: trainingsList[i][b].title,
                      reason: trainingsList[i][b].reason,
                      createdTime: trainingsList[i][b].createdTime,
                      modifiedTime: trainingsList[i][b].modifiedTime,
                      rejectedReason: trainingsList[i][b].rejectedReason,
                      rejectedTime: trainingsList[i][b].rejectedTime,
                    })
                    images = []
                    week++
                    this.toPrintItems.push({
                      idx:b,
                      date:trainingsList[i][b].workDate.substr(2,2)+"/"+String(Number(trainingsList[i][b].workDate.substr(8,2))) +"("+trainingsList[i][b].day+")", 
                      contents:trainingsList[i][b].contents
                    })
                  }
                  else if(trainingsList[i][b].state == 0){
                    att.push({days:userDateList[i][a].day, stat:1, index:a}) // 미승인(주황색)
                    for(c=0; c<trainingsList[i][b].images.length; c++){
                      images.push(trainingsList[i][b].images[c].images)
                    }
                    trainingsData.push({
                      contents: trainingsList[i][b].contents,
                      date: trainingsList[i][b].workDate.substr(0,10),
                      datetime: trainingsList[i][b].workDate.substr(0,19),
                      day: trainingsList[i][b].day,
                      id: trainingsList[i][b].id,
                      idx: b,
                      images: images,
                      name: name,
                      state: false,
                      stateCode: 0,
                      title: trainingsList[i][b].title,
                      reason: trainingsList[i][b].reason,
                      createdTime: trainingsList[i][b].createdTime,
                      modifiedTime: trainingsList[i][b].modifiedTime,
                      rejectedReason: trainingsList[i][b].rejectedReason,
                      rejectedTime: trainingsList[i][b].rejectedTime,
                    })
                    images = []
                    week++
                    this.toPrintItems.push({
                      idx:b,
                      date:trainingsList[i][b].workDate.substr(2,2)+"/"+String(Number(trainingsList[i][b].workDate.substr(8,2))) +"("+trainingsList[i][b].day+")", 
                      contents:trainingsList[i][b].contents
                    })
                  }
                }
              }
              if(count == 0){ // 훈련기록에 같은 날짜가 없으면
                att.push({days:userDateList[i][a].day, stat:2, index:a}) // 미작성(빨간색)
                trainingsData.push({ // 미작성 훈련기록은 빈 데이터로 넣어주기
                  contents: "미작성",
                  date: userDateList[i][a].date,
                  datetime: userDateList[i][a].date + "T" + this.userInfoList[i].attType.offTime,
                  day: userDateList[i][a].day,
                  id: "",
                  idx: b,
                  images: "",
                  name: name,
                  state: true,
                  stateCode: 3,
                  title: userDateList[i][a].date + " " + name + " 훈련일지",
                  createdTime: "",
                  modifiedTime: "",
                  rejectedReason: "",
                  rejectedTime: "",
                })
              }
            }
            count = 0
          }
        }
        else if(todayMs < startMs){ // 선택한 주간이 미래주
          for(a=0; a<userDateList[i].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            att.push({days:userDateList[i][a].day, stat:9, index:a}) // 미래일(회색)
          }
        }
        else if(todayMs > endMs){ // 선택한 주간이 과거주
          for(a=0; a<userDateList[i].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            count = 0
            for(b=0; b<trainingsList[i].length; b++){
              if(trainingsList[i][b].workDate.substr(0,10) === userDateList[i][a].date){ // 해당 유저의 attType에 매칭된 날짜와 훈련일지 날짜 비교해서 같은 날짜가 있으면
                count = 1
                if(trainingsList[i][b].state == 1){ // 훈련일지 상태가 1번이면
                  att.push({days:userDateList[i][a].day, stat:0, index:a}) // 승인완료(초록색)
                    for(c=0; c<trainingsList[i][b].images.length; c++){
                      images.push(trainingsList[i][b].images[c].images)
                    }
                    trainingsData.push({
                      contents: trainingsList[i][b].contents,
                      date: trainingsList[i][b].workDate.substr(0,10),
                      datetime: trainingsList[i][b].workDate.substr(0,19),
                      day: trainingsList[i][b].day,
                      id: trainingsList[i][b].id,
                      idx: b,
                      images: images,
                      name: name,
                      state: true,
                      stateCode: 1,
                      title: trainingsList[i][b].title,
                      reason: trainingsList[i][b].reason,
                      createdTime: trainingsList[i][b].createdTime,
                      modifiedTime: trainingsList[i][b].modifiedTime,
                      rejectedReason: trainingsList[i][b].rejectedReason,
                      rejectedTime: trainingsList[i][b].rejectedTime,
                    })
                    images = []
                    week++
                }
                else if(trainingsList[i][b].state == 2){
                  att.push({days:userDateList[i][a].day, stat:1, index:a}) // 승인반려(주황색)
                  for(c=0; c<trainingsList[i][b].images.length; c++){
                    images.push(trainingsList[i][b].images[c].images)
                  }
                  trainingsData.push({
                    contents: trainingsList[i][b].contents,
                    date: trainingsList[i][b].workDate.substr(0,10),
                    datetime: trainingsList[i][b].workDate.substr(0,19),
                    day: trainingsList[i][b].day,
                    id: trainingsList[i][b].id,
                    idx: b,
                    images: images,
                    name: name,
                    state: false,
                    stateCode: 2,
                    title: trainingsList[i][b].title,
                    reason: trainingsList[i][b].reason,
                    createdTime: trainingsList[i][b].createdTime,
                    modifiedTime: trainingsList[i][b].modifiedTime,
                    rejectedReason: trainingsList[i][b].rejectedReason,
                    rejectedTime: trainingsList[i][b].rejectedTime,
                  })
                  images = []
                  week++
                }
                else if(trainingsList[i][b].state == 0){
                  att.push({days:userDateList[i][a].day, stat:1, index:a}) // 미승인(주황색)
                  for(c=0; c<trainingsList[i][b].images.length; c++){
                    images.push(trainingsList[i][b].images[c].images)
                  }
                  trainingsData.push({
                    contents: trainingsList[i][b].contents,
                    date: trainingsList[i][b].workDate.substr(0,10),
                    datetime: trainingsList[i][b].workDate.substr(0,19),
                    day: trainingsList[i][b].day,
                    id: trainingsList[i][b].id,
                    idx: b,
                    images: images,
                    name: name,
                    state: false,
                    stateCode: 0,
                    title: trainingsList[i][b].title,
                    reason: trainingsList[i][b].reason,
                    createdTime: trainingsList[i][b].createdTime,
                    modifiedTime: trainingsList[i][b].modifiedTime,
                    rejectedReason: trainingsList[i][b].rejectedReason,
                    rejectedTime: trainingsList[i][b].rejectedTime,
                  })
                  images = []
                  week++
                }
              }
            }
            if(count == 0){ // 훈련기록에 같은 날짜가 없으면
              att.push({days:userDateList[i][a].day, stat:2, index:a}) // 미작성(빨간색)
              trainingsData.push({ // 미작성 훈련기록은 빈 데이터로 넣어주기
                contents: "미작성",
                date: userDateList[i][a].date,
                datetime: userDateList[i][a].date + "T" + this.userInfoList[i].attType.offTime,
                day: userDateList[i][a].day,
                id: "",
                idx: b,
                images: "",
                name: name,
                state: true,
                stateCode: 3,
                title: userDateList[i][a].date + " " + name + " 훈련일지",
                createdTime: "",
                modifiedTime: "",
                rejectedReason: "",
                rejectedTime: "",
              })
            }
            count = 0
          }
        }
        attState.push(att)
        att = []
        
        this.workUser.push({ //최종 데이터 푸쉬
          attState:attState,
          name:name,
          week:week,
          weekWork:weekWork,
          workData:trainingsData,
          workRatio:(week/weekWork)*100
        })
        attState = []
        trainingsData = []
        week = 0
      }
      if(this.alarmState == true){
        await this.emitWork(this.workUser[this.userIdx].workData);
        this.alarmState = false
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
        strDate = dateMove.toISOString().slice(0,10);
        listDate.push(strDate);
      }
      else{
        while (strDate < endDate)
        {
          strDate = dateMove.toISOString().slice(0, 10);
          listDate.push(strDate);
          dateMove.setDate(dateMove.getDate() + 1);
        }
      }
      return listDate;
    },
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    inItWeekDates() {
      this.getWeekFirstDate();
      this.getWeekLastDate();
      this.getTrainingDataList();
      this.emitWork("reset");
    },
    //월요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekFirstDate: function () {
      this.weekFirstDate = this.$refs.weekPicker.getWeekFirstDate();
    },
    //일요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekLastDate: function () {
      this.weekLastDate = this.$refs.weekPicker.getWeekLastDate();
    },
    async emitWork(val){
      await this.$emit("workList",val)
    },
    companyWorkPrintDialogStateChange(val){
      this.$emit("companyWorkPrintDialogStateChange", val);
    },
    dialogCoverSet(val){
      this.$emit("dialogCoverSet",val);
    },
    async getComUserList(){
      await this.$emit("getComUserList");
    },

    // 기업 훈련일지 알림에서 바로가기 클릭시 실행
    async alarmChangeView(date, userIdx){
      this.userIdx = await userIdx
      this.alarmState = true
      this.workUser = []
      await this.$refs.weekPicker.alarmDate(date);
      await this.getTrainingDataList();
    },
  }
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
</style>