<template>
  <v-container style="max-width: none; padding:30px 0;">
    <v-row style="height:100%; display:flex; justify-content: space-between;" class="inner">

      <v-col style="padding:0; width:270px !important; flex-basis: unset; flex-grow:unset;">

        <v-card class="card-border-radius max-height-none card-shadow" outlined style="height:100%; overflow:hidden;">

          <div class="main-manage-aside-header">
            <p class="pre-400">설정 메뉴</p>
          </div>

          <v-tabs class="main-manage-aside-tap pre-600" vertical hide-slider color="grey darken-1" v-model="idx" style="height:100%;">
            <v-tab
              v-for="item of subTabs"
              :key="item.idx"
              :title="item.name"
              @click="changeSubView(item.idx)">
              {{item.name}}

              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 11.5C14.9941 11.283 14.9177 11.097 14.7591 10.9295L10.1871 6.21082C10.0519 6.07441 9.89324 6 9.69931 6C9.30558 6 9 6.32244 9 6.73788C9 6.9363 9.0764 7.12232 9.21156 7.26494L13.3252 11.5L9.21156 15.7351C9.0764 15.8777 9 16.0575 9 16.2621C9 16.6776 9.30558 17 9.69931 17C9.88737 17 10.0519 16.9256 10.1871 16.7892L14.7591 12.0643C14.9236 11.903 15 11.717 15 11.5Z" fill="#B4B4B4" stroke="#B4B4B4" stroke-width="0.5"/>
              </svg>

            </v-tab>
          </v-tabs>

        </v-card>

      </v-col>


      <v-col style="padding:0; width:870px !important; flex-basis: unset; flex-grow:unset;">
        <v-card class="card-border-radius max-height-none card-shadow" outlined style="height:100%;">
          <!-- 컴포넌트 전환 영역 -->
          <div>
            <component
              :is="this.seltab.componentName"
              ref="childComponent"
              @coverSetChild="loadingCover"
              @companySettingDialog="companySettingDialog"
            >
            </component>
          </div>
        </v-card>
      </v-col>
      
    </v-row>
  </v-container>
</template>

<script>
import AccountCreate from "/src/views/test_company/manage/AccountCreate";
import HumanResource from "/src/views/test_company/manage/HumanResource";
import Attendance from "/src/views/test_company/manage/AttendanceManage";
import Work from "/src/views/test_company/manage/WorkManage";
import Vacation from "/src/views/test_company/manage/Vacation";
import Pay from "/src/views/test_company/manage/PayManage";

export default {
  components: { AccountCreate, HumanResource, Attendance, Work, Vacation, Pay, },
  async created() {
    await this.loadingCover(true);
    await this.loadingCover(false);
  },
  data: () => ({
    subTabs: [
      { idx: 0, componentName: "AccountCreate", name:"신규선수등록" },
      { idx: 1, componentName: "HumanResource", name:"선수관리" },
      //{ idx: 2, componentName: "Attendance", name:"근무지관리" },
      //{ idx: 3, componentName: "Work", name:"업무관리" },
      //{ idx: 4, componentName: "Vacation", name:"휴가설정" },
      //{ idx: 5, componentName: "Pay", name:"급여관리" },
    ],
    seltab: { idx: 0, componentName: "AccountCreate", name:"신규선수등록" },
  }),
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    changeSubView: function(event) {
      const tab = this.subTabs[event];
      this.seltab = tab;
    },
    companySettingDialog(state, id){
      this.$emit('companySettingDialog',state ,id);
    },
    reloadingHuman(){
      this.$refs.childComponent.companyAccount();
    },
  },
  computed: {
    idx: {
      get() {
        return this.seltab.idx;
      },
      set() {
        return;
      },
    },
  },
};
</script>

<style>

  .main-manage-aside-header {
    height: 72px;
    padding: 0 24px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    border-bottom: .5px solid #b4b4b4;
  }
  .main-manage-aside-header p {
    font-size: 20px;
    color: #2e2e2e;
    margin: 0;
    font-weight: 700;
  }
  .main-manage-aside-tap .v-tab {
    color: #2e2e2e !important;
    font-size: 18px;
    height: 56px !important;
    padding: 0 24px !important;
    justify-content: space-between !important;
    align-items: center;
  }
  .main-manage-aside-tap .v-tab--active {
    color: #49ada9 !important;
  }

</style>