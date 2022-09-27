<template>
  <v-container style="height:90%; ">
    <v-row style="height:100%; ">
      <v-col cols="4">
        <v-card rounded="xl" style="height:100%;" class="pa-3">
          <v-row class="pa-3">
            <v-card-text class="text-h5">10월 총 근무 시간</v-card-text>
            <v-col cols="6" class="text-h6 pa-0">45시간</v-col>
            <v-col cols="6" style="text-align:right;" class>60</v-col>
            <v-progress-linear
                v-model="workRatio"
                height="20"
                class="mb-3"
                style="pointer-events: none;"
            >
              <strong>{{(45/60)*100}}%</strong>
            </v-progress-linear>
            <div style="width:100%; border-bottom:0.5px solid gray;"></div>
          </v-row>
          <v-row class="pa-3">
              <v-col cols="12" class="text-h5">10월 예상 총 급여</v-col>
              <v-col cols="12">627,840원</v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col cols="8">
        <v-card rounded="xl" style="height:100%;" class="pa-3">
            <v-card-text class="text-h6">10월 실 수령액</v-card-text>
            <v-card-text style="text-align:right; border-bottom:0.5px solid gray;" class="text-h5 pb-5">570,600원</v-card-text>
          <v-row style="border-bottom:0.5px solid gray;" class="pt-2">
            <v-col cols="3" style="text-align:center;">
              기본 근무
            </v-col>
            <v-col cols="3" style="text-align:center;">
              주휴시간
            </v-col>
            <v-col cols="3" style="text-align:center;">
              시급
            </v-col>
            <v-col cols="3" style="text-align:center;">
              공제액
            </v-col>
          </v-row>
          <v-row style="border-bottom:0.5px solid gray;">
            <v-col cols="3" style="text-align:center;">
              60시간
            </v-col>
            <v-col cols="3" style="text-align:center;">
              12시간
            </v-col>
            <v-col cols="3" style="text-align:center;">
              8,720원
            </v-col>
            <v-col cols="3" style="text-align:center;">
              <v-row>
                <v-col class="pb-0" style="text-align:center;">
                  28,120
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pt-0" style="text-align:center;">
                  (국민연금)
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pb-0" style="text-align:center;">
                  21,530
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pt-0" style="text-align:center;">
                  (건강보험)
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pb-0" style="text-align:center;">
                  5,020
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pt-0" style="text-align:center;">
                  (고용보험)
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pb-0" style="text-align:center;">
                  2,010
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pt-0" style="text-align:center;">
                  (소득세)
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    workRatio:75,
    
  }),
  async created() {
    await this.loadingCover(true);
    await this.loadingCover(false);
  },
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  }
};
</script>

<style></style>