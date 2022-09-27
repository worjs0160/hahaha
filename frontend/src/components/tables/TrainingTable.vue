<template>
  <v-container class="my-0 pa-0 overflow-y-auto" id="training-table">
    <v-simple-table class="hidden-sm-and-down pa-2">
      <thead>
        <tr>
          <!-- 월 선택 영역 시작-->
          <th colspan="4" class="text-center">
            <v-card elevation="0">
              <v-menu bottom rounded offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn text class="border text-h6" v-on="on">
                    {{ selectedMonth }}월 훈련일지
                  </v-btn>
                </template>
                <v-date-picker
                  locale="ko-kr"
                  type="month"
                  v-model="selectedDate"
                  no-title
                ></v-date-picker>
              </v-menu>
            </v-card>
          </th>
          <!-- 월 선택 영역 끝-->
        </tr>
        <tr>
          <th class="text-center" width="7%">날짜</th>
          <th class="text-center" width="43%">훈련내용</th>
          <th class="text-center" width="7%">날짜</th>
          <th class="text-center" width="43%">훈련내용</th>
        </tr>
      </thead>

      <tbody>
        <tr
          class="text-center"
          height="200px"
          v-for="i in aHalfOfLastDay"
          :key="i"
        >
          <!-- 날짜 영역(1) -->
          <td>{{ dayOfData(i) }}</td>
          <!-- 해당 날짜 훈련 내용 영역(1) -->
          <td class="px-0" style="position: relative">
            <div
              class="btn"
              v-if="dayOfData(i)"
              @click="showDialog(dayOfData(i))"
            >
              <v-btn icon class="ma-0 pa-0 pl-2" large color="white">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </div>
            <p
              :id="dayOfData(i)"
              class="px-2 py-1 mb-0"
              v-html="toHtmlFormat(dataOfDay(dayOfData(i)).contents)"
            ></p>
          </td>

          <!-- 날짜 영역(2) -->
          <td>{{ dayOfData(i + aHalfOfLastDay) }}</td>
          <!-- 해당 날짜 훈련 내용 영역(2) -->
          <td class="px-0" style="position: relative">
            <div
              class="btn"
              v-if="dayOfData(i + aHalfOfLastDay)"
              @click="showDialog(dayOfData(i + aHalfOfLastDay))"
            >
              <v-btn icon class="ma-0 pa-0 pl-2" large color="white">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </div>
            <p
              class="px-2 py-1 mb-0"
              :id="dayOfData(i + aHalfOfLastDay)"
              v-html="
                toHtmlFormat(dataOfDay(dayOfData(i + aHalfOfLastDay)).contents)
              "
            ></p>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
    <v-simple-table class="hidden-md-and-up pa-5">
      <thead>
        <tr>
          <!-- 월 선택 영역 시작-->
          <th colspan="4" class="text-center">
            <v-card elevation="0">
              <v-menu bottom rounded offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn text class="border text-h6" v-on="on">
                    {{ selectedMonth }}월 훈련일지
                  </v-btn>
                </template>
                <v-date-picker
                  locale="ko-kr"
                  type="month"
                  v-model="selectedDate"
                  no-title
                ></v-date-picker>
              </v-menu>
            </v-card>
          </th>
          <!-- 월 선택 영역 끝-->
        </tr>
        <tr>
          <th class="text-center" width="14%">날짜</th>
          <th class="text-center" width="86%">훈련내용</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="text-center"
          height="200px"
          v-for="i in lastDayOfMonth"
          :key="i"
        >
          <!-- 날짜 영역(1) -->
          <td>{{ dayOfData(i) }}</td>
          <!-- 해당 날짜 훈련 내용 영역(1) -->
          <td class="px-0" style="position: relative">
            <div
              class="btn"
              v-if="dayOfData(i)"
              @click="showDialog(dayOfData(i))"
            >
              <v-btn icon class="ma-0 pa-0 pl-2" large color="white">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </div>
            <p
              :id="dayOfData(i)"
              class="px-2 py-1 mb-0"
              v-html="toHtmlFormat(dataOfDay(dayOfData(i)).contents)"
            ></p>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
    <dialog-card ref="dialogCard">
      <training-form
        @saveAction="updateTableByUserAndDate()"
        @closeDialog="closeDialog()"
        :training="dataOfDay(dataIdx)"
      >
      </training-form>
    </dialog-card>
  </v-container>
</template>

<script>
import DialogCard from "/src/components/cards/DialogCard";
import TrainingForm from "/src/components/forms/TrainingForm";

