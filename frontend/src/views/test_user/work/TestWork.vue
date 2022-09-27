<template>
  <v-container style="padding:0;" class="paddingtop30">

    <div class="user-home-wrap user-work-wrap">

      <div class="width270 height632 main-box-wrap work-leftBox">

        <div class="btnBox">
          <v-btn type="button" @click="workAddDialog(true)">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 10V15C22 20 20 22 15 22H9C4 22 2 20 2 15V9C2 4 4 2 9 2H14" stroke="#49ADA9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M22 10H18C15 10 14 9 14 6V2L22 10Z" stroke="#49ADA9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 13H13" stroke="#49ADA9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 17H11" stroke="#49ADA9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            훈련내용 기록하기
          </v-btn>
        </div>

        <div class="timeBox">
          <week-num-picker
            v-on:change="inItWeekDates"
            ref="weekPicker"
          ></week-num-picker>
        </div>

        <div class="work-card-cover" id="workList">
        <div class="workCard" v-for="item in trainingsData" :key="item.workDate" @click="select(item), scrollTop()">
          <div class="cardBox" v-if="trainingsData.length > 0">

            <div class="cardHeader">
              <h2>{{item.workDate.substr(5,5)}} ({{item.day}})</h2>
              <p v-if="item.state==0||item.state==1||item.state==2">{{item.createdTime.substr(11,2)}}시 {{item.createdTime.substr(14,2)}}분</p>
              <p v-if="item.state==3||item.state==4">{{item.workDate.substr(11,2)}}시 {{item.workDate.substr(14,2)}}분</p>
              <div class="mark2" >
                <span style="background: #e0e0e0;" v-if="item.state==0">미승인</span>
                <span style="background: #61C0BD;" v-if="item.state==1">승인</span>
                <span style="background: #FF9900;" v-if="item.state==2">반려</span>
                <span style="background: #FF0000;" v-if="item.state==3">미작성</span>
                <span style="background: #E0E0E0;" v-if="item.state==4">작성예정</span>
              </div>
            </div>

            <p class="workTitle">
              {{item.title}}
            </p>

          </div>
        </div>
        </div>


      </div>

      <div class="width870 height632 work-rightBox">

        <div class="topBox main-box-wrap">

          <div class="header">
            <h2>총 훈련일지</h2>
            <span class="bar"></span>
            <p><span class="textColor">{{trainingCount}}</span>/{{days.length}}개</p>
          </div>

          <div class="monthBox">
            <h2>내 훈련일</h2>
            <div class="month-inner">
              <span v-for = "(item, idx) in days" :key="idx">{{item}}</span>
            </div>
          </div>

          <div class="gageWrap">
            <div class="textBox">
              <strong v-if="!Math.ceil(workRatio) || Math.ceil(workRatio)===Infinity">0%</strong>
              <strong v-else>{{ Math.ceil(workRatio) }}%</strong>
            </div>
            <div class="gageBox">
              <v-progress-linear
                v-model="workRatio"
                style="pointer-events: none;"
                color="rightgagecolor"
              >
              </v-progress-linear>
            </div>
          </div>

        </div>

        <!-- 상세내용 빈칸일때 -->
        <div class="btmBox main-box-wrap scroll-wrap" style="height:432px; overflow-x:hidden; overflow-y: scroll;" v-if="1 > Object.keys(selTraining).length"></div>
        
        <div class="btmBox main-box-wrap scroll-wrap" id="updateWork" style="height:432px; overflow-x:hidden; overflow-y: scroll;" v-if="1 < Object.keys(selTraining).length">

          <div class="btm-inner" v-show="!trainingUpdateState">

            <div class="header">
              <h2>{{selTraining.workDate.substr(5,5)}} ({{selTraining.day}})</h2>
              <p v-if="selTraining.state==0||selTraining.state==1||selTraining.state==2">
                작성시간 | {{selTrainingTime.createdTime}}
              </p>
            </div>

            <div class="textBox">
              <div class="titleBox" style="margin-bottom:20px;">
                <h2>훈련 제목</h2>
                <p v-if="selTraining.state==0||selTraining.state==1||selTraining.state==2">
                  수정시간 | {{selTrainingTime.modifiedTime}}
                </p>
                <h2 style="margin-top: 10px;" class="areaColor">{{selTraining.title}}</h2>
              </div>

              <div class="txtBox" style="margin-bottom:20px;">
                <h2>훈련 내용</h2>
                <textarea class="areaColor scroll-wrap" style="width: 100%;" name="" id="" cols="30" rows="7" readonly v-model="selTraining.contents"></textarea>
              </div>

              <div class="txtBox" style="margin-bottom:20px;" v-if="selTraining.reason">
                <h2>미작성 사유</h2>
                <textarea class="areaColor scroll-wrap" style="width: 100%;" name="" id="" cols="30" rows="7" readonly v-model="selTraining.reason"></textarea>
              </div>
              

              <div class="imgWrap">
                <h2>훈련 사진</h2>
                <div style="display: flex;" class="imgBox">
                  <template v-for="(item, index) in selTraining.images">                  
                      <div :key="index" style="width: 100px; height: 100px;" class="ma-1">
                        <v-img :src="item.images" style="width: 100px; height: 100px;"></v-img>
                      </div>
                  </template>
                </div>
              </div>

              <div class="txtBox" style="margin-top:20px; margin-bottom:20px;" v-if="selTraining.state==2">
                <h2>반려 사유</h2>
                <p v-if="selTraining.state==0||selTraining.state==1||selTraining.state==2">
                  반려시간 | {{selTrainingTime.rejectedTime}}
                </p>
                <textarea class="areaColor mt-2 scroll-wrap" style="width: 100%;" name="" id="" cols="30" rows="7" readonly v-model="selTraining.rejectedReason"></textarea>
              </div>
            </div>
            
          </div>

          <div class="btm-inner" v-show="trainingUpdateState">

            <div class="header">
              <h2>{{updateData.workDate.substr(5,5)}} ({{updateData.day}})</h2>
              <p v-if="selTraining.state==0||selTraining.state==1||selTraining.state==2">
                작성시간 | {{selTrainingTime.createdTime}}
              </p>
            </div>

            <div class="textBox">

              <div class="inputBox inputBox2">
                <h2>훈련 제목</h2>
                <p v-if="selTraining.state==0||selTraining.state==1||selTraining.state==2">
                  수정시간 | {{selTrainingTime.modifiedTime}}
                </p>
                <input style="margin-top: 10px;" placeholder="훈련 제목을 입력해주세요" type="text" v-model="updateData.title">
              </div>

              <div class="inputBox">
                <h2>훈련 내용</h2>
                <textarea class="scroll-wrap" placeholder="훈련 내용을 입력해주세요" name="" id="" cols="30" rows="7" v-model="updateData.contents"></textarea>
              </div>

              <div class="inputBox" v-if="selTraining.state == 3 || selTraining.reason">
                <h2>미작성 사유</h2>
                <textarea class="scroll-wrap" placeholder="사유를 입력해주세요" name="" id="" cols="30" rows="7" v-model="updateData.reason"></textarea>
              </div>

              <div class="btnBox">

                <!-- 이미지 수정 -->
                <div class="my-5 trainingImgSlot imgBtn22">
                  <v-btn @click="trainingImgAdd">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.5 10C10.3284 10 11 9.32843 11 8.5C11 7.67157 10.3284 7 9.5 7C8.67157 7 8 7.67157 8 8.5C8 9.32843 8.67157 10 9.5 10Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12.8 4H9.6C5.6 4 4 5.6 4 9.6V14.4C4 18.4 5.6 20 9.6 20H14.4C18.4 20 20 18.4 20 14.4V10.4" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15 6H19" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                    <path d="M17 8V4" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                    <path d="M5 18L8.82566 15.1435C9.4387 14.6861 10.3233 14.7379 10.8743 15.2643L11.1304 15.5146C11.7356 16.0928 12.7134 16.0928 13.3187 15.5146L16.5468 12.4337C17.1521 11.8554 18.1299 11.8554 18.7351 12.4337L20 13.6419" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <p>이미지 첨부  + (최대 5개)</p>
                  </v-btn>
                </div>
                <div id="trainingImgSlot">
                  <v-row v-for="(imgData, index) in trainingImgSlotData" :key="index" style="align-items: center;">
                    <v-col cols="4" style="
                    margin-right:10px;
                    width:250px;
                    ">
                      <div :key="index" style="display:flex;">
                        <v-file-input
                          v-model="imgData.image"
                          label="클릭하여 사진 첨부"
                          hide-details="auto"
                          style="width:100px; z-index:1;"
                          class="pt-0 mt-0 custom1"
                          prepend-icon=""
                          @change="trainingImgFileChange, checkValid()"
                          outlined
                          dense
                        ></v-file-input>
                      </div>
                    </v-col>
                    <v-col cols="2">
                      <v-btn class="cancelBtn22" outlined style="width:60px; text-align:center; cursor:pointer; " @click="trainingImgDelete(index)">취소</v-btn>
                    </v-col>
                  </v-row>
                </div>

                <div class="txtBox" style="margin-top:20px; margin-bottom:20px;" v-if="selTraining.state==2">
                  <h2>반려 사유</h2>
                  <p v-if="selTraining.state==0||selTraining.state==1||selTraining.state==2">
                    반려시간 | {{selTrainingTime.modifiedTime}}
                  </p>
                  <textarea class="areaColor mt-2 scroll-wrap" style="width: 100%;" name="" id="" cols="30" rows="7" readonly v-model="selTraining.rejectedReason"></textarea>
                </div>
              </div>
            </div>
          </div>

          <v-row align="center">
            <!-- 수정화면이 아닐 때 에러메세지 위치잡기용 -->
            <v-col v-if="!trainingUpdateState" cols="6" class="pb-0" align="left" style="
            color:red;
            font-family: 'Pretendard-Regular';
            font-size:15px;
            position:relative;
            left:30px;
            ">
            </v-col>
            <!-- 수정화면 에러메시지 -->
            <v-col v-if="trainingUpdateState" cols="6" class="pb-0" align="left" style="
            color:red;
            font-family: 'Pretendard-Regular';
            font-size:15px;
            position:relative;
            left:30px;
            ">
              {{errMsg}}
            </v-col>
            <v-col cols="6" class="pb-0" align="right">
              <v-card-actions class="pt-6 pb-4">
                <v-spacer></v-spacer>
                <v-btn v-if="selTraining.state==0||selTraining.state==2" v-show="!trainingUpdateState" color="success" @click="updateDataSet(selTraining), trainingUpdateState=!trainingUpdateState, scrollTop()">수정</v-btn>
                <v-btn v-if="selTraining.state==3" v-show="!trainingUpdateState" color="success" @click="updateDataSet(selTraining), trainingUpdateState=!trainingUpdateState, scrollTop()">작성</v-btn>
                <v-btn style="background: #EFF9F8; !important; color: #49ADA9 !important; font-size: 15px;" v-if="selTraining.state==1" :disabled="true" v-show="!trainingUpdateState" color="success" >승인되었습니다</v-btn>
                <v-btn v-if="dataFlag==true" v-show="trainingUpdateState" color="success" @click="(userWorkUpdate(updateData)), scrollTop()">저장</v-btn>
                <v-btn v-if="dataFlag==false" v-show="trainingUpdateState" color="gray">저장</v-btn>
                <v-btn style="background: #F5F5F5 !important; color: #646464 !important;" v-show="trainingUpdateState" @click="trainingUpdateState=!trainingUpdateState, soketDelete(), scrollTop()">취소</v-btn>
            </v-card-actions>
            </v-col>
          </v-row>
        </div>
      </div>
    </div>

  </v-container>
