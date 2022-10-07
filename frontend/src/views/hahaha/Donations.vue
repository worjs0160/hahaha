<template>
  <v-row justify="center" class="mt-5">
    <v-col cols="9">
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
</template>

<script>

export default {
  data: () => ({
    donations:
      [{user: "위플레이 식당", title: "멸치 1팩 소세지 5개 메추리알 1팩", date: "2022-10-01", image: "이미지",},
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
  },
};
</script>

<style></style>
