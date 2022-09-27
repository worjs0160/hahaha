<template>

  <v-container fill-height fluid class="overflow-y-auto" style="height: 100%">
    <!-- 상단 영역 시작 -->
    <v-row>
      <v-col>
        <h1>매칭</h1>
            <v-row>
              <v-col cols="6" style="border-right: 2px solid grey;">
                <!-- 복지관 선수 배정 코치 목록 시작 -->
                <div class="mt-2 mx-4">
                  <!--검색영역 및 근태 생성/삭제 버튼 -->
                  <div class="d-flex align-center justify-space-between mb-2">
                    <div class="d-flex mb-2" style="width: 300px">
                      <v-card-title>
                        선수 배정 코치
                        <v-spacer></v-spacer>
                        <v-text-field
                          v-model="search1"
                          append-icon="mdi-magnify"
                          label="search"
                          single-line
                          hide-details
                        ></v-text-field>
                      </v-card-title>
                    </div>
                    
                    <!-- <div class="pb-0 pr-0 hidden-sm-and-down">
                      <v-btn
                        color="error"
                        class="py-0"
                        :disabled="!isChecked"
                        @click="deleteAttendance"
                      >
                        선수배정 삭제
                      </v-btn>
                    </div> -->
                    <!-- <div class="pb-0 att-btn-group hidden-md-and-up">
                      <v-btn
                        color="error"
                        icon
                        :disabled="!isChecked"
                        @click="deleteAttendance"
                      >
                        <v-icon>mdi-minus</v-icon>
                      </v-btn>
                    </div> -->
                  </div>
                  <v-data-table
                    no-data-text="복지관 소속 코치가 없습니다."
                    v-model="checkedCoaches"
                    :headers="coaches_header"
                    :items="coachesList"
                    :search="search1"
                    height="50vh"
                    fixed-header
                  >
                    <template v-slot:[`item.actions`]="{ item }">
                      <v-icon small class="mr-2" @click="deleteItem(item)">
                        mdi-delete
                      </v-icon>
                    </template>
                  </v-data-table>

                  <dialog-card ref="dialogCard">
                    <attendance-form
                      :puttedData="toFormData"
                      @closeDialog="closeDialog()"
                      @saveAction="saveAction"
                    ></attendance-form>
                  </dialog-card>

                  <v-dialog v-model="dialogDelete" max-width="500px">
                    <v-card>
                      <v-card-title class="text-h5">배정선수를 삭제하시겠습니까?</v-card-title>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="closeDelete">아니오</v-btn>
                        <v-btn color="blue darken-1" text @click="deleteItemConfirm">네</v-btn>
                        <v-spacer></v-spacer>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </div>
            <!-- 복지관 선수 배정 코치 목록 종료 -->
              </v-col>
              <v-col cols="6">
                <!-- 미배정 선수 시작 --> 
                <div class="mt-2 mx-4">
                  <!--검색영역 및 근태 생성/삭제 버튼 -->
                  <div class="d-flex align-center justify-space-between mb-2">
                    <div class="d-flex mb-2" style="width: 300px">
                      <v-card-title>
                        미배정 선수
                        <v-spacer></v-spacer>
                        <v-text-field
                          v-model="search2"
                          append-icon="mdi-magnify"
                          label="search"
                          single-line
                          hide-details
                        ></v-text-field>
                      </v-card-title>
                    </div>
                  </div>
                  <v-data-table
                    no-data-text="미배정 선수가 없습니다."
                    v-model="playersList"
                    :headers="players_header"
                    :items="playersList"
                    :search="search2"
                    height="50vh"
                    fixed-header
                  >
                    <template v-slot:[`item.actions`]="{ item }">
                      <v-icon small class="mr-2" @click="showDialog(item)">
                        mdi-pencil
                      </v-icon>
                    </template>
                  </v-data-table>

                  <dialog-card ref="dialogCard">
                    <PlayerMatcingForm
                      :puttedData="toFormData"
                      @closeDialog="closeDialog()"
                      @saveAction="saveAction"
                    ></PlayerMatcingForm>
                  </dialog-card>
                </div>
                <!-- 미배정 선수 종료 -->
              </v-col>
            </v-row>
            
          <!-- </div> -->
    </v-col>
  </v-row>
</v-container>
</template>

<script>
import DialogCard from "/src/components/cards/DialogCard";
import PlayerMatcingForm from "/src/views/team/attendance/PlayerMatcingForm";


