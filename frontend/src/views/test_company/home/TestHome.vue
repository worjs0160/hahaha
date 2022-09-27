<template>
  <v-container style="max-width: none; padding:30px 0;">
    <v-row style="height:100%; display:flex; justify-content: space-between;" class="inner">

      <v-col style="padding:0; width:870px !important; flex-basis: unset; flex-grow:unset;">
        <v-card class="card-border-radius max-height card-shadow" outlined style="height:100%;">

          <v-row class="ma-0 py-0" style="border-bottom:.5px solid #e1e1e1;">
            <v-col class="py-0">
              <v-tabs centered color="grey darken-1" v-model="idx">
                  <v-tab class="pre-600" style="color:#2E2E2E; font-size:20px; min-width:0;"
                    v-for="item of subTabs"
                    :key="item.idx"
                    :title="item.name"
                    @click="changeSubView(item.idx)">
                    {{item.name}}
                  </v-tab>
              </v-tabs>
            </v-col>
          </v-row>

          <!-- 근무, 업무, 결재, 급여 컴포넌트 전환 영역 -->
          <div class="main-scrollbar-hidden" style="height: calc(100vh - 228px); overflow:hidden">
            <component
              :is="this.seltab.componentName"
              ref="childComponent"
              @attList="attList"
              @workList="workList"
              @coverSetChild="loadingCover"
              @companyAttendancePrintDialogStateChange="companyAttendancePrintDialogStateChange"
              @companyWorkPrintDialogStateChange="companyWorkPrintDialogStateChange"
              @dialogCoverSet="dialogCoverSet"
              @getComUserList="getComUserList"
            >
            </component>
          </div>
          
        </v-card>

      </v-col>

      <v-col style="padding:0; width:270px !important; flex-basis: unset; flex-grow:unset;">
        <v-card class="card-border-radius max-height card-shadow data-list" id="dataList" outlined style="height:100%;">

          <div v-if="this.seltab.componentName == 'Attendance'">
            <div class="main-aside-header">주간 훈련시간</div>
            <div v-for="(item, idx) in clickAttData.attData" :key="item.day">
              <v-row
                v-if="clickAttData.length != 0"
                @click="companyUserTaskSettingDialog(true, idx)"
                style="cursor: pointer; padding-bottom: 0;"
                justify="center"
                class="main-aside-row"
              >

                <div class="main-aside-row-top">
                  <p class="main-aside-row-top-p1">{{item.date}}({{item.day}})</p>

                  <p class="main-aside-row-top-p2 mark0" color="#49ADA9" v-if="item.markstat==0"><span>{{item.mark}}</span></p>
                  <p class="main-aside-row-top-p2 mark1" color="#FF6B00" v-if="item.markstat==1"><span>{{item.mark}}</span></p>
                  <p class="main-aside-row-top-p2 mark2" color="red" v-if="item.markstat==2"><span>{{item.mark}}</span></p>
                </div>

                <p class="main-aside-row-bottom-p" v-if="item.startTime || item.endTime">{{item.startTime.substr(0,5)}} ~ {{item.endTime.substr(0,5)}}</p>
                <p class="main-aside-row-bottom-p" v-if="!item.startTime">-</p>

                <div class="boundary-spacer"></div>
              </v-row>
            </div>

          </div>

          <div v-if="this.seltab.componentName == 'Work'">
            <div class="main-aside-header">주간 훈련일지</div>
            
            <div>
              <v-row
                v-for="(workData, idx) in clickWorkData" :key="workData.title"
                @click="companyUserWorkSettingDialog(true, idx)"
                style="cursor: pointer; padding-bottom: 0;"
                justify="center"
                class="main-aside-row"
              >

                <div class="main-aside-row-top">
                  <p class="main-aside-row-top-p1">{{workData.date.substr(5,5)}}({{workData.day}})</p>
                  <p class="main-aside-row-top-p2">
                    <span style="background: #B4B4B4" v-if="workData.stateCode==0">미승인</span>
                    <span style="background: #61C0BD" v-if="workData.stateCode==1">승인</span>
                    <span style="background: #FF9900" v-if="workData.stateCode==2">반려</span>
                    <span style="background: #FF0000" v-if="workData.stateCode==3">미작성</span>
                  </p>
                </div>
                <!-- <v-spacer></v-spacer> -->
                <!-- <div><span class="mark">{{workData.mark}}</span></div><v-spacer></v-spacer> -->
                <p class="main-aside-row-bottom-p">{{workData.title}}</p>
                
                <div class="boundary-spacer"></div>
              </v-row>

            </div>
            
          </div>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Attendance from "/src/views/test_company/home/Attendance";
import Work from "/src/views/test_company/home/Work";
import Approval from "/src/views/test_company/home/Approval";
import Pay from "/src/views/test_company/home/Pay";

