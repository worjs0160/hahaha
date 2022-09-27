<template>
  <v-container style="width:100%;">
    <v-row justify="center" style="text-align:center; background-color:#bfbfbf;" class="mt-3">
      <v-col cols="2">
        작성자
      </v-col>
      <v-col cols="3">
        근무시간
      </v-col>
      <v-col cols="2">
        급여
      </v-col>
      <v-col cols="2">
        공제액
      </v-col>
      <v-col cols="3">
        지급급여
      </v-col>
    </v-row>
    <v-row justify="center" style="text-align:center; border-bottom:0.5px solid gray;" class="mt-5">
      <v-col cols="2">
        허성만
      </v-col>
      <v-col cols="3">
        72시간(60+12)
      </v-col>
      <v-col cols="2">
        627,840
      </v-col>
      <v-col cols="2">
        27,840
      </v-col>
      <v-col cols="3">
        600,000
      </v-col>
    </v-row>
    <v-row justify="center" style="text-align:center; border-bottom:0.5px solid gray;" class="mt-5">
      <v-col cols="2">
        허성만
      </v-col>
      <v-col cols="3">
        72시간(60+12)
      </v-col>
      <v-col cols="2">
        627,840
      </v-col>
      <v-col cols="2">
        27,840
      </v-col>
      <v-col cols="3">
        600,000
      </v-col>
    </v-row>
    <v-row justify="center" style="text-align:center; border-bottom:0.5px solid gray;" class="mt-5">
      <v-col cols="2">
        허성만
      </v-col>
      <v-col cols="3">
        72시간(60+12)
      </v-col>
      <v-col cols="2">
        627,840
      </v-col>
      <v-col cols="2">
        27,840
      </v-col>
      <v-col cols="3">
        600,000
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