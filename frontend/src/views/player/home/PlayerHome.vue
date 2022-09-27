<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center" cols="4">
        <v-card class="home-card pa-2" rounded="lg">
          <div class="title">
            <v-card-title style="font-weight:1000; padding:8px;">{{myData.name}}님 반갑습니다.</v-card-title>
            <v-card-subtitle class="sub-title my-1">{{transformToDay()}}</v-card-subtitle>
          </div>
          <v-row class="title-display justify-center" style="width:90%;">
            <!--훈련종목 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title ">훈련종목</v-card-title>
              <v-card-text class="text-center">{{myData.sportType}}</v-card-text>
            </v-card>
            <!--훈련선수 명수 표시 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title">소속 기업</v-card-title>
              <v-card-text class="text-center">{{myData.company}}</v-card-text>
            </v-card>
            <!--연계기업 영역-->                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title">소속 복지관</v-card-title>
              <v-card-text class="text-center">{{myData.team}}</v-card-text>
            </v-card>
            <!--추가정보 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title">담당 코치</v-card-title>
              <v-card-text class="text-center">{{myData.coach}}</v-card-text>
            </v-card>
          </v-row>
        </v-card>
      </v-col>
      <!--당월 출퇴근 현황-->
      <v-col class="d-flex justify-center" cols="4">
        <v-card class="home-card pa-2" rounded="lg">
          <div class="title">
            <v-card-title class="mb-11" style="font-weight:1000; padding:8px;">{{nowMonth.substr(5, 2)}}월 출퇴근 현황</v-card-title>
          </div>
          <v-row>
            <v-col cols="12" class="d-flex flex-column">
              <v-date-picker
                v-model="todayDate"
                :picker-date.sync="nowMonth"
                color="primary"
                :day-format="setDayFormat"
                :events="myAttendanceState"
                locale="ko-kr"
                width="auto"
                no-title
                readonly
                style="width: 100%"
              >
              </v-date-picker>
            </v-col>
          </v-row>
          <v-container>
            <v-row>
              <v-col class="d-flex justify-center align-center" cols="6">
                <div class="green-circle ma-2"></div><div class="font-style">: 정상 퇴근</div>
              </v-col>
              <v-col class="d-flex justify-center align-center" cols="6">
                <div class="yellow-circle ma-2"></div><div class="font-style">: 출근중</div>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
      <!--당월 훈련일지 현황-->
      <v-col class="d-flex justify-center" cols="4">
        <v-card class="home-card pa-2" rounded="lg">
          <div class="title">
            <v-card-title class="mb-11" style="font-weight:1000; padding:8px;">{{today.substr(5,2)}}월 훈련일지 현황</v-card-title>
          </div>
          <v-row style="text-align:center; width:100%; overflow-y:auto;">
            <v-col class="pa-0">
              <div style="height:70%;">
              <v-simple-table>
                <thead>
                  <tr>
                    <th style="text-align:-webkit-center;">이름</th>
                    <th style="text-align:-webkit-center;">내용</th>
                    <th style="text-align:-webkit-center;">일시</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="myTraining in myTrainings" :key="myTraining.date">
                    <td>{{myTraining.name}}</td>
                    <td class="d-flex justify-center align-center"><div class="text-over-cut">{{myTraining.contents}}</div></td>
                    <td>{{myTraining.date.substr(5, 5)}}</td>
                  </tr>
                </tbody>
              </v-simple-table>
              </div>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed: {
    //당일 날짜 반환하는 함수
    todayDate: function () {
      var date = new Date();
      var year = date.getFullYear();
      var month = ("0" + (1 + date.getMonth())).slice(-2);
      var day = ("0" + date.getDate()).slice(-2);

      return year + "-" + month + "-" + day;
    },
  },
  methods: {
    transformToDay: function () {
      const days = ["일", "월", "화", "수", "목", "금", "토"];
      //오늘 날짜
      const inputedDate = new Date();
      
      const year = inputedDate.getFullYear();
      const month = inputedDate.getMonth() + 1; //근무날짜의 달
      const date = inputedDate.getDate(); //근무날짜의 일
      const day = days[inputedDate.getDay()]; //근무날짜의 요일

      return year + "년 " + month + "월 " + date + "일 " + day + "요일";
    },

    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },

    // 근태 상태 표현하기
    getState: function (attendance) {
      let start = attendance["startWorkTime"];
      let end = attendance["finishWorkTime"];

      // 해당 date의 출근기록이 있고 퇴근기록 또한 존재하는 경우
      if (start !== undefined && end.length !== 0) {
        return "green";
      }
      // 해당 date의 출근기록이 있고 퇴근기록이 없는 경우
      else if (start !== undefined && end.length == 0) {
        return "yellow";
      }
    },
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
  data: () => ({
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    nowMonth: "",
    todayStartTime:"",
    todayId:"",
    myAttendanceState:{},
    myCoachName: "",
    myData:{
      name:"",
      sportType:"",
      team:"",
      coach:"",
      company:"",
    },
    myTrainings:{},
  }),
  async created(){
    await this.loadingCover(true);
    // 근태 상태를 포함한 내 정보 가져오기
    await this.$axios({
      method: "GET",
      url:
        "/attendances/api/att_user/?id=" + this.$store.state.userStore.id,
    })
    .then((res) => {
      // 있는 데이터만 넣어주기
      if(res.data[0].name){
        this.myData.name =  res.data[0].name
      }
      if(res.data[0].sportType){
        this.myData.sportType = res.data[0].sportType.value
      }
      if(res.data[0].team){
        this.myData.team = res.data[0].team.value
      }
      if(res.data[0].coach>0){
        this.myData.coach = res.data[0].coachName[0].name
      }
      if(res.data[0].company){
        this.myData.company = res.data[0].company.value
      }
      // 내 정보에 근태 상태 추가하기
      for (let j = 0; j < res.data[0]["attendances"].length; j++) {
        let key = res.data[0]["attendances"][j]["startWorkTime"].split(" ")[0];
        let val = this.getState(res.data[0]["attendances"][j]);
        this.myAttendanceState[key] = val;
      }
    })
    .catch((res) => {
      console.log("Failed to get userList", res);
    })
    // 이번달 나의 근무일지 현황 가져오기
    await this.$axios({
      method: "POST",
      url:
        "trainings/get_latest_training/"+this.$store.state.userStore.id+"_"+this.today.substr(0, 7)+"/",
    })
    .then((res) => {
      this.myTrainings = res.data
    })
    .catch((res) => {
      console.log("Failed to get userList", res);
    });
    await this.loadingCover(false);
  },

};
</script>

<style scoped>
.home-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 620px;
  width: 360px;
}

.userdata-card {
  margin: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 110px;
  width: 50%;
}

.content-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 80px;
  width: 100%;
}

.title{
  width: 100%;
  padding: 6px;
  margin-bottom: 20px;
  border-bottom: 1px solid black;
}

.sub-title {
  font-weight: 10px;
}

.card-title{
  padding: 5px;
  font-size:1.1rem;
  font-weight: 600;
}

.text-over-cut {
  display: block;
  width: 110px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 0;
}

.green-circle{
  width : 17px;
  height : 17px;
  border-radius: 50%;
  background-color: green;
}

.yellow-circle{
  width : 17px;
  height : 17px;
  border-radius: 50%;
  background-color: yellow;
}

.font-style{
  font-weight: 1000;
  font-size: 15px;
}
</style>