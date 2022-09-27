<template>
    <div>
    <div style="width:100%; height:100%;">
    <div class="scroll-hidden" id="companyWorkModify" style="
    width:100%;
    height:100vh;
    padding:120px 0;
    overflow-y: scroll;
    ">
        <div class="manage-val3-wrap" style="
        width: 870px;
        background: #FFFFFF;
        box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
        border-radius: 20px;
        margin: 0 auto !important;
        ">

        <div class="manage-val3-header" style="display:flex; align-items:center; justify-content:space-between;">
            <h1 class="pre-400">훈련일지 조회</h1>
            <button  @click="dialogCoverSet(false), (companyUserWorkSettingDialogStateChange(false)), scrollTop()">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
            </svg>
            </button>
        </div>

        <div style="padding:24px">

            <div class="work-update-row2 atten-2222">

                <div class="nameCover" style="
                width: 171px;
                height: 39px;
                ">
                <v-autocomplete
                    label="이름(필수)"
                    v-model="companyUserWorkSettingDialogData"
                    :items="companyUserWorkSettingDialogData"
                    return-object
                    item-text="name"
                    :disabled="true"
                    solo
                    hide-details="auto"
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
                </div>

                <div class="btnBox" v-if="companyUserWorkSettingDialogData.stateCode == 0 || companyUserWorkSettingDialogData.stateCode == 1 || companyUserWorkSettingDialogData.stateCode == 2">
                    <v-checkbox
                        v-model="companyUserWorkSettingDialogData.state"
                        color="success2"
                        class="mt-0 pt-0 pr-1"
                        hide-details
                    ></v-checkbox>
                    <label v-if="companyUserWorkSettingDialogData.state==false" for="input-251" class="v-label theme--light" style="left: 0px; right: auto; position: relative;">미승인</label>
                    <label v-if="companyUserWorkSettingDialogData.state==true" for="input-251" class="v-label theme--light" style="left: 0px; right: auto; position: relative;">승인</label>
                </div>

            </div>

            <div class="atten-row1">
                <h2 class="pre-400">{{companyUserWorkSettingDialogData.datetime.substr(5,5)}} ({{companyUserWorkSettingDialogData.day}})</h2>
                <p class="pre-400" v-if="companyUserWorkSettingDialogData.stateCode==0||companyUserWorkSettingDialogData.stateCode==1||companyUserWorkSettingDialogData.stateCode==2">
                    작성시간&nbsp;&nbsp;|&nbsp;&nbsp;{{companyUserWorkSettingDialogData.createdTime}}
                </p>
            </div>

            <div class="atten-row2">
                
                <div class="titleBox" style="margin-bottom:25px;">
                    <h2 class="pre-400">제목</h2>
                    <p class="pre-400 mb-1" v-if="companyUserWorkSettingDialogData.stateCode==0||companyUserWorkSettingDialogData.stateCode==1||companyUserWorkSettingDialogData.stateCode==2">
                        수정시간&nbsp;&nbsp;|&nbsp;&nbsp;{{companyUserWorkSettingDialogData.modifiedTime}}
                    </p>
                    <p class="pre-400 areaColor">{{companyUserWorkSettingDialogData.title}}</p>
                </div><!--e:titleBox-->

                <div class="txtBox">
                    <h2 class="pre-400">훈련 내용</h2>
                    <textarea name="" id="" cols="30" rows="5" v-model="companyUserWorkSettingDialogData.contents" readonly style="
                    background: #F5F5F5;
                    border-radius: 6px;
                    padding: 10px;
                    width: 100%;
                    ">
                    </textarea>
                </div><!--e:txtBox-->

                <div class="txtBox" v-if="companyUserWorkSettingDialogData.reason">
                    <h2 class="pre-400">미작성 사유</h2>
                    <textarea name="" id="" cols="30" rows="5" v-model="companyUserWorkSettingDialogData.reason" readonly style="
                    background: #F5F5F5;
                    border-radius: 6px;
                    padding: 10px;
                    width: 100%;
                    ">
                    </textarea>
                </div><!--e:txtBox-->

                <div class="atten-imgBox2" style="margin-top: 20px;">
                    <h2 class="pre-400">훈련 이미지</h2>
                    <div class="mt-4" style="display: flex;">
                        <template v-for="(item, index) in companyUserWorkSettingDialogData.images">                  
                            <div :key="index" style="width: 100px; height: 100px; margin-right:10px; border-radius:5px; overflow:hidden; box-shadow:0 0 5px rgba(0,0,0,.2);">
                            <v-img :src="item" style="width: 100px; height: 100px;">
                            </v-img>
                            </div>
                        </template>
                    </div>
                </div><!--e:imgBox-->

            </div><!--e:atten-row2-->

            <div class="atten-row2">

                <div class="txtBox" v-if="!companyUserWorkSettingDialogData.state">
                    <h2 class="pre-400">반려 사유</h2>
                    <p class="pre-400 mb-1" v-if="(companyUserWorkSettingDialogData.stateCode==0||companyUserWorkSettingDialogData.stateCode==1||companyUserWorkSettingDialogData.stateCode==2)&&companyUserWorkSettingDialogData.rejectedReason">
                        반려시간&nbsp;&nbsp;|&nbsp;&nbsp;{{companyUserWorkSettingDialogData.rejectedTime}}
                    </p>
                    <textarea name="" id="" cols="30" rows="5" v-model="companyUserWorkSettingDialogData.rejectedReason" style="
                    background: #F5F5F5;
                    border-radius: 6px;
                    padding: 10px;
                    width: 100%;
                    ">
                    </textarea>
                </div><!--e:txtBox-->

            </div><!--e:atten-row2-->

            <p class="pre-400" v-if="!checkMsg"></p>
            <p class="pre-400" v-if="checkMsg" style="color:red;">{{checkMsg}}</p>

            <div class="btnBox22" v-if="companyUserWorkSettingDialogData.stateCode == 0 || companyUserWorkSettingDialogData.stateCode == 1 || companyUserWorkSettingDialogData.stateCode == 2">
            <v-btn style="color: #49ADA9 !important; background: #EFF9F8 !important;" class="pre-400" v-if="check" @click="dialogCoverSet(false), (companyUserWorkSettingDialogStateChange(false)), workStateChange(companyUserWorkSettingDialogData), scrollTop()">저장</v-btn>
            <v-btn style="background: rgb(200 200 200 / 66%) !important; color: white !important;" class="pre-400" v-if="!check">저장</v-btn>
            </div>

        </div>

        </div>
    </div>

    </div>





    <div style="width: 100%;height:100%; padding-top:200px; display:none !important;">



    <v-card  class="home-card pa-0" style="z-index: 13;margin:auto;display: block;max-height:none;width: 600px;height:600px; border-radius: 24px !important;     overflow:hidden; " rounded="lg">
        <!--폼 타이틀-->
        <v-card-title class="pl-4 pb-2">훈련일지조회<v-spacer></v-spacer>
        <label v-if="companyUserWorkSettingDialogData.stateCode==0" for="input-251" class="v-label theme--light" style="left: 0px; right: auto; position: relative;">미승인</label>
        <label v-if="companyUserWorkSettingDialogData.stateCode==1" for="input-251" class="v-label theme--light" style="left: 0px; right: auto; position: relative;">승인</label>
        <label v-if="companyUserWorkSettingDialogData.stateCode==2" for="input-251" class="v-label theme--light" style="left: 0px; right: auto; position: relative;">반려</label>
            <v-checkbox
            v-model="companyUserWorkSettingDialogData.state"
            color="success"
            class="mt-0 pt-0 pr-1"
            @change="workStateChange(companyUserWorkSettingDialogData)"
            hide-details
            ></v-checkbox>
        </v-card-title>
        <v-form class="px-2">
            
            <!--이름 입력-->
            <v-col class="px-2" cols="6" sm="4" md="4">
            <v-autocomplete
                label="이름(필수)"
                v-model="companyUserWorkSettingDialogData"
                :items="companyUserWorkSettingDialogData"
                return-object
                item-text="name"
                :disabled="true"
                solo
                hide-details="auto"
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
            
            <v-card-text class="pa-1 text-h6" style="font-weight:1000;">{{companyUserWorkSettingDialogData.datetime.substr(5,5)}} ({{companyUserWorkSettingDialogData.day}})</v-card-text>
            <v-card-text class="px-1 py-2" style="font-weight:700; border-bottom:0.5px solid gray;">
            작성시간 : {{companyUserWorkSettingDialogData.datetime.substr(11,2)}}시 {{companyUserWorkSettingDialogData.datetime.substr(14,2)}}분
            </v-card-text>
            <v-card-text class="px-1 pt-5 pb-1" style="font-weight:700;">제목 : {{companyUserWorkSettingDialogData.title}}</v-card-text>
            <v-card-text class="pa-1">{{companyUserWorkSettingDialogData.contents}}</v-card-text>
            <div class="mt-4" style="display: flex;">
            <template v-for="(item, index) in companyUserWorkSettingDialogData.images">                  
                <div :key="index" style="width: 100px; height: 100px;">
                    <v-img :src="item.images" style="width: 100px; height: 100px;">
                    </v-img>
                </div>
            </template>
            </div>
        </v-form>
        <div  class="mt-4 mx-4" style="display: flex;">
            <template v-for="(item, index) in companyUserWorkSettingDialogData.images">                  
            <div :key="index" style="width: 100px; height: 100px;">
            <v-img :src="item" style="width: 100px; height: 100px;">
            </v-img>
            </div>
            </template>
        </div>
        <v-card-actions class="pt-6 pb-4">
            <v-spacer></v-spacer>
            <!-- <v-btn color="success" @click="dialogCoverSet(false), (companyUserWorkSettingDialogStateChange(false)), (companyUserWorkUpdate(companyUserWorkSettingDialogData))">수정</v-btn> -->
            <v-btn color="error" @click="dialogCoverSet(false), (companyUserWorkSettingDialogStateChange(false)), scrollTop()">닫기</v-btn>
        </v-card-actions>
        </v-card>
    </div>
    </div>
