<template>
  <v-row justify="center" class="mt-5">
    <v-col cols="9">
      <v-row>
        <v-col cols="6" align="start">
          <div class="humansBox">
            <div class="humans-top">
              <h2 class="pre-600">가입한 가게 현황<span> ({{count}})</span></h2>
            </div>

            <v-row class="human" style="width:100%;" align="end">
              <v-col cols="12" class="pb-0">
                <p class="name pre-700" style="margin-left:12px;">식당명 (대표자)</p>
              </v-col>
            </v-row>

            <div class="humans-btm mt-3 pt-3 scroll-wrap" style="overflow-y:scroll; max-height: 550px;" v-if="count==0">
              <v-row class="human pl-5" style="width:100%; background: #fff5b0;">
                등록된 가게가 없습니다.
              </v-row>
            </div>

            <div class="humans-btm mt-3 pt-3 scroll-wrap" style="overflow-y:scroll; max-height: 550px;" v-if="count>0">
              <v-row class="human" style="width:100%; background: #fff5b0;" v-for="(item, idx) in this.users" :key="`o-${idx}`">
                <v-col cols="12"><p class="name pre-400 hidden_txt_line">{{item.storeName}} ({{item.storeMaster}})</p></v-col>
              </v-row>
            </div>

          </div><!--e:humansBox-->
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>

export default {
  data: () => ({
    users:[],
    count: 0,
  }),
  created() {
    this.getUsers()
  },
  watch: {
    // "data.name": function() {
    //   if(!this.data.name) {
    //     this.err.nameErrMsg = "필수 정보입니다."
    //   }
    //   else this.err.nameErrMsg = ""
    // },
  },
  methods: {
    getUsers(){
      this.users = []
      this.$axios({
        method: "GET",
        url:"users/api/user/?userType=1"
      }).then((res) => {
        this.users = res.data
        this.count = res.data.length
      })
    },
  },
};
</script>

<style>
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
</style>
