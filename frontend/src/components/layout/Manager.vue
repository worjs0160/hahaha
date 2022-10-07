<template>
  <v-app>
    <div class="inBox">
      <v-row justify="end">
        <v-col cols="1" align="end" class="pt-0">
          <v-btn icon @click="logout()" style="background:rgb(244 244 244);">
            <v-icon>mdi-logout</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4" align="center" v-for="(item, idx) in this.selectName" :key="`o-${idx}`">
          <v-card-title class="button-style" :class="{ yellow:changeColor == idx}" @click="change(idx)">
            {{selectName[idx]}}
          </v-card-title>
        </v-col>
      </v-row>
      <v-row class="mt-5" justify="center" v-if="this.selectComponent == 'main'">
        <img :src="require('@/views/auth/hahaha.png')" style="width:40%; height:40%;">
      </v-row>
      <v-row class="mt-5" v-if="this.selectComponent != 'main'">
        <component
          :is="this.selectComponent"
        ></component>
      </v-row>
    </div>
  </v-app>
</template>

<script>

export default {
  data: () => ({
    selectComponent: "main",
    selectName:["기부상점목록", "캘린더", "기부현황"],
    changeColor: -1,
  }),
  watch: {
    // "data.name": function() {
    //   if(!this.data.name) {
    //     this.err.nameErrMsg = "필수 정보입니다."
    //   }
    //   else this.err.nameErrMsg = ""
    // },
  },
  methods: {
    change(val) {
      if(val == 0){
        this.selectComponent = "Restaurant"
        this.changeColor = val
      }
      else if(val == 1){
        this.selectComponent = "Calendar"
        this.changeColor = val
      }
      else if(val == 2){
        this.selectComponent = "Donations"
        this.changeColor = val
      }
    },
    logout() {
      sessionStorage.clear();
      var router = this.$router;
      return router.push({ name: "Login" });
    },
  },
};
</script>

<style>
.button-style{
  width:170px;
  background: rgb(84 195 255);
  justify-content: center;
}
.yellow{
  background: #fff5b0;
}
</style>
