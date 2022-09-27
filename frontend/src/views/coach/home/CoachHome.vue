<template>
  <v-container>
    <v-row>
      <!--담당선수 출근 현황 리스트-->
      <v-col class="d-flex justify-center" cols="12" sm="12" md="4">
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
      <!--담당선수 일지 현황 리스트-->
      <v-col class="d-flex justify-center" cols="12" sm="12" md="4">
        <v-card style="width:100%" class="home-card pa-2" rounded="lg">
          <div class="title">
            <v-card-title style="font-weight:1000; padding:8px;">오늘의 일지 현황</v-card-title>
            <v-card-text>{{transformToDay()}}</v-card-text>
          </div>
          <v-row style="text-align:center; width:100%; height:95%;">
            <v-col class="pa-0">
              <v-simple-table>
                <thead>
                  <tr>
                      <th style="text-align:-webkit-center;">이름</th>
                      <th style="text-align:-webkit-center;">일지 내용</th>
                      <th style="text-align:-webkit-center;">작성 상태</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="training in trainings" :key="training.name">
                      <td>{{training.name}}</td>
                      <td v-if="training.state==1"><div class="text-over-cut">{{training.contents}}</div></td>
                      <td v-if="training.state==-1">-</td>
                      <td v-if="training.state==0">-</td>
                      <td v-if="training.state==1">작성완료</td>
                      <td v-if="training.state==-1">작성중</td>
                      <td v-if="training.state==0">미작성</td>
                  </tr>
                </tbody>
              </v-simple-table>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <!--담당선수 대회 일정 리스트-->
      <v-col class="d-flex justify-center" cols="12" sm="12" md="4">
        <v-card style="width:100%" class="home-card pa-2" rounded="lg">
          <div class="title">
            <v-card-title style="font-weight:1000; padding:8px;">담당선수 대회 일정</v-card-title>
            <v-card-text>{{transformToDay()}}</v-card-text>
          </div>
          <v-row style="text-align:center; width:100%; height:95%;">
            <v-col class="pa-0">
              <v-simple-table>
                <thead>
                  <tr>
                      <th style="text-align:-webkit-center;">이름</th>
                      <th style="text-align:-webkit-center;">대회명</th>
                      <th style="text-align:-webkit-center;">일시</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="training in trainings" :key="training.name">
                      <td>{{training.name}}</td>
                      <td><div class="text-over-cut">제네시스 인비테이셔널</div></td>
                      <td>{{today}}</td>
                  </tr>
                </tbody>
              </v-simple-table>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    //선수들의 근태 현황 가져오기
    await this.$axios({
      method: "POST",
      url:
        "attendances/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.id+"_"+ this.today +"/",
    })
      .then((res) => {
        this.users = res.data
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });
    //선수들의 근무일지 현황 가져오기
    await this.$axios({
      method: "POST",
      url:
        "trainings/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.id+"_"+ this.today +"/",
    })
      .then((res) => {
        this.trainings = res.data
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
    trainings:{},
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

.text-over-cut {
  display: block;
  width: 110px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 0;
}
</style>