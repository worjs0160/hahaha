<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card elevation="2">
        <v-btn class="mt-2 mr-0" absolute right icon @click="moveToLogin">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-card-title class="text-h4">비밀번호 찾기</v-card-title>
        <v-card-subtitle>정보관리</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>

        <div class="mx-7">
          <v-window v-model="step" touchless>
            <v-window-item :value="1">
              <v-container>
                <v-row justify="start">
                  <v-col cols="6">
                    <v-text-field
                      v-model="data.name"
                      label="이름 (기업과 복지관 계정은 기관명)"
                      hide-details="auto"
                      :rules="rules"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field
                      v-model="data.username"
                      label="아이디"
                      hide-details="auto"
                      :rules="rules"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row justify="start">
                  <v-col>
                    <v-text-field
                      v-model="data.email"
                      label="이메일"
                      hide-details="auto"
                      :rules="rules"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row justify="start">
                  <v-col>
                    <v-text-field
                      v-model="data.phoneNum"
                      label="연락처 (-제외)"
                      hide-details="auto"
                      :rules="rules"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-window-item>

            <v-window-item :value="2">
              <v-card-text class="font-weight-medium text-h6">
                비밀번호 변경
              </v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="pwData.password"
                      label="변경할 비밀번호"
                      hide-details="auto"
                      type="password"
                      :error-messages="pwErrMsg"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="passwordValid"
                      label="비밀번호 재입력"
                      hide-details="auto"
                      type="password"
                      :error-messages="pwErrMsg"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-window-item>

            <v-window-item :value="3">
              <v-container>
                <v-alert
                  dense
                  border="left"
                  elevation="2"
                  prominent
                  type="info"
                >
                  패스워드가 변경되었습니다.
                </v-alert>

                <v-btn block large class="mb-7" @click="moveToLogin">
                  로그인 페이지 이동
                </v-btn>
              </v-container>
            </v-window-item>
          </v-window>

          <v-card-actions>
            <v-row>
              <v-col>
                <v-btn block large class="mb-7" @click="back">
                  이전으로
                </v-btn>
              </v-col>
              <v-col>
                <v-btn block large class="mb-7" @click="next">
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
    data: {
      username: "",
      name: "",
      email: "",
      phoneNum: "",
    },
    pwData: {
      password: "",
    },
    id: "",
    passwordValid: "",
    pwErrMsg: "",
    rules: [(value) => !!value || "값을 입력해주세요."],
    step: 1,
  }),
  methods: {
    validate_info() {
      this.$axios
        .post("users/api/regist/val_info/", this.data)
        .then((res) => {
          this.id = res.data.id;
          this.step++;
        })
        .catch((err) => {
          alert(err.response.data.msg);
        });
    },
    // 패스워드 공백과, 패스워드 패스워드 확인 일치 여부 검사하는 함수
    validate_pw() {
      if (!this.pwData.password || !this.passwordValid) {
        this.pwErrMsg = "패스워드와 패스워드 확인을 입력해주세요.";
        return false;
      } else if (this.pwData.password !== this.passwordValid) {
        this.pwErrMsg = "패스워드와 패스워드 확인이 일치하지 않습니다.";
        return false;
      } else {
        this.pwErrMsg = "";
        return true;
      }
    },
    change_pw(payload) {
      this.$axios
        .patch("users/api/regist/" + this.id + "/", {
          password: payload.password,
        })
        .then((res) => {
          console.log(res);
          this.step++;
        })
        .catch((err) => {
          console.log(err.response);
          this.pwErrMsg = err.response.data.password;
        });
    },

    moveToLogin: function() {
      var router = this.$router;
      return router.push({ name: "Login" });
    },
    next() {
      if (this.step == 1) {
        this.validate_info();
      } else if (this.step == 2) {
        if (this.validate_pw() == true) {
          this.change_pw(this.pwData);
        }
      } else this.step++;
    },
    back() {
      if (this.step == 1) {
        this.moveToLogin();
      } else this.step--;
    },
  },
};
</script>

<style></style>
