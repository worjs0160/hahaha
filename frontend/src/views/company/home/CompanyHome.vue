<template>
  <v-container>
    <v-row>
      <!--담당선수 출근 현황 리스트-->
      <v-col class="d-flex justify-center" cols="12" sm="12" md="6">
        <v-card style="width:100%" class="home-card pa-2" rounded="lg">
          <div class="title">
            <v-card-title style="font-weight:1000; padding:8px;">오늘의 출근 현황</v-card-title>
            <v-card-text>{{transformToDay()}}</v-card-text>
          </div>
          <v-row style="text-align:center; width:100%; height:95%;">
            <v-col class="pa-0">
              <v-simple-table>
                <thead>
                  <tr>
                      <th style="text-align:-webkit-center;">이름</th>
                      <th style="text-align:-webkit-center;">근무 시간</th>
                      <th style="text-align:-webkit-center;">출근 상태</th>
                  </tr>
                </thead>
                <tbody v-if="users">
                  <tr v-for="user in users" :key="user.name">
                      <td>{{user.user}}</td>
                      <td v-if="user.startTime===null">-</td>
                      <td v-if="user.startTime">{{user.startTime}} ~ {{user.finishTime}}</td>
                      <td v-if="user.state==1">정상퇴근</td>
                      <td v-if="user.state==-1">미출근</td>
                      <td v-if="user.state==0">출근중</td>
                  </tr>
                </tbody>
              </v-simple-table>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col class="d-flex justify-center" cols="12" sm="12" md="6">
        <v-card style="width:100%" class="home-card pa-2" rounded="lg">
          <training-record
            :writingManagement="writingManagement"
            :unwrittenManagement="unwrittenManagement"
            :completedManagement="completedManagement"
          >
          </training-record>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import TrainingRecord from "/src/views/team/home/TrainingRecord.vue";

export default {
  components: {
    TrainingRecord,
  },
  async created() {
    await this.loadingCover(true);

    //선수들의 근태 현황 가져오기
    await this.$axios({
      method: "POST",
      url:
        "attendances/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.company.id+"_"+ this.today +"/",
    })
      .then((res) => {
        this.users = res.data
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });

    //선수들의 훈련일지 현황 가져오기
    await this.$axios({
      method: "POST",
      url:
        "trainings/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.company.id+"_"+this.today+"/",
    })
      .then((res) => {
        console.log(res.data)
        //훈련일지 상태(작성중, 미작성, 완료)에 따른 선수 분류
        for(var i=0; i < res.data.length; i++){
          if(res.data[i].state=="1"){
            this.completedManagement.push(res.data[i].name)
          }
          else if(res.data[i].state=="0"){
            this.unwrittenManagement.push(res.data[i].name)
          }
          else
            this.writingManagement.push(res.data[i].name)
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });

    await this.loadingCover(false);
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
    //MainLayout으로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    }
  },
  data: () => ({
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    users:{},
    writingManagement:[],
    unwrittenManagement:[],
    completedManagement:[],
  }),
};
</script>

<style>
.home-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 480px;
  width: 360px;
}

.title{
  width: 100%;
  padding: 6px;
  margin-bottom: 20px;
  border-bottom: 1px solid black;
}

</style>