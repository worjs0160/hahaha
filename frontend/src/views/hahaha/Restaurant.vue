<template>
  <v-row justify="center" class="mt-5">
    <v-col cols="9">
      <v-row>
        <v-col cols="6" align="start">
          <div class="humansBox">
            <div class="humans-top">
              <h2 class="pre-600">가입한 가게 현황<span> ({{this.users.length}})</span></h2>
            </div>

            <div class="humans-btm mt-3 pt-3 scroll-wrap" style="overflow-y:scroll; max-height: 550px;">
              <v-row class="human" style="width:100%; background: #fff5b0;" v-for="(item, idx) in this.users" :key="`o-${idx}`">
                <v-col cols="12"><p class="name pre-400 hidden_txt_line">{{item.name}}</p></v-col>
              </v-row>
            </div>

          </div><!--e:humansBox-->
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>

export default {
  data: () => ({
    users:[
      {name: "가게이름1",},
      {name: "가게이름2",},
      {name: "가게이름3",},
      {name: "가게이름4",},
      {name: "가게이름5",},
      {name: "가게이름6",},
      {name: "가게이름7",},
      {name: "가게이름8",},
      {name: "가게이름9",},
      {name: "가게이름10",},
      {name: "가게이름11",},
      {name: "가게이름12",},
      ],
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
    // next() {
    //   this.checkSmsNumber()
    //   // this.find_id();
    // },
  },
};
</script>

<style></style>
