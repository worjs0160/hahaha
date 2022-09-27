<template>
  <v-card>
    <!--폼 타이틀-->
    <v-card-title class="pl-4 pb-2">{{ formTitle }}</v-card-title>
    <v-form class="px-2">
      
      <!-- 선수 이름 표기 시작 -->
      
      <v-row class="pa-0 ma-0">
        <v-col cols="6" sm="4" md="4" class="py-0 mt-0" style="color: grey;">
          선수 이름
        </v-col>
        <v-col cols="6" sm="4" md="4" class="py-0 mt-0" style="color: grey;">
          근무 요일
        </v-col>
      </v-row>
      <v-row class="px-2 ma-0">
        <v-col class="px-2" cols="6" sm="4" md="4">
          <v-autocomplete
            label="이름(필수)"
            v-model="selectedUser"
            :items="editedPlayer.name"
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
        <v-col class="px-2" cols="6" sm="4" md="4">
          <v-btn-toggle
            v-model="selectWeek"
            multiple
          >
            <v-btn>월</v-btn>
            <v-btn>화</v-btn>
            <v-btn>수</v-btn>
            <v-btn>목</v-btn>
            <v-btn>금</v-btn>
            <v-btn>토</v-btn>
            <v-btn>일</v-btn>
          </v-btn-toggle>
        </v-col>
      </v-row>
        <!-- <v-col class="px-2" cols="6" sm="4" md="4">
          {{selectWeek}}
        </v-col> -->
      <!-- 선수 이름 표기 끝-->
      


      <v-row class="px-2 ma-0">
          <!-- 이메일-->
          <v-col class="px-2" cols="6" sm="4" md="4">
            <v-text-field
              v-model="editedPlayer.email"
              label="선수 이메일"
              hide-details="auto"
              flat
              readonly
              :error-messages="placeError"
            ></v-text-field>
          </v-col>
          <!-- 이메일 끝-->
          <v-col class="px-2" cols="3" sm="3" md="3">
            <v-text-field
              v-model="editedPlayer.trainingStartTime"
              label="출근 시간 (00~24h)"
              hide-details="auto"
              :rules="[numberRule]"
              type="number"
              min="0"
              flat
              :error-messages="placeError"
            ></v-text-field>
          </v-col>
          <v-col class="px-2" cols="3" sm="3" md="3">
            <v-text-field
              v-model="editedPlayer.trainingFinishTime"
              label="퇴근 시간 (00~24h)"
              hide-details="auto"
              :rules="[numberRule]"
              type="number"
              min="0"
              flat
              :error-messages="placeError"
            ></v-text-field>
          </v-col>
      </v-row>
      <!--소속-->
      <v-row class="px-2 ma-0">
        <v-col class="px-2" cols="6" sm="4" md="4">
          <v-text-field
            v-model="editedPlayer.team.value"
            label="소속"
            hide-details="auto"
            flat
            readonly
            :error-messages="placeError"
          ></v-text-field>
        </v-col>
        <v-col class="px-2" cols="6" sm="4" md="4">
          <v-text-field
            v-model="editedPlayer.monthWorkTime"
            label="월간 근로계약 시간"
            hide-details="auto"
            type="number"
            :rules="[monthNumberRule]"
            flat
            :error-messages="placeError"
          ></v-text-field>
        </v-col>
      </v-row>
      <!--소속 끝-->
      <!--코치선택-->
      <v-row class="px-2 ma-0">
        <v-col class="px-2" cols="6" sm="4" md="4">
          <v-autocomplete
            label="코치(필수)"
            v-model="selectCoach"
            :items="coachList"
            return-object
            item-text="value"
            :disabled="false"
            solo
            hide-details="auto"
            :error-messages="nameError"
          >
            <!--자동완성에 보여지는 리스트의 아이템 형태 정의-->
            <template v-slot:item="data">
              <v-list-item-content>
                <v-list-item-title v-html="data.item.name"> </v-list-item-title>
              </v-list-item-content>
              <v-list-item-content>
                <v-list-item-title v-html="data.item.email"> </v-list-item-title>
              </v-list-item-content>
            </template>
            <!--자동완성에 보여지는 리스트의 아이템 형태 정의 끝-->
          </v-autocomplete>
        </v-col>
        <v-col class="px-2" cols="6" sm="8" md="8" style="color: red; text-align: center;">
          {{warningText}}
        </v-col>
      </v-row>
      <!--코치선택 끝-->
    </v-form>
    <v-card-actions class="pt-6 pb-4">
      <v-spacer></v-spacer>
      <v-btn color="error" @click="closeDialog()">닫기</v-btn>
      <v-btn color="success" @click="saveAction()">저장</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    puttedData: {
      team: Object,
      email:"",
      id: null,
      name: "",
    },
  }, // 상위 컴포넌트로부터 받을 변수명($props 이용해 접근)
  data: () => ({
    editedPlayer: {
      team: { id: null,},
      id: null,
      name: "",
      email:"",
      trainingFinishTime:"",
      trainingStartTime:"",
      monthWorkTime:"",
      workDay:[{id:null,maincategory:null,value:""}]
    },
    numberRule: val => {
      if(val > 24) return '24시간을 초과할 수 없습니다.'
      return true
    },
    monthNumberRule: val => {
      if(val > 800) return '800시간을 초과할 수 없습니다.'
      return true
    },
    formState: false, //폼의 상태가 생성인지 수정인지에 대한 상태값 ==> true:수정 / false: 생성
    userList: [], //이름 선택의 자동완성목록을 위한 유저리스트 Array
    coachList: [], //코치 선택의 자동완성목록을 위한 코치리스트 Array

    nameError: null,
    startError: null,
    finishError: null,
    placeError: null,

    selectCoach: {id:null, name:null},
    selectWeek: [],
    warningText: "",
  }),
  watch: {
    puttedData: function () {
      //넘어온 정보의 user가 이름(ID) 의 데이터 즉, undefined가 아닐 때
      this.editedPlayer = this.puttedData;
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
        "/users/api/coach/" +
          "?team=" +
          this.$store.state.userStore.team.id
      )
      .then((res) => {
        console.log(res.data)
        for (var i = 0; i < res.data.length; i++) {
          var value = res.data[i].name + ' ' + res.data[i].email
          var obj = {value:value}
          var setData = Object.assign(res.data[i], obj);
          this.$set(this.coachList, i, setData);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // var attObj = {
    //   attData:{
    //     week:[],
    //     start:null,
    //     end:null,
    //     monthTime:null,
    //   }
    // }
    // var attSetData = Object.assign(this.puttedData, attObj);
    // this.editedPlayer = attSetData;
    
    var weekList = [{id:0,value:"월요일"},{id:1,value:"화요일"},{id:2,value:"수요일"},{id:3,value:"목요일"},{id:4,value:"금요일"},{id:5,value:"토요일"},{id:6,value:"일요일"}]
    this.editedPlayer = this.puttedData;
    
    for(const week of this.puttedData.workDay){
      for(const weekListData of weekList)
        if(week.value == weekListData.value){
          this.selectWeek.push(weekListData.id)
        }
    }
    if (this.puttedData.id !== null) {
      this.formState = true;
    } else {
      this.formState = false;
    }
  },
  computed: {
    //폼의 상태값에 따라 폼 타이틀 결정 ==> 수정(ture): 선수정보 수정 / 생성(false): 선수정보 삭제
    formTitle: function () {
      if (this.formState) {
        return "선수정보 수정";
      } else {
        return "선수정보 생성";
      }
    },
    //유저 선택시 현재 입력 정보가 담기는 객체(editedPlayer)의 유저값을 변경
    selectedUser: {
      set: function (selectedData) {
        this.editedPlayer.name = selectedData.name;
        this.editedPlayer.id = selectedData.id;
      },
      get: function () {
        return this.editedPlayer.name;
      },
    },
    //코치 선택시 현재 입력 정보가 담기는 객체(editedPlayer)의 유저값을 변경
    selectedCoach: {
      set: function (selectedData) {
        this.selectCoach.name = selectedData.name;
        this.selectCoach.id = selectedData.id;
      },
      get: function () {
        return this.selectCoach;
      },
    },

    //출근시간 형식에 맞게 변환
    startDateTime: {
      set: function (workTime) {
        //출근시간 input 필드 데이터 형식에서 DB 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환

        if (this.editedPlayer.startWorkTime !== undefined) {
          this.editedPlayer.startWorkTime =
            workTime.replace("T", " ") + ":00";
        }
      },
      get: function () {
        //출근시간 DB 형식에서 input 필드 데이터 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환
        if (this.editedPlayer.startWorkTime !== undefined) {
          return this.editedPlayer.startWorkTime.replace(" ", "T");
        }
        return this.editedPlayer.startWorkTime;
      },
    },
    //퇴근시간 형식에 맞게 변환
    endDateTime: {
      set: function (workTime) {
        //퇴근시간 input 필드 데이터 형식에서 DB 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환
        if (this.editedPlayer.finishWorkTime !== undefined) {
          this.editedPlayer.finishWorkTime =
            workTime.replace("T", " ") + ":00";
        }
      },
      get: function () {
        //퇴근시간 DB 형식에서 input 필드 데이터 형식에 맞게 변환
        //YYYY-MM-DDThh:mm => YYYY-MM-DD hh:mm 로 변환
        if (this.editedPlayer.finishWorkTime !== undefined) {
          return this.editedPlayer.finishWorkTime.replace(" ", "T");
        }
        return this.editedPlayer.finishWorkTime;
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
    async saveAction () {
      
      let sendData = Array();
      sendData.push(this.editedPlayer)
      
      console.log(this.selectedCoach.id)
      // console.log(Number(this.editedPlayer.trainingStartTime) , Number(this.editedPlayer.trainingFinishTime))
      
      if(Number(this.editedPlayer.trainingStartTime) >= Number(this.editedPlayer.trainingFinishTime)){
        this.warningText = "퇴근 시간 보다 출근 시간이 같거나 클 수 없습니다.";
        return false
      }
      if(Number(this.editedPlayer.trainingStartTime) > 24 || Number(this.editedPlayer.trainingFinishTime) > 24){
        this.warningText = "시간을 다시 한번 확인해주세요.";
        return false
      }
      if(Number(this.editedPlayer.monthWorkTime) > 800){
        this.warningText = "800시간을 초과할 수 없습니다.";
        return false
      }

      if(this.editedPlayer.monthWorkTime == null || this.editedPlayer.monthWorkTime == ""){
        this.warningText = "월간 근로계약 시간을 입력해주세요.";
        return false
      }

      if(this.selectWeek.length == 0){
        this.warningText = "근무요일을 선택해주세요.";
        return false
      }

      if(this.selectedCoach.id == null || this.selectedCoach.id == ""){
        this.warningText = "코치를 선택해주세요.";
        return false
      }


      await this.$axios
        .post("users/api/detail/set_player_contect/", {
          player: sendData[0].id,
          set_data: {
            coach: this.selectedCoach.id,
            monthWorkTime:sendData[0].monthWorkTime,
            trainingStartTime:sendData[0].trainingStartTime,
            trainingFinishTime:sendData[0].trainingFinishTime,
          },
          category_data: {workDay:this.selectWeek},
        })
        .then((res) => {
          console.log(res);
          return true;
        })
        .catch((err) => {
          console.log(err);
          return false;
        });
      this.$router.go(); // 현재 경로로 페이지 다시 이동

    },
  },
};
</script>

<style>
</style>
