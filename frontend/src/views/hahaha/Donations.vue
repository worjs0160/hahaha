<template>
    <div style="width:100%; height:600px;">
      <div class="donationsInBox">

      <!-- 토스트 메시지 -->
      <v-snackbar
        :color="color"
        absolute
        v-model="snackbar"
        :timeout="timeout"
        center
        top
      >
        <v-icon class="mr-2">mdi-check</v-icon>
        <span>{{ this.$store.state.toast.message }}</span>
        <template v-slot:action="{ attrs }">
          <v-btn color="white" text v-bind="attrs" @click="snackbar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>

      <v-row>
        <v-col cols="5" align="center">
          <v-row>
            <v-col cols="12">
              <v-card-title class="inBox-title pa-1">
                음식 기부내역
              </v-card-title>
            </v-col>
          </v-row>
          <v-row class="scroll-wrap" style="overflow-y:scroll; max-height: 700px;">
            <div class="scroll-cover"></div>

            <v-col cols="12" align="start">
              <div class="humansBox">
                <div class="humans-top">
                  <h2 class="pre-600">전체 기부현황<span> ({{count}})</span></h2>
                </div>

                <div class="humansBox" v-if="count==0">
                  <div class="humans-top">
                    <h2 class="pre-600">등록된 기부내역이 없습니다.</h2>
                  </div>
                </div>

                <div v-if="count>0">
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

                  <div class="humans-btm mt-4">
                    <v-row class="human" style="width:100%;" v-for="(item, idx) in this.donations" :key="`o-${idx}`" @click="select(item, donateTimes[idx].startPickUp, donateTimes[idx].endPickUp)">
                      <v-col cols="3"><p class="name pre-400 hidden_txt_line">{{item.donator.storeName}}</p></v-col>
                      <v-col cols="5"><p class="name pre-400 hidden_txt_line">{{item.foodName}}</p></v-col>
                      <v-col cols="4"><p class="name pre-400 ">{{donateTimes[idx].createdTime}}</p></v-col>
                    </v-row>
                  </div>
                </div>

              </div><!--e:humansBox-->
            </v-col>
          </v-row>
        </v-col>

        <v-spacer></v-spacer>

        <v-col cols="6">
          <!-- 선택한 기부내역 상세보기 영역 -->
          <v-row>
            <v-col cols="12" align="center">
              <v-card-title class="inBox-title pa-1">
                상세보기
              </v-card-title>
            </v-col>
          </v-row>
          <v-row class="mt-3 scroll-wrap" style="max-height:630px; overflow-y: scroll;" v-if="this.selectItem.foodName && this.change == false">
            <div class="scroll-cover"></div>
            <v-col>
              <v-row>
                <v-col cols="12" align="start">
                  <v-row align="center">
                    <v-col cols="10">
                      픽업시간 : {{startPickUp}} ~ {{endPickUp}}
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
                      {{selectItem.foodName}}
                    </v-col>
                  </v-row>

                  <v-row class="mt-10">
                    <v-col cols="12">
                      이미지
                    </v-col>
                    <v-col cols="3" align="center" v-for="(foodImages, idx) in selectItem.foodImage" :key="`o-${idx}`">
                      <v-img :src="foodImages.images" style="width: 100px; height: 100px;"></v-img>
                    </v-col>
                  </v-row>

                  <v-row class="line mt-10" v-if="selectItem.comment">
                    <v-col cols="12">
                      코멘트
                    </v-col>
                    <v-col cols="12" class="areaColor">
                      {{selectItem.comment}}
                    </v-col>
                  </v-row>
                  <v-row class="mt-10" v-if="selectItem.comment">
                    <v-col cols="12">
                      활동사진
                    </v-col>
                    <v-col cols="3" align="center" v-for="(commentImages, idx) in selectItem.commentImage" :key="`o-${idx}`">
                      <v-img :src="commentImages.images" style="width: 100px; height: 100px;"></v-img>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
              <v-row justify="end" class="mt-7">
                <v-col cols="2" align="end">
                  <v-btn outlined @click="dialogChange(true), commentItem(selectItem), dialogCoverSet(true)" style="background:rgb(244 244 244); border: none;">
                    코멘트
                  </v-btn>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <!-- 선택한 기부내역 상세보기 영역 종료 -->
        </v-col>
      </v-row>
      </div>
    </div>