export default {
  props: { todayDate: String },
  data: () => ({
    selectedDate: "",
    dataIdx: Number,
    monthTrainings: {},
  }),
  components: { DialogCard, TrainingForm },
  computed: {
    selectedMonth() {
      // console.log(this.selectedDate.split("-")[1]);
      return parseInt(this.selectedDate.split("-")[1], 10);
    },
    getSelectedUser: function () {
      return this.$store.state.selectedUser.id;
    },

    //테이블에 날짜를 표현하기 위해 마지막 날짜의 절반 값을 반환
    aHalfOfLastDay() {
      return Math.floor((this.lastDayOfMonth + 1) / 2);
    },
    //선택된 달의 마지막 일(day)를 반환
    lastDayOfMonth() {
      const splitedDate = this.selectedDate.split("-");
      const dateYear = splitedDate[0];
      const dateMonth = splitedDate[1];

      //선택된 달의 마지막 날짜(일)
      const lastDateOfMonth = new Date(dateYear, dateMonth, 0);

      return parseInt(lastDateOfMonth.getDate());
    },
  },

  async created() {
    this.selectedDate = this.todayDate.substring(0, 7); //당일 날짜의 yyyy-mm 형태로 selectedDate를 init

    await this.updateTableByUserAndDate();
  },

  watch: {
    getSelectedUser: function () {
      this.updateTableByUserAndDate();
    },

    selectedDate: function () {
      this.updateTableByUserAndDate();
    },
  },

  methods: {
    //day가 해당 달의 마지막 날짜를 넘으면 null 반환.
    dayOfData: function (day) {
      if (day > this.lastDayOfMonth) {
        return null;
      }
      return day;
    },
    //해당 날짜의 훈련 데이터 객체 반환(해당 날이 없으면 빈 객체 반환)
    dataOfDay: function (day) {
      const key = day;
      // 해당 일(day)에 해당하는 데이터가 이미 존재한 경우 해당 객체 반환 ==> UPDATE 동작과 동일
      if (key in this.monthTrainings) {
        return this.monthTrainings[key];
      }
      // 해당 일(day)의 데이터가 없는 경우  ==> CREATE 동작과 동일

      let newDate = ("0" + day).slice(-2);
      newDate = this.selectedDate + "-" + newDate;
      return {
        trainingDate: newDate,
        coach: this.$store.state.userStore.id,
        user: this.$store.state.selectedUser.id,
      };
    },

    closeDialog: function () {
      this.$refs.dialogCard.closeDialog();
    },

    //dialog를 띄우기 위한 함수
    showDialog: function (day) {
      this.dataIdx = day;
      this.$refs.dialogCard.showDialog();
    },

    //선택된 유저와 선택된 년월(yyyy-mm)으로 테이블 데이터 갱신
    updateTableByUserAndDate: function () {
      this.monthTrainings = {};

      this.$axios({
        method: "GET",
        url:
          "trainings/api/user_and_date/?user=" +
          this.$store.state.selectedUser.id +
          "&trainingDate=" +
          this.selectedDate,
      })
        .then((res) => {
          for (var i = 0; i < res.data.length; i++) {
            const training = res.data[i]; // 각각의 훈련 데이터 객체
            const dayOfTraining = parseInt(
              training["trainingDate"].split("-")[2],
              10
            ).toString(); //훈련날짜의 일(day)로 데이터 분류를 위한 키

            this.$set(this.monthTrainings, dayOfTraining, training); //코치로 받아온 유저데이터 users에 복사
          }
        })
        .catch((res) => {
          console.log("Failed to get training Data", res);
        });
    },

    toHtmlFormat(contents) {
      if (contents === undefined) {
        return null;
      }
      return String(contents).replace(/(?:\r\n|\r|\n)/g, "<br />");
    },
  },
};
</script>

<style scoped>
.border {
  border: solid 2px black;
}
tr > * {
  border-right: 1px solid #e0e0e0;
}
tr > th:first-child,
tr > td:first-child {
  border-left: 1px solid #e0e0e0;
}

tbody > tr:last-child > td {
  border-bottom: 1px solid #e0e0e0;
}

tr:hover:not(.v-data-table__expanded__content) {
  background: #ffffff !important;
}

thead th {
  border-top: 1px solid #e0e0e0;
}

#training-table .training-card {
  margin: 0;
  width: 96%;
  height: 200px;
}

#training-table tbody td {
  background-color: white;
  z-index: 3;
}

tbody td:nth-child(2):hover > .btn,
tbody td:nth-child(4):hover > .btn,
.btn :hover {
  display: flex;
}

tbody td p {
  text-align: left;
  word-break: break-all;
  word-wrap: break-word;
}

.btn {
  position: absolute;
  display: none;
  align-items: center;
  justify-content: center;
  top: 0;
  width: 100%;
  height: 100%;
  border: 2px solid black;
  background-color: #212121;
  opacity: 0.46;
  padding: 0;
}
</style>
