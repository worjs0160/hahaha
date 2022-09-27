<template>
  <v-container style="height:100%;">
    <v-row>훈련기관 기업정보 화면입니다.</v-row>
      <v-row>
        <v-col cols="5" style="height:100%;">
          <v-card class="home-card">
            <v-col class="d-flex justify-center">
              <!-- <v-card-title>{{company.data[0][0]}} 선수 : {{company.data[0][1]}} {{company.data[0][1]}}</v-card-title> -->
            </v-col>
          </v-card>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    company: []
  }),
  async created() {
    await this.$axios({
      method: "POST",
      url: "datasets/test/" + this.$store.state.userStore.team.id
    })
      .then((res) => {
        console.log(res.data)
        this.company = res.data
      })
      .catch((res) => {
        console.log(res);
      })
  }
};
</script>

<style></style>