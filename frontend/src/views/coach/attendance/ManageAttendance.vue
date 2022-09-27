<template>
  <div class="mt-2 mx-4">
    <!--검색영역 및 근태 생성/삭제 버튼 -->
    <div class="d-flex align-center justify-space-between mb-2">
      <div class="d-flex mb-2" style="width: 300px">
        <v-text-field
          v-model="search"
          class="mr-2"
          append-icon="mdi-magnify"
          placeholder="근태 검색"
          hide-details
        ></v-text-field>
        <v-menu bottom rounded offset-y>
          <template v-slot:activator="{ on }">
            <v-btn icon class="align-self-end" v-on="on">
              <v-icon>mdi-filter-variant</v-icon>
            </v-btn>
          </template>
          <v-list class="pa-0">
            <v-list-item>
              <v-btn class="pl-0" text>-날짜</v-btn>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      <!--근태 생성/삭제 버튼 -->
      <div class="pb-0 pr-0 hidden-sm-and-down">
        <v-btn color="success" class="mr-2 py-0" @click="showDialog(null)">
          근태기록 생성
        </v-btn>
        <v-btn
          color="error"
          class="py-0"
          :disabled="!isChecked"
          @click="deleteAttendance"
        >
          근태기록 삭제
        </v-btn>
      </div>
      <div class="pb-0 att-btn-group hidden-md-and-up">
        <v-btn color="success" icon @click="showDialog(null)">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
        <v-btn
          color="error"
          icon
          :disabled="!isChecked"
          @click="deleteAttendance"
        >
          <v-icon>mdi-minus</v-icon>
        </v-btn>
      </div>
    </div>
    <v-data-table
      no-data-text="근태기록이 없습니다."
      v-model="checkedAttendance"
      :headers="tableItems"
      :items="attendanceList"
      :search="search"
      height="50vh"
      fixed-header
      show-select
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="showDialog(item)">
          mdi-pencil
        </v-icon>
      </template>
    </v-data-table>

    <dialog-card ref="dialogCard">
      <attendance-form
        :puttedData="toFormData"
        @closeDialog="closeDialog()"
        @saveAction="saveAction"
      ></attendance-form>
    </dialog-card>
  </div>
</template>

<script>
import DialogCard from "/src/components/cards/DialogCard";
import AttendanceForm from "/src/views/coach/attendance/AttendanceForm";

export default {
  components: {
    DialogCard,
    AttendanceForm,
  },
  computed: {
    //테이블에서 체크한 선수가 있는지 확인하는 함수(있으면 true, 없으면 false)
    isChecked: function() {
      if (this.checkedAttendance.length > 0) {
        return true;
      }
      return false;
    },
  },
  watch: {
    checkedUser: function(val) {
      console.log(val);
    },
  },
  async created() {
    await this.getAttendanceData();
  },

  data: () => ({
    //근태테이블 칼럼 정의(이름, 출근시간, 퇴근시간, 출근장소, 메모, 작업)
    tableItems: [
      {
        text: "이름",
        sortable: false,
        value: "user.name",
      },
      { text: "출근시간", value: "startWorkTime" },
      { text: "퇴근시간", value: "finishWorkTime" },
      { text: "출근장소", value: "workPlace" },
      { text: "메모", value: "memo" },
      { text: "작업", value: "actions", sortable: false },
    ],
    search: "",
    checkedAttendance: [], // 삭제 체크한 근태기록 담을 리스트
    attendanceList: [], // 근태기록 담을 리스트
    toFormData: {
      user: { id: null, name: "", username: "" },
      startWorkTime: "",
      finishWorkTime: "",
      workPlace: "",
      memo: "",
      id: null,
    }, // 근태 폼으로 보낼 임시 데이터
  }),
  methods: {
    // 코치에 해당하는 유저들의 근태 데이터 가져오기
    async getAttendanceData() {
      await this.loadingCover(true);
      await this.$axios
        .get(
          "/attendances/api/att_list/" +
            "?coach=" +
            this.$store.state.userStore.id
        )
        .then((res) => {
          console.log(this.$store.state.userStore)
          for (var i = 0; i < res.data.length; i++) {
            this.$set(this.attendanceList, i, res.data[i]);
            this.$delete(this.attendanceList[i], "url");
          }
        })
        .catch((err) => {
          console.log(err.response);
        });
      await this.loadingCover(false);
    },
    //근태 생성/수정 다이얼로그 열기
    showDialog: function(item) {
      
      if (item === null) {
        this.toFormData = {
          user: { id: null, name: "", username: "" },
          startWorkTime: "",
          finishWorkTime: "",
          workPlace: "",
          memo: "",
          id: null,
        };
      } else {
        this.toFormData = item;
      }
      this.$refs.dialogCard.showDialog();
    },

    //근태 생성/수정 다이얼로그 닫기
    closeDialog: function() {
      this.$refs.dialogCard.closeDialog();
    },
    //삭제요청 함수
    deleteAttendance: function() {
      var listDel = [];
      // 삭제할 게시물 pk 리스트로 묶기
      for (var i = 0; i < this.checkedAttendance.length; i++) {
        listDel.push(this.checkedAttendance[i].id);
      }

      this.$axios({
        method: "POST",
        url: "attendances/api/att_list/multiple_delete/",
        data: listDel,
      })
        .then(() => {
          // 삭제하고 새로고침시 데이터 길이가 줄어들어서 끝에있는 데이터를 없에주기위해 데이터 초기화 
          this.checkedAttendance = [];
          this.attendanceList = [];

          // 데이터 다시 불러오기
          this.getAttendanceData();
          
          this.$store.dispatch("callToast", {
            msg: "삭제 완료",
            result: "fail",
          });
        })
        .catch(() => {
          this.$store.dispatch("callToast", {
            msg: "삭제 실패",
            result: "fail",
          });
        });
    },
    //저장완료 확인 후 처리 함수
    saveAction: function(text) {
      this.$store.dispatch("callToast", { msg: text, result: "success" });
      this.getAttendanceData();
    },
    //MainAttendance로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 600px) {
  .att-btn-group {
    display: flex;
  }
}
</style>
