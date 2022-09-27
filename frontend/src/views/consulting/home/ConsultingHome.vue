<template>
  <v-container class="consulting-main-container">
  <!-- height:90%;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 20px; -->
    <v-row style="height:100%;">
      <v-col cols="12">
        <v-row>
          <v-col class="pre-400" cols="9" height="50" elevation="0" style="
          width: 100%;
          display: flex;
          justify-content: flex-start;
          position: relative;
          top: 10px;
          ">
            <div class="searchBox">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11.5 18C15.0899 18 18 15.0899 18 11.5C18 7.91015 15.0899 5 11.5 5C7.91015 5 5 7.91015 5 11.5C5 15.0899 7.91015 18 11.5 18Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M19 19L17 17" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <v-text-field
                v-if="selectFilter=='이름'"
                placeholder="선수이름 검색"
                clearable
                clear-icon="mdi-close-thick"
                hide-details="auto"
                v-model="searchName"
                maxlength="5"
              >
              </v-text-field>
              <v-text-field
                v-if="selectFilter=='주소'"
                placeholder="주소 검색"
                @change="test()"
                clearable
                clear-icon="mdi-close-thick"
                hide-details="auto"
                v-model="searchAddr"
              >
              </v-text-field>
              <v-select
                v-if="selectFilter=='운동종목'"
                placeholder="운동종목 검색"
                clearable
                clear-icon="mdi-close-thick"
                :items="sportTypeList"
                item-text="value"
                item-value="value"
                hide-details="auto"
                v-model="searchSport"
              ></v-select>
              <v-select
                v-if="selectFilter=='장애유형'"
                placeholder="장애유형 검색"
                clearable
                clear-icon="mdi-close-thick"
                :items="disabilityList"
                item-text="value"
                item-value="value"
                hide-details="auto"
                v-model="searchDisability"
              ></v-select>
              <v-text-field
                v-if="selectFilter=='경력'"
                type="number"
                placeholder="경력 검색"
                clearable
                clear-icon="mdi-close-thick"
                hide-details="auto"
                v-model="searchCareer"
                maxlength="2"
              >
              </v-text-field>
            </div>

            <div class="searchBox ml-2" style="width:15%;" v-if="selectFilter=='경력'">
              <v-checkbox
                :label="`${awardsState}`"
                hide-details="auto"
                v-model="searchAwards"
                class="px-0"
              ></v-checkbox>
            </div>
          </v-col>

          <v-col cols="3" height="50" elevation="0" style="
          width: 100%;
          display: flex;
          justify-content: flex-end;
          position: relative;
          ">
            <div class="pre-400 d-flex justify-center align-center ma-2" style="
            background: #F5F5F5;
            border-radius: 6px;
            padding: 0 20px;
            width:100px;
            ">
              <v-menu bottom rounded offset-y>
                <template v-slot:activator="{ attrs, on }">
                  <v-btn icon class="align-self-end" style="box-shadow: unset;" v-bind="attrs" v-on="on">
                    {{selectFilter}}<v-icon>mdi-filter-variant</v-icon>
                  </v-btn>
                </template>
                <v-list class="pa-0">
                  <v-list-item v-for="(item, idx) in filterItems" :key="idx">
                    <v-list-tile-title class="pl-0" style="cursor:pointer" @click="selectFilter=item, searchDataClear()">- {{ item }}</v-list-tile-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </div>
          </v-col>
        </v-row>
        <v-row class="mb-2">
          <v-chip
            v-if="searchName"
            class="ma-2"
            close
            @click:close="searchName = ''"
          >
            {{searchName}}
          </v-chip>
          <v-chip
            v-if="searchAddr"
            class="ma-2"
            close
            @click:close="searchAddr = ''"
          >
            {{searchAddr}}
          </v-chip>
          <v-chip
            v-if="searchSport"
            class="ma-2"
            close
            @click:close="searchSport = ''"
          >
            {{searchSport}}
          </v-chip>
          <v-chip
            v-if="searchDisability"
            class="ma-2"
            close
            @click:close="searchDisability = ''"
          >
            {{searchDisability}}
          </v-chip>
          <v-chip
            v-if="searchCareer"
            class="ma-2"
            close
            @click:close="searchCareer = ''"
          >
            {{searchCareer}}년
          </v-chip>
          <v-chip
            v-if="searchAwards"
            class="ma-2"
            close
            @click:close="searchAwards = false"
          >
            {{awardsState}}
          </v-chip>
        </v-row>


        <!-- 선수 카드 목록 영역 -->
        <v-slide-group
          v-model="model"
          class="pa-0"
          show-arrows
          style="
          width:100%;
          "
        >

        <v-slider-item
          v-for="item,idx in players"
          :key="item"
          class="mr-1"
        >
          <v-card
            v-bind:item="item"
            v-if="searchResult(item)"
            width="250"
            style="
            border-radius: 20px;
            box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.06);
            "
            class="scroll-hidden"
          >

            <div class="imgBox" style="
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
            ">

              <div class="pre-400" style="
                background: #fff;
                height: 35px;
                display: flex;
                color: #2e2e2e;
                font-weight:700;
                justify-content: center;
                align-items: center;
                font-size: 18px;
                ">
                  {{item.name}}
              </div>

              <v-img
                :src="playerImages[idx].profile"
                width="90%"
                height="250px"
                dark
                style="
                display: flex;
                justify-content: center;
                align-items: flex-end;
                border-radius: 15px;
                "
              ></v-img>
              
            </div>


            <v-list two-line>

              <v-list-item style="height: 45px !important; min-height: unset;">
                <v-list-item-icon>
                  <svg style="width:22px;height:22px" viewBox="0 0 24 24">
                      <path fill="currentColor" d="M17.58,4H14V2H21V9H19V5.41L15.17,9.24C15.69,10.03 16,11 16,12C16,14.42 14.28,16.44 12,16.9V19H14V21H12V23H10V21H8V19H10V16.9C7.72,16.44 6,14.42 6,12A5,5 0 0,1 11,7C12,7 12.96,7.3 13.75,7.83L17.58,4M11,9A3,3 0 0,0 8,12A3,3 0 0,0 11,15A3,3 0 0,0 14,12A3,3 0 0,0 11,9Z" />
                  </svg>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title style="font-size: 15px;">성별 : {{item.gender}}</v-list-item-title>
                </v-list-item-content>

              </v-list-item>

              <v-divider inset style="margin-left:0; max-width:100%; width:100%;"></v-divider>

              <v-list-item style="height: 45px !important; min-height: unset;">
                <v-list-item-icon>
                  <svg style="width:22px;height:22px" viewBox="0 0 24 24">
                      <path fill="currentColor" d="M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z" />
                  </svg>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title v-if="item.userAddr1" style="font-size: 15px;">주소 : {{item.userAddr1.split(" ")[0] + " " + item.userAddr1.split(" ")[1]}}</v-list-item-title>
                  <v-list-item-title v-if="!item.userAddr1" style="font-size: 15px;">주소 : </v-list-item-title>
                </v-list-item-content>

              </v-list-item>

              <v-divider inset style="margin-left:0; max-width:100%; width:100%;"></v-divider>

              <v-list-item style="height: 45px !important; min-height: unset;">
                <v-list-item-icon>
                  <svg style="width:22px;height:22px" viewBox="0 0 24 24">
                      <path fill="currentColor" d="M16.93 17.12L16.13 15.76L17.59 11.39L19 10.92L20 11.67C20 11.7 20 11.75 20 11.81C20 11.88 20.03 11.94 20.03 12C20.03 13.97 19.37 15.71 18.06 17.21L16.93 17.12M9.75 15L8.38 10.97L12 8.43L15.62 10.97L14.25 15H9.75M12 20.03C11.12 20.03 10.29 19.89 9.5 19.61L8.81 18.1L9.47 17H14.58L15.19 18.1L14.5 19.61C13.71 19.89 12.88 20.03 12 20.03M5.94 17.21C5.41 16.59 4.95 15.76 4.56 14.75C4.17 13.73 3.97 12.81 3.97 12C3.97 11.94 4 11.88 4 11.81C4 11.75 4 11.7 4 11.67L5 10.92L6.41 11.39L7.87 15.76L7.07 17.12L5.94 17.21M11 5.29V6.69L7 9.46L5.66 9.04L5.24 7.68C5.68 7 6.33 6.32 7.19 5.66S8.87 4.57 9.65 4.35L11 5.29M14.35 4.35C15.13 4.57 15.95 5 16.81 5.66C17.67 6.32 18.32 7 18.76 7.68L18.34 9.04L17 9.47L13 6.7V5.29L14.35 4.35M4.93 4.93C3 6.89 2 9.25 2 12S3 17.11 4.93 19.07 9.25 22 12 22 17.11 21 19.07 19.07 22 14.75 22 12 21 6.89 19.07 4.93 14.75 2 12 2 6.89 3 4.93 4.93Z" />
                  </svg>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title style="font-size: 15px;">운동종목 : {{item.sportType.value}}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-divider inset style="margin-left:0; max-width:100%; width:100%;"></v-divider>

              <v-list-item style="height: 45px !important; min-height: unset;">
                <v-list-item-icon>
                  <svg style="width:22px;height:22px" viewBox="0 0 24 24">
                      <path fill="currentColor" d="M8.5 4A2 2 0 0 1 6.5 6A2 2 0 0 1 4.5 4A2 2 0 0 1 6.5 2A2 2 0 0 1 8.5 4M5 7C3.89 7 3 7.89 3 9V15H5V22H8.61A7 7 0 0 1 6.5 17A7 7 0 0 1 10 10.95V9C10 7.89 9.11 7 8 7M13 8V16H18.5L21.2 19.6L22.8 18.4L19.5 14H15V8M12 12.23A5 5 0 0 0 8.5 17A5 5 0 0 0 13.5 22A5 5 0 0 0 18.5 17H16.5A3 3 0 0 1 13.5 20A3 3 0 0 1 10.5 17A3 3 0 0 1 12 14.41Z" />
                  </svg>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title style="font-size: 15px;">장애유형 : {{item.disabilityType.value}}</v-list-item-title>
                </v-list-item-content>

              </v-list-item>

              <v-divider inset style="margin-left:0; max-width:100%; width:100%;"></v-divider>

              <v-list-item style="height: 45px !important; min-height: unset;">
                <v-list-item-icon>
                  <svg style="width:22px;height:22px" viewBox="0 0 24 24">
                      <path fill="currentColor" d="M6 8C6 5.79 7.79 4 10 4S14 5.79 14 8 12.21 12 10 12 6 10.21 6 8M10 14C5.58 14 2 15.79 2 18V20H13.09C13.04 19.67 13 19.34 13 19C13 17.36 13.66 15.87 14.74 14.78C13.41 14.29 11.78 14 10 14M19 15L16 18H18V22H20V18H22L19 15Z" />
                  </svg>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title style="font-size: 15px;">경력 : {{item.career}}년</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-divider inset style="margin-left:0; max-width:100%; width:100%;"></v-divider>

              <v-list-item style="height: 45px !important; min-height: unset;">

                <v-list-item-icon>
                  <svg style="width:22px;height:22px" viewBox="0 0 24 24">
                      <path fill="currentColor" d="M17.71 6.15C17.46 5.38 16.79 5.21 16.45 4.77C16.14 4.31 16.18 3.62 15.53 3.15S14.23 2.92 13.7 2.77 12.81 2 12 2 10.82 2.58 10.3 2.77 9.13 2.67 8.47 3.15 7.86 4.31 7.55 4.77C7.21 5.21 6.55 5.38 6.29 6.15S6.5 7.45 6.5 8 6 9.08 6.29 9.85 7.21 10.79 7.55 11.23C7.86 11.69 7.82 12.38 8.47 12.85S9.77 13.08 10.3 13.23 11.19 14 12 14 13.18 13.42 13.7 13.23 14.87 13.33 15.53 12.85 16.14 11.69 16.45 11.23C16.79 10.79 17.45 10.62 17.71 9.85S17.5 8.55 17.5 8 18 6.92 17.71 6.15M12 12A4 4 0 1 1 16 8A4 4 0 0 1 12 12M14 8A2 2 0 1 1 12 6A2 2 0 0 1 14 8M13.71 15.56L13.08 19.16L12.35 23.29L9.74 20.8L6.44 22.25L7.77 14.75A4 4 0 0 0 9.66 15.17A4.15 4.15 0 0 0 11 15.85A3.32 3.32 0 0 0 12 16A3.5 3.5 0 0 0 13.71 15.56M17.92 18.78L15.34 17.86L15.85 14.92A3.2 3.2 0 0 0 16.7 14.47L16.82 14.37Z" />
                  </svg>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title style="font-size: 15px;">수상여부 : {{awardsList[idx]}}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-list-item style="height: 45px !important; min-height: unset;">
                  <v-row>
                    <v-col cols="12" align="center">
                      <v-btn @click="consultingPlayerDialog(true, item)" class="pre-400" style="
                      background: none;
                      border: 0;
                      font-size:15px;
                      width: 100%;
                      background: #61C0BD;
                      border-radius: 20px;
                      color: #fff;
                      box-shadow: unset;
                      ">상세정보 보기</v-btn>
                    </v-col>
                  </v-row>                
              </v-list-item>

            </v-list>
          </v-card>
        </v-slider-item>

        </v-slide-group>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    await this.getPlayer();
    await this.getProfile();

    // 장애유형 가져오기
    await this.$axios
    .get("datasets/api/disability_type/")
    .then((res) => {
      for (const data of res.data) {
        this.disabilityList.push(data);
      }
    })
    .catch((err) => {
      console.log(err.response);
    });

    // 운동종목 가져오기
    await this.$axios
    .get("datasets/api/sport_type/")
    .then((res) => {
      for (const data of res.data) {
        this.sportTypeList.push(data);
      }
    })
    .catch((err) => {
      console.log(err.response);
    });

    await this.loadingCover(false);
  },
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
    test(){
      console.log(this.searchAddr)
    },
    searchResult(item) {
      var nameCheck = 0
      var addrCheck = 0
      var sportCheck = 0
      var disabilityCheck = 0
      var careerCheck = 0

        // 이름 필터
        if (!this.searchName) {
          nameCheck = 1
        }
        else if (item.name.includes(this.searchName)) {
          nameCheck = 1
        }
        else nameCheck = 0

        // 주소 필터
        if (!this.searchAddr) {
          addrCheck = 1
        }
        else if (item.userAddr1.includes(this.searchAddr)) {
          addrCheck = 1
        }
        else addrCheck = 0

        // 운동종목 필터
        if (!this.searchSport) {
          sportCheck = 1
        }
        else if (item.sportType.value.includes(this.searchSport)) {
          sportCheck = 1
        }
        else sportCheck = 0

        // 장애유형 필터
        if (!this.searchDisability) {
          disabilityCheck = 1
        }
        else if (item.disabilityType.value.includes(this.searchDisability)) {
          disabilityCheck = 1
        }
        else disabilityCheck = 0

        // 경력 필터
        if (this.searchAwards >= 0 && this.searchAwards == false) { //검색 경력보다 이상인것만 보여줌
          if (!this.searchCareer) {
            careerCheck = 1
          }
          else if(item.career >= this.searchCareer){
            careerCheck = 1
          }
          else careerCheck = 0
        }
        else if(!this.searchCareer && this.searchAwards == true){
          if(item.awards){
            careerCheck = 1
          }
          else careerCheck = 0
        }
        else if(this.searchAwards >= 0 && this.searchAwards == true){
          if(item.career >= this.searchCareer && item.awards){
          careerCheck = 1
          }
          else careerCheck = 0
        }

        if(nameCheck + addrCheck + sportCheck + disabilityCheck + careerCheck == 5)return true
        else return false
    },
    consultingPlayerDialog(state, val){
      this.$emit('consultingPlayerDialog',state, val);
    },
    async getPlayer(){
      await this.$axios
      .get("consultings/api/player/")
      .then((res) => {
        var idx
        this.players = res.data
        for(idx in res.data){
          if(res.data[idx].awards) this.awardsList.push("있음")
          else this.awardsList.push("없음")
        }
      })
      .catch((err) => {
        console.log(err)
      });
    },
    async getProfile(){
      await this.$axios
      .get("consultings/api/image/")
      .then((res) => {
        this.playerImages = res.data
      })
      .catch((err) => {
        console.log(err.response);
      });
    },
  },
  data: () => ({
    searchName: "",
    searchAddr: "",
    searchSport: "",
    searchDisability: "",
    searchCareer: "",
    searchAwards: false,
    awardsState: "수상없음",
    players: [],
    playerImages: [],
    model: null,
    filterItems: ["이름", "주소", "운동종목", "장애유형", "경력",],
    selectFilter: "이름",
    sportTypeList: [],
    disabilityList: [],
    awardsList: [],
  }),
  watch: {
    "searchAwards": function(){
      if(this.searchAwards){
        this.awardsState = "수상있음"
      }
      else if(!this.searchAwards){
        this.awardsState = "수상없음"
      }
    },
  },
};
</script>

<style>
.header-profile-cover {
  background: #ffffff;
  width: 40px;
  height: 40px;
  border-radius: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.searchBox {
  width: 50%;
  height: 39px;
  display: flex;
  align-items: center;
  border-radius: 3px;
  border: 1px solid #e1e1e1;
  margin-bottom: 10px;
  padding: 0 12px;
}
.searchBox svg {
  margin-right: 13px;
}
.searchBox input {
  font-size: 16px;
  color: #2e2e2e;
  font-weight: 300;
  width: 95%;
  padding: 0 5px;
}
.searchBox input::placeholder {
  color: #B4B4B4;
  font-weight: 300;
}
.consulting-main-container {}
</style>