<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center">
        <v-card class="home-card pa-2" rounded="lg">
            <div class="title">
              <v-avatar class="mx-4" width="150" height="70" tile>
                <v-img src="@/assets/trainingCenterLogo.jpg"></v-img>
              </v-avatar>
              <v-card-title style="font-weight:1000; padding:8px;">{{$store.state.userStore.team.value}}</v-card-title>
            </div>
          <v-row class="title-display justify-center" style="width:90%;">
            <!--훈련종목 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title ">훈련종목({{sportType.length}}개)</v-card-title>
              <v-card-text class="text-center">{{printType(sportType)}}</v-card-text>
            </v-card>
            <!--훈련선수 명수 표시 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title">훈련선수</v-card-title>
              <v-card-text class="text-center">{{userLength}}명</v-card-text>
            </v-card>
            <!--연계기업 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title">연계 기업({{company.length}}개)</v-card-title>
              <v-card-text class="text-center">{{printType(company)}}</v-card-text>
            </v-card>
            <!--추가정보 영역-->
            <v-card class="content-card my-5" color="#C4FCD7" rounded="lg">
              <v-card-title class="card-title">추가정보</v-card-title>
            </v-card>
          </v-row>
        </v-card>
      </v-col>
      <!--코치 미배치 선수 리스트 컴포넌트-->
      <v-col class="d-flex justify-center">
        <v-card class="home-card" style="border:0;" outlined rounded="lg">
          <v-card class="sub-card">
            <no-coach-user></no-coach-user>
          </v-card>
      <!--오늘의 근무 리스트 컴포넌트-->
          <v-card class="sub-card mt-5">
            <today-attendance
            :goToWorkPlayer="goToWorkPlayer"
            :noWorkPlayer="noWorkPlayer"
            :offWorkPlayer="offWorkPlayer"
          ></today-attendance>
          </v-card>  
        </v-card>
      </v-col>
      <!--훈련일지 상태 현황 컴포넌트-->
      <v-col class="d-flex justify-center">
        <v-card class="home-card pa-2" rounded="lg">
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
import NoCoachUser from './NoCoachUser.vue';
import TodayAttendance from './TodayAttendance.vue';
import TrainingRecord from './TrainingRecord.vue';
export default {
  components: {
    NoCoachUser,
    TodayAttendance,
    TrainingRecord,
  },
  methods: {
    printType: function(type){
      //타입 이름 나열해주기
      var arrange = ""
      for(var i = 0; i < type.length; i++){
        if(i==type.length-1){
          arrange += type[i]
        }
        else{
          arrange += type[i]+","
        }
      }
      return arrange
    },
    // MainLayout으로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
  data: () => ({
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    sportType:[],
    userLength: 0,
    company:[],
    offWorkPlayer: [],
    goToWorkPlayer: [],
    noWorkPlayer: [],
    writingManagement:[],
    unwrittenManagement:[],
    completedManagement: [],
  }),
  async created() {
    await this.loadingCover(true);

    await this.$axios({
      method: "GET",
      url:"users/api/player/?team=" + this.$store.state.userStore.team.id
    })
      .then((res) => {
        this.userLength = res.data.length;
        for (var i = 0; i < res.data.length; i++){
          //선수들의 운동종목과 소속기업을 중복제거하고 배열로 저장
          if(res.data[i].sportType){
            if (this.sportType.indexOf(res.data[i].sportType.value) === -1) 
              this.sportType.push(res.data[i].sportType.value);
          }
          if(res.data[i].company){
            if (this.company.indexOf(res.data[i].company.value) === -1) 
              this.company.push(res.data[i].company.value);
          }
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });

    await this.$axios({
      method: "POST",
      url:
        "attendances/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.team.id+"_"+ this.today +"/",
    })
      .then((res) => {
        //근무중, 미출근, 퇴근 선수 분류
        for(var i=0; i < res.data.length; i++){
          if(res.data[i].state=="1"){
            this.offWorkPlayer.push(res.data[i].user)
          }
          else if(res.data[i].state=="0"){
            this.goToWorkPlayer.push(res.data[i].user)
          }
          else
            this.noWorkPlayer.push(res.data[i].user)
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });

    await this.$axios({
      method: "POST",
      url:
        "trainings/get_today_state/"+this.$store.state.userStore.userType+"_"+this.$store.state.userStore.team.id+"_"+this.today+"/",
    })
      .then((res) => {
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

.sub-card{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 320px;
  width: 360px;
}

.title{
  width: 100%;
  padding: 6px;
  margin-bottom: 20px;
  border-bottom: 1px solid black;
}

.card-title{
  padding: 5px;
  font-size:1.1rem;
  font-weight: 600;
}

.title-display{
  display: block;
  margin: 0px;
}

.content-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 80px;
  width: 100%;
}

@media screen and (max-width:350px) {
  .content-card{
    height: 80px;
    width: 100%;
  }
  .v-card__title{
    font-size:0.9rem;
  }

  .home-card {
  height: 600px;
  }

  .sub-card{
    height: 320px;
    width: 310px;
  }
}
</style>