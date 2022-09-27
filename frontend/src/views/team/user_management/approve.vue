<template>

  <v-container fill-height fluid class="overflow-y-auto" style="height: 100%">
    <!-- 상단 영역 시작 -->
    <v-row>
      <v-col>
  <h1>승인</h1>

            <v-row>
              <v-col>
                <v-card>
                  <v-card-title>
                    미승인 코치
                    <v-spacer></v-spacer>
                    <v-text-field
                      v-model="search1"
                      append-icon="mdi-magnify"
                      label="search"
                      single-line
                      hide-details
                    ></v-text-field>
                  </v-card-title>
                  <v-data-table
                    v-model="true_coaches"
                    :headers="coaches_header"
                    :items="init_false_coaches"
                    :search="search1"
                    show-select
                  >
                  </v-data-table>
                </v-card>
              </v-col>

              <v-col>
                <v-card>
                  <v-card-title>
                    승인 코치
                    <v-spacer></v-spacer>
                    <v-text-field
                      v-model="search2"
                      append-icon="mdi-magnify"
                      label="search"
                      single-line
                      hide-details
                    ></v-text-field>
                  </v-card-title>
                  <v-data-table
                    v-model="false_coaches"
                    :headers="coaches_header"
                    :items="init_true_coaches"
                    :search="search2"
                    show-select
                  >
                  </v-data-table>
                </v-card>
              </v-col>
            </v-row>
            
          <v-row justify="end">
            <v-col cols="3">
              <v-btn block large class="mb-7 mt-7" @click="coach_submit">
                정보수정
              </v-btn>
            </v-col>
          </v-row>
          <!-- </div> -->
    </v-col>
  </v-row>
  <!-- 상단 영역 종료 -->
  
  <!-- 아래 영역 시작 -->
  <v-row>
    <v-col>
            <v-row>
              <v-col>
                <v-card>
                  <v-card-title>
                    미승인 선수
                    <v-spacer></v-spacer>
                    <v-text-field
                      v-model="search3"
                      append-icon="mdi-magnify"
                      label="search"
                      single-line
                      hide-details
                    ></v-text-field>
                  </v-card-title>
                  <v-data-table
                    v-model="true_players"
                    :headers="players_header"
                    :items="init_false_players"
                    :search="search3"
                    show-select
                  >
                  </v-data-table>
                </v-card>
              </v-col>

              <v-col>
                <v-card>
                  <v-card-title>
                    승인 선수
                    <v-spacer></v-spacer>
                    <v-text-field
                      v-model="search4"
                      append-icon="mdi-magnify"
                      label="search"
                      single-line
                      hide-details
                    ></v-text-field>
                  </v-card-title>
                  <v-data-table
                    v-model="false_players"
                    :headers="players_header"
                    :items="init_true_players"
                    :search="search4"
                    show-select
                  >
                  </v-data-table>
                </v-card>
              </v-col>
            </v-row>
            
          <v-row justify="end">
            <v-col cols="3">
              <v-btn block large class="mb-7 mt-7" @click="player_submit">
                정보수정
              </v-btn>
            </v-col>
          </v-row>

    </v-col>
  </v-row>
  <!-- 아래 영역 종료 -->
</v-container>
</template>

