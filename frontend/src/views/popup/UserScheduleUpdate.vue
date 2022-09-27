<template>
    <div style="width: 100%;height:100%;">
            <div class="scroll-hidden" style="
            width:100%;
            height:100vh;
            padding:150px 0;
            overflow-y: scroll;
            ">
                <div  class="manage-val3-wrap" style="
                width: 670px;
                background: #FFFFFF;
                box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
                border-radius: 20px;
                margin: 0 auto !important;
                ">
            

                    <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
                        <h1 class="pre-400">일정 수정하기</h1>
                        <button @click="dialogCoverSet(false), (scheduleUpdateDialogStateChange(false))">
                        <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
                        </svg>
                        </button>
                    </div>

                    <div style="padding:24px;">

                        <div class="work-update-row4-1 mt-5 px-2">
                            <h2 style="
                            font-size: 15px;
                            color: #989898;
                            font-family: 'Pretendard-Regular';
                            font-weight: 400;
                            ">일정시간</h2>
                            <div class="timeinputBox">

                                <v-text-field
                                v-model="scheduleUpdateDialogData.start"
                                label=""
                                type="datetime-local"
                                hide-details="auto"
                                class="mr-2 mb-4 mb-md-0"
                                ></v-text-field>

                                <span>~</span>

                                <v-text-field
                                v-model="scheduleUpdateDialogData.end"
                                label=""
                                type="datetime-local"
                                hide-details="auto"
                                class="ml-2 mb-4 mb-md-0"
                                ></v-text-field>

                            </div>
                        </div>
                        <!-- 제목 -->
                        <v-col class="jin123 px-2 p-1" cols="12">
                            <h2 style="
                            font-size: 15px;
                            color: #989898;
                            font-family: 'Pretendard-Regular';
                            font-weight: 400;
                            ">제목</h2>
                            <input type="text" v-model="scheduleUpdateDialogData.title" style="
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
                            <textarea name="" id="" cols="30" rows="5" v-model="scheduleUpdateDialogData.contents" style="
                            background: #F5F5F5;
                            border-radius: 6px;
                            padding: 10px;
                            width: 100%;
                            ">
                        </textarea>
                        </v-col>

                        <div class="btnBox22">
                            <v-btn style="color: #49ADA9 !important; background: #EFF9F8 !important;" class="pre-400" @click="dialogCoverSet(false), (scheduleUpdateDialogStateChange(false)), (scheduleUpdateData(scheduleUpdateDialogData))">저장</v-btn>
                            <v-btn color="error" class="pre-400 ml-3" @click="dialogCoverSet(false), (scheduleUpdateDialogStateChange(false)), (scheduleDeleteData(scheduleUpdateDialogData))">삭제</v-btn>
                        </div>
                    </div>



                </div>
            </div>
        

    </div>
</template>

<script>
export default {
    props:[
        'scheduleUpdateDialogData',
    ],
    methods:{
        dialogCoverSet(val){
            this.$emit("dialogCoverSet",val);
        },
        scheduleUpdateDialogStateChange(val){
            this.$emit("scheduleUpdateDialogStateChange", val);
        },
        scheduleUpdateData(val){
            this.$emit("scheduleUpdateData", val);
        },
        scheduleDeleteData(val){
            this.$emit("scheduleDeleteData", val);
        },
    }
};
</script>

<style></style>