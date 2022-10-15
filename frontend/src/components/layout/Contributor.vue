<template>
  <v-app>
    <div class="inBox">

      <!-- 토스트 메시지 -->
      <v-snackbar
        :color="color"
        absolute
        v-model="snackbar"
        :timeout="timeout"
        center
        top
        style="z-index:100;"
      >
        <v-icon class="mr-2">mdi-check</v-icon>
        <span>{{ this.$store.state.toast.message }}</span>
        <template v-slot:action="{ attrs }">
          <v-btn color="white" text v-bind="attrs" @click="snackbar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>

      <v-row justify="end">
        <v-col cols="1" align="end">
          <v-btn outlined @click="logout()" style="background:rgb(244 244 244); border: none;">
            로그아웃
            <!-- 아이콘 사용시 v-btn에 icon 붙혀줘야함 -->
            <!-- <v-icon>mdi-logout</v-icon> -->
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
                v-model="donationInfo.foodName"
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
                    v-model="startDate"
                  />
                </v-col>
                <v-col cols="5" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                  <input
                    style="width:100%;"
                    type="time"
                    v-model="startTime"
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
                    v-model="endDate"
                  />
                </v-col>
                <v-col cols="5" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                  <input
                    style="width:100%;"
                    type="time"
                    v-model="endTime"
                  />
                </v-col>
                <v-col cols="2" align="start" class="pr-0">
                  까지
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <v-row class="mt-7 mb-5">
            <v-col cols="3" align="start" style="font-size: 18px;">
              음식 사진
            </v-col>
            <v-col cols="9" align="start">
              <v-file-input
                label="클릭하여 사진 첨부"
                hide-details="auto"
                style="width:200px; z-index:1;"
                class="pt-0 mt-0 custom1"
                prepend-icon=""
                @change="preview_createImage"
                outlined
                dense
                multiple
              ></v-file-input>
            </v-col>
          </v-row>
          <v-row class="mt-3 mb-5">
            <v-col cols="2" align="start">
            </v-col>
            <v-col cols="3" align="center" v-for="(foodImages, idx) in createUrl" :key="`o-${idx}`">
              <v-img :src="foodImages" style="width: 100px; height: 100px;"></v-img>
            </v-col>
          </v-row>

          <!-- 저장버튼 -->
          <v-row>
            <v-col align="end">
              <v-btn @click="donationSave()">
                저장
              </v-btn>
            </v-col>
          </v-row>
        </v-col>

        <v-spacer></v-spacer>

        <v-col cols="6" align="center" class="scroll-wrap" style="max-height:630px; overflow-y: scroll;">
          <div class="scroll-cover"></div>
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
                  <h2 class="pre-600">전체 기부현황<span> ({{count}})</span></h2>
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

                <div class="humans-btm mt-4">
                  <v-row class="human" style="width:100%;" v-for="(item, idx) in this.donations" :key="`o-${idx}`" @click="select(item, donateTimes[idx].startPickUp, donateTimes[idx].endPickUp)">
                    <v-col cols="3"><p class="name pre-400 hidden_txt_line">{{item.donator.storeName}}</p></v-col>
                    <v-col cols="5"><p class="name pre-400 hidden_txt_line">{{item.foodName}}</p></v-col>
                    <v-col cols="4"><p class="name pre-400 ">{{donateTimes[idx].createdTime}}</p></v-col>
                  </v-row>
                </div>

              </div><!--e:humansBox-->
            </v-col>
          </v-row>

          <!-- 선택한 기부내역 상세보기 영역 -->
          <v-row class="mt-3" v-if="this.selectItem.foodName && this.change == false">
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
                    <v-col cols="3" align="center" v-for="(commentImage, idx) in selectItem.commentImage" :key="`o-${idx}`">
                      <v-img :src="commentImage.images" style="width: 100px; height: 100px;"></v-img>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
              <v-row justify="end" class="mt-9">
                <v-col cols="2" align="end">
                  <v-btn outlined @click="change=true, selectUpdateItem(selectItem), dialogCoverSet(true)" style="background:rgb(244 244 244); border: none;">
                    수정
                  </v-btn>
                </v-col>
                <v-col cols="2" align="end">
                  <v-btn outlined @click="Delete(selectItem)" style="background:rgb(244 244 244); border: none;">
                    삭제
                  </v-btn>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <!-- 선택한 기부내역 상세보기 영역 종료 -->
        </v-col>
      </v-row>
    </div>

    <!-- 선택한 기부내역 수정 영역 -->
    <div class="scroll-hidden" style="
      width:100%;
      height:100vh;
      display:flex;
      jutify-content:center;
      align-items:center;
      padding:50px 0;
      overflow-y: scroll;
      position:absolute;
      z-index: 99;
      "
      v-if="this.updateItem && this.change == true"
    >
      <div class="manage-val3-wrap" style="
          width: 720px;
          background: #FFFFFF;
          box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
          border-radius: 20px;
          margin: 0 auto !important;
          ">

        <v-row justify="center" class="pa-7">
          <v-col cols="12" align="center">
            <!-- 음식 기부하기 -->
            <v-row>
              <v-col cols="12" align="center">
                <v-card-title class="inBox-title">
                  음식 기부하기
                </v-card-title>
              </v-col>
            </v-row>
            <v-row class="mt-7 mb-5">
              <v-col cols="2" align="start" style="font-size: 18px;">
                음식명
              </v-col>
              <v-col cols="10" align="start" style="border:1px solid;">
                <input
                  style="width:100%;"
                  type="text"
                  placeholder=" (ex:멸치 1팩)"
                  v-model="updateItem.foodName"
                />
              </v-col>
            </v-row>

            <!-- 픽업시간 -->
            <v-row>
              <v-col cols="2" align="start" style="font-size: 18px;">
                픽업 시간
              </v-col>
              <v-col cols="10">
                <v-row>
                  <v-col cols="4" align="start" style="border:1px solid; border-right:0px;">
                    <input
                      type="date"
                      v-model="updateStartDate"
                    />
                  </v-col>
                  <v-col cols="5" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                    <input
                      style="width:100%;"
                      type="time"
                      v-model="updateStartTime"
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
                      v-model="updateEndDate"
                    />
                  </v-col>
                  <v-col cols="5" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                    <input
                      style="width:100%;"
                      type="time"
                      v-model="updateEndTime"
                    />
                  </v-col>
                  <v-col cols="2" align="start" class="pr-0">
                    까지
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <!-- 픽업시간 종료 -->

            <v-row class="mt-7 mb-5">
              <v-col cols="2" align="start" style="font-size: 18px;">
                음식 사진
              </v-col>
              <v-col cols="10" align="start">
                <v-file-input
                  label="클릭하여 사진 첨부"
                  hide-details="auto"
                  style="width:200px; z-index:1;"
                  class="pt-0 mt-0 custom1"
                  prepend-icon=""
                  @change="preview_updateImage"
                  outlined
                  dense
                  multiple
                ></v-file-input>
              </v-col>
            </v-row>
            <v-row class="mt-3 mb-5">
              <v-col cols="2" align="start">
                미리보기
              </v-col>
              <v-col cols="3" align="center" v-for="(foodImages, idx) in updateUrl" :key="`o-${idx}`">
                <v-img :src="foodImages" style="width: 100px; height: 100px;"></v-img>
              </v-col>
            </v-row>

            <v-row justify="end" class="mt-9">
              <v-col cols="2" align="end">
                <v-btn outlined @click="Update()" style="background:rgb(244 244 244); border: none;">
                  저장
                </v-btn>
              </v-col>
              <v-col cols="2" align="end">
                <v-btn outlined @click="url = [], change=false, dialogCoverSet(false)" style="background:rgb(244 244 244); border: none;">
                  취소
                </v-btn>
              </v-col>
            </v-row>

          </v-col>
        </v-row>

      </div>
    </div>
    <!-- 선택한 기부내역 수정 영역 종료 -->
  </v-app>
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

    updateStartDate: "",
    updateStartTime: "",
    updateEndDate: "",
    updateEndTime: "",

    donationInfo:{donator: "", foodName: "", startPickUp : "", endPickUp: "", foodImage: [],},
    donations: [], // 기부내용 저장 할 변수
    donateTimes:[], // 기부내용들의 시간 재정의 데이터 (T와 초단위까지 나오는 데이터 정리)
    count: 0,
    selectItem: {},
    updateItem: {},
    change: false,
    timeout: 2000, // 알림창 타임아웃
    dialogCoverState: false,

    updateImage: [],
    createUrl: [], // 생성시 미리보기용 url
    updateUrl: [], // 수정시 미리보기용 url
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
    logout() {
      sessionStorage.clear();
      var router = this.$router;
      return router.push({ name: "Login" });
    },
    getDonations(){
      this.$axios({
        method: "GET",
        url:"donates/api/donateAndImageInfo/?donator="+this.$store.state.userStore.id
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
    reloadSelect(val){
      this.$axios({
        method: "GET",
        url:"donates/api/donateAndImageInfo/"+val
      }).then((res) => {
        this.selectItem = res.data
      })
    },
    async donationSave(){
      this.donationInfo.startPickUp = this.startDate + "T" + this.startTime
      this.donationInfo.endPickUp = this.endDate + "T" + this.endTime

      let sendImgData = []
      let sendImg = []

      // 넣은 이미지가 있으면 이미지데이터 생성
      if(this.updateImage.length > 0){
        for(var i=0; i < this.updateImage.length; i++){
          if(this.updateImage[i] != null){
            var getImageSize = await this.getImageSize(this.updateImage[i])


            var formData = new FormData();
            formData.append("images", this.updateImage[i]);
            formData.append("width", getImageSize.width);
            formData.append("height", getImageSize.width);
            
            var result = await this.$axios({
              method: 'POST',
              url: "donates/api/foodImage/",
              headers: {
                "Content-Type": "multipart/form-data"
              },
              data: formData
            })
            var id = result.data.id
            var images = result.data.images
            var width = result.data.width
            var height = result.data.height
            sendImgData.push(id)
            sendImg.push({'images':images,'id':id,'width':width,'height':height})

            this.donationInfo.foodImage = sendImgData
          }
        }
      }

      if(this.donationInfo.foodName.length <= 0){
        this.$store.dispatch("callToast", {
          msg: "기부 할 음식명을 입력해주세요.",
          result: "error",
        });
      }
      else if(this.startDate.length < 1 || this.startTime.length < 1 || this.endDate.length < 1 || this.endTime.length < 1){
        this.$store.dispatch("callToast", {
          msg: "픽업가능 날짜를 선택해주세요.",
          result: "error",
        });
      }
      else{
        this.$axios({
          method: "POST",
          url: "donates/api/donateInfo/",
          data: this.donationInfo,
        }).then(() => {
          this.$store.dispatch("callToast", {
            msg: "기부내용이 등록되었습니다.",
            result: "success",
          });

          //등록 후 기부내역 리로드
          this.getDonations()

          //등록 후 입력 데이터 초기화
          this.donationInfo = {donator: this.$store.state.userStore.id, foodName: "", startPickUp : "", endPickUp: "",}
          this.startDate = ""
          this.startTime = ""
          this.endDate = ""
          this.endTime = ""
          this.createUrl = []
        });
      }
    },
    selectUpdateItem(val){
      this.updateItem = JSON.parse(JSON.stringify(val));
      this.updateStartDate = JSON.parse(JSON.stringify(val.startPickUp.substr(0,10)));
      this.updateStartTime = JSON.parse(JSON.stringify(val.startPickUp.substr(11,5)));
      this.updateEndDate = JSON.parse(JSON.stringify(val.endPickUp.substr(0,10)));
      this.updateEndTime = JSON.parse(JSON.stringify(val.endPickUp.substr(11,5)));
    },
    async Update(){
      this.updateItem.startPickUp = this.updateStartDate +"T"+ this.updateStartTime
      this.updateItem.endPickUp = this.updateEndDate +"T"+ this.updateEndTime
      this.startPickUp = this.updateStartDate +" "+ this.updateStartTime
      this.endPickUp = this.updateEndDate +" "+ this.updateEndTime

      this.updateItem.donator = this.$store.state.userStore.id

      let sendImgData = []
      let sendImg = []

      // 넣은 이미지가 있으면 이미지데이터 생성
      if(this.updateImage.length > 0){
        for(var i=0; i < this.updateImage.length; i++){
          if(this.updateImage[i] != null){
            var getImageSize = await this.getImageSize(this.updateImage[i])


            var formData = new FormData();
            formData.append("images", this.updateImage[i]);
            formData.append("width", getImageSize.width);
            formData.append("height", getImageSize.width);
            
            var result = await this.$axios({
              method: 'POST',
              url: "donates/api/foodImage/",
              headers: {
                "Content-Type": "multipart/form-data"
              },
              data: formData
            })
            var id = result.data.id
            var images = result.data.images
            var width = result.data.width
            var height = result.data.height
            sendImgData.push(id)
            sendImg.push({'images':images,'id':id,'width':width,'height':height})

            this.updateItem.foodImage = sendImgData
          }
        }
      }

      if(this.updateItem.foodName.length <= 0){
        this.$store.dispatch("callToast", {
          msg: "기부 할 음식명을 입력해주세요.",
          result: "error",
        });
        return 0;
      }
      else if(this.updateStartDate.length < 1 || this.updateStartTime.length < 1 || this.updateEndDate.length < 1 || this.updateEndTime.length < 1){
        this.$store.dispatch("callToast", {
          msg: "픽업가능 날짜를 선택해주세요.",
          result: "error",
        });
        return 0;
      }
      else{
        this.$axios({
          method: "PATCH",
          url:"donates/api/donateInfo/" + this.updateItem.id+ "/",
          data: this.updateItem,
        }).then((res) => {
          this.$store.dispatch("callToast", {
            msg: "기부내역을 수정하였습니다.",
            result: "success",
          });

          this.selectItem = JSON.parse(JSON.stringify(this.updateItem));
          this.upodateItem = {}
          this.updateStartDate = ""
          this.updateStartTime = ""
          this.updateEndDate = ""
          this.updateEndTime = ""

          this.change = false
          this.updateUrl = []
          this.dialogCoverSet(false)
          this.getDonations()
          this.reloadSelect(res.data.id)
        });
      }
    },
    Delete(val){
        this.$axios({
          method: "DELETE",
          url:"donates/api/donateInfo/" +val.id +"/",
        }).then(() => {
          this.$store.dispatch("callToast", {
            msg: "기부내역을 삭제하였습니다.",
            result: "error",
          });
          this.selectItem = {}
          this.getDonations()
        });
    },
    dialogCoverSet(state){
      if(state){
        document.getElementById('top_cover').classList.replace('off', 'on');
      }else{
        document.getElementById('top_cover').classList.replace('on', 'off');
      }
      this.dialogCoverState = state;
    },
    getImageSize : async function(image){
      let _URL = window.URL || window.webkitURL;
      let objectUrl = _URL.createObjectURL(image);
      return new Promise((resolve, reject) => {
        let img = new Image()
        img.onload = () => resolve({
        width : img.width,
        height : img.height
        })
        img.onerror = reject
        img.src = objectUrl
      })
    },
    preview_updateImage(images) {
      this.updateUrl = [] // 기부내용 저장, 수정, 취소 후엔 초기화 해줘야함
      for(var i=0; i < images.length; i++){
        if(images[i] != null){
          this.updateUrl.push(URL.createObjectURL(images[i]))
        }
      }
      this.updateImage = images
    },
    preview_createImage(images) {
      this.createUrl = [] // 기부내용 저장, 수정, 취소 후엔 초기화 해줘야함
      for(var i=0; i < images.length; i++){
        if(images[i] != null){
          this.createUrl.push(URL.createObjectURL(images[i]))
        }
      }
      this.updateImage = images
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
