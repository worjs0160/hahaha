<template>
  <v-container style="padding:0;" class="paddingtop30">

    <div class="user-home-wrap">

      <div class="width270 height632 main-box-wrap user-info-left">

        <div class="header">
          <svg width="134" height="41" viewBox="0 0 134 41" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <rect width="134" height="41" fill="url(#pattern0)"/>
          <defs>
          <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
          <use xlink:href="#image0_142_2915" transform="translate(0 -0.00191638) scale(0.00142857 0.00466899)"/>
          </pattern>
          <image id="image0_142_2915" width="700" height="215" xlink:href="data:image/jpeg;base64,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1ewk06+kgccA5Q+or16c1ON0fJYmg6NRwZTqzAKACgDuvB2mtaWbXMq4knxgHstedianNKy6H0WWYd04c8t2dFXMemFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFAFDV9JttUh8udcOPuuOq1y4rB08TG09+50YfEzoSvE4288KajbsfJVZ07FTg/lXzlbJ68H7uqPbpZnRkve0ZWi8O6rI237Iy+7HArCOWYmTty2NpY+hFfEdFovhOO2kWe/YSyLysY+6D7+texg8njTanVd326HmYrM3NctPRHTgYHFe4eSLQAUAFABQAUAFABQAUAFABQAUAFABQBR1XS7bU4PLuFww+646rWlOpKm7o58RhoV42kcfeeFdQgY+QFnTsVOD+Vd0cTB76Hh1csrQfu6oqxeHtVkbb9kZfdjgVTr011Mo4DEN25ToNG8KJbyLNqDLIw5EY+6Pr61zVcU3pE9LC5WoPmq6+R04GOBXIeuLQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAUAFABQAhIHXigBnnRDjzU/wC+hQAefF/z1T/voUAHnxf89U/76FAB58X/AD1T/voUAHnxf89U/wC+hQAefF/z1T/voUAHnxf89U/76FAB58X/AD1T/voUAHnxf89U/wC+hQAqyxscK6k+gNAD6ADpQBH50X/PVP8AvoUAHnQ/89U/76FAB50P/PVP++hQAedD/wA9U/76FAB58X/PVP8AvoUAPVgwypBHqKAFoAKACgAoAKACgAoAKACgAoAKACgAoAMUAGKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKACgAoAKAMvU/EGm6bkXFwpkH8CfMaTaQ7HL3/AI+kJK2Fmqj+/Kcn8h/jU84+Uw7rxTrNyfmvGjHpGAv8qnmY7IzZb67mOZbmZj7uaVwI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"/>
          </defs>
          </svg>
        </div>

        <div class="middleBox">

          <h2>
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
            {{comData.comName}}
            </h2>

          <div>
            <h3>대표자</h3>
            <p>{{comData.ceoName}}</p>
          </div>

          <div>
            <h3>회사 전화번호</h3>
            <p class="tell">{{comData.comNum}}</p>
          </div>

          <div>
            <h3>회사 주소</h3>
            <p>{{comData.comAddr1}} {{comData.comAddr2}} ({{comData.comZip}})</p>
          </div>

          <div>
            <h3>사업자 등록번호</h3>
            <p>{{comData.businessNum}}</p>
          </div>

        </div>

        <div class="btmBox middleBox">

          <div>
            <h3>담당자명</h3>
            <p>{{comData.managerName}}</p>
          </div>

          <div>
            <h3>담당자 번호</h3>
            <p class="tell">{{comData.managerNum}}</p>
          </div>

        </div>

      </div>


      <div class="width870 height632 main-box-wrap user-info-right;" style="
      overflow:hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      ">
        <img
        style="width:100%;"
        :src="getNaverUrl()" alt="">
      </div>

    </div>
    
  </v-container>
</template>

<script>
export default {
  data: () => ({
    apiURL: "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster-cors?",
    option: "w=800&h=635&markers=type:d|pos:",
    comData: "",
    key: "21flkvcdod",
  }),
  async created() {
    await this.loadingCover(true);
    await this.getComInfo();
    await this.loadingCover(false);
  },
  methods: {
    loadingCover(val) {
      this.$emit("coverSetChild", val);
    },
    getComInfo() {
      this.$axios({
        method: "GET",
        url:
          "datasets/api/company_list/" +
          this.$store.state.userStore.comID +
          "/",
      })
        .then((res) => {
          this.comData = res.data;
          this.apiURL =
            this.apiURL +
            this.option +
            this.comData.longitude +
            " " +
            this.comData.latitude +
            "&X-NCP-APIGW-API-KEY-ID=" +
            this.key;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getNaverUrl() {
      const naverStaticMap =
        this.apiURL +
        this.option +
        this.comData.longitude +
        " " +
        this.comData.latitude +
        "&X-NCP-APIGW-API-KEY-ID=" +
        this.key;

      return naverStaticMap;
    },
  },
};
</script>

<style>
  .user-info-left .header {
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 0.5px solid #B4B4B4;
    height: 100px;
  }
  .user-info-left .middleBox {
    padding: 16px 24px 24px;
  }
  .user-info-left .middleBox h2,
  .user-info-left .middleBox h3,
  .user-info-left .middleBox p {
    margin: 0;
    font-family: 'Pretendard-Regular';
  }
  .user-info-left .middleBox h2 {
    font-size: 20px;
    color: #2e2e2e;
    margin-bottom: 32px;
    display: flex;
    align-items: center;
  }
  .user-info-left .middleBox h2 svg {
    margin-right: 10px;
  }
  .user-info-left .middleBox h3 {
    font-size: 13px;
    color: #989898;
    font-weight: 500;
  }
  .user-info-left .middleBox p {
    font-size: 16px;
    color: #2e2e2e;
  }
  .user-info-left .middleBox > div {
    margin-bottom: 16px;
  }
  .user-info-left .middleBox p.tell {
    color: #008BD6;
  }
  .user-info-left .middleBox {
    border-bottom: 0.5px solid #B4B4B4;
  }
  .user-info-left .btmBox {
    border-bottom: 0;
  }

</style>
