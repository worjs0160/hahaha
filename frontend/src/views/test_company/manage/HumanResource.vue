<template>

  <div class="main-human scroll-wrap main-scrollbar-hidden" style="overflow-y:scroll; height: calc(100vh - 300px);">

    <div class="scroll-cover"></div>

    <div class="main-human-header">
      <h1 class="pre-600">인원 관리</h1>
      <div class="header-btnBox">


        <v-menu offset-y>
          <!-- <template v-slot:activator="{ on }">
            <button type="button" class="pre-400" v-on="on">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.04061 4H11.9517C12.5263 4 13 4.50263 13 5.11236V6.33182C13 6.77676 12.736 7.32883 12.4797 7.60898L10.2278 9.71834C9.91723 9.99849 9.70754 10.5505 9.70754 10.9955V13.385C9.70754 13.7146 9.49789 14.1595 9.23387 14.3326L8.50393 14.8352C7.82059 15.2801 6.88097 14.7775 6.88097 13.8876V10.946C6.88097 10.5588 6.67133 10.0562 6.46167 9.77602L4.47376 7.5513C4.20974 7.27115 4.00009 6.77676 4.00009 6.43894V5.1618C3.99233 4.50262 4.46598 4 5.04061 4Z" stroke="#646464" stroke-width="1.2" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M4 11.9028V14.332C4 18.3806 5.6 20 9.6 20H14.4C18.4 20 20 18.3806 20 14.332V9.47369C20 6.94738 19.376 5.36033 17.928 4.53442C17.52 4.2996 16.704 4.12146 15.96 4" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M13 13H17" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M11 16H17" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              근무상태
            </button>
            
          </template> -->
          <div class="header-drop">
            <button class="pl-0 pre-400" type="button">이름</button>
            <button class="pl-0 pre-400" type="button">직급</button>
          </div>
        </v-menu>

      </div>
    </div><!--e:main-human-header-->

    <div class="searchBox">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M11.5 18C15.0899 18 18 15.0899 18 11.5C18 7.91015 15.0899 5 11.5 5C7.91015 5 5 7.91015 5 11.5C5 15.0899 7.91015 18 11.5 18Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M19 19L17 17" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <input
        class="pre-400"
        type="text"
        placeholder="이름으로 검색해보세요"
        v-model="search"
      >
    </div><!--e:searchBox-->

    <div class="humansBox">

      <div class="humans-top">

        <h2 class="pre-600">전체 구성원<span> ({{count}})</span></h2>

      </div>

      <v-row class="human" align="end">
        <v-col cols="1" class="pb-0">
          <p class="name pre-400">프로필</p>
        </v-col>
        <v-col cols="3" class="pb-0">
          <p class="name pre-400" style="margin-left:12px;">이름(ID)</p>
        </v-col>
        <v-col cols="4" class="pb-0">
          <p class="name pre-400" style="margin-left:12px;">훈련시간</p>
        </v-col>
        <v-col cols="4" class="pb-0">
          <p class="name pre-400" style="margin-left:12px;">훈련기관</p>
        </v-col>
      </v-row>

      <div class="humans-btm mt-4">

        <template v-for="item of accountList">
          <v-row class="human" :key="item.id" @click="companySettingDialog(true, item.id)" style="cursor: pointer;" v-bind:item="item" v-if="searchByName(item.name)">
            <v-col cols="1">
              <div class="imgBox">
                <img :src="item.profile" alt="">
              </div>
            </v-col>
            <v-col cols="3"><p class="name pre-400">{{item.name}}<br><span>({{item.username}})</span></p></v-col>
            <v-col cols="4"><p class="name pre-400">{{item.attType.onTime}}~{{item.attType.offTime}}</p></v-col>
            <v-col cols="4"><p class="name pre-400">{{item.teamID.teamName}}</p></v-col>
          </v-row>
        </template>

      </div>

    </div><!--e:humansBox-->

  </div>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    await this.companyAccount();
    await this.loadingCover(false);
  },
    data: () => ({
    count:0,
    accountList:[],
    search:"",
  }),
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    searchByName: function(name) {
      if (this.search.length === 0) {
        return true;
      } else if (name.includes(this.search)) {
        return true;
      } else {
        return false;
      }
    },
    companySettingDialog(state,id){
      this.$emit('companySettingDialog', state, id);
    },
    async companyAccount(){
      this.$axios({
        method: "GET",
        url: "users/api/employee/?comID="+this.$store.state.userStore.comID,
      }).then((res) => {
        this.accountList = res.data;
        this.count = res.data.length
      });
    }
  },
  computed: {
    idx: {
      get() {
        return this.$store.state.tabStore.subIdx;
      },
      set() {
        return;
      },
    },
  },
};
</script>

<style>
  .main-human {
    padding: 18px 24px 24px;
  }
  .main-human-header {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }
  .main-human-header h1 {
    font-size: 18px;
    color: #2e2e2e;
  }
  .main-human .header-btnBox button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 135px;
    height: 48px;
    background: #F5F5F5;
    border-radius: 10px;
    font-size: 18px;
    color: #646464;
  }
  .main-human .header-btnBox button svg {
    margin-right: 12px;
  }
  .main-human .searchBox {
    width: 100%;
    height: 39px;
    display: flex;
    align-items: center;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    margin-bottom: 32px;
    padding: 0 12px;
  }
  .main-human .searchBox svg {
    margin-right: 13px;
  }
  .main-human .searchBox input {
    font-size: 16px;
    color: #2e2e2e;
    font-weight: 300;
    width: 95%;
    padding: 0 5px;
  }
  .main-human .searchBox input::placeholder {
    color: #B4B4B4;
    font-weight: 300;
  }
  .humans-top h2 {
    font-size: 18px;
    color: #2e2e2e;
    margin-bottom: 16px;
  }
  .humans-top h2 span {
    font-size: 18px;
    color: #008bd6;
  }
  .humans-btm .human {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
    border-radius: 5px;
    transition: all .3s;
    background: #FFFFFF;
    box-shadow: 0px 2px 20px rgba(0, 0, 0, 0.06);
    border-radius: 6px;
  }
  .humans-btm .human:hover .name,
  .humans-btm .human:hover span {
    color: #49ADA9;
  }
  .humans-btm .human .imgBox {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    width: 60px;
    height: 60px;
    background: #CAE5F4;
    border-radius: 6px;
  }
  .humans-btm .human .imgBox img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .humans-btm .human p {
    margin: 0;
    margin-left: 12px;
    color: #2e2e2e;
    font-size: 16px;
    transition: all .3s;
    line-height: 1.2;
  }
  .humans-btm .human p span {
    font-size: 13px;
    color: rgb(172 172 177);
    transition: all .1s;
  }
  .header-drop {
    background: #fff;
    opacity: 1;
    display: flex;
    flex-direction: column;
  }
  .header-drop button {
    font-size: 15px;
    color: #2e2e2e;
    padding: 10px 0;
    transition: all .3s;
  }
  .header-drop button:hover {
    background: #CAE5F4;
  }
</style>