<template>
  <!-- 오늘의 근무 리스트 시작 -->
  <v-container style="height:100%;">
    <div class="title mb-3">
      <v-row>
        <v-col class="d-flex justify-center pa-0">
          <v-card-title style="font-weight:1000; padding:8px;">오늘의 근무({{goToWorkPlayer.length + offWorkPlayer.length}}명)</v-card-title>
        </v-col>
      </v-row>
    </div>
    <!-- 근무중, 미출근, 퇴근 버튼 -->
    <v-row class="justify-center my-3">
      <div>
        <v-btn class="btn" @click="(goToWork = true), (offWork = false), (noWork = false)">근무중({{ goToWorkPlayer.length }})</v-btn>
        <v-btn class="btn" @click="(goToWork = false), (offWork = false), (noWork = true)">미출근({{ noWorkPlayer.length }})</v-btn>
        <v-btn class="btn" @click="(goToWork = false), (offWork = true), (noWork = false)">퇴근({{ offWorkPlayer.length }})</v-btn>
        <v-btn class="btn">대회</v-btn>
      </div>
    </v-row>
    <!-- 근무중인 선수 리스트 -->
    <v-row class="justify-center" v-if="goToWork">
      <!-- 리스트에 보이는 선수는 최대 3명 -->
      <v-card class="d-flex user-card" outlined v-for="user in goToWorkPlayer.slice (0, 3)" :key="user">
        <v-avatar class="ma-1" color="white" size="25">
          <v-icon>mdi-account</v-icon>
        </v-avatar>
        <v-card-text class="card-text">{{ user }}</v-card-text>
      </v-card>
      <!-- 보이는 선수가 4명 이상이면 dialog로 볼 수 있게 버튼 활성화 -->
      <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="goToWorkPlayer.length > 3">
        <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
      </v-card>
    </v-row>
    <!-- 미출근 선수 리스트 -->
    <v-row class="justify-center" v-if="noWork">
      <v-card class="d-flex user-card" outlined v-for="user in noWorkPlayer.slice (0, 3)" :key="user">
        <v-avatar class="ma-2" color="white" size="20">
          <v-icon>mdi-account</v-icon>
        </v-avatar>
        <v-card-text class="card-text">{{ user }}</v-card-text>
      </v-card>
      <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="noWorkPlayer.length > 3">
        <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
      </v-card>
    </v-row>
    <!-- 퇴근 선수 리스트 -->
    <v-row class="justify-center" v-if="offWork">
      <v-card class="d-flex user-card" outlined v-for="user in offWorkPlayer.slice (0, 3)" :key="user">
        <v-avatar class="ma-2" color="white" size="20">
          <v-icon>mdi-account</v-icon>
        </v-avatar>
        <v-card-text class="card-text">{{ user }}</v-card-text>
      </v-card>
      <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="offWorkPlayer.length > 3">
        <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
      </v-card>
    </v-row>
  <!-- 오늘의 근무 리스트 디테일 시작 -->
    <v-dialog v-model="dialog" max-width="600px">
      <v-card class="dialog-card pa-3" outlined>
        <v-btn class="mt-2 mr-0" absolute right icon @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-card-title>오늘의 근무({{goToWorkPlayer.length + offWorkPlayer.length}}명)</v-card-title>
        <v-card-subtitle class="sub-title">{{transformToDay()}}</v-card-subtitle>
        <!-- 근무중, 미출근, 퇴근 버튼 -->
        <v-row class="max-row justify-center">
          <div>
            <v-btn class="ma-2 btn" @click="(goToWork = true), (offWork = false), (noWork = false)">근무중({{ goToWorkPlayer.length }})</v-btn>
            <v-btn class="ma-2 btn" @click="(goToWork = false), (offWork = false), (noWork = true)">미출근({{ noWorkPlayer.length }})</v-btn>
            <v-btn class="ma-2 btn" @click="(goToWork = false), (offWork = true), (noWork = false)">퇴근({{ offWorkPlayer.length }})</v-btn>
            <v-btn class="ma-2 btn">대회(2)</v-btn>
          </div>
        </v-row>
        <!-- 근무중인 선수 리스트 -->
        <v-row class="max-row justify-center" v-if="goToWork">
          <v-card class="d-flex user-card" outlined v-for="user in goToWorkPlayer" :key="user">
            <v-avatar color="white" size="40">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
            <v-card-text class="card-text">{{ user }}</v-card-text>
          </v-card>
        </v-row>
        <!-- 미출근 선수 리스트 -->
        <v-row class="max-row justify-center" v-if="noWork">
          <v-card class="d-flex user-card" outlined v-for="user in noWorkPlayer" :key="user">
            <v-avatar class="ma-0" color="white" size="40">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
            <v-card-text class="justify-center">{{ user }}</v-card-text>
          </v-card>
        </v-row>
        <!-- 퇴근 선수 리스트 -->
        <v-row class="max-row justify-center" v-if="offWork">
          <v-card class="d-flex user-card" outlined v-for="user in offWorkPlayer" :key="user">
            <v-avatar class="ma-0" color="white" size="40">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
            <v-card-text class="card-text">{{ user }}</v-card-text>
          </v-card>
        </v-row>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: {
    goToWorkPlayer: {type: Array},
    noWorkPlayer: {type: Array},
    offWorkPlayer: {type: Array},
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
  },
  data: () => ({
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    users: [],
    goToWork: true,
    offWork: false,
    noWork: false,
    dialog: false,
  }),
};
</script>

<style scoped>
.title{
  width: 100%;
  border-bottom: 1px solid black;
}

.sub-title {
  font-weight: 10px;
  margin-bottom: 10px;
}

.btn {
  width: 70px;
  margin: 8px;
}

@media screen and (max-width:380px) {
  .btn{
    width: 50px;
    margin: 5px;
  }
}

.max-row{
  background : white;
  max-height: 70px;
}

.user-card {
  background-color: rgb(248, 248, 248);
  width: 90%;
  height: 45px;
  border: 0;
  padding: 3px;
}

.detail-btn {
  background-color: rgb(208, 208, 208);
  width: 90%;
  height: 20px;
  border: 0;
  padding: 1px;
}

.v-card__text{
  padding: 5px;
  font-weight: 700;
}

.dialog-card{
  height: 500px;
}

.v-dialog{
    background-color: white;
}

</style>
