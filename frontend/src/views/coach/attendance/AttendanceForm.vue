<template>
  <v-card>
    <!--폼 타이틀-->
    <v-card-title class="pl-4 pb-2">{{ formTitle }}</v-card-title>
    <v-form class="px-2">
      <!--이름 입력-->
      <v-col class="px-2" cols="6" sm="4" md="4">
        <v-autocomplete
          label="이름(필수)"
          v-model="selectedUser"
          :items="userList"
          return-object
          item-text="name"
          :disabled="formState"
          solo
          hide-details="auto"
          :error-messages="nameError"
        >
          <!--자동완성에 보여지는 리스트의 아이템 형태 정의-->
          <template v-slot:item="data">
            <v-list-item-avatar color="primary">
              <span class="white--text">{{ data.item.name[0] }}</span>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="data.item.name"> </v-list-item-title>
            </v-list-item-content>
          </template>
          <!--자동완성에 보여지는 리스트의 아이템 형태 정의 끝-->
        </v-autocomplete>
      </v-col>
      <!--이름 입력 끝-->
      <v-col cols="10" md="12" class="d-flex px-2 flex-column flex-md-row">
        <!--출근 날짜 및 시간-->
        <v-text-field
          v-model="startDateTime"
          label="출근시간(필수)"
          type="datetime-local"
          hide-details="auto"
          class="mr-2 mb-4 mb-md-0"
          :error-messages="startError"
        ></v-text-field>
        <!--출근 날짜 및 시간 끝-->

        <!--퇴근 날짜 및 시간-->
        <v-text-field
          v-model="endDateTime"
          label="퇴근시간(필수)"
          type="datetime-local"
          hide-details="auto"
          class="mr-2 mr-md-0"
          :error-messages="finishError"
        ></v-text-field>
        <!--퇴근 날짜 및 시간 끝-->
      </v-col>
      <!--훈련 장소-->
      <v-col class="px-2" cols="6" sm="4" md="4">
        <v-text-field
          v-model="editedAttendance.workPlace"
          label="훈련장소"
          hide-details="auto"
          flat
          :error-messages="placeError"
        ></v-text-field>
      </v-col>
      <!--훈련 장소 끝-->
      <!--메모-->
      <v-col class="px-2" cols="12">
        <v-text-field
          v-model="editedAttendance.memo"
          label="메모"
          hide-details
          flat
        ></v-text-field>
      </v-col>
      <!--메모 끝-->
    </v-form>
    <v-card-actions class="pt-6 pb-4">
      <v-spacer></v-spacer>
      <v-btn color="error" @click="closeDialog">닫기</v-btn>
      <v-btn color="success" @click="saveAction">저장</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    puttedData: {
      user: Object,
      startWorkTime: "",
      finishWorkTime: "",
      workPlace: "",
      memo: "",
      id: null,
    },
  }, // 상위 컴포넌트로부터 받을 변수명($props 이용해 접근)
  data: () => ({
    editedAttendance: {
      user: { id: null, name: "" },
      startWorkTime: "",
      finishWorkTime: "",
      workPlace: "",
      memo: "",
      id: null,
    },
    formState: false, //폼의 상태가 생성인지 수정인지에 대한 상태값 ==> true:수정 / false: 생성
    userList: [], //이름 선택의 자동완성목록을 위한 유저리스트 Array

    nameError: null,
    startError: null,
    finishError: null,
    placeError: null,
  }),
  watch: {
    puttedData: function () {
      //넘어온 정보의 user가 이름(ID) 의 데이터 즉, undefined가 아닐 때
      this.editedAttendance = this.puttedData;
      if (this.puttedData.id !== null) {
        this.formState = true;
      } else {
        this.formState = false;
      }
    },
  },
  async created() {
    // 소속 팀 선수 리스트 가져오기
    await this.$axios
      .get(
        "/attendances/api/att_user/" +
          "?coach=" +
          this.$store.state.userStore.id
      )
      .then((res) => {
        for (var i = 0; i < res.data.length; i++) {
          this.$set(this.userList, i, res.data[i]);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });
    this.editedAttendance = this.puttedData;
    if (this.puttedData.id !== null) {
      this.formState = true;
    } else {
      this.formState = false;
    }
  },
  computed: {
    //폼의 상태값에 따라 폼 타이틀 결정 ==> 수정(ture): 근태기록 수정 / 생성(false): 근태기록 삭제
    formTitle: function () {
      if (this.formState) {
        return "근태기록 수정";
      } else {
        return "근태기록 생성";
      }
    },
    //유저 선택시 현재 입력 정보가 담기는 객체(editedAttendance)의 유저값을 변경
    selectedUser: {
      set: function (selectedData) {
        this.editedAttendance.user.name = selectedData.name;
        this.editedAttendance.user.id = selectedData.id;
      },
      get: function () {
        return this.editedAttendance.user.name;
      },
    },

    //출근시간 형식에 맞게 변환
    startDateTime: {
      set: function (workTime) {
        //출근시간 input 필드 데이터 형식에서 DB 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환

        if (this.editedAttendance.startWorkTime !== undefined) {
          this.editedAttendance.startWorkTime =
            workTime.replace("T", " ") + ":00";
        }
      },
      get: function () {
        //출근시간 DB 형식에서 input 필드 데이터 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환
        if (this.editedAttendance.startWorkTime !== undefined) {
          return this.editedAttendance.startWorkTime.replace(" ", "T");
        }
        return this.editedAttendance.startWorkTime;
      },
    },
    //퇴근시간 형식에 맞게 변환
    endDateTime: {
      set: function (workTime) {
        //퇴근시간 input 필드 데이터 형식에서 DB 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환
        if (this.editedAttendance.finishWorkTime !== undefined) {
          this.editedAttendance.finishWorkTime =
            workTime.replace("T", " ") + ":00";
        }
      },
      get: function () {
        //퇴근시간 DB 형식에서 input 필드 데이터 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환
        if (this.editedAttendance.finishWorkTime !== undefined) {
          return this.editedAttendance.finishWorkTime.replace(" ", "T");
        }
        return this.editedAttendance.finishWorkTime;
      },
    },
  },
  methods: {
    // dialog 닫기를 위한 메소드. 상위 컴포넌트로 closeDialog 이벤트 전달
    closeDialog: function () {
      this.errorStateInit();
      this.$emit("closeDialog");
    },

    errorStateInit: function () {
      this.nameError = null;
      this.startError = null;
      this.finishError = null;
      this.placeError = null;
    },
    //입력에 대한 검증
    checkInputData: function (Data) {
      //유저에 대한 입력이 없는 경우
      if (!Data.user) {
        this.nameError = "선수를 선택해 주세요.";
        return false;
      }
      this.nameError = null;
      //출근시간에 대한 입력이 없는 경우
      if (!Data.startWorkTime) {
        this.startError = "출근시간을 입력해 주세요.";
        return false;
      }
      this.startError = null;
      //퇴근시간에 대한 입력이 없는 경우
      // if (!Data.finishWorkTime) {
      //   this.finishError = "퇴근시간을 입력해 주세요.";
      //   return false;
      // }
      // this.finishError = null;
      //훈련장소에 대한 입력이 없는 경우
      if (!Data.workPlace) {
        this.placeError = "훈련장소를 입력해주세요.";
        return false;
      }
      this.placeError = null;
      //모든 입력이 확인된 후 출/퇴근 시간 순서 체크
      const start = new Date(Data.finishWorkTime);
      const finish = new Date(Data.startWorkTime);
      if (start < finish) {
        this.startError = "퇴근시간이 출근시간보다 앞설 수 없습니다.";
        this.finishError = "퇴근시간이 출근시간보다 앞설 수 없습니다.";
        return false;
      }
      this.startError = null;
      this.finishError = null;
      //모든 인풋에 대해 검증 완료
      return true;
    },

    //저장 동작을 수행하기 위한 메소드
    saveAction: function () {
      //기존의 데이터를 건드리지 않기 위해 전송용 객체 따로 생성
      let sendingData = new Object();
      Object.assign(sendingData, this.editedAttendance);
      sendingData.user = sendingData.user.id;

      //입력 데이터 검증
      if (!this.checkInputData(sendingData)) {
        return false;
      }

      //Attendance의 id가 존재하는 경우 ==> 수정(update)
      if (sendingData.id) {
        this.$axios({
          method: "PATCH",
          url: "attendances/api/att_list/" + this.editedAttendance.id + "/",
          data: sendingData,
        })
        .then(() => {
          this.$emit("saveAction", this.formTitle + " 완료");
          this.$emit("closeDialog");
        })
        .catch((err) => {
          console.log(err.response);
          if(err.response.data.non_field_errors) {
            alert(err.response.data.non_field_errors);
          }
          else { 
            alert(err.response.data);
          }
        });
      }
      // Attendance의 id가 존재하지 않는 경우 ==> 생성(Create)
      else {
        console.log(sendingData)
        this.$axios({
          method: "POST",
          url: "attendances/api/att_list/",
          data: sendingData,
        })
        .then(() => {
          this.$emit("saveAction", this.formTitle + " 완료");
          this.$emit("closeDialog");
        })
        .catch((err) => {
          console.log(err.response);
          if(err.response.data.non_field_errors) {
            alert(err.response.data.non_field_errors);
          }
          else { 
            alert(err.response.data);
          }
        });
      }
    },
  },
};
</script>

<style>
</style>
