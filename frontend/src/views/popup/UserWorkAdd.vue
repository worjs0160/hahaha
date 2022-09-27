<template>
    <div style="width: 100%;height:100%;">
        <div class="scroll-hidden" id="playerWorkAdd" style="
        width:100%;
        height:100vh;
        padding: 150px 0;
        overflow-y: scroll;
        ">
            <div style="overflow: hidden; z-index: 13; margin:auto; display: block; max-height:none; width: 600px; height:auto; border-radius: 24px !important; background:#fff;" rounded="lg">
            <!--폼 타이틀-->
            <v-card-title class="pl-4" style="
            font-family: 'Pretendard-Regular';
            font-size: 20px;
            color: #2e2e2e;
            font-weight: 600;
            padding-bottom: 15px;
            border-bottom: 0.5px solid #B4B4B4;
            ">일지 작성</v-card-title>
            <v-form class="px-2">
                <!--이름 입력-->
                <v-col class="px-2" cols="6" sm="4" md="4">
                <v-autocomplete
                    label="이름(필수)"
                    v-model="workAddDialogData.name"
                    :items="workAddDialogData.name"
                    return-object
                    item-text="name"
                    :disabled="true"
                    solo
                    hide-details="auto"
                    :error-messages="nameError"
                >
                    <!--자동완성에 보여지는 리스트의 아이템 형태 정의-->
                    <template v-slot:item="data">
                    <v-list-item-avatar color="primary">
                        <span class="white--text">{{ data.item.name[0] }}</span>
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title v-html="data.item.name"> </v-list-item-title>
                    </v-list-item-content>
                    </template>
                    <!--자동완성에 보여지는 리스트의 아이템 형태 정의 끝-->
                </v-autocomplete>
                </v-col>
                <!--이름 입력 끝-->
                
                
                <!-- 제목 -->
                <v-col class="jin123 px-2 p-1" cols="12">
                    <h2 style="
                    font-size: 15px;
                    color: #989898;
                    font-family: 'Pretendard-Regular';
                    font-weight: 400;
                    ">제목</h2>
                    <input type="text" v-model="workAddDialogData.title" style="
                    background: #F5F5F5;
                    border-radius: 6px;
                    padding: 10px;
                    width: 100%;
                    ">
                </v-col>
                <!-- 내용 -->
                <v-col class="jin1234 px-2" cols="12">
                    <h2 style="
                    font-size: 15px;
                    color: #989898;
                    font-family: 'Pretendard-Regular';
                    font-weight: 400;
                    ">내용</h2>
                    <textarea name="" id="" cols="30" rows="5" v-model="workAddDialogData.contents" style="
                    background: #F5F5F5;
                    border-radius: 6px;
                    padding: 10px;
                    width: 100%;
                    ">
                
                

                </textarea>

                <!-- 이미지 추가 -->
                <div class="my-5 trainingImgSlot imgBtn22">
                    <v-btn @click="trainingImgAdd">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.5 10C10.3284 10 11 9.32843 11 8.5C11 7.67157 10.3284 7 9.5 7C8.67157 7 8 7.67157 8 8.5C8 9.32843 8.67157 10 9.5 10Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12.8 4H9.6C5.6 4 4 5.6 4 9.6V14.4C4 18.4 5.6 20 9.6 20H14.4C18.4 20 20 18.4 20 14.4V10.4" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15 6H19" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                    <path d="M17 8V4" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                    <path d="M5 18L8.82566 15.1435C9.4387 14.6861 10.3233 14.7379 10.8743 15.2643L11.1304 15.5146C11.7356 16.0928 12.7134 16.0928 13.3187 15.5146L16.5468 12.4337C17.1521 11.8554 18.1299 11.8554 18.7351 12.4337L20 13.6419" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <p style="
                    font-family: 'Pretendard-Regular';
                    font-size: 15px;
                    color: #2e2e2e;
                    ">이미지 첨부  + (최대 5개)</p>
                    </v-btn>
                </div>
                <div id="trainingImgSlot">
                    <v-row v-for="(imgData, index) in trainingImgSlotData" :key="index" style="align-items: center;">
                    <v-col cols="5">
                        <div :key="index" style="display:flex;">
                        <v-file-input
                            v-model="imgData.image"
                            label="클릭하여 사진 첨부"
                            hide-details="auto"
                            style="width:100px; z-index:1;"
                            class="pt-0 mt-0 custom1"
                            prepend-icon=""
                            @change="trainingImgFileChange, workDataValid()"
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
                </v-col>
                <!--메모 끝-->
                <v-row class="pa-3">
                <v-col cols="6" class="pb-0" align="left" style="color:red;">
                    {{errMsg}}
                </v-col>
                <v-col cols="6" class="pb-0" align="right">
                    <v-card-actions class="pt-6 pb-4">
                    <v-spacer></v-spacer>
                    <v-btn class="jinBtn" color="gray" @click="dialogCoverSet(false), soketDelete(), (workAddDialogStateChange(false)), scrollTop()">닫기</v-btn>
                    <v-btn class="jinBtn" v-if="dataFlag==true" color="success" @click="dialogCoverSet(false), (workAddDialogStateChange(false)), (userWorkAddData(workAddDialogData)), scrollTop()">저장</v-btn>
                    <v-btn style="background: #EFF9F8 !important; color: #49ADA9;" class="jinBtn" v-if="dataFlag==false">저장</v-btn>
                    </v-card-actions>
                </v-col>
                </v-row>
            </v-form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props:[
      'workAddDialogData',
      'errMsg',
      'trainingImgSlotData',
      'dataFlag',
    ],
    // props: ['errMsg'],
    data: () => ({
      nameError: null,
    }),
    methods:{
      scrollTop(){
        document.getElementById('playerWorkAdd').scrollTo(0,0)
      },
      soketDelete(){
        this.$emit("soketDelete");
      },
      dialogCoverSet(val){
        this.$emit("dialogCoverSet",val);
      },
      userWorkAddData(val){
        this.$emit("userWorkAddData",val);
      },
      trainingImgDelete(val){
        this.$emit("trainingImgDelete",val);
      },
      trainingImgAdd(){
        this.$emit("trainingImgAdd");
      },
      workAddDialogStateChange(val){
        console.log(val)
        this.$emit("workAddDialogStateChange", val);
      },
      trainingImgFileChange(){
        this.$emit("trainingImgFileChange");
      },
      workDataValid(){
        this.$emit("workDataValid");
      },
    }
};
</script>

<style></style>