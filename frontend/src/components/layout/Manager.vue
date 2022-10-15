<template>
  <v-app style="height:60vh;">
    <div class="manageInbox">
      <v-row justify="end">
        <v-col cols="1" align="end" class="pt-0">
          <v-btn outlined @click="logout()" style="background:rgb(244 244 244);">
            로그아웃
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
        <img :src="require('@/views/auth/hahaha.png')" style="width:40%;">
      </v-row>
      <v-row class="pa-3" v-if="this.selectComponent != 'main'">
        <component
          :is="this.selectComponent"
          ref="childComponent"
          @dialogCoverSet="dialogCoverSet"
          @dialogChange="dialogChange"
          @commentItem="commentItem"
        ></component>
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
      v-if="this.updateItem && this.dialogChangeState == true"
    >
      <div class="manage-val3-wrap pa-3 scroll-wrap" style="
          width: 720px;
          max-height:850px;
          background: #FFFFFF;
          box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
          border-radius: 20px;
          margin: 0 auto !important;
          overflow-y: scroll;
          ">
        <div class="scroll-cover"></div>
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
                  readonly
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
                  <v-col cols="2" align="start" style="border:1px solid; border-right:0px;">
                    <input
                      type="date"
                      v-model="updateStartDate"
                      readonly
                    />
                  </v-col>
                  <v-col cols="3" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                    <input
                      style="width:100%;"
                      type="time"
                      v-model="updateStartTime"
                      readonly
                    />
                  </v-col>
                  <v-col cols="2" align="start" class="pr-0">
                    부터
                  </v-col>
                </v-row>
                <v-row class="mt-5">
                  <v-col cols="2" align="start" style="border:1px solid; border-right:0px;">
                    <input
                      type="date"
                      v-model="updateEndDate"
                      readonly
                    />
                  </v-col>
                  <v-col cols="3" align="start" class="pr-0" style="border:1px solid; border-left:0px;">
                    <input
                      style="width:100%;"
                      type="time"
                      v-model="updateEndTime"
                      readonly
                    />
                  </v-col>
                  <v-col cols="2" align="start" class="pr-0">
                    까지
                  </v-col>
                </v-row>
              </v-col>
            </v-row>

            <v-row class="mt-10">
              <v-col cols="12" align="start">
                이미지
              </v-col>
              <v-col cols="3" align="center" v-for="(foodImages, idx) in updateItem.foodImage" :key="`o-${idx}`">
                <v-img :src="foodImages.images" style="width: 100px; height: 100px;"></v-img>
              </v-col>
            </v-row>

            <v-row class="mt-10 mb-2">
              <v-col cols="2" align="start" style="font-size: 18px;">
                코멘트
              </v-col>
              <v-col cols="10" align="start" style="border:1px solid;">
                <input
                  style="width:100%;"
                  type="text"
                  placeholder=""
                  v-model="updateItem.comment"
                />
              </v-col>
            </v-row>
            <v-row class="ma-0" v-if="err.commentMessage">
              <v-col cols="2">
                
              </v-col>
              <v-col cols="10" align="start" class="pa-0">
                <span class="manage-val1-errBox pre-400" style="color: red;">
                  {{err.commentMessage}}
                </span>
              </v-col>
            </v-row>
            <v-row class="mt-10">
              <v-col cols="2" align="start" style="font-size: 18px;">
                활동사진
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
              <v-col cols="12" align="start">
                미리보기
              </v-col>
              <v-col cols="3" align="center" v-for="(activityImages, idx) in updateUrl" :key="`o-${idx}`">
                <v-img :src="activityImages" style="width: 100px; height: 100px;"></v-img>
              </v-col>
            </v-row>

            <v-row justify="end" class="mt-9">
              <v-col cols="2" align="end">
                <v-btn outlined v-if="!commentValidFlag" style="background:rgb(244 244 244); border: none;">
                  확인
                </v-btn>
                <v-btn outlined v-if="commentValidFlag" @click="dialogChangeState=false, dialogCoverSet(false), Update(), dataReload()" style="background:rgb(244 244 244); border: none;">
                  확인
                </v-btn>
              </v-col>
              <v-col cols="2" align="end">
                <v-btn outlined @click="dialogChangeState=false, dialogCoverSet(false), dataReload()" style="background:rgb(244 244 244); border: none;">
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
    selectComponent: "main",
    selectName:["기부상점목록", "캘린더", "기부현황"],
    changeColor: -1,
    dialogCoverState:false,
    dialogChangeState:false,

    updateItem:[],
    updateStartDate: "",
    updateStartTime: "",
    updateEndDate: "",
    updateEndTime: "",
    donatorId: 0,

    updateUrl: [],
    updateImage: [],

    comment: "",
    commentValidFlag: false,
    err:[{
      commentMessage: "",
    }],
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
    dialogCoverSet(state){
      if(state){
        document.getElementById('top_cover').classList.replace('off', 'on');
      }else{
        document.getElementById('top_cover').classList.replace('on', 'off');
      }
      this.dialogCoverState = state;
    },
    dialogChange(state){
      this.dialogChangeState = state;
    },
    commentItem(item, updateStartDate, updateStartTime, updateEndDate, updateEndTime, id){
      this.updateItem = JSON.parse(JSON.stringify(item));
      this.updateStartDate = JSON.parse(JSON.stringify(updateStartDate));
      this.updateStartTime = JSON.parse(JSON.stringify(updateStartTime));
      this.updateEndDate = JSON.parse(JSON.stringify(updateEndDate));
      this.updateEndTime = JSON.parse(JSON.stringify(updateEndTime));
      this.donatorId = JSON.parse(JSON.stringify(item.donator.id));
    },
    async Update(){
      this.updateItem.donator = this.donatorId

      let foodImage = []

      //기존에 있는 음식사진의 데이터를 dict에서 pk값으로 바꿔줌(저장형식때문에 진행)
      if(this.updateItem.foodImage.length > 0){
        for(var i=0; i < this.updateItem.foodImage.length; i++){
          foodImage.push(JSON.parse(JSON.stringify(this.updateItem.foodImage[i].id)))
          console.log(this.updateItem.foodImage[i].id)
        }
        this.updateItem.foodImage = JSON.parse(JSON.stringify(foodImage))
      }

      let sendImgData = []

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
              url: "donates/api/activityImage/",
              headers: {
                "Content-Type": "multipart/form-data"
              },
              data: formData
            })
            var id = result.data.id
            sendImgData.push(id)

            this.updateItem.commentImage = sendImgData
          }
        }
      }
      this.$axios({
        method: "PATCH",
        url:"donates/api/donateInfo/" + this.updateItem.id+ "/",
        data: this.updateItem,
      }).then(() => {
        this.$store.dispatch("callToast", {
          msg: "코멘트가 작성되었습니다.",
          result: "success",
        });
        this.updateUrl = []
        this.dataReload(this.updateItem.id)
        this.$refs.childComponent.select(this.updateItem, this.updateStartDate+" "+this.updateStartTime, this.updateEndDate+" "+this.updateEndTime)
      });
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
    dataReload(val){
      this.$refs.childComponent.getDonations();
      this.$refs.childComponent.reloadSelect(val);
    },
    commentValid(){
      this.commentValidFlag = false
      if(!this.updateItem.comment){
        this.err.commentMessage = "코멘트 작성은 필수입니다."
      }
      else{
        this.commentValidFlag = true
        this.err.commentMessage = ""
      }
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
  },
  watch:{
    "updateItem.comment": function() {
      // 코멘트 체크
      this.commentValid();
    },
  },
};
</script>

<style>
.manageInbox {
  width: 90%;
  margin: 30px auto;
}
.button-style{
  width:170px;
  background: rgb(84 195 255);
  justify-content: center;
}
.yellow{
  background: #fff5b0;
}
</style>