<script>
export default {
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
    search3: "",
    search4: "",
    coaches_header: [
      {
        text: "코치이름",
        align: "start",
        sortable: true,
        value: "name",
      },
      { text: "이메일", value: "email" },
      { text: "소속", value: "team.value" },
    ],
    players_header: [
      {
        text: "선수이름",
        align: "start",
        sortable: true,
        value: "name",
      },
      { text: "이메일", value: "email" },
      { text: "소속", value: "team.value" },
      { text: "코치", value: "coach_name" },
    ],
    false_coaches: [], // 선수 false 로 바꿀 선수 목록
    true_coaches: [], // 선수 true 로 바꿀 선수 목록
    init_false_coaches: [], // 비활성화 선수 목록
    init_true_coaches: [], // 활성화 선수 목록

    
    false_players: [], // 선수 false 로 바꿀 선수 목록
    true_players: [], // 선수 true 로 바꿀 선수 목록
    init_false_players: [], // 비활성화 선수 목록
    init_true_players: [], // 활성화 선수 목록
  }),
  
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
            if(player.is_active){
              this.init_true_players.push(player);
            }else{
              this.init_false_players.push(player);
            }
          }
        }
        this.reset_players = this.sel_players;
      });

    // 복지관의 소속과 일치하는 코치정보 가져오기
    await this.$axios
      .get("users/api/coach/?team=" + this.$store.state.userStore.team.id)
      .then((res) => {
        for (const player of res.data) {

          if (player.team.id === this.$store.state.userStore.team.id) {
            player.coach_name = this.data.username;
            
            // 활성화 여부 체크
            if(player.is_active){
              this.init_true_coaches.push(player);
            }else{
              this.init_false_coaches.push(player);
            }

          } else if (player.coach === null) {
            player.coach_name = "없음";
            
            // 활성화 여부 체크
            if(player.is_active){
              this.init_true_coaches.push(player);
            }else{
              this.init_false_coaches.push(player);
            }
          }
        }
        this.reset_players = this.sel_players;
      });
    // 세션에 저장된 유저 데이터 가져와 vue data에 입력
    this.data = this.$store.getters.getUser;
    await this.loadingCover(false);
  },

  methods: {
    
    // 복지관의 소속과 일치하는 선수정보 가져오기
    set_players() {
      this.init_true_players = [];
      this.init_false_players = [];

      this.$axios
        .get("users/api/player/?team" + this.$store.state.userStore.team.id)
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

    // 복지관의 소속과 일치하는 코치정보 가져오기
    set_coches() {
      this.init_true_coaches = [];
      this.init_false_coaches = [];
      
      this.$axios
        .get("users/api/coach/?team=" + this.$store.state.userStore.team.id)
        .then((res) => {
          for (const player of res.data) {
            if (player.team.id === this.$store.state.userStore.team.id) {
              player.coach_name = this.data.username;
              
              // 활성화 여부 체크
              if(player.is_active){
                this.init_true_coaches.push(player);
              }else{
                this.init_false_coaches.push(player);
              }

            } else if (player.coach === null) {
              player.coach_name = "없음";
              
              // 활성화 여부 체크
              if(player.is_active){
                this.init_true_coaches.push(player);
              }else{
                this.init_false_coaches.push(player);
              }
            }
          }
          this.reset_players = this.sel_players;
        });
    },
    // 선수 코치 값 업데이트 요청 보내는 함수
    set_active_players(list_player, value) {
      this.$axios
        .post("users/api/player/set_active_players/", {
          list_player: list_player,
          set_data: { is_active: value },
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
    set_active_coaches(list_player, value) {
      this.$axios
        .post("users/api/coach/set_active_coaches/", {
          list_player: list_player,
          set_data: { is_active: value },
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
    // async await 로 함수가 완료되는 것을 기다림 -- 함수가 순차적으로 실행하게 변경
    async player_submit() {

      // 선수 추가 제거 -- 복지관 계정만
      if (this.$store.state.userStore.userType === 3) {
        await this.set_active_players(this.true_players, true);
        await this.set_active_players(this.false_players, false);
      }
      this.true_players = []
      this.false_players = []
      this.set_players(); // 선수 목록 새로고침
    this.$router.go(this.$router.currendRoute);
    },
    // async await 로 함수가 완료되는 것을 기다림 -- 함수가 순차적으로 실행하게 변경
    async coach_submit() {

      // 선수 추가 제거 -- 복지관 계정만
      if (this.$store.state.userStore.userType === 3) {
        await this.set_active_coaches(this.true_coaches, true);
        await this.set_active_coaches(this.false_coaches, false);
      }

      this.true_coaches = []
      this.false_coaches = []
    this.set_coches(); // 코치 목록 새로고침
    this.$router.go(this.$router.currendRoute);
    },
    //layout으로 로딩상태 전달
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  }
};
</script>
