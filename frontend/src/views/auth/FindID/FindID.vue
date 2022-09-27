<template>
    <v-row justify="center">
        <v-col cols="8">
            <v-card elevation="2">
                <v-btn class="mt-2 mr-0" absolute right icon @click="moveToPage('Login')">
                    <v-icon>mdi-home</v-icon>
                </v-btn>
                <v-card-title class="text-h4">아이디 찾기</v-card-title>
                <v-card-subtitle>정보관리</v-card-subtitle>
                <v-divider class="mx-7"></v-divider>

                <div class="mx-7">
                     <v-card-text class="font-weight-medium text-h6">
                        유형 선택
                    </v-card-text> 
                    <v-container>
                        <v-row>

                            <v-col class="d-flex justify-center">
                                <v-card
                                    id="1"
                                    class="usertype-card"
                                    rounded="lg"
                                    color="#C4FCD7"
                                    @click="moveToPage('PlayerFindID')"
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
                                    @click="moveToPage('ExceptFindID')"
                                >
                                    <v-icon color="black" size="100"
                                        >fas fa-users</v-icon
                                    >
                                    <span>이 외</span>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-container>

                <v-card-actions>
                    <v-row class="mt-10">
                    <v-col cols="6">
                        <v-btn
                            block
                            large
                            class="mb-7"
                            @click="back"
                        >
                        이전으로
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

  }),

  methods: {
    moveToPage: function(val) {
      var router = this.$router;
      return router.push({ name: val });
    },
    back() {
        this.moveToPage('Login')
    },
  },
}
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