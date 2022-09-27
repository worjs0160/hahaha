<template>
  <v-container fill-height fluid class="overflow-y-auto" style="height: 100%">
    <v-row>
      <v-col>
        <v-card-title class="text-h4">회원정보 수정</v-card-title>
        <v-card-subtitle>정보관리</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>

        <div class="mx-7">
          <v-card-text class="font-weight-medium text-h6 px-0">
            개인정보 수정
          </v-card-text>
          <v-row>
            <v-col>
              <v-text-field
                v-model="data.username"
                label="아이디"
              ></v-text-field>
            </v-col>

            <v-col>
              <v-text-field
                v-model="data.name"
                label="이름"
              ></v-text-field>
            </v-col>

            <v-col>
              <v-text-field
                v-model="data.email"
                label="이메일"
              ></v-text-field>
            </v-col>

            <v-col>
              <v-text-field
                v-model="data.phoneNum"
                label="연락처"
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-select
                  v-model="data.team.id"
                  :items="teamList"
                  item-text="value"
                  item-value="id"
                  hide-details="auto"
              ></v-select>
            </v-col>
            <v-col>
              <v-select
                  v-model="data.company.id"
                  :items="companyList"
                  item-text="value"
                  item-value="id"
                  hide-details="auto"
              ></v-select>
            </v-col>
          </v-row>

          <!-- 로그인한 유저가 선수일 때에만 출력-->
          <div v-if="this.$store.state.userStore.userType === 2"></div>

          <v-row justify="end">
            <v-col cols="3">
              <v-btn block large class="mb-7 mt-7" @click="submit">
                정보수정
              </v-btn>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    data: {
      username: "",
      name: "",
      email: "",
      userType: "",
      coach: "",
      phoneNum: "",
      team: {id:"",value:","},
      company: {id:"",value:","},
    },
    search1: "",
    search2: "",
    headers: [
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
    companyList: [], // 기업목록 리스트
    teamList: [], // 복지관(훈련기관) 리스트
  }),
  async created() {
    // 세션에 저장된 유저 정보 업데이트
    await this.$axios
      .get("users/api/user/" + this.$store.state.userStore.id)
      .then((res) => {
        this.$store.commit("setUser", res.data);
      });

    // 기업목록 가져오기
    await this.$axios
      .get("datasets/api/company_list/")
      .then((res) => {
        for (const data of res.data) {
          this.companyList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 복지관(훈련기관) 가져오기
    await this.$axios
      .get("datasets/api/team_list/")
      .then((res) => {
        for (const data of res.data) {
          this.teamList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 유저 데이터 가져와 vue data에 입력
    await this.$axios({
        method: "GET",
        url: "users/api/player/?id="+this.$store.state.userStore.id,
      })
      .then((res) => {
        this.data.username = res.data[0].username
        this.data.name = res.data[0].name
        this.data.email = res.data[0].email
        this.data.phoneNum = res.data[0].phoneNum
        this.data.team.id = res.data[0].team.id
        this.data.company.id = res.data[0].company.id
      })
      .catch((err) => {
        return err;
      });
   },

  methods: {

    //회원정보 수정
    submit() {
      console.log(this.data.team)
      console.log(this.data.company)
      this.$axios
        .post("users/api/detail/update_info/", {
            user: this.$store.state.userStore.id,
            data: {
              username: this.data.username,
              name: this.data.name,
              email: this.data.email,
              phoneNum: this.data.phoneNum,
            },
            category_data:{team:this.data.team.id, company: this.data.company.id,},
        })
        .then((res) => {
          console.log(res)
          return true;
        })
        .catch((err) => {
          console.log(err);
          return false;
        });

      this.$router.go(); // 현재 경로로 페이지 다시 이동
    },
  },
};
</script>

<style></style>
