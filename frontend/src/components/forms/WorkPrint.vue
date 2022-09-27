<template>
<div>
  <div class="a4 print-area2">
    <!-- <div style="border: 1px solid black; width:100px; height:100px; float:right; text-align: center; margin-bottom:5px;">승 인
      <div style="border-bottom: 1px solid black; width:100px; height:10px;"></div>
    </div>
    <div style="border: 1px solid black; width:100px; height:100px; float:right; text-align: center; margin-bottom:5px;">검 토
      <div style="border-bottom: 1px solid black; width:100px; height:10px;"></div>
    </div>
    <div style="border: 1px solid black; width:100px; height:100px; float:right;  text-align: center;margin-bottom:5px;">접 수
      <div style="border-bottom: 1px solid black; width:100px; height:10px;"></div>
    </div> -->
    <table id="print-form">
    <colgroup>
      <col width="16%">
      <col width="16%">
      <col width="16%">
      <col width="16%">
      <col width="16%">
      <col width="16%">
    </colgroup>
      <tbody>
        <tr>
          <td class="table-header" style="font-size:20pt; height:25px;" colspan="6">{{formTitle}}</td>
        </tr>
        <tr>
          <td class="table-header" style="font-size:12pt; height:20px;" colspan="3">종목: {{selectedUser.sportType.value}}</td>
          <td class="table-header" style="font-size:12pt; height:20px;" colspan="3">성명: {{selectedUser.name}}</td>
        </tr>
        <tr>
          <td class="table-header" style="font-size:12pt; height:20px;" colspan="1">일자</td>
          <td class="table-header" style="font-size:12pt; height:20px;" colspan="1">제목</td>
          <td class="table-header" style="font-size:12pt; height:20px;" colspan="4">내용</td>
        </tr>
        <template v-if="Math.floor(printDataLen/9)>0">
          <!-- 단일 반복문 이용한 출력 -->
          <tr v-for="i in printDataLen" :key="i - 1">
            <td colspan="1" v-if="i <= printDataLen" style="font-size:11pt;">
              {{ printData[i - 1].workDate.substr(0,10) }}
            </td>
            <td colspan="1" v-else></td>
            <td colspan="1" v-if="i <= printDataLen" style="font-size:11pt;">
              {{ printData[i - 1].title.substr(10) }}
            </td>
            
            <td colspan="1" v-else></td>
            <td colspan="4" v-if="i <= printDataLen">
              <textarea class="text-area" readonly v-model="printData[i - 1].contents" style="
              background-color: transparent;
              border-style: none;
              width:90%;
              height:65px;
              resize: none;
              word-break: break-all;
              overflow: hidden;"
              ></textarea>
            </td>
            
            <td colspan="4" v-else>
              <textarea class="text-area" readonly style="
              background-color: transparent;
              border-style: none;
              width:90%;
              height:65px;
              resize: none;
              word-break: break-all;
              overflow: hidden;"
              ></textarea>
            </td>
            <!-- 
            <td v-if="i <= printDataLen">{{ printData[i - 1 + j * 9].workDate.substr(11, 5) }}</td>
            <td v-else></td>
            <td v-if="i <= printDataLen">{{ printData[i - 1 + j * 9].offTime.substr(11, 5) }}</td>
            <td v-else></td>
            <td v-if="i <= printDataLen">
            </td>
            <td v-else></td>
            -->
          </tr>
        </template>
        <template v-else>
          <!-- 단일 반복문 이용한 출력 -->
            <tr v-for="i in 9" :key="j+''+i">
              <td colspan="1" v-if="i <= printDataLen" style="font-size:11pt;">
                {{ printData[i - 1].workDate.substr(0,10) }}
              </td>
              <td colspan="1" v-else></td>
              <td colspan="1" v-if="i <= printDataLen" style="font-size:11pt;">
                {{ printData[i - 1].title.substr(10) }}
              </td>
              
              <td colspan="1" v-else></td>
              <td class="pa-0" colspan="4" v-if="i <= printDataLen">
                <textarea class="text-area" readonly v-model="printData[i - 1].contents" style="
                background-color: transparent;
                border-style: none;
                width:90%;
                height:80px;
                resize: none;
                word-break: break-all;
                overflow: hidden;"
                ></textarea>
              </td>
              
              <td colspan="4" v-else>
                <textarea class="text-area" readonly style="
                background-color: transparent;
                border-style: none;
                width:90%;
                height:80px;
                resize: none;
                word-break: break-all;
                overflow: hidden;"
                ></textarea>
              </td>
              <!-- 
              <td v-if="i <= printDataLen">{{ printData[i - 1].workDate.substr(11, 5) }}</td>
              <td v-else></td>
              <td v-if="i <= printDataLen">{{ printData[i - 1].offTime.substr(11, 5) }}</td>
              <td v-else></td>
              <td v-if="i <= printDataLen">
              </td>
              <td v-else></td>
              -->
            </tr>
        </template>

      </tbody>
    </table>
  </div>
</div>
</template>

<script>
import TeamHome from '../../views/team/home/TeamHome.vue';
export default {
  components: { TeamHome },
  props: [
    'formTitle',
    'printData',
    'selectedUser',
  ],
  data: () => ({
    formContent:'test',
    formUser:'test',
    formDate:'test',
    }),
  computed: {
    printDataLen() {
      if(this.printData == undefined) return 0;
      return this.printData.length;
    },
  }
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
@page a4sheet { size: 21cm 29.7cm; }
.a4 {
  page: a4sheet;
  page-break-after: always;
}

.print-area {
  display: flex;
  align-items: center;
}
.table-header{
  padding-top: 10px;
  padding-bottom: 10px;
}
.text-area{
  background-color: transparent;
  border-style: none;
  width:90%;
  height:100px;
  resize: none;
  word-break: break-all;
  overflow: hidden;
}
</style>
