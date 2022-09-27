<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card elevation="2">
        <v-btn class="mt-2 mr-0" absolute right icon @click="moveToPage('Login')">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-card-title class="text-h4">회원가입</v-card-title>
        <v-card-subtitle>위플레이 회원가입</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>

        <div class="mx-7">
          <v-window v-model="step" touchless>
            <v-window-item :value="1">
              <v-card-text class="font-weight-medium text-h6">
                가입약관
              </v-card-text>
              <v-row>
                <v-col cols="12">
                  <v-card class="overflow-y-auto mx-3" max-height="300">
                    <v-card-text>
                      <div class="mb-4">
                        가입약관 내용 텍스트
                      </div>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
              <v-row justify="end">
                <v-col cols="2">
                  <v-checkbox v-model="chkTerms" label="동의합니다">
                  </v-checkbox>
                </v-col>
              </v-row>
            </v-window-item>

            <v-window-item :value="2">
              <v-card-text class="font-weight-medium text-h6">
                가입 유형 선택
              </v-card-text>
              <v-container>
                <v-row>

                  <v-col class="d-flex justify-center">
                    <v-card
                      class="usertype-card"
                      rounded="lg"
                      color="#C4FCD7"
                      @click="moveToPage('Coach')"
                    >
                      <v-icon color="black" size="100"
                        >mdi-account-clock</v-icon
                      >
                      <span>코치</span>
                    </v-card>
                  </v-col>
                  
                  <v-col class="d-flex justify-center">
                    <v-card
                      class="usertype-card"
                      rounded="lg"
                      color="#C4FCD7"
                      @click="moveToPage('Player')"
                    >
                      <v-icon color="black" size="100"
                        >mdi-weight-lifter</v-icon
                      >
                      <span>선수</span>
                    </v-card>
                  </v-col>

                  <v-col class="d-flex justify-center">
                    <v-card
                      class="usertype-card"
                      rounded="lg"
                      color="#C4FCD7"
                      @click="moveToPage('Team')"
                    >
                      <v-icon color="black" size="100">mdi-warehouse</v-icon>
                      <span>훈련기관</span>
                    </v-card>
                  </v-col>

                  <v-col class="d-flex justify-center">
                    <v-card
                      class="usertype-card"
                      rounded="lg"
                      color="#C4FCD7"
                      @click="moveToPage('Company')"
                    >
                      <v-icon color="black" size="100">mdi-domain</v-icon>
                      <span>기업</span>
                    </v-card>
                  </v-col>

                  <v-col class="d-flex justify-center">
                    <v-card
                      class="usertype-card"
                      rounded="lg"
                      color="#C4FCD7"
                      @click="moveToPage('Admin')"
                    >
                      <v-icon color="black" size="100">mdi-domain</v-icon>
                      <span>위플레이</span>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-window-item>
          </v-window>

          <v-card-actions>
            <v-row class="mt-10">
              <v-col>
                <v-btn
                  block
                  large
                  class="mb-7"
                  @click="back"
                >
                  이전으로
                </v-btn>
              </v-col>

              <v-col>
                <v-btn
                  v-if="chkTerms"
                  block
                  large
                  class="mb-7"
                  @click="next"
                  :disabled="step === 2"
                >
                  다음으로
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

export default {
  data: () => ({
    chkTerms: false, // 이용약관 동의 여부
    step: 1, // v-window-item 단계 변수
  }),
  
  methods: {
    moveToPage: function(val) {
      var router = this.$router;
      return router.push({ name: val });
    },
    back() {
      if(this.step===1){
        this.moveToPage('Login')
      }
      this.step--;
    },
    next() {
      this.step++;
    },
  },
};
</script>

<style scoped>
.usertype-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 200px;
  width: 200px;
}

.usertype-card span {
  color: black;
  margin-top: 30px;
  font-size: 20px;
}
</style>
