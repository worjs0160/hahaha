<template>
  <v-sheet style="width:100%;">
    <v-row class="ma-0">
      <v-col class="border-right hidden-sm-and-down" cols="3">
        <v-container class="pa-0" fluid>
          <v-row>
            <v-col class="mt-2 d-flex flex-column align-center" cols="12">
              <!-- 선수 사진 영역-->
              <v-avatar color="primary" size="80">
                <img
                  alt="Avatar"
                  src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                />
              </v-avatar>
              <p>{{myName}}</p>
              <v-divider width="200" class="ma-2"></v-divider>
              <v-date-picker
                v-model="today"
                :events="trainingState"
                color="rgba(150,150,150,0.4)"
                readonly
                no-title
                width="100%"
                locale="ko-kr"
                :day-format="setDayFormat"
              ></v-date-picker>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
      <!-- 훈련일정 영역 시작 -->
      <v-col class="pa-0" md="9" sm="12">
        <v-container class="py-0" fluid>
          <!-- 훈련일정 테이블 시작 -->
          <v-row>
            <v-col class="pa-0" cols="12" style="position: relative;">
              <v-btn
                class="drawer-btn hidden-md-and-up"
                icon
                @click.stop="drawer = !drawer"
              >
                <v-icon>mdi-menu</v-icon>
              </v-btn>

              <training-table
                :todayDate="today"
                class="mt-1 mb-2"
              ></training-table>
            </v-col>
          </v-row>
          <!-- 훈련일정 테이블 끝 -->
        </v-container>
      </v-col>
    </v-row>
  </v-sheet>
</template>
<script>
import TrainingTable from "/src/components/tables/TrainingTable";

export default {
  components: {
    TrainingTable,
  },
  data: () => ({
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    drawer: false,
    users: [],
    search: "",
    date: "",
    myName: "",
    trainingState:{},
  }),

  async created() {
    this.loadingCover(true);
    this.myName = this.$store.state.userStore.name
    // 훈련기록 가져오기
    await this.$axios({
      method: "POST",
      url:
        "trainings/get_latest_training/"+this.$store.state.userStore.id+"_"+ this.today.substr(0,7) +"/",
    })
      .then((res) => {
        // 훈련일지 상태 추가하기
        for (let j = 0; j < res.data.length; j++) {
          let key = res.data[j].date
          this.trainingState[key] = "green";
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });

    await this.$axios({
      method: "GET",
      url:
        "users/api/player/?id=" + this.$store.state.userStore.id,
    })
      .then((res) => {
        this.$store.commit("setSelectedUser", res.data[0]);
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });
    this.loadingCover(false);
  },
  mounted: function () {},
   computed: {
    //  //당일 날짜 반환하는 함수
    //  todayDate: function () {
    //    var date = new Date();
    //    var year = date.getFullYear();
    //    var month = ("0" + (1 + date.getMonth())).slice(-2);
    //    var day = ("0" + date.getDate()).slice(-2);

    //    return year + "-" + month + "-" + day;
    //  },
   },
  methods: {
    //date-picker 일 출력 형식 변환 (ex) 3일 => 3
    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },
    //오브젝트 타입인지 체크하는 함수
    isObject: function (item) {
      return typeof item === "object";
    },
    getSelectedUser: function () {
      console.log(this.$store.state.selectedUser.id);
      return this.$store.state.selectedUser.id;
    },
    showDialog: function () {
      this.$refs.dialogCard.showDialog();
    },
    toUserList: function () {
      this.$emit("child", "UserList");
    },
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
  margin-top: 30px !important;
  margin-left: 28px !important;
  z-index: 2;
}
</style>
