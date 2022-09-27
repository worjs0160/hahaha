<template>
<div class="scroll-hidden" id="companyInfoModify" style="
        width:100%;
        height:100vh;
        display:flex;
        jutify-content:center;
        align-items:center;
        padding:50px 0;
        overflow-y: scroll;
    ">
        <div class="manage-val3-wrap" style="
            width: 1170px;
            background: #FFFFFF;
            box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
            border-radius: 20px;
            margin: 0 auto !important;
            ">

        <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
            <h1 class="pre-400">회사 기본정보 수정</h1>
            <button  @click="dialogCoverSet(false), (companyInfoDialogStateChange(false)), scrollTop()">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
            </svg>
            </button>
        </div>

        <div class="info-sub-title">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM11.25 8C11.25 7.59 11.59 7.25 12 7.25C12.41 7.25 12.75 7.59 12.75 8V13C12.75 13.41 12.41 13.75 12 13.75C11.59 13.75 11.25 13.41 11.25 13V8ZM12.92 16.38C12.87 16.51 12.8 16.61 12.71 16.71C12.61 16.8 12.5 16.87 12.38 16.92C12.26 16.97 12.13 17 12 17C11.87 17 11.74 16.97 11.62 16.92C11.5 16.87 11.39 16.8 11.29 16.71C11.2 16.61 11.13 16.51 11.08 16.38C11.03 16.26 11 16.13 11 16C11 15.87 11.03 15.74 11.08 15.62C11.13 15.5 11.2 15.39 11.29 15.29C11.39 15.2 11.5 15.13 11.62 15.08C11.86 14.98 12.14 14.98 12.38 15.08C12.5 15.13 12.61 15.2 12.71 15.29C12.8 15.39 12.87 15.5 12.92 15.62C12.97 15.74 13 15.87 13 16C13 16.13 12.97 16.26 12.92 16.38Z" fill="#0081C7"/>
            </svg>
            <p class="pre-400">
            회사의 기본 정보를 입력하고 관리하세요.<br>
            구성원들이 회사정보에서 손쉽게 정보를 열람할 수 있게 됩니다.
            </p>
        </div>

        <div class="val3Box1" style="
        padding: 24px 24px 32px;
        width: 700px;
        margin:0 auto;
        ">

            <div class="defaultBox" style="width:100%;">

            <h2 class="pre-600">기본정보</h2>

            <div class="nameBox val3-inputBox">
                <h3>회사명</h3>
                <input type="text" placeholder="회사명을 입력해 주세요" v-model="companyInfoDialogData.comName">
            </div>

            <div class="nameBox val3-inputBox">
                <h3>대표자명</h3>
                <input type="text" placeholder="대표자명을 입력해 주세요" v-model="companyInfoDialogData.ceoName">
            </div>

            <div class="addressBox val3-inputBox">

                <div class="addressBox-1">
                <h3>회사주소</h3>
                <input type="text" placeholder="* 우편번호(주소검색)" v-model="companyInfoDialogData.comZip" readonly>
                <button class="pre-600" type="button" @click="showDaum">우편번호 검색</button>
                </div>

                <div class="addressBox-2">
                <div class="address-emptyBox"></div>
                <input type="text" placeholder="* 기본주소(주소검색)" v-model="companyInfoDialogData.comAddr1" readonly>
                </div>
            
                <div class="addressBox-3">
                <div class="address-emptyBox"></div>
                <input type="text" placeholder="상세주소(입력해 주세요)" v-model="companyInfoDialogData.comAddr2">
                </div>
                
            </div>

            <div class="nameBox val3-inputBox">
                <h3>회사 연락처</h3>
                <input type="text" placeholder="회사 연락처를 입력해 주세요" v-model="companyInfoDialogData.comNum">
            </div>

            <div class="nameBox val3-inputBox">
                <h3>사업자<br>등록번호</h3>
                <input type="text" placeholder="사업자 등록번호를 입력해 주세요" v-model="companyInfoDialogData.businessNum">
            </div>

            <div class="nameBox val3-inputBox">
                <h3>담당자</h3>
                <input type="text" placeholder="담당자를 입력해 주세요" v-model="companyInfoDialogData.managerName">
            </div>

            <div class="nameBox val3-inputBox">
                <h3>담당자 연락처</h3>
                <input type="text" placeholder="담당자 연락처를 입력해 주세요" v-model="companyInfoDialogData.managerNum">
            </div>

            <div class="update-btnBox" style="width: 100%;">
                <v-btn class="update-btn1 pre-400" @click="dialogCoverSet(false), (companyInfoDialogStateChange(false)), scrollTop()">닫기</v-btn>
                <v-btn class="update-btn2 pre-400"  @click="dialogCoverSet(false), companyInfoUpdate(companyInfoDialogData), (companyInfoDialogStateChange(false)), scrollTop()">저장</v-btn>
            </div>

            </div>

        </div><!--e:val3Box1-->

        </div>
    </div>
</template>

<script>
export default {
    props:[
        'companyInfoDialogData',
    ],
    methods:{
        dialogCoverSet(val){
            this.$emit("dialogCoverSet",val);
        },
        scrollTop(){
            document.getElementById('companyInfoModify').scrollTo(0,0)
        },
        companyInfoDialogStateChange(val){
            this.$emit("companyInfoDialogStateChange", val);
        },
        showDaum(){
            this.$emit("showDaum");
        },
        companyInfoUpdate(val){
            this.$emit("companyInfoUpdate", val);
        },
    }
};
</script>

<style></style>