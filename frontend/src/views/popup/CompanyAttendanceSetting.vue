<template>
    <div style="width: 100%; height:100%;">

    <div style="
    width:100%;
    height:100vh;
    padding:120px 0;
    ">
        <div class="manage-val3-wrap" style="
        width: 870px;
        background: #FFFFFF;
        box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
        border-radius: 20px;
        margin: 0 auto !important;
        ">
            <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
            <h1 class="pre-400">훈련시간 수정</h1>
            <button  @click="dialogCoverSet(false), (companyUserTaskSettingDialogStateChange(false)), scrollTop()">
                <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
                </svg>
            </button>
            </div>

            <div style="padding:24px;">

            <div class="work-update-row2">
                <h2 class="name pre-400"  style="
                font-size:18px;
                font-weight:500;
                border: 1px solid #e1e1e1;
                padding: 10px 117px 10px 12px;
                border-radius: 3px;
                ">{{taskUpdateName}}</h2>
            </div>

            <div class="work-update-row3">
                <div class="dateBox">
                <h2 class="pre-400">{{companyUserTaskSettingDialogData.date}} ({{companyUserTaskSettingDialogData.day}})</h2>                
                <p class="pre-400">총 훈련시간&nbsp;&nbsp;|&nbsp;&nbsp;{{markData.workTime}}시간</p>
                </div>
                <div class="timeBox">
                <span v-if="markData.markstat == 0" class="mark0 pre-400">
                    {{markData.mark}}
                </span>
                <span v-if="markData.markstat == 1" class="mark1 pre-400">
                    {{markData.mark}}
                </span>
                <p class="pre-400">
                    {{companyUserTaskSettingDialogData.startTime}} ~ {{companyUserTaskSettingDialogData.endTime}}
                </p>
                </div>
            </div>

            <div class="work-update-row4">
                <h2 class="pre-400">시간 입력하기</h2>
                <div class="timeinputBox">

                <v-text-field
                v-model="taskUpdateStartTime"
                label="훈련시작(필수)"
                type="time"
                hide-details="auto"
                class="mr-2 mb-4 mb-md-0"
                ></v-text-field>

                <span>~</span>

                <v-text-field
                v-model="taskUpdateEndTime"
                label="훈련종료(필수)"
                type="time"
                hide-details="auto"
                class="ml-2 mb-4 mb-md-0"
                ></v-text-field>

                </div>
            </div>

            <div class="workplusBox">
                <p class="pre-400">설정된 훈련 시간의 인정되는 훈련량 : {{creditTime}}</p>
                <p class="pre-400">해당 선수의 훈련 시간 : {{taskUpdateCheckOnTime}} ~ {{taskUpdateCheckOffTime}}</p>
                <p class="pre-400" v-if="!attErrMsg"></p>
                <p class="pre-400" v-if="attErrMsg" style="color:red;">{{attErrMsg}}</p>
            </div>

            <div class="btnBox22">
                <v-btn style="background: rgb(200 200 200 / 66%) !important; color: white !important;" class="pre-400" v-if="attUpdateFlag==false">수정하기</v-btn>
                <v-btn style="background: #EFF9F8 !important; color: #49ADA9 !important;" class="pre-400" v-if="attUpdateFlag==true" @click="dialogCoverSet(false), (companyUserTaskSettingDialogStateChange(false)), (companyUserTaskUpdate(companyUserTaskSettingDialogData, taskUpdateStartTime, taskUpdateEndTime)), scrollTop()">수정하기</v-btn>
            </div>
            </div>


        </div>

        <div style="height:120px;"></div>

    </div>

    </div>
</template>

