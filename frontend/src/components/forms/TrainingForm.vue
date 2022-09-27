<template>
  <!-- 훈련 상세 내용 폼 -->
  <v-card>
    <v-form class="pr-2">
      <v-card-text class="pb-0">
        <v-container>
          <v-row class="pa-0">
            <v-col cols="12" class="pa-0">
              <!-- 훈련 내용 Input 영역 -->
              <v-textarea
                id="contents"
                placeholder="훈련 내용"
                filled
                clearable
                outlined
                auto-grow
                v-model="tempContents"
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-form>
    <v-card-actions class="pt-0">
      <v-spacer></v-spacer>
      <v-btn color="red darken-1" text @click="closeDialog">닫기</v-btn>
      <v-btn color="#0dbc79" text @click="saveAction">저장</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    training: {
      trainingDate: "",
      contents: "",
      coach: Number,
      user: Number,
      id: null,
    },
  },
  data: () => ({
    tempContents: "",
  }),

  created() {
    this.tempContents = this.training.contents;
  },
  watch: {
    training: function () {
      this.tempContents = this.training.contents;
    },
  },
  methods: {
    closeDialog: function () {
      this.tempContents = this.training.contents;
      this.$emit("closeDialog");
    },
    saveAction: function () {
      //데이터가 이미 id를 갖는 경우 ==> PATCH or PUT 으로 수정 기능
      console.log(this.training)
      if (this.training.id) {
        this.training.contents = this.tempContents;
        if(!this.training.contents){
          this.training.contents = "";
        }
        this.$axios({
          method: "PATCH",
          url:
            "trainings/api/trainings/" +
            this.training.id +
            "/",
          data: this.training,
        }).then(() => {
          this.$emit("saveAction");
        });
      }
      //데이터가 id를 갖고 있지 않는 경우 ==> POST 로 새로운 데이터 생성
      else {
        this.training.contents = this.tempContents;
        this.$axios({
          method: "POST",
          url: "trainings/api/trainings/",
          data: this.training,
        }).then(() => {
          this.$emit("saveAction");
        });
      }
      this.closeDialog();
    },
  },
};
</script>

<style>
</style>