</template>

<script>
export default {
    props:[
        'companyUserWorkSettingDialogData',
    ],
    // props: ['errMsg'],
    methods:{
        dialogCoverSet(val){
            this.$emit("dialogCoverSet",val);
        },
        scrollTop(){
            document.getElementById('companyWorkModify').scrollTo(0,0)
        },
        workStateChange(val){
            this.$emit("workStateChange",val);
        },
        companyUserWorkSettingDialogStateChange(val){
            this.$emit("companyUserWorkSettingDialogStateChange", val);
        },
        checkValid(){
            if(this.companyUserWorkSettingDialogData.state == true){
                this.check = true
                this.checkMsg = ""
            }
            else if(this.companyUserWorkSettingDialogData.state == false){
                if(this.companyUserWorkSettingDialogData.rejectedReason){
                    this.check = true
                    this.checkMsg = ""
                }
                else if(!this.companyUserWorkSettingDialogData.rejectedReason){
                    this.check = false
                    this.checkMsg = "반려사유가 필요합니다."
                }
            }
        },
    },
    data: () => ({
        check: true,
        checkMsg: "",
    }),
    watch:{
        "companyUserWorkSettingDialogData.state":function(){
            this.checkValid()
        },
        "companyUserWorkSettingDialogData.rejectedReason":function(){
            this.checkValid()
        },
    },
};
</script>

<style></style>