<!-- 근로자 근무관리 페이지 -->
<template>
  <v-container style="padding:0;" class="paddingtop30">

    <div class="user-atten-wrap mb-10">

      <div class="topBox main-box-wrap" style="margin-bottom:30px;">
        <h2 class="pre-400">주간 훈련시간</h2>
        <div class="timeBox">
          <h3><span>{{maxWeekTime}}</span> 시간중</h3>
          <p><span>{{weekWorkTime}}</span> 시간 훈련을 마쳤습니다.</p>
        </div>

        <div class="dayBox">
          <p class="pre-400">
            내 훈련일
          </p>
          <span class="pre-400" v-for = "(item, idx) in days" :key="idx">{{item}}</span>
        </div>

        <div class="gageWrap">
          <div class="gageText">
            <strong v-if="!Math.ceil(ratio(1))">0%</strong>
            <strong v-if="Math.ceil(ratio(1))===Infinity">0%</strong>
            <strong v-if="Math.ceil(ratio(1))">{{ Math.ceil(ratio(1)) }}%</strong>
          </div>
          <div class="gageBox">
            <v-progress-linear
              v-model="workRatio"
              style="pointer-events: none;"
              color="testgage"
            >
            </v-progress-linear>
          </div>
        </div>

      </div>

        <!-- 유급휴가 부분 -->
        <!-- <v-col cols="5" class="pa-1">
          <v-row>
            <v-col>
              <v-card-text class="px-1 pt-1 pb-0" style="font-weight:1000;">유급휴가</v-card-text>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-card-text class="text-h6 px-1 py-0">{{vacation}}일</v-card-text>
            </v-col>
          </v-row>
          <v-progress-linear
            v-model="remainRatio"
            height="20"
            class="mb-3"
            style="pointer-events: none;"
          >
            <strong>{{ Math.ceil(ratio(2)) }}%</strong>
          </v-progress-linear>
        </v-col> -->

        <div class="btmBox main-box-wrap">

          <div class="header">
            <week-num-picker
              v-on:change="inItWeekDates"
              ref="weekPicker"
              class="mb-2"
            ></week-num-picker>
          </div>

          <div class="atten-dropBox">
            <!-- 근무리스트 -->
            <v-expansion-panels>
              <v-expansion-panel v-for = "(item, idx) in attData" :key="idx">
                
                <!-- 한줄 내용  -->
                <div style="padding: 16px 24px;">
                      <div >
                        <h2 style="    font-size: 20px;
                                      color: #2e2e2e;
                                      font-family: 'Pretendard-Regular';
                                      font-weight: 400;
                                      margin-bottom: 20px;
                                  ">{{titleCreate(item)}}</h2>
                      </div>
                  <div class="dropTopBox" style="display: flex;">

                    <div class="noClickBox">
                      <div class="mark2" >
                        <span style="background: #61C0BD;" v-if="workType[idx]=='훈련완료'">훈련완료</span>
                        <span style="background: #FF9900;" v-if="workType[idx]=='시간미달'">시간미달</span>
                        <span style="background: #b4b4b4;" v-if="workType[idx]=='훈련중'">훈련중</span>
                        <span style="background: #ff0000;" v-if="workType[idx]=='미훈련'">미훈련</span>
                        <span style="background: #e0e0e0;" v-if="workType[idx]=='훈련예정'">훈련예정</span>
                      </div>
                      <p class="time">{{timeCreate(item, workType[idx])}}</p>

                      <div class="mark2Box" style="margin-right:60px;">
                        <span style="background: #61C0BD;" v-if="workType[idx]=='훈련완료'">{{workTime[idx]}}H</span>
                        <span style="background: #FF9900;" v-if="workType[idx]=='시간미달'">{{workTime[idx]}}H</span>
                        <span style="background: #b4b4b4;" v-if="workType[idx]=='훈련중'">0H</span>
                        <span style="background: #ff0000;" v-if="workType[idx]=='미훈련'">0H</span>
                        <span style="background: #e0e0e0;" v-if="workType[idx]=='훈련예정'">0H</span>
                      </div>
                      
                        
                      <div class="dropBtmBox" style="display:block; padding: 0px;">
                        <div class="rightBox">

                          <div style="
                          width: 722px;
                          height: 20px;
                          display: flex;
                          align-items: center;
                          background-color:#EFF9F8;
                          border-radius: 5px;
                          " class="px-1 justify-center">
                            <div style="width:0.5px; height:100%;" v-for="(minute, i) in workTimeMinute[idx]" :key="i">
                              <div style="width:0.4px; height:100%;" v-if="i==0"></div>
                              <div style="width:0.5px; height:100%; background-color:#61C0BD;" v-if="minute==1 && i%60!=0"></div>
                              <!-- <div style="width:0.5px; height:100%; background-color:rgb(179 220 243)" v-if="minute==0 && i%60!=0"></div> -->
                              <div style="width:0.4px; height:100%;" v-if="minute==1 && (i%60)==0 && i!=0"></div>
                              <div style="width:0.4px; height:100%;" v-if="minute==0 && (i%60)==0 && i!=0"></div>
                            </div>
                          </div>

                          <div class="timeBox" style="width:60px; float:left;" v-for="i in 13" :key="i">
                            <p class="time">{{timeList[i-1]}}</p>
                          </div>
                        </div>

                      </div>



                    </div>
                    
                  </div>
                  
                </div>
                <div style="    padding: 0 24px 16px;
                                flex: 1 1 auto;
                                max-width: 100%;">
                </div>

              </v-expansion-panel>
              <v-expansion-panel v-if = "attData.length == 0">

                <!-- 한줄 클릭하면 아래에 확장되어 보여지는 부분 -->
                
                <!-- 한줄 내용  -->
                <div class="pre-400" style="padding: 16px 24px; text-align: center; font-size:18px;">
                  훈련 정보가 없습니다. 
                </div>
                <!-- 한줄 클릭하면 아래에 확장되어 보여지는 부분 -->

              </v-expansion-panel>
            </v-expansion-panels>
          </div>

        </div>

    </div>

  </v-container>
