<template>
  <div style="background:#fff;">
    <div class="inner info-inner">

      <div class="info-header">
        <h1 class="pre-400">회사 기본정보</h1>
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

      <div class="company-nameBox">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M2 22H22" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M17 2H7C4 2 3 3.79 3 6V22H21V6C21 3.79 20 2 17 2Z" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M7 16.5H10" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M14 16.5H17" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M7 12H10" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M14 12H17" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M7 7.5H10" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M14 7.5H17" stroke="#2E2E2E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <h2 class="pre-400">{{ this.data.comName }}</h2>
      </div>

      <div class="info-centerBox">

        <div class="info-row">

          <div class="info-item info-item1">
            <h3>대표자</h3>
            <p>{{ this.data.ceoName }}</p>
          </div>

          <div class="info-item info-item2">
            <h3>담당자명</h3>
            <p>{{ this.data.managerName }}</p>
          </div>

        </div>

        <div class="info-row">

          <div class="info-item info-item1">
            <h3>회사 전화번호</h3>
            <p class="number-color">{{ this.data.comNum }}</p>
          </div>

          <div class="info-item info-item2">
            <h3>담당자 번호</h3>
            <p class="number-color">{{ this.data.managerNum }}</p>
          </div>

        </div>

        <div class="info-row">

          <div class="info-item info-item1">
            <h3>회사주소</h3>
            <p>{{ this.data.comAddr1 }} {{this.data.comAddr2}} ({{this.data.comZip}})</p>
          </div>

        </div>

        <div class="info-row">

          <div class="info-item info-item1">
            <h3>사업자 등록번호</h3>
            <p>{{ this.data.businessNum }}</p>
          </div>

        </div>

      </div>
      
      <div class="buttonBox">
        <button type="button" class="pre-400" @click="companyInfoDialog(true)">수정하기</button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    data: {
      comName: "",
      ceoName: "",
      comAddr1: "",
      comAddr2: "",
      comZip: "",
      comNum: "",
      businessNum: "",
      managerName: "",
      managerNum: "",
    },
  }),
  async created() {
    await this.loadingCover(true);
    await this.getCompanyInfo();
    await this.loadingCover(false);
  },
  methods: {
    loadingCover(val) {
      this.$emit("coverSetChild", val);
    },
    async getCompanyInfo(){
      await this.$axios
      .get(
        "datasets/api/company_list/" + this.$store.state.userStore.comID + "/"
      )
      .then((res) => {
        this.data = res.data;
        this.managerName = this.$store.state.userStore.name;
        this.managerNum = this.$store.state.userStore.comNum;
      })
      .catch((err) => {
        console.log(err.response);
      });
    },
    companyInfoDialog(state){
      this.$emit('companyInfoDialog',state,this.data);
    },
    async infoDataReset(){
      await this.getCompanyInfo();
    },
  },
};
</script>

<style>
.background {
  background-color: rgba(240, 240, 240);
  border-radius: 10px;
}
.info-inner {
  box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
  border-radius: 20px;
  /* height:700px; */
  height: 600px;
  margin-top: 30px;
}
.info-header {
  border-bottom: 0.5px solid #B4B4B4;
  height: 72px;
  display: flex;
  align-items: center;
  padding: 0 23px;
}
.info-header h1 {
  font-size: 20px;
  color: #2E2E2E;
}
.info-sub-title {
  display: flex;
  align-items: center;
  padding-left: 30px;
  margin: 16px 0 32px;
}
.info-sub-title p {
  margin: 0;
  margin-left: 8px;
  font-size: 14px;
  color: #0081c7;
}
.company-nameBox {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 48px;
}
.company-nameBox h2 {
  margin: 0;
  margin-left: 8px;
  font-size: 20px;
  color: #2e2e2e;
}
.info-row {
  width: 650px;
  margin: 0 auto 25px;
  display: flex;
  justify-content: space-between;
}
.info-item {}
.info-item2 {
  width: 222px;
}
.info-item h3 {
  margin: 0;
  font-size: 13px;
  color: #989898;
  font-family: 'Pretendard-SemiBold';
  margin-bottom: 2px;
}
.info-item p {
  margin: 0;
  font-size: 16px;
  color: #2e2e2e;
  font-family: 'Pretendard-Regular';
}
.info-item .number-color {
  color: #008BD6;
}
.buttonBox {
  display: flex;
  justify-content: center;
  /* margin-top: 120px; */
}
.buttonBox button {
  width: 252px;
  height: 48px;
  background: #61C0BD;
  border-radius: 10px;
  color: #fff;
  font-size: 18px;
  transition: all .3s;
}
.buttonBox button:hover {
  background: #77ddda;
}
</style>
