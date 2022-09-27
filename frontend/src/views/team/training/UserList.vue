<template>
  <v-container fluid style="height: 100%">
    <v-toolbar height="50" elevation="0">
      <div class="d-flex align-center ma-2">
        <v-text-field
          placeholder="선수 검색"
          prepend-inner-icon="mdi-magnify"
          clearable
          clear-icon="mdi-close-thick"
          hide-details="auto"
          class="mr-2"
          style="width: 200px"
          v-model="search"
        >
        </v-text-field>
        <v-btn icon>
          <v-icon>mdi-filter-variant</v-icon>
        </v-btn>
      </div>
    </v-toolbar>
    <!-- 선수 카드 목록 영역 -->

    <v-slide-group show-arrows style="width: 100%; height: 91%">
      <div
        v-if="noData"
        class="text-center align-self-center"
        style="width: 100%"
      >
        <h1>등록된 선수가 없습니다.</h1>
      </div>
      <v-slide-item class="my-auto" v-for="user in users" :key="user.id">
        <!-- 유저 카드 -->
        <user-card v-bind:user="user" v-if="searchByName(user.name)">
          <v-card-actions
            class="d-flex flex-column justify-space-around border fill-height"
            style="width: 100%"
          >
            <v-btn
              class="mx-auto"
              width="70%"
              outlined
              @click="toTrainingRecord(user)"
              >훈련 일지 작성
            </v-btn>
          </v-card-actions>
          <template v-slot:chart>
            <p class="text-option" style="font-size:20px;">월간 훈련일지 상황</p>
            <div style="height:90%; width:50%;">
              <ChartDoughnut :chartData="chartDataDoughnut" />
            </div>
            <p class="text-option">월간 훈련 일지 : {{chartDataDoughnut.datasets[0].data[0]}}/{{chartDataDoughnut.datasets[0].data[0]+chartDataDoughnut.datasets[0].data[1]}} 작성</p>
          </template>
        </user-card>
      </v-slide-item>
    </v-slide-group>
  </v-container>
</template>

<script>
import UserCard from "/src/components/cards/UserCard";
import ChartDoughnut from "@/components/charts/ChartDoughnut.vue";
export default {
  data: () => ({
    search: "",
    noData: false,
    users: [],
    chartDataDoughnut: {
      datasets: [
      {
          data: [10, 20],
          backgroundColor: [
              'rgba(255, 150, 0, 0.5)',
              'rgba(0, 0, 0, 0.1)',
          ]
      }
      ],
      labels: ["완료 일지", "잔여 일지",]
    }
    // optionsDoughnut: {}
  }),
  components: {
    UserCard,
    ChartDoughnut,
  },
  async created() {
    await this.loadingCover(true);
    await this.$axios({
      method: "GET",
      url: "users/api/player/?is_active=true&team=" + this.$store.state.userStore.team.id,
    })
      .then((res) => {
        for (var i = 0; i < res.data.length; i++) {
          this.$set(this.users, i, res.data[i]); //팀으로 받아온 유저데이터 users에 복사
        }
      })
      .catch((res) => {
        console.log("Failed to get userList", res);
      })
      .finally(() => {
        if (this.users.length === 0) {
          this.noData = true;
        } else {
          this.noData = false;
        }
      });
    await this.loadingCover(false);
  },
  methods: {
    toTrainingRecord: function(user) {
      this.$store.commit("setSelectedUser", user);
      this.$emit("child", "TrainingRecord");
    },
    searchByName: function(name) {
      if (this.search.length === 0) {
        return true;
      } else if (name.includes(this.search)) {
        return true;
      } else {
        return false;
      }
    },
    // MainTraining으로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
};
</script>

<style scoped>
.border {
  border: solid 2px rgb(204, 198, 198);
}

.fill-height {
  height: 70%;
}
</style>
