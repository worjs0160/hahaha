<template>
<div>
    <!-- <div style="border: 1px solid black; width:100px; height:100px; float:right; text-align: center; margin-bottom:5px;">승 인
      <div style="border-bottom: 1px solid black; width:100px; height:10px;"></div>
    </div>
    <div style="border: 1px solid black; width:100px; height:100px; float:right; text-align: center; margin-bottom:5px;">검 토
      <div style="border-bottom: 1px solid black; width:100px; height:10px;"></div>
    </div>
    <div style="border: 1px solid black; width:100px; height:100px; float:right; text-align: center; margin-bottom:5px;">접 수
      <div style="border-bottom: 1px solid black; width:100px; height:10px;"></div>
    </div> -->
  <div class="a4 print-area">
    <table id="print-form">
      <thead>
        <tr>
          <th colspan="6">{{formTitle}}</th>
        </tr>
        <tr>
          <th>훈련일자</th>
          <th>이름</th>
          <th>훈련스케줄</th>
          <th>훈련시작</th>
          <th>훈련종료</th>
          <th>훈련상태</th>
          <!-- <th>훈련종료판정</th> -->
        </tr>
      </thead>
      <tbody>
        <template v-if="Math.floor(printDataLen/10)>0">
            <!-- 단일 반복문 이용한 출력 -->
            <tr v-for="i in printDataLen" :key="j+''+i">
              <td v-if="i <= printDataLen">
                {{ printData[i - 1].onTime.substr(0,10) }}
              </td>
              <td v-else></td>
              <td v-if="i <= printDataLen">
                {{ printData[i - 1].user.name }}
              </td>
              <td v-else></td>
              <td v-if="i <= printDataLen">
                <template v-for="item of printData[i - 1].attType.days">
                  {{item}}
                </template>
              </td>
              <td v-else></td>
              <td v-if="i <= printDataLen">{{ printData[i - 1].onTime.substr(11, 5) }}</td>
              <td v-else></td>
              <td v-if="i <= printDataLen">{{ printData[i - 1].offTime.substr(11, 5) }}</td>
              <td v-else></td>
              <td v-if="i <= printDataLen">
                
              </td>
              <td v-else></td>
              <!-- <td v-if="i <= printDataLen">
              
              </td>
              <td v-else></td> -->
            </tr>
        </template>
        <template v-else>
          <!-- 단일 반복문 이용한 출력 -->
          <tr v-for="i in 10" :key="i">
            <td v-if="i <= printDataLen">
              {{ printData[i - 1].onTime.substr(0,10) }}
            </td>
            <td v-else></td>
            <td v-if="i <= printDataLen">
              {{ printData[i - 1].user.name }}
            </td>
            <td v-else></td>
            <td v-if="i <= printDataLen">
              <template v-for="item of printData[i - 1].attType.days">
                {{item}}
              </template>
            </td>
            <td v-else></td>
            <td v-if="i <= printDataLen">{{ printData[i - 1].onTime.substr(11, 5) }}</td>
            <td v-else></td>
            <td v-if="i <= printDataLen">{{ printData[i - 1].offTime.substr(11, 5) }}</td>
            <td v-else></td>
            <td v-if="i <= printDataLen">
              {{dataState[i-1]}}
            </td>
            <td v-else></td>
            <!-- <td v-if="i <= printDataLen">
            
            </td>
            <td v-else></td> -->
          </tr>
        </template>

      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  props: {
    formTitle:String,
    printData:Array,
    dataState:Array,
  },
  computed: {
    printDataLen() {
      if(this.printData == undefined) return 0;
      return this.printData.length;
    },
  },
};
</script>

<style scoped>
/* 테이블 전체 디자인 */
#print-form {
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 15pt;
}
/* 헤드 첫줄 제목 디자인 */
#print-form thead > tr:nth-child(1) {
  font-size: 25pt;
}
/* 테이블 헤드의 th 디자인 */
#print-form thead th {
  padding-top: 10px;
  padding-bottom: 10px;
}

/* 테이블 바디 여백 */
#print-form tbody td {
  height: 80px;
}

/* 테이블 테두리 한줄 설정 */
#print-form,
td,
th {
  border: 1px solid black;
  border-collapse: collapse;
}
/* A4 사이즈 설정 */
@page a4sheet {
  size: 21cm 29.7cm;
}
.a4 {
  page: a4sheet;
  page-break-after: always;
}

.print-area {
  display: flex;
  align-items: center;
}
</style>
