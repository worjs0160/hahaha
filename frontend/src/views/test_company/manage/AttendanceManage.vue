<template>
  <v-container class="pa-5">
    <v-row>
      <v-col style="border-bottom: 0.5px solid gray;">
        <v-card-title class="pa-0" style="font-weight: 800;">허용 IP 목록</v-card-title>
      </v-col>
      <v-col style="border-bottom: 0.5px solid gray;" align="end">
        <v-btn color="success" @click="companyIPAddDialog(true)">추가하기</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" class="py-0">
        <v-card-text style="text-align:center;">
          제목
        </v-card-text>
      </v-col>
      <v-col cols="5" class="py-0">
        <v-card-text style="text-align:center;">
          장소
        </v-card-text>
      </v-col>
      <v-col cols="4" class="py-0">
        <v-card-text style="text-align:center;">
          허용 IP
        </v-card-text>
      </v-col>
    </v-row>
    <v-row style="border-bottom: 0.5px solid gray;" v-for = "(item, idx) in getIP" :key="idx" >
      <v-col cols="3" class="py-0 mt-2">
        <v-card-text style="text-align:center;">
          {{item.title}}
        </v-card-text>
      </v-col>
      <v-col cols="5" class="py-0">
        <v-card-text style="text-align:center;">
          {{item.place}}
        </v-card-text>
      </v-col>
      <v-col cols="4" class="py-0">
        <v-card-text style="text-align:center;">
          {{item.permissionIP}}
        </v-card-text>
      </v-col>
    </v-row>
    <!-- <v-row>
      <v-col style="border-bottom: 0.5px solid gray;">
        <v-card-title class="pa-0" style="font-weight: 800;">허용IP 등록하기</v-card-title>
      </v-col>
    </v-row>
    <v-row class="mt-5 background">
      <v-card-text style="font-weight: 700;">등록된 IP에서만 출퇴근을 체크할 수 있습니다.</v-card-text>
    </v-row>
    <v-row>
      <v-col cols="3" class="pb-0">
        <v-card-text class="px-0" style="font-weight: 700;">유형 제목</v-card-text>
      </v-col>
      <v-col cols="9" class="pb-0">
        <v-text-field
          v-model="data.title"
          filled
          hide-details="false"
          background-color="rgba(240, 240, 240)"
          rounded
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" class="pb-0">
        <v-card-text class="px-0" style="font-weight: 700;">근무지 IP</v-card-text>
      </v-col>
      <v-col cols="9" class="pb-0">
        <v-text-field
          v-model="data.permissionIP"
          filled
          label="ex:192.168.0.1"
          hide-details="false"
          background-color="rgba(240, 240, 240)"
          rounded
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <v-card-text class="px-0" style="font-weight: 700;">근무지 GPS</v-card-text>
      </v-col>
      <v-col>
        <v-switch
          v-model="gpsSwitch"
          :label="`${gpsStat.toString()}`"
        ></v-switch>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" class="pb-0">
        <v-card-text class="px-0" style="font-weight: 700;">근무지 이름</v-card-text>
      </v-col>
      <v-col cols="9" class="pb-0">
        <v-text-field
          v-model="data.place"
          filled
          hide-details="false"
          background-color="rgba(240, 240, 240)"
          rounded
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row class="mt-5" justify="end">
      <v-col align="end">
        <v-btn @click="createIP" color="success">등록하기</v-btn>
      </v-col>
    </v-row> -->
  </v-container>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    this.data.createUser = this.$store.state.userStore.id //생성자
    this.data.company = this.$store.state.userStore.comID //고용기업
    await this.getIPList();
    await this.loadingCover(false);
  },
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    companyIPAddDialog(state){
      this.$emit('companyIPAddDialog',state);
    },
    async createIP() {
      await this.$axios({
        method: 'POST',
        url: "attendances/api/ipRegister/",
        data: this.data,
      })
      .then((res) => {
        console.log(res.data);
        this.$store.dispatch("callToast", {
          msg: "해당 허용IP이 등록되었습니다.",
          result: "success",
        });
      })
      .catch(() => {
        console.log("허용IP 생성 실패");
      });
    },
    async getIPList(){
      await this.$axios({
        method: "GET",
        url:"attendances/api/ipRegister/"
      })
      .then((res) => {
        this.getIP = res.data
        console.log(this.getIP)
      })
      .catch((err) => {
        console.log(err);
      });
    },
  },
  data: () => ({
    data:{
      createUser: 0,
      title: "",
      permissionIP: "",
      place: "",
      company: 0,
    },
    gpsSwitch: false,
    gpsStat: "사용안함",
    getIP: [],
  }),
  watch:{
    "gpsSwitch": function(){
      if(this.gpsSwitch == false)
        this.gpsStat = "사용안함"
      else
        this.gpsStat = "사용함"
    }
  },
};
</script>

<style>
  .background{
    background-color:rgba(240, 240, 240);
    border-radius: 10px;
  }
</style>