export default {
  components: {
    DialogCard,
    PlayerMatcingForm,
  },
  data: () => ({
    
    data: {
      id: "",
      username: "",
      name: "",
      email: "",
      userType: "",
      coach: "",
      phoneNum: "",
      team: "",
      company: "",
    },
    search1: "",
    search2: "",
    coaches_header: [
      {
        text: "코치이름",
        align: "start",
        sortable: true,
        value: "name",
      },
      { text: "코치 이메일", value: "email" },
      //{ text: "소속", value: "value" },
      { text: "배정선수", value: "user.name" },
      { text: "작업", value: "actions", sortable: false },
    ],
    players_header: [
      {
        text: "선수이름",
        align: "start",
        sortable: true,
        value: "name",
      },
      { text: "선수 이메일", value: "email" },
      //{ text: "소속", value: "team.value" },
      { text: "소속 기업", value: "company.value" },
      { text: "작업", value: "actions", sortable: false },
    ],
    checkedCoaches: [], // 체크한 선수 목록
    coachesList: [],  // 복지관 코치 목록
    playersList: [],  // 복지관 코치 목록

    toFormData: {
      team: { id: null,},
      id: null,
      email:""
    }, // 미배정 선수 폼으로 보낼 임시 데이터
    dialogDelete: false,
    editedIndex: -1,
    editedItem: {
      name: '',
      user: {team:'',name:''},
    },
    defaultItem: {
      name: '',
      user: {team:'',name:''},
    },
  }),
  
  computed: {
    //테이블에서 체크한 선수가 있는지 확인하는 함수(있으면 true, 없으면 false)
    isChecked: function() {
      if (this.checkedCoaches.length > 0) {
        return true;
      }
      return false;
    },
  },
  async created() {
    await this.loadingCover(true);
    // 세션에 저장된 유저 정보 업데이트
    await this.$axios
      .get("users/api/user/" + this.$store.state.userStore.id)
      .then((res) => {
        this.$store.commit("setUser", res.data);
      });

    // 복지관의 소속과 일치하는 선수정보 가져오기
    await this.$axios
        .get("users/api/player/?team=" + this.$store.state.userStore.team.id)
        .then((res) => {
          for (const player of res.data) {
            if (player.team.id === this.$store.state.userStore.team.id) {
              if(!player.coach || player.coach == -1){
                this.playersList.push(player);
              }
            }
          }
          this.reset_players = this.sel_players;
        });

    // 복지관의 소속과 일치하는 코치정보 가져오기
    await this.$axios
      .post("users/get_matching/" + this.$store.state.userStore.team.id + '/')
      .then((res) => {
        // var coachesNum = 0
        for (const coaches of res.data.data) {
          var usersNum = 0
          // this.coachesList.push(coaches)
          
          for(const users of coaches){
            if(usersNum == 0){
              var coachesData = coaches[usersNum]
              
              if(coaches.length == 1){
                this.coachesList.push(coachesData)
              }

            }else{
              var setData = {
                id: coachesData.id,
                name: coachesData.name,
                email: coachesData.email,
                user:{
                  coach: users.coach,
                  id: users.id,
                  name: users.name
                },
                //value: users.value,
              }
              this.coachesList.push(setData)
            }
            
            
            usersNum++
          }
          // coachesNum++
        }
      });

    // 세션에 저장된 유저 데이터 가져와 vue data에 입력
    this.data = this.$store.getters.getUser;
    await this.loadingCover(false);
  },

  methods: {
    set_players() {
      this.init_true_players = [];
      this.init_false_players = [];

      this.$axios
        .get("users/api/player/?team=" + this.$store.state.userStore.team.id)
        .then((res) => {
          for (const player of res.data) {
            
            if (player.team.id === this.$store.state.userStore.team.id) {
              player.coach_name = this.data.username;
              
              // 활성화 여부 체크
              if(player.is_active){
                this.init_true_players.push(player);
              }else{
                this.init_false_players.push(player);
              }

            } else if (player.coach === null) {
              player.coach_name = "없음";
              
              // 활성화 여부 체크
              if(player.is_active == false){
                this.init_true_players.push(player);
              }else{
                this.init_false_players.push(player);
              }
            }
          }
          this.reset_players = this.sel_players;
        });
    },
    
    //삭제요청 함수
    deleteAttendance: function() {
      var listDel = [];
      // 삭제할 게시물 pk 리스트로 묶기
      for (var i = 0; i < this.checkedAttendance.length; i++) {
        listDel.push(this.checkedAttendance[i].id);
      }

      this.$axios({
        method: "POST",
        url: "attendances/api/att_list/multiple_delete/",
        data: listDel,
      })
        .then(() => {
          // 삭제하고 새로고침시 데이터 길이가 줄어들어서 끝에있는 데이터를 없에주기위해 데이터 초기화 
          this.checkedAttendance = [];
          this.attendanceList = [];

          // 데이터 다시 불러오기
          this.getAttendanceData();
          
          this.$store.dispatch("callToast", {
            msg: "삭제 완료",
            result: "fail",
          });
        })
        .catch(() => {
          this.$store.dispatch("callToast", {
            msg: "삭제 실패",
            result: "fail",
          });
        });
    },
    //저장완료 확인 후 처리 함수
    saveAction: function(text) {
      this.$store.dispatch("callToast", { msg: text, result: "success" });
      this.getAttendanceData();
    },
    //선수배정 수정 다이얼로그 열기
    showDialog: function(item) {

      if (item === null) {
        this.toFormData = {
          team: { id: null,},
          id: null,
          email:""
        };
      } else {
        this.toFormData = item;
      }
      this.$refs.dialogCard.showDialog();
    },
    //선수배정 수정 다이얼로그 닫기
    closeDialog: function() {
      this.$refs.dialogCard.closeDialog();
    },

    deleteItem (item) {
      this.editedIndex = this.coachesList.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    
    deleteItemConfirm () {
      this.$axios({
        method: "PATCH",
        url: "users/api/player/" + this.coachesList[this.editedIndex].user.id + '/',
        data: {coach: -1},
      })
        .then(() => {
          // 삭제하고 새로고침시 데이터 길이가 줄어들어서 끝에있는 데이터를 없에주기위해 데이터 초기화 
          
          this.$store.dispatch("callToast", {
            msg: "삭제 완료",
            result: "fail",
          });
        })
        .catch(() => {
          this.$store.dispatch("callToast", {
            msg: "삭제 실패",
            result: "fail",
          });
        });
      // 새로고침
      this.$router.go(this.$router.currendRoute);
      this.closeDelete()
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    //layout으로 로딩상태 전달
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  }
};
</script>
