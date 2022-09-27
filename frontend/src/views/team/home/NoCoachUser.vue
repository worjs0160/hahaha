<template>
    <v-container style="height:100%;">
        <!-- 미배치 선수 리스트 시작 -->
        <div class="title">
            <v-row>
                <v-col cols="12" class="d-flex justify-center pa-0">
                    <v-card-title style="font-weight:1000; padding:8px;">코치 미배치 선수({{users.length}}명)</v-card-title>
                </v-col>
            </v-row>
        </div>
        <v-row align="center">
            <v-col class="pb-0">
                <v-simple-table>
                    <thead>
                        <tr>
                            <th class="text-left">이름</th>
                            <th class="text-left">종목</th>
                            <th class="text-left">소속기업</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="users in users.slice (0, 3)" :key="users.name">
                            <td>{{ users.name }}</td>
                            <td v-if="users.sportType">{{ users.sportType.value }}</td>
                            <td v-if="!users.sportType">없음</td>
                            <td v-if="users.company">{{ users.company.value }}</td>
                            <td v-if="!users.company">없음</td>
                        </tr>
                    </tbody>
                </v-simple-table>
            </v-col>
        </v-row>
        <v-row class="justify-center">
            <v-card class="d-flex detail-btn justify-center" outlined @click="dialog = true" v-if="users.length > 3">
                <v-icon style="height:70%;">mdi-arrow-down-bold</v-icon>
            </v-card>
        </v-row>
        <!-- 미배치 선수 리스트 디테일 시작 -->
        <v-dialog v-model="dialog" max-width="600px" >
            <v-card class="dialog-card pa-3" outlined>
                <v-btn absolute right icon @click="dialog = false">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <div class="title mt-9">
                    <v-row>
                        <v-col cols="12" class="d-flex justify-center pt-0">
                            <v-card-title>트레이너 미배치 선수({{users.length}}명)</v-card-title>
                        </v-col>
                    </v-row>
                </div>
                <v-row>
                    <v-col style="padding:5px;">
                        <v-simple-table>
                            <thead>
                                <tr>
                                    <th class="text-left">이름</th>
                                    <th class="text-left">종목</th>
                                    <th class="text-left">소속기업</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="users in users" :key="users.name">
                                    <td>{{ users.name }}</td>
                                    <td v-if="users.sportType">{{ users.sportType.value }}</td>
                                    <td v-if="!users.sportType">없음</td>
                                    <td v-if="users.company">{{ users.company.value }}</td>
                                    <td v-if="!users.company">없음</td>
                                </tr>
                            </tbody>
                        </v-simple-table>
                    </v-col>
                </v-row>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>
export default {
  props: {
  },
  methods: {
  },
  data: () => ({
    users: [],
    dialog: false,
  }),

  async created() {
    await this.$axios({
      method: "GET",
      url:"users/api/player/null_players/?team=" + this.$store.state.userStore.team.id
    })
      .then((res) => {
        this.users=res.data
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      });
  },
};

</script>

<style scoped>
.title{
  border-bottom: 1px solid black;
}

.dialog-card{
  height: 500px;
}

.detail-btn {
  background-color: rgb(208, 208, 208);
  width: 90%;
  height: 20px;
  border: 0;
}

.v-dialog{
    background-color: white;
}
</style>