</template>

<script>
import WeekNumPicker from "/src/components/pickers/WeekNumPicker";

export default {
  components: {WeekNumPicker,},
  methods:{
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
    async trainingImgFileChange(file){      
      const reader = new FileReader();
      reader.onload = (e) => {
        console.log(e.target);
      };
      reader.readAsDataURL(file);

      this.checkValid();

      // 업로드 파일에 대해 조건을 걸수 있습니다.

      // if(file.size > 10485760){
      //   this.image2 = undefined;
      //   this.image2Url = "";
      //   this.$emit("snack",{checkedData:true,checkedDataText:"10mb 이하 사진만 업로드 가능합니다."});
      //   return
      // }
      // this.createImage2(file);
    },
    trainingImgAdd(){
      if(this.trainingImgSlotYN){
        this.trainingImgSlotData.push({image:null});
        if(this.trainingImgSlotData.length >= this.trainingImgSlotLimit){
          this.trainingImgSlotYN = false;
        }
      }
    },
    trainingImgDelete(idx){
      this.trainingImgSlotData.splice(idx,1);
      if(this.trainingImgSlotData.length < this.trainingImgSlotLimit){
        this.trainingImgSlotYN = true;
      }
    },
    soketDelete(){
      this.trainingImgSlotData = []
    },
    async userWorkUpdate(data){
      let sendImgData = []
      let sendImg = []
      // let sendTrainingData = []

      let imgChk = false;
      let oneChk = false;
      // 첨부된 이미지가 있는지 확인
      if(this.trainingImgSlotData.length > 0){
        for(var i=0; i < this.trainingImgSlotData.length; i++){
          if(this.trainingImgSlotData[i].image != null){
            var getImageSize = await this.getImageSize(this.trainingImgSlotData[i].image)


            var formData = new FormData();
            formData.append("images", this.trainingImgSlotData[i].image);
            formData.append("width", getImageSize.width);
            formData.append("height", getImageSize.width);
                        
            var result = await this.$axios({
              method: 'POST',
              url: "trainings/api/userTrainingsImg/",
              headers: {
                "Content-Type": "multipart/form-data"
              },
              data: formData
            })
            var id = result.data.id
            var images = result.data.images
            sendImgData.push(id)
            sendImg.push({'images':images})
            oneChk = true;
            imgChk = false;
            data.images = sendImgData
          }else{
            if(!oneChk){
              imgChk = true;
            }
          }
        }


      }else{
        imgChk = true;
      }

      if(imgChk){
        console.log('첨부된 이미지가 없습니다.');
        return
      }
      
      if(this.updateData.state==0||this.updateData.state==2){ // 반려나 미승인 훈련일지는 수정
        this.updateData.state=0
        this.$axios({
            method: "PATCH",
            url: "trainings/api/trainings/"+data.id+"/",
            data: data,
          }).then((res) => {
            this.selTraining.title=res.data.title;
            this.selTraining.contents=res.data.contents;
            this.selTraining.rejectedReason=res.data.rejectedReason
            this.selTraining.images=sendImg;
            if(res.data.reason)this.selTraining.reason=res.data.reason;
            this.selTrainingTime.createdTime = res.data.createdTime.substr(5,5)+" "+res.data.createdTime.substr(11,2)+":"+res.data.createdTime.substr(14,2)
            this.selTrainingTime.modifiedTime = res.data.modifiedTime.substr(5,5)+" "+res.data.modifiedTime.substr(11,2)+":"+res.data.modifiedTime.substr(14,2)
            if(res.data.rejectedTime){
              this.selTrainingTime.rejectedTime = res.data.rejectedTime.substr(5,5)+" "+res.data.rejectedTime.substr(11,2)+":"+res.data.rejectedTime.substr(14,2)
            }
            
            // this.trainingData.push({'day':dayOfWeek,'user':data.user,'title':data.title,'contents':data.contents,'workDate':data.workDate})
            this.trainingImgSlotData = []
            this.dataFlag = false
            this.trainingUpdateState=!this.trainingUpdateState;
            this.$emit("saveAction");
            this.$emit("updateAlarm");
            this.inItWeekDates();
            this.$store.dispatch("callToast", {
              msg: "훈련내용 기록이 수정되었습니다.",
              result: "success",
            });
          });
      }
      else if(this.updateData.state==3){ // 미작성 훈련일지는 생성
        this.$axios({
            method: "POST",
            url: "trainings/api/trainings/",
            data: {'user':this.$store.state.userStore.id,'title':data.title,'contents':data.contents, 'workDate':data.workDate, 'reason':data.reason, 'images':sendImgData, 'state':0},
          }).then((res) => {
            this.selTraining.title=res.data.title;
            this.selTraining.contents=res.data.contents;
            this.selTraining.reason=res.data.reason;
            this.selTraining.images=sendImg;
            this.selTrainingTime.createdTime = res.data.createdTime.substr(5,5)+" "+res.data.createdTime.substr(11,2)+":"+res.data.createdTime.substr(14,2)
            this.selTrainingTime.modifiedTime = res.data.modifiedTime.substr(5,5)+" "+res.data.modifiedTime.substr(11,2)+":"+res.data.modifiedTime.substr(14,2)
            
            // this.trainingData.push({'day':dayOfWeek,'user':data.user,'title':data.title,'contents':data.contents,'workDate':data.workDate})
            this.trainingImgSlotData = []
            this.dataFlag = false
            this.trainingUpdateState=!this.trainingUpdateState;
            this.$emit("saveAction");
            this.$emit("updateAlarm");
            this.$store.dispatch("callToast", {
              msg: "훈련내용 기록이 작성되었습니다.",
              result: "success",
            });
            this.getWork();
          });
      }
    },
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    scrollTop(){
      document.getElementById('updateWork').scrollTo(0,0)
    },
    async inItWeekDates() {
      await this.getWeekFirstDate();
      await this.getWeekLastDate();
      await this.getWork();
      document.getElementById('workList').scrollTo(0,0)
      this.trainingUpdateState = false
      this.selTraining = {};
    },
    //월요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekFirstDate: function () {
      this.weekFirstDate = this.$refs.weekPicker.getWeekFirstDate();
    },
    //일요일의 날짜를 받아오는 함수 => weekNumPicker에서 받아옴
    getWeekLastDate: function () {
      this.weekLastDate = this.$refs.weekPicker.getWeekLastDate();
    },
    async checkMyAtt() {
      await this.$axios({
        method: "GET",
        url:
          "attendances/api/empAtt/?user_id=" +
          this.$store.state.userStore.id +
          "&onTime__range=" +
          this.today.substr(0, 10) +
          "," +
          this.tomorrow.substr(0, 10),
      })
      .then((res) => {
        this.myAtt = res.data
      })
      .catch((err) => {
        console.log(err);
      });
    },
    workAddDialog(state){
      if(this.myAtt.length == 0){
        this.$store.dispatch("callToast", {
          msg: "오늘의 훈련시간 기록이 없습니다.",
          result: "fail",
        });
        return false
      }
      //유저의 근무 유형이랑 비교해서 근무일이 아니면 실행X
      for(var count=0; this.days[count] ; count++){
        if(this.days.indexOf(this.week[new Date(Date.now()).getDay()]) == -1){
          this.$store.dispatch("callToast", {
            msg: "오늘은 훈련일이 아니네요.",
            result: "fail",
          });
          return false
        }
      }
      if(this.todayTraining.createdTime){
        this.$store.dispatch("callToast", {
          msg: "오늘 작성된 훈련일지가 있습니다.",
          result: "fail",
        });
        return false
      }
      //근무 유형이랑 비교해서 근무일이면 실행O
      this.$emit('workAddDialog', state, this.user_data, this.today.substr(0,10));
    },
    async select(val){
      this.trainingUpdateState = false
      this.selTrainingTime.createdTime = ""
      this.selTrainingTime.modifiedTime = ""
      this.selTrainingTime.rejectedTime = ""
      this.selTraining = {}
      this.updateData = {day:"", workDate:"", id:"", title:"", contents:"", state:"", reason:"",},
      this.trainingImgSlotData = []

      this.selTraining = val;
      if(val.createdTime)this.selTrainingTime.createdTime = this.selTraining.createdTime.substr(5,5)+" "+this.selTraining.createdTime.substr(11,2)+":"+this.selTraining.createdTime.substr(14,2)
      if(val.modifiedTime)this.selTrainingTime.modifiedTime = this.selTraining.modifiedTime.substr(5,5)+" "+this.selTraining.modifiedTime.substr(11,2)+":"+this.selTraining.modifiedTime.substr(14,2)
      if(val.rejectedTime)this.selTrainingTime.rejectedTime = this.selTraining.rejectedTime.substr(5,5)+" "+this.selTraining.rejectedTime.substr(11,2)+":"+this.selTraining.modifiedTime.substr(14,2)
    },
    
    //선택한 주간의 근무일지 가져오기
    async getWork(){
      await this.$axios({
        method: "GET",
        url:"trainings/api/CCUserTrainings/?user_id="+this.$store.state.userStore.id+"&workDate__range="+this.weekFirstDate+","+this.weekLastDate+"T23:59:59"
      })
      .then(async(res)=>{
        let year = new Date().getFullYear(); // 현재 년도
        let month = new Date().getMonth() + 1;  // 현재 월
        let date = new Date().getDate();  // 현재 날짜
        let todayMs = new Date(year + '/' + month + '/' + date).getTime() // 현재 날짜의 ms
        let startMs = new Date(this.weekFirstDate).getTime()-32400000 // 선택한 주간의 시작날짜 ms
        let endMs = new Date(this.weekLastDate).getTime()-32400000 // 선택한 주간의 끝날짜 ms

        var dateList = [] // 선택한 주간의 모든날짜(7일)
        var dayList = ["월", "화", "수", "목", "금", "토", "일"]
        await this.getDateRange(this.weekFirstDate, this.weekLastDate, dateList) // 주간 날짜 가져오기
        var userDateList = [] // 유저의 attType에 맞게 매칭된 날짜 
        this.trainingsData = []

        this.trainingCount = 0
        for(var a=0; a<this.days.length; a++){ // 해당 유저의 attType의 요일수만큼 반복
          for(var b=0; b<dayList.length; b++){ // 일주일 반복
            if(this.days[a] === dayList[b]){ // 해당 유저의 attType의 요일과 일주일을 비교하여 선택한 주간의 날짜와 매칭
              userDateList.push({date:dateList[b], day:dayList[b]})
            }
          }
        }
        if(todayMs >= startMs && todayMs <= endMs){ // 선택한 주간이 이번주
          for(a=0; a<userDateList.length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            var check = 0
            if(new Date(userDateList[a].date+"T23:59:59").getTime()-32400000>todayMs){ // 매칭된 날짜가 오늘 날짜보다 미래이면 작성예정 훈련일지
              for(var count=0; res.data[count]; count++){
                if(res.data[count].workDate.substr(0,10) === userDateList[a].date){
                  check = 1
                  this.trainingsData.push(res.data[count])
                  this.trainingCount++
                  }
              }
              if(check == 0){
                this.trainingsData.push({
                  day: userDateList[a].day,
                  title: "작성예정 제목",
                  contents: "",
                  workDate: userDateList[a].date + "T" + this.myAttType.offTime,
                  images: "",
                  state: 4,
                })
              }
            }
            else if(new Date(userDateList[a].date).getTime()-32400000<=todayMs){ // 매칭된 날짜가 오늘 날짜보다 과거이면
              for(count=0; res.data[count]; count++){
                if(res.data[count].workDate.substr(0,10) === userDateList[a].date){ // 훈련시간 기록날짜가 훈련유형의 날짜와 같을때
                  check = 1
                  this.trainingsData.push(res.data[count])
                  this.trainingCount++
                }
              }
              if(check == 0){ // 미작성 훈련일지
                this.trainingsData.push({
                  day: userDateList[a].day,
                  title: userDateList[a].date + " " + this.user_data[0].name + " 훈련일지",
                  contents: "미작성",
                  workDate: userDateList[a].date + "T" + this.myAttType.offTime,
                  images: "",
                  state: 3,
                })
              }
              check = 0
            }
          }
        }
        else if(todayMs < startMs){ // 선택한 주간이 미래주
          for(a=0; a<userDateList[a].length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
            this.trainingsData = []
          }
        }
        else if(todayMs > endMs){ // 선택한 주간이 과거주
          for(a=0; a<userDateList.length; a++){ // 해당 유저의 attType에 매칭된 날짜만큼 반복
          check = 0
            for(count=0; res.data[count]; count++){
              if(res.data[count].workDate.substr(0,10) === userDateList[a].date){ // 훈련시간 기록날짜가 훈련유형의 날짜와 같을때
                check = 1
                this.trainingsData.push(res.data[count])
                this.trainingCount++
              }
            }
            if(check == 0){ // 미작성 훈련일지
              this.trainingsData.push({
                day: userDateList[a].day,
                title: userDateList[a].date + " " + this.user_data[0].name + " 훈련일지",
                contents: "미작성",
                workDate: userDateList[a].date + "T" + this.myAttType.offTime,
                images: "",
                state: 3,
              })
            }
            check = 0
          }
        }

        this.workRatio = (res.data.length/this.days.length)*100;
        if (this.workRatio===Infinity) {
          this.workRatio = 0
        }
      })
      .catch((err)=>{
        console.log(err)
      })

      //오늘 일지가 있는지 체크
      this.$axios({
        method: "GET",
        url:"trainings/api/CCUserTrainings/?user_id="+this.$store.state.userStore.id+"&workDate__range="+this.today.substr(0,10)+","+this.today.substr(0,10)+"T23:59:59"
      })
      .then((res)=>{
        if(res.data[0]){
          this.todayTraining = res.data[0]
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    //두 날짜 사이의 날짜 배열로 가져오기
    getDateRange(startDate, endDate, listDate)
    {
      var dateMove = new Date(startDate);
      var strDate = startDate;
      if (startDate == endDate){
        strDate = dateMove.toISOString().slice(0,10);
        listDate.push(strDate);
      }
      else{
        while (strDate < endDate)
        {
          strDate = dateMove.toISOString().slice(0, 10);
          listDate.push(strDate);
          dateMove.setDate(dateMove.getDate() + 1);
        }
      }
      return listDate;
    },
    
    async getAttTypeData(){
      await this.$axios
      .get("attendances/api/userAttType/?id="+ this.$store.state.userStore.id)
      .then((res) => {
        this.myAttType = res.data[0].attType
        this.days = res.data[0]['days'];
        this.user_data.push({'name':res.data[0]['name'],'user':res.data[0]['id']})
      })
      .catch((err) => {
        console.log(err);
        console.log("유저 근무유형 가져오기 실패.");
      });
    },

    //업무일지 수정하기 위한 데이터 세팅
    async updateDataSet(data){
      this.updateData.day = data.day
      this.updateData.workDate = data.workDate
      this.updateData.id = data.id
      this.updateData.title = data.title
      this.updateData.contents = data.contents
      this.updateData.state = data.state
      if(data.reason)this.updateData.reason = data.reason
    },

    //업무일지 수정시 valid체크
    checkValid(){
      this.dataFlag = false
      var checkImage = false
      if(!this.updateData.title) this.errMsg = "제목을 입력해주세요"
      else if(!this.updateData.contents) this.errMsg = "내용을 입력해주세요"
      else if(this.selTraining.state == 3 && !this.updateData.reason){
        this.errMsg = "사유를 입력해주세요"
      }
      else if(this.trainingImgSlotData.length == 0) this.errMsg = "첨부된 이미지가 없습니다"
      else if(this.trainingImgSlotData.length > 0){
        for(var i=0; i < this.trainingImgSlotData.length; i++){
          if(this.trainingImgSlotData[i].image == null)this.errMsg = "첨부된 이미지가 없습니다"
          else if(this.trainingImgSlotData[i].image != null){
            checkImage = true
          }
        }
      }
      if(this.updateData.title && this.updateData.contents && checkImage){
        this.errMsg = ""
        this.dataFlag = true;
      }
    },

    //알람 바로가기 클릭시 해당 훈련일지 보이기
    async alarmChangeView(date, item){
      this.alarmState = true
      await this.$refs.weekPicker.alarmDate(date);
      await this.getWeekFirstDate();
      await this.getWeekLastDate();
      await this.getAttTypeData();
      await this.getWork();
      await this.select(item);
    },
  },
  async created() {
    await this.loadingCover(true);
    await this.getAttTypeData();
    await this.checkMyAtt();
    if(this.alarmState == false){
      await this.inItWeekDates();
    }
    await this.loadingCover(false);
  },
  watch:{
    "updateData.title": function(){
      this.checkValid();
    },
    "updateData.contents": function(){
      this.checkValid();
    },
    "updateData.reason": function(){
      if(this.selTraining.state == 3){
        this.checkValid();
      }
    },
  },
  data: () => ({
    today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString(),
    weekFirstDate: "", //일주일 중 첫번째인 월요일의 날짜
    weekLastDate: "", //일주일 중 마지막인 일요일의 날짜
    trainingsData:[],
    workRatio:0,
    selTraining:{},
    selTrainingTime:{createdTime:"", modifiedTime:"", rejectedTime:"",},
    updateData:{day:"", workDate:"", id:"", title:"", contents:"", state:"", reason:"",},
    trainingCount: 0,
    days:[],
    user_data:[],
    week:["일", "월", "화", "수", "목", "금", "토"], //근무 유형이랑 비교하기 위한 날짜
    // 유저 훈련 이미지 슬롯 관련
    trainingUpdateState:false,
    trainingImgSlotLimit:5,
    trainingImgSlotYN:true,
    trainingImgSlotData:[],
    trainingImgSlotChange:0,
    todayTraining:{},
    errMsg:"",
    dataFlag:false,
    tomorrow: new Date(Date.now() + 86400000 - new Date().getTimezoneOffset() * 60000).toISOString(),
    myAtt: [],
    myAttType: [],
    alarmState: false, // 알림의 바로가기를 통해 접근했을경우 true값을 가져 created에서 api 실행을 막음
  }),
  computed:{},
};
</script>

<style>
  .full-height{
    height : 100%;
  }
  .full-width{
    width : 100%;
  }
  .green-circle{
    width : 7px;
    height : 7px;
    border-radius: 50%;
    background-color: green;
}
.user-work-wrap .work-leftBox .btnBox {
  padding: 24px;
}
.work-card-cover{
  height:430px;
  overflow-y: auto;
}
.work-card-cover::-webkit-scrollbar{
  display:none
}
.user-work-wrap .work-leftBox .btnBox button {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  color: #49ADA9;
  font-family: 'Pretendard-Regular';
  background: #EFF9F8;
  border-radius: 16px;
  width: 222px;
  height: 64px;
  box-shadow: none;
}
.user-work-wrap .work-leftBox .btnBox button svg {
  margin-right: 18px;
}
.user-work-wrap .work-leftBox .timeBox {
  width: 270px;
  height: 72px;
  background: #F9F9F9;
  display: flex;
  justify-content: center;
  align-items: center;
}
.user-work-wrap .work-leftBox .timeBox div {
  font-size: 20px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
}
.user-work-wrap .work-leftBox .cardBox {
  padding: 16px 24px;
  border-bottom: 0.5px solid #B4B4B4;
  cursor: pointer;
}
.user-work-wrap .work-leftBox .cardBox .cardHeader {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.user-work-wrap .work-leftBox .cardBox .workTitle {
  font: 16px;
  color: #989898;
  font-family: 'Pretendard-Regular';
  margin: 0;
  margin-top: 12px;
}
.user-work-wrap .work-leftBox .cardBox h2 {
  font-size: 20px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
  margin: 0;
}
.user-work-wrap .work-leftBox .cardBox p {
  font-size: 13px;
  color: #989898;
  font-family: 'Pretendard-Regular';
  margin: 0;
}
.user-work-wrap .work-rightBox .topBox {
  padding: 24px 24px 35px;
  height: 170px;
}
.user-work-wrap .work-rightBox .topBox .header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.user-work-wrap .work-rightBox .topBox .header h2 {
  margin: 0;
  font-size: 22px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
}
.user-work-wrap .work-rightBox .topBox .header .bar {
  background: #989898;
  width: 1px;
  height: 15px;
  margin: 0 8px;
}
.user-work-wrap .work-rightBox .topBox .header p {
  font-size: 16px;
  color: #646464;
  font-family: 'Pretendard-Regular';
  margin: 0;
  letter-spacing: 1.5px;
}
.user-work-wrap .work-rightBox .topBox .header p span {
  color: #008BD6;
}
.user-work-wrap .work-rightBox .topBox .monthBox {
  display: flex;

}
.user-work-wrap .work-rightBox .topBox .monthBox h2 {
  font-size: 16px;
  color: #646464;
  font-family: 'Pretendard-Regular';
  margin-right: 10px;
  font-weight: 400;
}
.user-work-wrap .work-rightBox .topBox .monthBox .month-inner {
  display: flex;
  align-items: center;
}
.user-work-wrap .work-rightBox .topBox .monthBox .month-inner span {
  width: 24px;
  height: 24px;
  background: #E4F2F9;
  border-radius: 4px;
  font-size: 16px;
  color: #008bd6;
  font-family: 'Pretendard-Regular';
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 4px;
}
.user-work-wrap .work-rightBox .topBox .gageWrap .textBox {
  display: flex;
  justify-content: flex-end;
  font-size: 22px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
  margin-bottom: 5px;
}
.user-work-wrap .work-rightBox .topBox .gageWrap .gageBox {
  width: 100%;
  height: 24px;
  border-radius: 6px !important;
  overflow: hidden;
}
.user-work-wrap .work-rightBox .topBox .gageWrap .gageBox div {
  height: 24px !important;
}
.user-work-wrap .work-rightBox .topBox .gageWrap .rightgagecolor {
  background: #008BD6;
}
.user-work-wrap .work-rightBox .btmBox {
  margin-top: 30px;
}
.user-work-wrap .work-rightBox .btmBox .header {
  padding: 24px;
  border-bottom: 0.5px solid #B4B4B4;
  display: flex;
  align-items: center;
}
.user-work-wrap .work-rightBox .btmBox .header h2 {
  font-size: 20px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
  margin: 0;
  margin-right: 16px;
}
.user-work-wrap .work-rightBox .btmBox .header p {
  font-size: 16px;
  color: #0081c7;
  font-family: 'Pretendard-Regular';
  margin: 0;
}
.user-work-wrap .work-rightBox .btmBox .textBox {
  padding: 24px;
}
.user-work-wrap .work-rightBox .btmBox .textBox h2 {
  font-size: 18px;
  color: #2e2e2e;
  font-family: 'Pretendard-SemiBold';
  margin: 0;
  margin-bottom: 10px;
}
.user-work-wrap .work-rightBox .btmBox .textBox p {
  font-size: 16px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
  margin: 0;
}
.user-work-wrap .work-rightBox .btmBox .textBox .imgWrap {}
.user-work-wrap .work-rightBox .btmBox .textBox .imgBox > div {
  box-shadow: rgb(0 0 0 / 20%) 0px 0px 5px;
  border-radius: 5px;
  overflow: hidden;
}
.work-rightBox .v-card__actions > .v-btn.v-btn {
  width: 126px;
  height: 48px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  color: #49ADA9;
  font-family: 'Pretendard-Regular';
  background: #EFF9F8 !important;
  border-radius: 10px;
  box-shadow: none;
}
.work-rightBox .inputBox h2 {
  color: #646464 !important;
}
.work-rightBox .inputBox input {
  background: tomato;
  padding:5px 10px;
  width: 100%;
  height: 43px;
  background: #F5F5F5;
  border-radius: 6px;
  font-family: 'Pretendard-Regular';
  color: #2e2e2e;
  font-size: 16px;
}
.work-rightBox .inputBox input::placeholder {
  color: #b4b4b4;
}
.work-rightBox .inputBox2 {
  margin-bottom: 24px;
}
.work-rightBox .inputBox textarea {
  width: 100%;
  background: #F5F5F5;
  border-radius: 6px;
  font-family: 'Pretendard-Regular';
  color: #2e2e2e;
  font-size: 16px;
  padding:5px 10px;
}
.work-rightBox .inputBox textarea::placeholder {
  color: #b4b4b4;
}
.imgBtn22 > button p {
  margin: 0;
}
.imgBtn22 > button {
  font-size: 18px;
  color: #646464;
  background: #F5F5F5;
  border-radius: 10px;
  padding: 25px 20px !important;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: none;
}
.imgBtn22 > button svg {
  margin-right: 10px;
}
#trainingImgSlot .v-file-input__text {
  cursor: pointer;
}
.cancelBtn22 {
  font-size: 18px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
  border: none;
  background: #F5F5F5 !important;
}
#trainingImgSlot .v-file-input__text {
  font-family: 'Pretendard-Regular';
  overflow: hidden;
  font-size: 14px;
}
.mark2 span {
    padding: 0 10px;
    height: 22px;
    border-radius: 11.5px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 13px;
    color: #fff;
    font-family: 'Pretendard-Regular';
  }
</style>