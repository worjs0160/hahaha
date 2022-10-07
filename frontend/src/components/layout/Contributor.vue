<template>
  <v-app>
    <div class="inBox">
      <v-row justify="end">
        <v-col cols="1" align="end">
          <v-btn icon @click="logout()" style="background:rgb(244 244 244);">
            <v-icon>mdi-logout</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="5" align="center">
          <!-- 음식 기부하기 -->
          <v-row>
            <v-col cols="12" align="center">
              <v-card-title class="inBox-title">
                음식 기부하기
              </v-card-title>
            </v-col>
          </v-row>
          <v-row class="mt-7 mb-5">
            <v-col cols="3" align="start" style="font-size: 18px;">
              음식명
            </v-col>
            <v-col cols="9" align="start" style="border:1px solid;">
              <input
                style="width:100%;"
                type="text"
                placeholder=" (ex:멸치 1팩)"
              />
            </v-col>
          </v-row>

          <!-- 픽업시간 -->
          <v-row>
            <v-col cols="3" align="start" style="font-size: 18px;">
              픽업 시간
            </v-col>
            <v-col cols="9">
              <v-row>
                <v-col cols="4" align="start" style="border:1px solid; border-right:0px;">
                  <input
                    type="date"
                  />
                </v-col>
                <v-col cols="5" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                  <input
                    style="width:100%;"
                    type="time"
                  />
                </v-col>
                <v-col cols="2" align="start" class="pr-0">
                  부터
                </v-col>
              </v-row>
              <v-row class="mt-5">
                <v-col cols="4" align="start" style="border:1px solid; border-right:0px;">
                  <input
                    type="date"
                  />
                </v-col>
                <v-col cols="5" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                  <input
                    style="width:100%;"
                    type="time"
                  />
                </v-col>
                <v-col cols="2" align="start" class="pr-0">
                  까지
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <!-- 저장버튼 -->
          <v-row>
            <v-col align="end">
              <v-btn>
                저장
              </v-btn>
            </v-col>
          </v-row>
        </v-col>

        <v-spacer></v-spacer>

        <v-col cols="6" align="center">
          <v-row>
            <v-col cols="12">
              <v-card-title class="inBox-title">
                음식 기부내역
              </v-card-title>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" align="start">
              <div class="humansBox">
                <div class="humans-top">
                  <h2 class="pre-600">전체 기부현황<span> ({{this.donations.length}})</span></h2>
                </div>

                <v-row class="human" style="width:100%;" align="end">
                  <v-col cols="3" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;">식당명</p>
                  </v-col>
                  <v-col cols="5" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;">제목</p>
                  </v-col>
                  <v-col cols="4" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;">등록시간</p>
                  </v-col>
                </v-row>

                <div class="humans-btm mt-4 scroll-wrap" style="overflow-y:scroll; max-height: 200px;">
                  <v-row class="human" style="width:100%;" v-for="(item, idx) in this.donations" :key="`o-${idx}`" @click="select(item)">
                    <v-col cols="3"><p class="name pre-400 hidden_txt_line">{{item.user}}</p></v-col>
                    <v-col cols="5"><p class="name pre-400 hidden_txt_line">{{item.title}}</p></v-col>
                    <v-col cols="4"><p class="name pre-400 ">{{item.date}}</p></v-col>
                  </v-row>
                </div>

              </div><!--e:humansBox-->
            </v-col>
          </v-row>
          <v-row class="mt-3" v-if="this.selectItem.title">
            <v-col cols="12" align="start">
              <v-row align="center">
                <v-col cols="10">
                  {{selectItem.date}}
                </v-col>
                <v-col cols="2" align="end">
                  <v-btn icon @click="close()">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row class="line">
                <v-col cols="12">
                  기부음식명
                </v-col>
                <v-col cols="12" class="areaColor">
                  {{selectItem.title}}
                </v-col>
              </v-row>
              <v-row class="mt-10">
                <v-col cols="12">
                  이미지
                </v-col>
                <v-col cols="12" class="areaColor">
                  {{selectItem.image}}
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </div>
  </v-app>
</template>

<script>

export default {
  data: () => ({
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menu: false,
    donations: [{user: "위플레이 식당", title: "멸치 1팩 소세지 5개 메추리알 1팩", date: "2022-10-01", image: "이미지",},
                {user: "위플레이 식당", title: "멸치 1팩 소세지 5개", date: "2022-10-02", image: "이미지",},
                {user: "위플레이 식당", title: "멸치 1팩 메추리알 1팩", date: "2022-10-03", image: "이미지",},
                {user: "위플레이 식당", title: "소세지 5개 메추리알 1팩", date: "2022-10-04", image: "이미지",},
                {user: "위플레이 식당", title: "멸치 1팩", date: "2022-10-05", image: "이미지",},
                {user: "위플레이 식당", title: "멸치 1팩 소세지 5개 메추리알 1팩", date: "2022-10-06", image: "이미지",},
                {user: "위플레이 식당", title: "메추리알 1팩", date: "2022-10-07", image: "이미지",},
                {user: "위플레이 식당", title: "멸치 1팩 소세지 5개 메추리알 1팩", date: "2022-10-08", image: "이미지",},
                ],
    selectItem: {},
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
    select(val){
      this.selectItem = val
    },
    close() {
      this.selectItem = {}
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
  .inBox {
    width: 90% !important;
    margin: 80px auto;
  }
  .inBox-title{
    width:170px;
    background: rgb(84 195 255);
    justify-content: center;
    border-radius:10px;
  }
  .hidden_txt_line {
      width:80%;
      overflow:hidden;
      text-overflow:ellipsis;
      white-space:nowrap;
  }
  .line{
    border: 1px solid;
    border-right: 0px;
    border-bottom: 0px;
    border-left: 0px;
  }
  .areaColor {
    background: #F5F5F5;
    padding: 10px;
    border-radius: 6px;
  }
</style>
