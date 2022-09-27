<template>
  <v-container style="width:100%;">
    <v-row justify="center" style="text-align:center; background-color:#bfbfbf;" class="mt-3">
      <v-col cols="3">
        작성자
      </v-col>
      <v-col cols="3">
        제목
      </v-col>
      <v-col cols="3">
        진행
      </v-col>
      <v-col cols="3">
        결재일
      </v-col>
    </v-row>
    <v-row justify="center" style="text-align:center; border-bottom:0.5px solid gray;" class="mt-5">
      <v-col cols="3">
        허성만
      </v-col>
      <v-col cols="3">
        전국체전 참가
      </v-col>
      <v-col cols="3">
        승인필요
      </v-col>
      <v-col cols="3">
        2021.11.02
      </v-col>
    </v-row>
    <v-row justify="center" style="text-align:center; border-bottom:0.5px solid gray;" class="mt-5">
      <v-col cols="3">
        허성만
      </v-col>
      <v-col cols="3">
        연차휴가
      </v-col>
      <v-col cols="3">
        승인완료
      </v-col>
      <v-col cols="3">
        2021.11.02
      </v-col>
    </v-row>
    <v-row justify="center" style="text-align:center; border-bottom:0.5px solid gray;" class="mt-5">
      <v-col cols="3">
        허성만
      </v-col>
      <v-col cols="3">
        연차휴가
      </v-col>
      <v-col cols="3">
        반려
      </v-col>
      <v-col cols="3">
        2021.11.02
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    await this.loadingCover(false);
  },
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  }
};
</script>

<style></style>