export default {
  components: { Attendance, Work, Approval, Pay, },
  async created() {
    await this.loadingCover(true);
    await this.loadingCover(false);
  },
  data: () => ({
    subTabs: [
      { idx: 0, componentName: "Attendance", name: "선수현황", thum:"mdi-clock-outline" },
      { idx: 1, componentName: "Work", name: "훈련일지", thum:"mdi-calendar-check" },
      //{ idx: 2, componentName: "Approval", name: "결재", thum:"mdi-script-text-outline" },
      //{ idx: 3, componentName: "Pay", name: "급여", thum:"mdi-hand-coin-outline" },
    ],
    seltab: { idx: 0, componentName: "Attendance", name: "근무", thum:"mdi-clock-outline" },
    clickAttData:[],
    clickWorkData:[],
    clickIdx:0, //클릭한 리스트의 index
  }),
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    async changeSubView(event) {
      const tab = this.subTabs[event];
      this.seltab = tab;
    },
    scrollTop(){
      document.getElementById('dataList').scrollTo(0,0)
    },
    async companyUserWorkSettingDialog(state, index){ //훈련일지
      this.$emit('companyUserWorkSettingDialog',state, this.clickWorkData[index]);
    },
    companyUserTaskSettingDialog(state, index){ //훈련현황
      this.$emit('companyUserTaskSettingDialog',state, this.clickAttData.attData[index], this.clickAttData.name, this.clickAttData.attTypeOnTime, this.clickAttData.attTypeOffTime);
    },
    //클릭한 유저의 근무리스트
    attList(val){
      this.scrollTop()
      if(val == "reset"){
        this.clickAttData = []
      }
      else{
        this.clickAttData = val;
      }
    },
    //클릭한 유저의 업무리스트
    workList(val){
      this.scrollTop()
      if(val == "reset"){
        this.clickWorkData = []
      }
      else{
        this.clickWorkData = val;
      }
    },
    companyAttendancePrintDialogStateChange(val){
      this.$emit("companyAttendancePrintDialogStateChange", val);
    },
    companyWorkPrintDialogStateChange(val){
      this.$emit("companyWorkPrintDialogStateChange", val);
    },
    dialogCoverSet(val){
      this.$emit("dialogCoverSet",val);
    },
    async getComUserList(){
      await this.$emit("getComUserList");
    },
    //근무시간 데이터 수정후 데이터 갱신(MainLayout.vue에서 실행함)
    async attDataReset(){
      await this.$refs.childComponent.inItWeekDates();
      await this.$refs.childComponent.emitAttList(this.clickIdx)
    },
    async workDataReset(){
      await this.$refs.childComponent.inItWeekDates();
      await this.$refs.childComponent.getComUser();
      await this.$refs.childComponent.getTrainingDataList();
    },
    async alarmChangeView(date, userIdx){
      await this.changeSubView(1) // 기업 메인탭의 서브탭을 훈련일지로 변경
      await this.$refs.childComponent.alarmChangeView(date, userIdx);
    },
  },
  computed: {
    idx: {
      get() {
        return this.seltab.idx;
      },
      set() {
        return;
      },
    },
  },
};
</script>

<style>
.data-list{
  height:430px;
  overflow-y: auto;
}
.data-list::-webkit-scrollbar{
  display:none
}
.mark{
  border: 1px solid #ccc;
  padding: 3px;
  border-radius: 8px;
  min-width: 40px;
}
.boundary-spacer{
  margin-top:10px;
  margin-left: 5px;
  margin-right: 5px;
  border-bottom: 1px solid #ccc;
}
.card-border-radius {
  border-radius: 20px !important;
}
.card-shadow {
  box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
  border: none !important;
}
.max-height {max-height: 640px !important;}

.main-aside-header {
  background: #fff;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  font-family: 'Pretendard-Regular';
  color: #2e2e2e;
  border-bottom: 0.5px solid #B4B4B4;
}
.main-aside-row p {
  margin: 0;
}
.main-aside-row {
  height: 87px;
  border-bottom: 0.5px solid #B4B4B4;
  padding: 16px 24px !important;
  margin: 0 !important;
  background: #fff;
}
.main-aside-row-top {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
}
.main-aside-row-top-p1 {
  font-size: 20px;
  font-family: 'Pretendard-Regular';
  color: #2e2e2e;
}
.main-aside-row-top-p2 span {
  padding: 0 10px;
  height: 22px;
  border-radius: 11.5px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 13px;
  font-family: 'Pretendard-SemiBold';
  color: #fff;
}
.main-aside-row-top-p2.mark0 span {
  background:#49ADA9;
}.main-aside-row-top-p2.mark1 span {
  background:#FF6B00;
}.main-aside-row-top-p2.mark2 span {
  background:red;
}
.main-aside-row-bottom-p {
  width: 100%;
  color: #646464;
  font-size: 16px;
  font-family: 'Pretendard-Regular';
}

</style>