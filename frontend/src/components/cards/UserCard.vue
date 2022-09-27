<template>
  <div>
    <v-card class="border card ma-2 pa-3 d-flex flex-column align-center" @click="dialog = true">
      <div>
        <!--선수 리스트 프로필 사진 영역 -->
        <v-avatar color="primary" size="50" v-if="!user.profile_img_src">
          <v-img max-height="150" max-width="150"></v-img>
        </v-avatar>
        <v-avatar color="primary" size="50" v-if="user.profile_img_src">
          <img :src="user.profile_img_src" />
        </v-avatar>
      </div>
      <!-- 선수 리스트 이름 카드 영역-->
        <center class="mt-2">{{ user.name }}</center>
        <center class="mb-2 text-caption" v-if="user.company">소속 : {{user.company.value}}</center>
        <center class="mb-2 text-caption" v-if="!user.company">무소속</center>
      <v-divider width="200" class="ma-2"></v-divider>
      <slot />
    </v-card>
    <!--유저 디테일 영역 시작-->
    <v-dialog v-model="dialog">
      <v-card>
        <v-btn class="mt-2 mr-0" absolute right icon @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-row class="py-2 ma-0 d-flex flex-column flex-md-row">
          <!--유저 디테일 프로필 사진 영역-->
          <v-col xs="12" sm="12" md="4" class="d-flex flex-column align-center justify-center">
            <v-avatar class="my-5" color="primary" size="200" tile v-if="!user.profile_img_src">
              <v-img max-height="150" max-width="150"></v-img>
            </v-avatar>
            <v-avatar class="mt-2 mb-4" color="primary" size="70%" tile v-if="user.profile_img_src">
              <img :src="user.profile_img_src" />
            </v-avatar>
            <p class="text-option">{{ user.name }}</p>
          </v-col>
          <!--유저 디테일 프로필 내용 영역-->
          <v-col xs="12" sm="12" md="4" class="text-option col-border">
            <p class="text-option" style="font-size:20px;">세부 사항</p>
            <v-simple-table>
              <tbody>
                <tr>
                  <td>신장 / 체중</td>
                  <td>{{ user.height }}cm / {{ user.weight }}kg</td>
                </tr>
                <tr>
                  <td>선수 전화번호</td>
                  <td>{{phoneNumFormat(user.phoneNum)}}</td>
                </tr>
                <tr>
                  <td>장애 유형 / 경증, 중증</td>
                  <td v-if="user.disabilityType">{{ user.disabilityType.value }} / {{ user.disabilityGrade.value }}</td>
                  <td v-if="!user.disabilityType"> </td>
                </tr>
                <tr>
                  <td>휠체어 사용 여부</td>
                  <td>{{dataCheck(user.wheelchair)}}</td>
                </tr>
                <tr>
                  <td>보호자 성명</td>
                  <td>{{user.guardianName}}</td>
                </tr>
                <tr>
                  <td>보호자 전화번호</td>
                  <td>{{phoneNumFormat(user.guardianNum)}}</td>
                </tr>
              </tbody>
            </v-simple-table>
          </v-col>
          <!--유저 디테일 근태 상황 차트 영역-->
          <v-col xs="12" sm="12" md="4" class="d-flex flex-column align-center justify-center">
            <slot name="chart">
              <p class="text-option" style="font-size:20px;">월간 근태 상황</p>
              <div style="height:90%; width:50%;">
                <ChartDoughnut :chartData="chartDataDoughnut" />
              </div>
              <p class="text-option">총 {{chartDataDoughnut.datasets[0].data[0]+chartDataDoughnut.datasets[0].data[1]}}시간 중 {{chartDataDoughnut.datasets[0].data[0]}} 시간 근무하셨습니다.</p>
            </slot>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import ChartDoughnut from "@/components/charts/ChartDoughnut.vue";
import Chart from "chart.js";
export default {
  components: {
      ChartDoughnut,
    },
  props: {
    user: { id: Number, name: String },
  },

  mounted(){
    //도넛 차트 가운데에 문자 입력 (n번째 줄, 내용)(중복 호출이 심해서 잠시 빼둠)
    //this.textCenter(0,this.today);
    //this.textCenter(1,"출석체크");
    //this.textCenter(2,"내용물");
  },

  methods: {
    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },
    phoneNumFormat: function (num) {
      // -이 들어간 전화번호 형식으로 바꿔줌
      if (num) {
        var phoneNum = "";
        phoneNum =
          num.substring(0, 3) +
          "-" +
          num.substring(3, 7) +
          "-" +
          num.substring(7, 11);
        return phoneNum;
      }
    },
    dataCheck: function (data) {
      //프로필 내용의 다양한 데이터를 원하는 형식으로 출력
      if (data === true) {
        return "사용";
      } else if (data === false) {
        return "미사용";
      } else if (data) {
        return data;
      } else {
        return "없음";
      }
    },
    gradeCheck: function (grade) {
      //급수 데이터를 원하는 형식으로 출력
      if (grade) {
        return grade + "급";
      } else {
        return "없음";
      }
    },
    textCenter(idx,val) {
      // 도넛차트 가운데에 내용 넣기
      Chart.pluginService.register({
      beforeDraw: function(chart) {
        var width = chart.chart.width;
        var height = chart.chart.height;
        var ctx = chart.chart.ctx;

        ctx.restore();
        ctx.font = 1.2 + "em sans-serif";
        ctx.textBaseline = "middle";
        var text = val;
        var textX = Math.round((width - ctx.measureText(text).width) / 2);
        var textY = (height / 2) + (idx * 20);

         ctx.fillText(text, textX, textY);
         ctx.save();
       }
     });

     Chart.plugins.unregister(this.chartDataDoughnut);
   },
  },
  data: () => ({
    dialog: false,
    //today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10),
    chartDataDoughnut: {
            datasets: [
            {
                data: [10, 20],
                backgroundColor: [
                    'rgba(255, 150, 0, 0.5)',
                    'rgba(0, 0, 0, 0.1)',
                ]
            }
            ],
            labels: ["출근 시간", "잔여 시간",]
        }
        // optionsDoughnut: {}
  }),
};
</script>

<style>
.border {
  border: solid 2px black;
}

.card {
  width: 300px;
  height: 520px;
}

.v-date-picker-table{
    height: 200px;
  }

/* @media screen and (max-width:1025px) and (min-width:515px){
  .card {
    width: 300px;
    height: 400px;
  }
  .v-date-picker-table{
    height: 220px;
  }
} */

.text-option{
  text-align: center;
  font-weight: bold;
}

.col-border{
  border-left: solid 2px rgb(204, 198, 198);
  border-right: solid 2px rgb(204, 198, 198);
  border-top: none;
  border-bottom: none;
}

@media screen and (max-width:960px) {
  .col-border{
    border-top: solid 2px rgb(204, 198, 198);
    border-bottom: solid 2px rgb(204, 198, 198);
    border-left: none;
    border-right: none;
  }
  .v-dialog{
    max-width:320px;
  }
  .v-card{
    max-height: 600px;
    overflow-y: auto;
  }
}
</style>