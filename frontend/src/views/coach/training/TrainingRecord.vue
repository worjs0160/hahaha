<template>
  <v-sheet style="width:100%;">
    <v-row class="ma-0">
      <v-col class="border-right hidden-sm-and-down" cols="3">
        <v-container class="pa-0" fluid>
          <v-row>
            <v-col class="d-flex flex-column align-center" cols="12">
              <!--선수목록으로 이동하는 버튼 -->
              <v-btn
                class="pl-0 mb-2 align-self-start"
                text
                @click="toUserList"
              >
                <v-icon>mdi-arrow-left</v-icon>선수목록
              </v-btn>

              <!-- 선수 사진 영역-->
              <v-avatar color="primary" size="80">
                <img
                  alt="Avatar"
                  src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                />
              </v-avatar>
              <!-- 선수 검색 변경 입력-->
              <v-col cols="6">
                <v-autocomplete
                  v-model="selectedUser"
                  class="ma-2"
                  solo
                  hide-details
                  :items="users"
                  item-text="name"
                  return-object
                >
                  <!--자동완성에 보여지는 리스트의 아이템 형태 정의-->
                  <template v-slot:item="data">
                    <v-list-item-avatar color="primary">
                      <span class="white--text">{{ data.item.name[0] }}</span>
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title
                        v-html="data.item.name"
                      ></v-list-item-title>
                    </v-list-item-content>
                  </template>
                  <!--자동완성에 보여지는 리스트의 아이템 형태 정의 끝-->
                </v-autocomplete>
              </v-col>
              <!-- 선수 검색 변경 입력 끝-->
              <v-divider width="200" class="ma-2"></v-divider>
              <v-date-picker
                class="my-auto"
                v-model="today"
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
      <v-navigation-drawer
        class="hidden-md-and-up"
        v-model="drawer"
        absolute
        temporary
      >
        <v-container class="pa-0" fluid>
          <v-row>
            <v-col class="d-flex flex-column align-center" cols="12">
              <!--선수목록으로 이동하는 버튼 -->
              <v-btn
                class="pl-0 mb-2 align-self-start"
                text
                @click="toUserList"
              >
                <v-icon>mdi-arrow-left</v-icon>선수목록
              </v-btn>

              <!-- 선수 사진 영역-->
              <v-avatar color="primary" size="80">
                <img
                  alt="Avatar"
                  src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                />
              </v-avatar>
              <!-- 선수 검색 변경 입력-->
              <v-col>
                <v-autocomplete
                  v-model="selectedUser"
                  class="ma-2"
                  solo
                  hide-details
                  :items="users"
                  item-text="name"
                  return-object
                >
                  <!--자동완성에 보여지는 리스트의 아이템 형태 정의-->
                  <template v-slot:item="data">
                    <v-list-item-avatar color="primary">
                      <span class="white--text">{{
                        data.item.name[0]
                      }}</span>
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title
                        v-html="data.item.name"
                      ></v-list-item-title>
                    </v-list-item-content>
                  </template>
                  <!--자동완성에 보여지는 리스트의 아이템 형태 정의 끝-->
                </v-autocomplete>
              </v-col>
              <!-- 선수 검색 변경 입력 끝-->
              <v-divider width="200" class="ma-2"></v-divider>
              <v-date-picker
                class="my-auto"
                v-model="today"
                readonly
                no-title
                width="100%"
                locale="ko-kr"
                :day-format="setDayFormat"
              ></v-date-picker>
            </v-col>
          </v-row>
        </v-container>
      </v-navigation-drawer>
      <!-- 훈련일정 영역 시작 -->
      <v-col class="pa-0" md="9" sm="12">
        <v-container class="py-0" fluid>
          <!-- 훈련일정 테이블 시작 -->
          <v-row class="my-auto">
            <v-col class="pa-0" cols="12" style="position: relative">
              <v-btn
                class="drawer-btn ml-3 mt-3 hidden-md-and-up"
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
    drawer: false,
    users: [],
    search: "",
    date: "",
  }),

  async created() {
    await this.loadingCover(true);
    await this.$axios({
      method: "GET",
      url:
        "users/api/player/?coach=" + this.$store.state.userStore.id,
    })
      .then((res) => {
        console.log(res)
        for (var i = 0; i < res.data.length; i++) {
          this.$set(this.users, i, res.data[i]); //코치로 받아온 유저데이터 users에 복사
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
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

    toUserList: function () {
      this.$emit("child", "UserList");
    },
    //MainTraining으로 로딩상태 보내기
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
