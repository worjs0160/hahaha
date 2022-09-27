<template>
    <div style="width: 100%; height:100%;">

    <div style="
    width:100%;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    ">
    <div class="manage-val3-wrap" style="
    width: 870px;
    background: #FFFFFF;
    box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
    border-radius: 20px;
    margin: 0 auto !important;
    ">
    
      <print :formTitle="formTitle" :printData="toPrintItems" :dataState="attState" class="print-visible"></print>
        <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
        <h1 class="pre-400">선수 훈련시간 현황 출력</h1>
        <button  @click="dialogCoverSet(false), (companyAttendancePrintDialogStateChange(false))">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
            </svg>
        </button>
        </div>

        <div style="padding:24px;">
        
        <h2 class="pre-400 print-h2">선수 선택</h2>
      <!--이름 입력-->
      <v-col class="px-2 print-name-pos" cols="6" sm="4" md="4">
        <v-autocomplete
          label="선수 이름(필수)"
          v-model="selectedUser"
          :items="comUserList"
          return-object
          item-text="name"
          solo
          hide-details="auto"
        >
          <!--자동완성에 보여지는 리스트의 아이템 형태 정의-->
          <template v-slot:item="data">
            <v-list-item-avatar color="primary">
              <span class="white--text">{{ data.item.name[0] }}</span>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="data.item.name"></v-list-item-title>
            </v-list-item-content>
          </template>
          <!--자동완성에 보여지는 리스트의 아이템 형태 정의 끝-->
        </v-autocomplete>
      </v-col>
      <!--이름 입력 끝-->


        <div class="work-update-row4 work-update-row4-print">
            <h2 class="pre-400 print-h2">날짜 범위 설정</h2>
            <div class="timeinputBox">

            <v-text-field
            v-model="startDate"
            label="시작일(필수)"
            type="date"
            hide-details="auto"
            class="mr-2 mb-4 mb-md-0"
            ></v-text-field>

            <span>~</span>

            <v-text-field
            v-model="endDate"
            label="종료일(필수)"
            type="date"
            hide-details="auto"
            class="ml-2 mb-4 mb-md-0"
            ></v-text-field>

            </div>
        </div>


        <div class="print-btnBox">
            <v-btn class="pre-400" @click="dialogCoverSet(false), (companyAttendancePrintDialogStateChange(false), print())">출력</v-btn>
        </div>
        </div>


    </div>
    </div>

    </div>
</template>

<script>

import { Printd } from "printd";
import Print from "@/components/forms/AttendancePrint.vue";

export default {
    components: {Print,},
    props:['comUserList',],
    
    
    data: () => ({
      selectedUser:"",
      startDate: "",
      endDate: "",
      formTitle: '선수 훈련시간',
      toPrintItems:[],
      attState:[],
    }),
    methods:{
        dialogCoverSet(val){
          this.$emit("dialogCoverSet",val);
        },
        companyUserTaskUpdate(val){
          this.$emit("companyUserTaskUpdate",val);
        },
        companyAttendancePrintDialogStateChange(val){
          this.$emit("companyAttendancePrintDialogStateChange", val);
        },
        async print() {
          if(await this.getUserAttData()){
            const d = new Printd();
            const css = `/* 테이블 전체 디자인 */
                          #print-form {
                            width: 100%;
                            height: 100%;
                            text-align: center;
                            font-size: 10pt;
                          }
                          
                          table{
                            table-layout: fixed;
                            word-break: break-all;
                          }
                          /* 테이블 헤드의 th 디자인 */
                          #print-form thead th {
                            padding-top: 10px;
                            padding-bottom: 10px;
                          }

                          /* 테이블 바디 여백 */
                          #print-form tbody td {
                            height: 80px;
                          }

                          /* 테이블 테두리 한줄 설정 */
                          #print-form,
                          td,
                          th {
                            border: 1px solid black;
                            border-collapse: collapse;
                          }

                          .sign-img{
                            width:150px;
                            height:50px;
                          }
                          @media print {
                            .print-visible {
                              display: initial;
                            }
                            /* 헤드 첫줄 제목 디자인 */
                            #print-form thead > tr:nth-child(1) {
                              font-size: 24pt;
                              width:100px;
                            }
                            #print-form thead > tr:nth-child(2),
                            #print-form thead > tr:nth-child(3) {
                              font-size: 12pt;
                            }
                            #print-form tbody tr td:nth-child(2),
                            #print-form tbody tr td:nth-child(4){
                              width:80px;
                            }
                          }
                          /* A4 사이즈 설정 */
                          @page a4sheet {
                            size: 21cm 29.7cm;
                          }
                          .a4 {
                            page: a4sheet;
                            page-break-after: always;
                          }

                          .print-area {
                            display: flex;
                            align-items: center;
                          }`;

            const print_sheet = document.querySelector(".print-area");
            d.print(print_sheet, [css]);
          }else{
            console.log("필수 항목들을 선택해주세요.");
          }
        },
        async getUserAttData(){
          if(this.selectedUser == ""){
            return false;
          }else{
            let data = {
              user_id:this.selectedUser.id,
              onTime__range:this.startDate+"T00:00:00,"+this.endDate+"T00:00:00",
            }
            
            await this.$axios({
              method: "GET",
              url: "attendances/api/empAtt/",
              params: data,
            })
            .then((res) => {
              this.toPrintItems = []
              for(const data of res.data){
                this.toPrintItems.push(data)
                if(Number(data.attType.offTime.substr(0,2)) - Number(data.attType.onTime.substr(0,2)) == Number(data.workTime)){
                  this.attState.push("훈련완료")
                }
                else{this.attState.push("시간미달")}
              }
            })
            .catch((err) => {
              console.log(err);
              console.log("유저 근무정보 가져오기 실패.");
            });
            return true;
          }
        },
    }
};
</script>

<style>
.print-visible {
  display: none ;
}
.print-btnBox {
  width: 100%;
  display: flex;
  justify-content: flex-end; 
}
.print-btnBox button {
  background: rgb(239, 249, 248) !important;
  color: rgb(73, 173, 169) !important;
  border-radius: 10px !important;
  width: 126px !important;
  height: 48px !important;
  font-size: 18px !important;
  box-shadow: none;
}
.print-name-pos {
  position: relative;
  left: -8px;
}
</style>

