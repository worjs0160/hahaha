<template>
  <v-container style="height:100%; padding-top:4px;">
    <div class="title mb-3">
      <v-row>
        <v-col cols="12" class="d-flex justify-center pt-0">
          <v-card-title style="font-weight:1000; padding:8px;">훈련일지</v-card-title>
        </v-col>
      </v-row>
    </div>
     <!-- 훈련일지 작성중, 미작성, 완료 상태 버튼 -->
    <v-row class="justify-center my-2">
      <div>
        <v-btn class="ma-2 btn" @click="(writing = true), (unwritten = false), (completed = false)">작성중({{ writingManagement.length }})</v-btn>
        <v-btn class="ma-2 btn" @click="(writing = false), (unwritten = true), (completed = false)">미작성({{ unwrittenManagement.length }})</v-btn>
        <v-btn class="ma-2 btn" @click="(writing = false), (unwritten = false), (completed = true)">완료({{ completedManagement.length }})</v-btn>
      </div>
    </v-row>
     <!-- 훈련일지 작성중인 선수 리스트 -->
    <v-row class="justify-center" v-if="writing">
      <v-card class="d-flex user-card" outlined v-for="user in writingManagement.slice (0, 8)" :key="user">
        <v-avatar class="ma-2" color="white" size="40">
          <v-icon>mdi-account</v-icon>
        </v-avatar>
        <v-card-text class="card-text">{{user}}</v-card-text>
      </v-card>
      <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="writingManagement.length > 8">
        <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
      </v-card>
    </v-row>
    <!-- 훈련일지 미작성인 선수 리스트 -->
    <v-row class="justify-center" v-if="unwritten">
      <v-card class="d-flex user-card" outlined v-for="user in unwrittenManagement.slice (0, 8)" :key="user">
        <v-avatar class="ma-2" color="white" size="40">
          <v-icon>mdi-account</v-icon>
        </v-avatar>
        <v-card-text class="card-text">{{user}}</v-card-text>
      </v-card>
      <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="unwrittenManagement.length > 8">
        <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
      </v-card>
    </v-row>
    <!-- 훈련일지 완성된 선수 리스트 -->
    <v-row class="justify-center" v-if="completed">
      <v-card class="d-flex user-card" outlined v-for="user in completedManagement.slice (0, 8)" :key="user">
        <v-avatar class="ma-2" color="white" size="40">
          <v-icon>mdi-account</v-icon>
        </v-avatar>
        <v-card-text class="card-text">{{user}}</v-card-text>
      </v-card>
      <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="completedManagement.length > 8">
        <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
      </v-card>
    </v-row>
      <!-- 훈련일지 현황 디테일 시작 -->
    <v-dialog v-model="dialog" max-width="600px">
      <v-card class="dialog-card pa-3" outlined>
        <v-btn class="mt-2 mr-0" absolute right icon @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-card-title>훈련일지</v-card-title>
        <v-card-subtitle class="sub-title">{{transformToDay()}}</v-card-subtitle>
        <!-- 훈련일지 작성중, 미작성, 완료 상태 버튼 -->
        <v-row class="max-row justify-center">
          <div>
            <v-btn class="ma-2 btn" @click="(writing = true), (unwritten = false), (completed = false)">작성중({{ writingManagement.length }})</v-btn>
            <v-btn class="ma-2 btn" @click="(writing = false), (unwritten = true), (completed = false)">미작성({{ unwrittenManagement.length }})</v-btn>
            <v-btn class="ma-2 btn" @click="(writing = false), (unwritten = false), (completed = true)">완료({{ completedManagement.length }})</v-btn>
          </div>
        </v-row>
        <!-- 근무중인 선수 리스트 -->
        <v-row class="justify-center" v-if="writing">
          <v-card class="d-flex user-card" outlined v-for="user in writingManagement.slice (0, 8)" :key="user">
            <v-avatar class="ma-2" color="white" size="40">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
            <v-card-text class="card-text">{{user}}</v-card-text>
          </v-card>
        </v-row>
        <!-- 훈련일지 미작성인 선수 리스트 -->
        <v-row class="justify-center" v-if="unwritten">
          <v-card class="d-flex user-card" outlined v-for="user in unwrittenManagement.slice (0, 8)" :key="user">
            <v-avatar class="ma-2" color="white" size="40">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
            <v-card-text class="card-text">{{user}}</v-card-text>
          </v-card>
        </v-row>
        <!-- 훈련일지 완성된 선수 리스트 -->
        <v-row class="justify-center" v-if="completed">
          <v-card class="d-flex user-card" outlined v-for="user in completedManagement.slice (0, 8)" :key="user">
            <v-avatar class="ma-2" color="white" size="40">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
            <v-card-text class="card-text">{{user}}</v-card-text>
          </v-card>
        </v-row>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: {
    writingManagement: {type: Array},
    unwrittenManagement: {type: Array},
    completedManagement: {type: Array},
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
    dialog: false,
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    writing: true,
    unwritten:false,
    completed: false,
  }),

  async created() {},
};
</script>

<style scoped>
.title{
  border-bottom: 1px solid black;
}

.sub-title{
  padding: 6px;
  font-weight: 10px;
  margin-bottom: 20px;
}

.btn {
  width: 90px;
  margin: 8px;
}

@media screen and (max-width:380px) {
  .btn{
    width: 75px;
    margin: 5px;
  }
}

.detail-btn {
  background-color: rgb(208, 208, 208);
  width: 90%;
  height: 20px;
  border: 0;
  padding: 1px;
}

.user-card{
  background: rgb(245, 245, 245);
  width: 90%;
  border: 0;
}

.card-text{
  font-weight: 1000;
  font-size: 1em;
}

.dialog-card{
  height: 500px;
}
</style>