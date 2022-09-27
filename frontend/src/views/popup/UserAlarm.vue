<template>
  <div style="width: 100%; height:100%;">

    <div style="
    width:100%;
    height:100vh;
    padding:120px 0;
    ">
      <div class="manage-val3-wrap" style="
      width: 700px;
      background: #FFFFFF;
      box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
      border-radius: 20px;
      margin: 0 auto !important;
      ">
          <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
            <h1 class="pre-400">알림 상세보기</h1>
            <button  @click="dialogCoverSet(false), (userAlarmDialogStateChange(false)), scrollTop()">
                <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
                </svg>
            </button>
          </div>

          <div class="scroll-wrap" id="userAlarm" style="overflow-y:scroll; height: calc(100vh - 360px);">
          <div class="scroll-cover"></div>
            <div style="padding:24px; min-height: 350px;">
              <div class="humansBox">

                <div class="humans-top">

                  <h2 class="pre-600">반려된 훈련일지<span> ({{issueTrainingList.length}})</span></h2>

                </div>

                <v-row class="human" align="end">
                  <v-col cols="5" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;">제목</p>
                  </v-col>
                  <v-col cols="3" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;">반려날짜</p>
                  </v-col>
                  <v-col cols="2" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;">상태</p>
                  </v-col>
                  <v-col cols="2" class="pb-0">
                    <p class="name pre-400" style="margin-left:12px;"></p>
                  </v-col>
                </v-row>

                <div class="humans-btm mt-4">

                  <template v-for="item of issueTrainingList">
                    <v-row class="human" :key="item.id">
                      <v-col cols="5"><p class="name pre-400 txt_line">{{item.title}}</p></v-col>
                      <v-col cols="3"><p class="name pre-400">{{item.rejectedTime.substr(0,10)}}</p></v-col>
                      <v-col cols="2"><p class="name pre-400">반려</p></v-col>
                      <v-col cols="2"><v-btn class="name pre-400" @click="dialogCoverSet(false), (userAlarmDialogStateChange(false)), scrollTop(), userChangeView(2, item.title, item)">바로가기</v-btn></v-col>
                    </v-row>
                  </template>

                </div>

              </div><!--e:humansBox-->
            </div>
          </div>


      </div>

        <div style="height:120px;"></div>

    </div>

  </div>
</template>

<script>
export default {
    props:[
      'issueTrainingList',
    ],
    methods:{
      dialogCoverSet(val){
        this.$emit("dialogCoverSet",val);
      },
      userAlarmDialogStateChange(val){
        this.$emit("userAlarmDialogStateChange", val);
      },
      scrollTop(){
        document.getElementById('userAlarm').scrollTo(0,0)
      },
      userChangeView(idx, date, item){
        this.$emit('userChangeView', idx, date.substr(0,10), item);
      },
    },
    watch:{
    },
    data: () => ({
    }),
};
</script>

<style>
.txt_line {
  width:250px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>