</template>

<script>
import WeekNumPicker from "/src/components/pickers/WeekNumPicker";

export default {
  components: {WeekNumPicker,},
  methods:{
    //주간 선택 함수
    inItWeekDates: function () {
      this.getWeekFirstDate();
      this.getWeekLastDate();
      this.getAttData();
    },
    //월요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekFirstDate: function () {
      this.weekFirstDate = this.$refs.weekPicker.getWeekFirstDate();
    },
    //일요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekLastDate: function () {
      this.weekLastDate = this.$refs.weekPicker.getWeekLastDate();
    },
    ratio: function (type) {
      if (type==1){ // 근무량
        this.workRatio = (this.weekWorkTime/this.maxWeekTime)*100
        return ((this.weekWorkTime/this.maxWeekTime)*100)
      }
      else if(type==2){ //휴가 사용량
        this.remainRatio = (this.useVacation/this.vacation)*100
        return ((this.useVacation/this.vacation)*100)
      }
    },

    //자신의 훈련유형 가져오기
    async getMyAttType(){
      var time
      //근무유형 정리
      await this.$axios({
        method: "GET",
        url:"attendances/api/userAttType/"+this.$store.state.userStore.id
      })
      .then((res)=>{
        time = Number(res.data.attType.offTime.substr(0,2)) - Number(res.data.attType.onTime.substr(0,2))
        //주간 예상 근무시간 계산
        if(res.data){
          this.myAttType = res.data.attType
          this.days = res.data.days
          this.todayTime = time
          this.maxWeekTime = time * res.data.days.length
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    //자신의 근무데이터 가져오기
    async getAttData(){
      //자신의 근무시간 계산
      await this.$axios({
        method: "GET",
        url:"attendances/api/empAtt/?user_id="+this.$store.state.userStore.id+"&onTime__range="+this.weekFirstDate+","+this.weekLastDate+"T23:59:59"
      })
      .then((res)=>{
        let year = new Date().getFullYear(); // 현재 년도
        let month = new Date().getMonth() + 1;  // 현재 월
        let date = new Date().getDate();  // 현재 날짜
        let todayMs = new Date(year + '/' + month + '/' + date).getTime() // 현재 날짜의 ms
        let startMs = new Date(this.weekFirstDate).getTime()-32400000 // 선택한 주간의 시작날짜 ms
        let endMs = new Date(this.weekLastDate).getTime()-32400000 // 선택한 주간의 끝날짜 ms

        var dateList = [] // 선택한 주간의 모든날짜(7일)
        var dayList = ["월", "화", "수", "목", "금", "토", "일"]
        this.getDateRange(this.weekFirstDate, this.weekLastDate, dateList) // 주간 날짜 가져오기
        this.attData = []
        var userDateList = [] // 유저의 attType에 맞게 매칭된 날짜 
        var time = Number(this.myAttType.offTime.substr(0,2)) - Number(this.myAttType.onTime.substr(0,2))

        //총 주간 근무시간 계산
        this.weekWorkTime = 0;
        this.workTime=[];
        this.workType=[];
        this.workTimeMinute = [];

        for(var a=0; a<this.days.length; a++){ // 해당 유저의 attType의 요일수만큼 반복
          for(var b=0; b<dayList.length; b++){ // 일주일 반복
            if(this.days[a] === dayList[b]){ // 해당 유저의 attType의 요일과 일주일을 비교하여 선택한 주간의 날짜와 매칭
              userDateList.push({date:dateList[b], day:dayList[b]})
            }
          }
        }

        if(todayMs >= startMs && todayMs <= endMs){ // 선택한 주간이 이번주
          for(a=0; a<userDateList.length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            var check = 0
            if(new Date(userDateList[a].date).getTime()-32400000>todayMs){ // 매칭된 날짜가 오늘 날짜보다 미래이면
              this.attData.push({
                attType:this.myAttType,
                day:userDateList[a].day,
                onTime:userDateList[a].date.substr(0,10),
                onType:false,
                offTime:"",
                offType:false,
              })
              this.workType.push("훈련예정")
            }
            else if(new Date(userDateList[a].date).getTime()-32400000<=todayMs){ // 매칭된 날짜가 오늘 날짜보다 과거이면
              for(var count=0; res.data[count]; count++){
                if(res.data[count].onTime.substr(0,10) === userDateList[a].date){ // 훈련시간 기록날짜가 훈련유형의 날짜와 같을때
                  check = 1
                  if(res.data[count].onType == true && res.data[count].offType == true){ //출퇴근 둘 다 찍혔을 때
                    if(time <= res.data[count].workTime){//근무 유형의 하루 근무량보다 오늘 근무량이 클 경우 인정되는 시간은 근무 유형대로
                      this.attData.push(res.data[count]);
                      this.workType.push("훈련완료")
                      this.workTime.push(res.data[count].workTime);
                      this.weekWorkTime += parseInt(res.data[count].workTime);//이번주 총 근무시간에 근무유형의 하루 근무량 만큼만 더해주기
                      this.timeSet(true, res.data[count].onTime.substr(11,5), res.data[count].offTime.substr(11,5))//출퇴근 시간 게이지바 그리기
                    }
                    else if(time > res.data[count].workTime){//근무유형 근무량보다 오늘 근무량이 적을 경우 미달처리
                      this.attData.push(res.data[count]);
                      this.workType.push("시간미달")
                      this.workTime.push(res.data[count].workTime)
                      this.weekWorkTime += parseInt(res.data[count].workTime);//미달일 경우 그 시간만큼만 이번주 총 근무시간에 더해주기
                      this.timeSet(true, res.data[count].onTime.substr(11,5), res.data[count].offTime.substr(11,5))//출퇴근 시간 게이지바 그리기
                    }
                  }
                  else if(res.data[count].onType == true && res.data[count].offType == false){ //출근만 찍혔을 때
                    this.attData.push(res.data[count]);
                    this.workType.push("훈련중")
                    this.workTime.push("체크중")//실제 화면에는 표시되지 않으나 workType과 workTime의 배열 자릿수 맞추기 위해서 데이터 삽입
                    this.timeSet(false, res.data[count].onTime, res.data[count].offTime)
                  }
                }
              }
              if(check == 0){
                this.attData.push({
                  attType:this.myAttType,
                  day:userDateList[a].day,
                  onTime:userDateList[a].date.substr(0,10),
                  onType:false,
                  offTime:"",
                  offType:false,
                })
                this.workType.push("미훈련")
                this.timeSet(false, 0, 0)
              }
              check = 0
            }
          }
        }
        else if(todayMs < startMs){ // 선택한 주간이 미래주
          for(a=0; a<userDateList[a].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            this.attData = [] // 미래일
          }
        }
        else if(todayMs > endMs){ // 선택한 주간이 과거주
          for(a=0; a<userDateList.length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            check = 0
            for(count=0; res.data[count]; count++){
              if(res.data[count].onTime.substr(0,10) === userDateList[a].date){ // 훈련시간 기록날짜가 훈련유형의 날짜와 같을때
                check = 1
                if(res.data[count].onType == true && res.data[count].offType == true){ //출퇴근 둘 다 찍혔을 때
                  if(time <= res.data[count].workTime){//근무 유형의 하루 근무량보다 오늘 근무량이 클 경우 인정되는 시간은 근무 유형대로
                    this.attData.push(res.data[count]);
                    this.workType.push("훈련완료")
                    this.workTime.push(res.data[count].workTime);
                    this.weekWorkTime += parseInt(res.data[count].workTime);//이번주 총 근무시간에 근무유형의 하루 근무량 만큼만 더해주기
                    this.timeSet(true, res.data[count].onTime.substr(11,5), res.data[count].offTime.substr(11,5))//출퇴근 시간 게이지바 그리기
                  }
                  else if(time > res.data[count].workTime){//근무유형 근무량보다 오늘 근무량이 적을 경우 미달처리
                    this.attData.push(res.data[count]);
                    this.workType.push("시간미달")
                    this.workTime.push(res.data[count].workTime)
                    this.weekWorkTime += parseInt(res.data[count].workTime);//미달일 경우 그 시간만큼만 이번주 총 근무시간에 더해주기
                    this.timeSet(true, res.data[count].onTime.substr(11,5), res.data[count].offTime.substr(11,5))//출퇴근 시간 게이지바 그리기
                  }
                }
                else if(res.data[count].onType == true && res.data[count].offType == false){ //출근만 찍혔을 때
                  this.attData.push(res.data[count]);
                  this.workType.push("훈련중")
                  this.workTime.push("0")//실제 화면에는 표시되지 않으나 workType과 workTime의 배열 자릿수 맞추기 위해서 데이터 삽입
                  this.timeSet(false, res.data[count].onTime, res.data[count].offTime)
                }
              }
            }
            if(check == 0){
              this.attData.push({
                attType:this.myAttType,
                day:userDateList[a].day,
                onTime:userDateList[a].date.substr(0,10),
                onType:false,
                offTime:"",
                offType:false,
              })
              this.workType.push("미훈련")
              this.timeSet(false, 0, 0)
            }
            check = 0
          }
        }
      })
      .catch((err)=>{
        console.log(err)
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

    //n월 n일 또는 미출근 표시 해주는 함수
    titleCreate(val){
      if(val.onTime){
        return val.onTime.substr(5,2) + "월" + val.onTime.substr(8,2) + "일 (" + val.day + ")";
      }
      else if(!val.onTime){
        return "미출근"
      }
    },
    
    //출퇴근 시간 표시해주는 함수
    timeCreate(val, workType){
      if(val.onType == true && val.offType == true){
        return val.onTime.substr(11,5) + " ~ " + val.offTime.substr(11,5);
      }
      else if(val.onType == true && val.offType == false){
        return val.onTime.substr(11,5) + " ~ 기록없음";
      }
      else if(val.onType == false && val.offType == false && workType == "미훈련"){
        return "미훈련";
      }
      else if(val.onType == false && val.offType == false && workType == "훈련예정"){
        return "훈련예정";
      }
    },
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    timeSet(state, start, end){ // 출퇴근 시간을 분단위로 배열값 만듦(24시 = 1440분)
      var arrStart = 0
      var arrEnd = 0
      var nowArr = []
      
      if(state == true){
        for(var count=0; count<24; count++){
          if(parseInt(start.substr(0,2)) == count){
            arrStart = 60*count
            arrStart += parseInt(start.substr(3,2))
          }
        }
        for(count=0; count<24; count++){
          if(parseInt(end.substr(0,2)) == count){
            arrEnd = 60*count
            arrEnd += parseInt(end.substr(3,2))
          }
        }

        for(var i=0; i<1440; i++){
          nowArr[i]=0
        }

        for(var j=arrStart; j<=arrEnd; j++){
          nowArr[j]=1
        }

        this.workTimeMinute.push(nowArr)
      }
      else if(state == false){
        for(i=0; i<1440; i++){
          nowArr[i]=0
        }
        this.workTimeMinute.push(nowArr)
      }
    },
  },
  async created() {
    await this.loadingCover(true);
    await this.getMyAttType();
    await this.getAttData();
    await this.loadingCover(false);
  },
  data: () => ({
    weekFirstDate: "", //일주일 중 첫번째인 월요일의 날짜
    weekLastDate: "", //일주일 중 마지막인 일요일의 날짜
    myAttType: [],
    attData:[],
    weekWorkTime:0, //이번주 근무한 시간
    workRatio:0, // 이번주 근무한 시간 비율
    todayTime:0, //하루 근무시간
    maxWeekTime:0,//이번주 총 예상 근무시간
    workTime:[],//근무시간(시간 초과시 근무유형만큼만 인정하기 위해서 필요)
    workState:[],//근무상태(훈련완료, 훈련중...)
    days:[],
    vacation:1,
    useVacation:0,
    remainRatio:0,
    time:10,
    timeList:[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],//progress 시간표시
    workTimeMinute:[]
  }),
};
</script>

<style>
  .full-height{
    height : 100%;
  }
  .full-width{
    width : 100%;
  }
  .green-circle{
    width : 7px;
    height : 7px;
    border-radius: 50%;
    background-color: green;
  }
  .user-atten-wrap .topBox {
    padding: 24px 24px 35px;
  }
  .user-atten-wrap .topBox h2 {
    font-size: 22px;
    color: #2e2e2e;
    margin: 0;
    margin-bottom: 10px;
  }
  .user-atten-wrap .topBox .timeBox h3,
  .user-atten-wrap .topBox .timeBox p {
    margin: 0;
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    font-weight: 500;
  }
  .user-atten-wrap .topBox .timeBox h3 span,
  .user-atten-wrap .topBox .timeBox p span {
    color: #008BD6;
  }
  .user-atten-wrap .topBox .timeBox h3 {
    margin-right: 10px;
  }
  .user-atten-wrap .topBox .timeBox {
    display: flex;
    align-items: center;
  }
  .user-atten-wrap .topBox .dayBox {
    display: flex;
    align-items: center;
    margin: 15px 0;
  }
  .user-atten-wrap .topBox .dayBox p {
    font-size: 16px;
    color: #646464;
    margin: 0;
    margin-right: 10px;
  }
  .user-atten-wrap .topBox .dayBox span {
    width: 24px;
    height: 24px;
    background: #E4F2F9;
    border-radius: 4px;
    color: #008BD6;
    font-size: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 4px;
  }
  .user-atten-wrap .topBox .gageWrap {
    position: relative;
    margin-top: -30px;
  }
  .user-atten-wrap .topBox .gageWrap .gageBox {
    width: 100%;
    height: 24px;
    border-radius: 6px;
    overflow: hidden;
  }
  .user-atten-wrap .topBox .gageWrap .gageBox div {
    height: 24px !important;
  }
  .user-atten-wrap .topBox .gageWrap .gageBox .testgage {
    background: #008BD6;
  }
  .user-atten-wrap .topBox .gageWrap .gageText {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    font-size: 22px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    margin-bottom: 5px;
  }
  .user-atten-wrap .btmBox {
    overflow: hidden;
  }
  .user-atten-wrap .btmBox .header {
    height: 72px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    font-size: 20px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    padding-left: 15px;
  }
  .user-atten-wrap .btmBox .header div {
    margin: 0 !important;
  }
  .atten-dropBox {}
  .atten-dropBox .dropTopBox h2 {
    font-size: 20px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    font-weight: 400;
    margin-bottom: 20px;
  }
  .atten-dropBox .dropTopBox .noClickBox {
    display: flex;
    align-items: center;
  }
  .atten-dropBox .dropTopBox .noClickBox p {
    margin: 0;
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    margin-left: 20px;
    width: 120px;
  }
  .atten-dropBox .dropTopBox .noClickBox .mark2 span {
    padding: 0 10px;
    width: 65px;
    height: 22px;
    border-radius: 11.5px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 13px;
    color: #fff;
    font-family: 'Pretendard-Regular';
  }
  .atten-dropBox .dropTopBox .noClickBox .mark2Box span {
    font-size: 13px;
    color: #fff;
    font-family: 'Pretendard-Regular';
    width: 28px;
    height: 28px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 4px;
  }
  .atten-dropBox .dropBtmBox {
    display: flex;
    align-items: center;
    padding: 20px 0;
  }
  .atten-dropBox .dropBtmBox .leftBox {
    width: 97px;
  }
  .atten-dropBox .dropBtmBox h2 {
    margin: 0;
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    margin-bottom: 15px;
  }
  .atten-dropBox .dropBtmBox .mark2Box span {
      width: 69px;
      height: 22px;
      border-radius: 11.5px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 13px;
      color: #fff;
      font-family: 'Pretendard-Regular';
  }
  .atten-dropBox .dropBtmBox .rightBox {
    width: 100%;
  }
  .atten-dropBox .dropBtmBox .rightBox .gageBox {
    border-radius: 3px !important;
    overflow: hidden;
  }
  .atten-dropBox .dropBtmBox .rightBox .gageBox div {
    width: 100%;
    height: 14px !important;
  }
  .atten-dropBox .dropBtmBox .rightBox .dropBtmGage {
    background: #61C0BD;
  }
  .atten-dropBox .dropBtmBox .rightBox .timeBox {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .atten-dropBox .dropBtmBox .rightBox .timeBox p {
    font-size: 12px;
    color: #989898;
    font-family: 'Pretendard-Regular';
    margin: 0;
    margin-top: 8px;
  }
</style>