<script>
export default {
    methods:{
      dialogCoverSet(val){
        this.$emit("dialogCoverSet",val);
      },
      scrollTop(){
        document.getElementById('companyAttendanceSetting').scrollTo(0,0)
      },
      setDialogDate(val){
          this.$emit("setDialogData",val);
      },
      companyUserTaskSettingDialogStateChange(val){
        this.$emit("companyUserTaskSettingDialogStateChange", val);
      },
      settingData(item, name, onTime, offTime){
        this.companyUserTaskSettingDialogData = item;
        this.taskUpdateName = name
        this.taskUpdateStartTime = item.startTime.substr(0,5);
        this.taskUpdateEndTime = item.endTime.substr(0,5);
        this.taskUpdateCheckOnTime = onTime;
        this.taskUpdateCheckOffTime = offTime;
        this.creditTime = Math.floor((new Date(item.date+'T'+this.taskUpdateEndTime).getTime() - new Date(item.date+'T'+this.taskUpdateStartTime).getTime())/1000/3600)
        this.timeCACL(this.companyUserTaskSettingDialogData);
        this.markData.workTime = item.workTime
        this.markData.markstat = item.markstat
        this.markData.mark = item.mark
      },
      //수정할 근무시간 처리 함수
      async timeCACL(item){
        var checkStartTime = 0;
        var checkEndTime = 0;
        if(new Date(item.date+'T'+this.taskUpdateStartTime).getTime() < new Date(item.date+'T'+this.taskUpdateEndTime).getTime()){
          if(new Date(item.date+'T'+this.taskUpdateStartTime).getTime() >= new Date(item.date+'T' + this.taskUpdateCheckOnTime).getTime()){
            //내 출근시간이 근무유형의 시간보다 늦으면 내 출근 시간으로 체크
            checkStartTime = new Date(item.date+'T'+this.taskUpdateStartTime).getTime() //근무시간 계산용 출근 시간
          }
          else if(new Date(item.date+'T'+this.taskUpdateStartTime).getTime() < new Date(item.date+'T' + this.taskUpdateCheckOnTime).getTime()){
            //내 출근시간이 근무유형의 시간보다 빠르면 근무유형 출근 시간으로 체크
            checkStartTime = new Date(item.date+'T' + this.taskUpdateCheckOnTime).getTime()
          }

          if(new Date(item.date+'T'+this.taskUpdateEndTime).getTime() >= new Date(item.date+'T' + this.taskUpdateCheckOffTime).getTime()){
            //내 퇴근시간이 근무유형의 시간보다 늦으면 근무유형 퇴근 시간으로 체크
            checkEndTime = new Date(item.date+'T' + this.taskUpdateCheckOffTime).getTime() //근무시간 계산용 퇴근 시간
          }
          else if(new Date(item.date+'T'+this.taskUpdateEndTime).getTime() < new Date(item.date+'T' + this.taskUpdateCheckOffTime).getTime()){
            //내 퇴근시간이 근무유형의 시간보다 빠르면 내 퇴근 시간으로 체크
            checkEndTime = new Date(item.date+'T'+this.taskUpdateEndTime).getTime()
          }

          if((checkEndTime - checkStartTime) <= 0){
            this.creditTime = 0
          }
          else if((checkEndTime - checkStartTime) > 0){
            this.creditTime = Math.floor((checkEndTime - checkStartTime)/1000/3600)
          }
          this.attErrMsg = ""
          this.attUpdateFlag = true
        }
        else{
          this.creditTime = 0
          this.attErrMsg = "잘못된 시간 설정 입니다."
          this.attUpdateFlag = false
        }
      },
      async companyUserTaskUpdate(item, start, end){
        await this.timeCACL(item)
        console.log(item)
        var create_data = {
          user:item.userId,
          onTime:item.date+'T'+start,
          onType: true,
          offTime:item.date+'T'+end,
          offType: true,
          workTime: this.creditTime,
          place: "",
          memo: "",
          id: null,
          attType: item.attTypeId,
        }

        var update_data = {
          onTime:item.date+'T'+start,
          offTime:item.date+'T'+end,
          offType: true,
          workTime: this.creditTime
        }
        if(item.markstat == 2){ // 훈련현황이 미훈련일 경우
          await this.$axios({
            method: "POST",
            url:
            "attendances/api/empAtt/",
            data: create_data,
          }).then(() => {
            this.$emit("companyUserListUpdate");
            this.$emit("saveAction");
            this.$store.dispatch("callToast", {
              msg: this.taskUpdateName+"님의 훈련시간을 작성하였습니다.",
              result: "success",
            });
          });
        }
        else{
          await this.$axios({
            method: "PATCH",
            url:
            "attendances/api/empAtt/" + item.id + "/",
            data: update_data,
          }).then(() => {
            this.$emit("companyUserListUpdate");
            this.$emit("saveAction");
            this.$store.dispatch("callToast", {
              msg: this.taskUpdateName+"님의 훈련시간을 수정하였습니다.",
              result: "success",
            });
          });
        }
      },
    },
    watch:{
      "taskUpdateStartTime": function(){
        this.timeCACL(this.companyUserTaskSettingDialogData);
      },
      "taskUpdateEndTime": function(){
        this.timeCACL(this.companyUserTaskSettingDialogData);
      },
    },
    data: () => ({
      //유저 근무 업데이트 값 관련
      taskUpdateName:"",
      taskUpdateStartTime:"",
      taskUpdateEndTime:"",
      taskUpdateCheckOnTime:"",
      taskUpdateCheckOffTime:"",
      creditTime:0,
      attErrMsg:"",
      attUpdateFlag:true,
      markData:{
        workTime:"",
        markstat: 0,
        mark: "",
      },
    }),
};
</script>

<style></style>