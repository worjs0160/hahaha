<template>
  <v-sheet class="">
    <v-row class="ma-0">
      <v-col class="mr-2" cols="2">
        <v-container class="pa-0" fluid>
          <v-row>
            <v-col cols="12" class="justify-center ">
              선수 목록
            </v-col>
          </v-row>
          <v-row class="">
            <v-col class="d-flex flex-column align-center mt-1" 
            v-for="(user, index) in users" 
            :key="index" 
            @click="toUserList(index)"
            cols="12" 
            style ="border: 2px solid grey; cursor:pointer">
                    {{user.username}}     
            </v-col>
          </v-row>
        </v-container>
      </v-col>
      
      <v-col class="border-right border-top border-bottom" cols="7" style="border-left: 2px solid grey;">
        <v-container class="pa-0" fluid>
        
         
          <!--유저 디테일 프로필 내용 영역-->
            <v-row>
              <v-col cols="3" class="justify-center ">
                세부사항
              </v-col>
              <v-col cols="9">
                <v-btn v-if="page" small class="pa-0" @click="modifyPlayer()">수정</v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                신장 / 체중
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.height" /> cm / <input style="border: 1px solid black;" v-model="playerDetail.weight" /> kg
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                선수 전화번호
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.phoneNum" />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                장애 유형 / 경증, 중증
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.disabilityGrade" />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                휠체어 사용 여부
              </v-col>
              <v-col cols="9">
                <v-checkbox
                    v-model="playerDetail.wheelchair"
                    :label="`사용 체크`"
                    hide-details="auto"
                    class="mt-0"
                    style="font-weight: bold;"
                  ></v-checkbox>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                보호자 성명
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.guardianName" />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                보호자 전화번호
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.guardianNum" />
              </v-col>
            </v-row>
            <v-row style="border-top: 2px solid grey;">
              <v-col cols="3" class="justify-center ">
                계약사항
              </v-col>
              <!-- <v-col cols="9">
              </v-col> -->
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                근무요일
              </v-col>
              <v-col cols="9">
                <v-btn-toggle
                  v-model="selectWeek"
                  multiple
                >
                  <v-btn class="px-0">월</v-btn>
                  <v-btn class="px-0">화</v-btn>
                  <v-btn class="px-0">수</v-btn>
                  <v-btn class="px-0">목</v-btn>
                  <v-btn class="px-0">금</v-btn>
                  <v-btn class="px-0">토</v-btn>
                  <v-btn class="px-0">일</v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                출근시간
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.guardianNum" />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                퇴근시간
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.guardianNum" />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="3" class="justify-center ">
                월간 계약시간
              </v-col>
              <v-col cols="9">
                <input style="border: 1px solid black;" v-model="playerDetail.guardianNum" />
              </v-col>
            </v-row>
          <!--유저 디테일 근태 일정 영역-->
        </v-container>
      </v-col>
    </v-row>
    
      
  </v-sheet>
</template>
<script>
// import TrainingTable from "/src/components/tables/TrainingTable";

export default {
  components: {
    // TrainingTable,
  },
  data: () => ({
    drawer: false,
    users: [],
    search: "",
    date: "",
    playerDetail:{
      id:"",
      height: "",
      weight: "",
      phoneNum: "",
      disabilityGrade: "",
      disabilityType: "",
      wheelchair: "",
      guardianName: "",
      guardianNum: "",
    },
    page: false,
    pageNum: null,
    selectWeek:[],
  }),

  async created() {
    await this.loadingCover(true);
    // 복지관의 소속과 일치하는 선수정보 가져오기
    await this.$axios
      .get("users/api/detail/detail_search/?team=" + this.$store.state.userStore.team.id)
      .then((res) => {
        for (const player of res.data) {
          console.log(player);
            
          this.users.push(player);
        }
        // this.reset_players = this.sel_players;
      });
    await this.loadingCover(false);
  },
  mounted: function () {},
  computed: {
    selectedUser: {
      set: function (val) {
        this.$store.commit("setSelectedUser", val);
      },
      get: function () {
        return this.$store.getters.getSelectedUser;
      },
    },
    //당일 날짜 반환하는 함수
    today: function () {
      var date = new Date();
      var year = date.getFullYear();
      var month = ("0" + (1 + date.getMonth())).slice(-2);
      var day = ("0" + date.getDate()).slice(-2);

      return year + "-" + month + "-" + day;
    },
  },
  methods: {
    //date-picker 일 출력 형식 변환 (ex) 3일 => 3
    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },
    getSelectedUser: function () {
      console.log(this.$store.state.selectedUser.id);
      return this.$store.state.selectedUser.id;
    },
    //오브젝트 타입인지 체크하는 함수
    isObject: function (item) {
      return typeof item === "object";
    },

    showDialog: function () {
      this.$refs.dialogCard.showDialog();
    },

    toUserList: function (value) {
      // 클릭한 유저의 데이터 보여줌
      this.playerDetail = this.users[value]
      this.playerDetail.disabilityGrade = this.users[value].disabilityGrade.value
      this.page = true
      this.pageNum = true
    },

    modifyPlayer: function () {


      if(this.wheelchair != "true"){
        this.wheelchair = true
      }else if(this.wheelchair != "false"){
        this.wheelchair = false
      }else{
       this.wheelchair = false 
      }
        this.$axios
        .post("users/api/detail/set_detail_player/", {
          player: this.playerDetail.id,
          set_data: {
            phoneNum:this.playerDetail.phoneNum,
            height:this.playerDetail.height,
            weight:this.playerDetail.weight,
          },
          category_data: {disabilityGrade:1,}
        })
        .then((res) => {
          console.log(res);
          return true;
        })
        .catch((err) => {
          console.log(err);
          return false;
        });
    },
    //layout으로 로딩상태 전달
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
};
</script>
<style scoped>
.border-right {
  border-right: solid 2px grey;
}
.border-top {
  border-top: solid 2px grey;
}
.border {
  border: solid 2px grey;
}
.full-height {
  height: calc(100vh - 56px);
}
.drawer-btn {
  position: absolute;
  z-index: 2;
}
</style>
