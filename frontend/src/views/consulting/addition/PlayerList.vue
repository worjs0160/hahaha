<template>
  <div class="main-human scroll-wrap main-scrollbar-hidden" style="overflow-y:scroll;">

    <div class="scroll-cover"></div>

    <div class="main-human-header">
      <h1 class="pre-600">선수 관리</h1>
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

        <h2 class="pre-600">등록된 훈련선수({{accountList.length}})</h2>

      </div>

      <v-row class="human" align="end">
        <v-col cols="2" class="pb-0">
          <p class="name pre-400">프로필</p>
        </v-col>
        <v-col cols="4" class="pb-0">
          <p class="name pre-400" style="margin-left:12px;">선수이름</p>
        </v-col>
        <v-col cols="3" class="pb-0">
          <p class="name pre-400" style="margin-left:12px;">운동종목</p>
        </v-col>
        <v-col cols="3" class="pb-0">
          <p class="name pre-400" style="margin-left:12px;">수상경력</p>
        </v-col>
      </v-row>

      <div class="humans-btm mt-4">

        <template v-for="item,idx in accountList">
          <v-row
          class="human"
          :key="idx"
          @click="consultingSettingDialog(true, item.id)"
          style="cursor: pointer;"
          v-if="searchByName(item.name)"
          >
            <v-col cols="2">
              <div class="imgBox">
                <img :src="profileList[idx].profile" alt="">
              </div>
            </v-col>
            <v-col cols="4"><p class="name pre-400">{{item.name}}</p></v-col>
            <v-col cols="3"><p class="name pre-400">{{item.sportType.value}}</p></v-col>
            <v-col cols="3"><p class="name pre-400">{{item.awards}}</p></v-col>
          </v-row>
        </template>

      </div>

    </div>


  </div>
</template>

<script>
export default {
  data: () => ({
    search:"",
    accountList:[],
    profileList:[],
  }),
  async created() {
    await this.loadingCover(true);
    await this.getPlayer();
    await this.getProfile();
    await this.loadingCover(false);
  },
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
    async getPlayer(){
      await this.$axios
      .get("consultings/api/player/")
      .then((res) => {
        this.accountList = res.data
      })
      .catch((err) => {
        console.log(err.response);
      });
    },
    async getProfile(){
      await this.$axios
      .get("consultings/api/image/")
      .then((res) => {
        this.profileList = res.data
      })
      .catch((err) => {
        console.log(err.response);
      });
    },
    consultingSettingDialog(state,id){
      this.$emit('consultingSettingDialog',state, id);
    },
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

<style></style>