</template>

<script>

export default {
  data: () => ({
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menu: false,

    startDate: "",
    startTime: "",
    endDate: "",
    endTime: "",
    startPickUp: "",
    endPickUp: "",

    donationInfo:{donator: "", foodName: "", startPickUp : "", endPickUp: "",},
    donations: [], // 기부내용 저장 할 변수
    donateTimes:[], // 기부내용들의 시간 재정의 데이터 (T와 초단위까지 나오는 데이터 정리)
    count: 0,
    selectItem: {},
    updateItem: {},
    change: false,
    timeout: 2000, // 알림창 타임아웃
    dialogCoverState: false,
  }),
  created() {
    this.donationInfo.donator = this.$store.state.userStore.id
    this.getDonations()
  },
  watch: {
    // "data.name": function() {
    //   if(!this.data.name) {
    //     this.err.nameErrMsg = "필수 정보입니다."
    //   }
    //   else this.err.nameErrMsg = ""
    // },
  },
  methods: {
    select(val, start, end){
      this.selectItem = JSON.parse(JSON.stringify(val));
      this.startPickUp = JSON.parse(JSON.stringify(start));
      this.endPickUp = JSON.parse(JSON.stringify(end));
    },
    close() {
      this.selectItem = {}
    },
    
    getDonations(){
      this.$axios({
        method: "GET",
        url:"donates/api/donateAndImageInfo/"
      }).then((res) => {
        var startPickUp
        var endPickUp
        var createdTime

        this.donations = res.data
        this.count = res.data.length
        //기부내용 시간 데이터의 형식 재정의(T제거, 시간초 및 소수점 제거)
        for(var a=0; a<this.donations.length; a++){
          startPickUp = this.donations[a].startPickUp.substr(0,10)+" "+this.donations[a].startPickUp.substr(11,5)
          endPickUp = this.donations[a].endPickUp.substr(0,10)+" "+this.donations[a].endPickUp.substr(11,5)
          createdTime = this.donations[a].createdTime.substr(0,10)+" "+this.donations[a].createdTime.substr(11,5)
          this. donateTimes.push({
            startPickUp: startPickUp,
            endPickUp: endPickUp,
            createdTime: createdTime,
          })
        }
      })
    },
    dialogCoverSet(state){
      this.$emit("dialogCoverSet",state);
    },
    dialogChange(state){
      this.$emit("dialogChange",state);
    },
    commentItem(item){
      var updateStartDate = JSON.parse(JSON.stringify(item.startPickUp.substr(0,10)));
      var updateStartTime = JSON.parse(JSON.stringify(item.startPickUp.substr(11,5)));
      var updateEndDate = JSON.parse(JSON.stringify(item.endPickUp.substr(0,10)));
      var updateEndTime = JSON.parse(JSON.stringify(item.endPickUp.substr(11,5)));

      this.$emit("commentItem",item, updateStartDate, updateStartTime, updateEndDate, updateEndTime);
    },
    reloadSelect(val){
      this.$axios({
        method: "GET",
        url:"donates/api/donateAndImageInfo/"+val
      }).then((res) => {
        this.selectItem = res.data
      })
    },
  },
  computed: {
    idx: {
      get() {
        return this.$store.state.tabStore.idx;
      },
      set() {
        return;
      },
    },
    color: {
      get() {
        return this.$store.getters.getColor;
      },
      set() {},
    },
    snackbar: {
      get() {
        return this.$store.getters.getSnackbar;
      },
      set(val) {
        this.$store.commit("setSnackbar", val);
      },
    },
  },
};
</script>

<style>
  .donationsInBox {
    width: 90%;
    margin: 20px auto;
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
  .page-cover {
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 10;
    background-color: rgb(255, 255, 255);
  }
</style>
