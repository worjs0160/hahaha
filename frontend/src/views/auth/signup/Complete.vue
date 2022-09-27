<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card elevation="2">
        <v-card-title class="text-h4">회원가입</v-card-title>
        <v-card-subtitle>위플레이 회원가입</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>
        <div class="mx-7">
          <v-container justify="center">
            <v-alert
                border="left"
                color="green"
                elevation="2"
                prominent
                type="success"
            >
                회원가입이 완료되었습니다.
            </v-alert>

            <v-btn block large class="mb-7" @click="moveToPage('Login')">
                로그인 페이지 이동
            </v-btn>
            </v-container>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
    methods:{
        moveToPage: function(val) {
            var router = this.$router;
            return router.push({ name: val });
        },
    },
};
</script>

<style></style>