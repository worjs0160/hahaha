<template>
  <v-row justify="center">
    <v-col cols="12">
      <v-card elevation="2">
        <v-btn class="mt-2 mr-0" absolute right icon @click="moveToPage('Login')">
          <v-icon>mdi-home</v-icon>
        </v-btn>
        <v-card-title class="text-h4">회원가입</v-card-title>
        <v-card-subtitle>위플레이 회원가입</v-card-subtitle>
        <v-divider class="mx-7"></v-divider>
        <div class="mx-7">
          <v-card-text class="font-weight-medium text-h6 pb-0">
            선수 가입정보 입력
          </v-card-text>
          <v-container>
            <!-- 기본정보 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              기본정보
            </div>
          </v-container>
          <v-container style="border: 2px solid grey;">
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="3" class="d-flex justify-center align-center" style="border-right: 2px solid grey;">
                <div v-if="!data.profileImgSrc">프로필</div>
                <v-img max-width="100%" :src="uploadImageFile" v-if="uploadImageFile"></v-img>
              </v-col>
              <v-col cols="9">
                <v-container class="pa-0">
                  <v-row style="border-bottom: 2px solid grey;">
                    <v-col cols="4" class="d-flex justify-center align-center content-title">
                      아이디<span style="color:red; ">*</span>
                    </v-col>
                    <v-col cols="5">
                      <v-text-field
                        v-model="data.username"
                        :error-messages="err.idErrMsg"
                
                      >
                      </v-text-field>
                    </v-col>
                    <v-col cols="3">
                      <v-btn large @click="validId">중복확인</v-btn>
                    </v-col>
                  </v-row>

                  <v-row style="border-bottom: 2px solid grey;">
                    <v-col cols="4" class="d-flex justify-center align-center content-title">
                      비밀번호<span style="color:red; ">*</span>
                    </v-col>
                    <v-col cols="8">
                      <v-text-field
                        label="8자 이상, 특수문자, 숫자포함"
                        v-model="data.password"
                        type="password"
                        :error-messages="err.pwErrMsg"
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col cols="4" class="d-flex justify-center align-center content-title">
                      비밀번호 확인<span style="color:red; ">*</span>
                    </v-col>
                    <v-col cols="8">
                      <v-text-field
                        v-model="data.passwordValid"
                        type="password"
                        :error-messages="err.pwCkErrMsg"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                프로필<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" class="d-flex justify-center align-center" style="border-right: 2px solid grey;">
                <v-file-input
                  v-model="data.profileImgSrc"
                  label="클릭하여 사진 넣기"
                  accept="image/png, image/jpeg, image/bmp"
                  prepend-icon="mdi-camera"
                  show-size
                  style="font-weight: 1000;"
                  @change="onFileSelected"
                  :error-messages="err.profErrMsg"
                ></v-file-input>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                성별<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-select
                  v-model="data.gender"
                  :items="genderList"
                  item-text="type"
                  item-value="value"
                  :error-messages="err.genderErrMsg"
                ></v-select>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                이름<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.name"
                  :error-messages="err.nameErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                이메일
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.email"
                  type="mail"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                생년월일<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="year"
                  label="년(4자리)"
                  type="number"
                  :error-messages="err.yearErrMsg"
                  prepend-icon="mdi-calendar"
                  style="font-weight: 1000;"
                  @change="checkDate"
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-select
                  v-model="month"
                  label="월"
                  :items="selectMonth"
                  :error-messages="err.monthErrMsg"
                  style="font-weight: 1000;"
                ></v-select>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  v-model="day"
                  label="일"
                  type="number"
                  :error-messages="err.dayErrMsg"
                  style="font-weight: 1000;"
                  @change="checkDate"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                연락처
              </v-col>
              <v-col cols="6">
                <v-text-field
                  label="( - 제외)"
                  type="number"
                  min="0"
                  v-model="data.phoneNum"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="인증번호받기" large @click="getSmsNumber(data.phoneNum)"
                  >인증번호받기
                </v-btn>
              </v-col>
            </v-row>
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                인증번호 입력
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="data.authNum"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="인증번호확인" large @click="checkSmsNumber(data.phoneNum, data.authNum)"
                  >인증번호확인
                </v-btn>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                보호자 성명<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="2" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.guardianName"
                  :error-messages="err.guardNameErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="1" class="d-flex justify-center align-center content-title">
                관계<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="1" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.relation"
                  :error-messages="err.relationErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                보호자 이메일<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.guardianEmail"
                  :error-messages="err.guardEmailErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                보호자 전화번호<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="data.guardianNum"
                  type="number"
                  style="font-weight: 1000;"
                  :error-messages="err.guardNumErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="인증번호받기" large @click="getSmsNumber(data.guardianNum)"
                  >인증번호받기
                </v-btn>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                인증번호 입력<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="data.guardNumCheck"
                  type="number"
                  style="font-weight: 1000;"
                  :error-messages="err.guardNumCkErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="인증번호확인" large @click="checkSmsNumber(data.guardianNum, data.guardNumCheck)"
                  >인증번호확인
                </v-btn>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
              </v-col>
              <v-col cols="6">
                <v-text-field
                  label="*우편번호(주소검색)"
                  v-model="data.userZip"
                  readonly
                  :error-messages="err.zipErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn label="*주소검색" large @click="showDaum" style="font-weight: 1000;"
                  >주소검색
                </v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                주소지<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="10">
                <v-text-field
                  label="*기본주소(주소검색)"
                  v-model="data.userAddr1"
                  readonly
                  :error-messages="err.addr1ErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
              </v-col>
              <v-col cols="10">
                <v-text-field
                  label="상세주소(입력 해주세요)"
                  v-model="data.userAddr2"
                  :error-messages="err.addr2ErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <v-container>
            <!-- 경력사항 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              경력사항
            </div>
          </v-container>
          <v-container style="border: 2px solid grey;">
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                운동종목<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-select
                  v-model="data.sportType"
                  :items="sportTypeList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.sportErrMsg"
                ></v-select>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                선수경력<br>(숫자로 입력)
              </v-col>
              <v-col cols="1">
                <v-text-field
                  v-model="data.career"
                  suffix="년"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                소속(복지관)<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-select
                  v-model="data.team"
                  :items="teamList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.teamErrMsg"
                ></v-select>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                소속(기업)
              </v-col>
              <v-col cols="4">
                <v-select
                  v-model="data.company"
                  :items="companyList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                수상경력
              </v-col>
              <v-col cols="10">
                <v-textarea
                  v-model="data.awards"
                  clearable
                  clear-icon="mdi-close-circle"
                  no-resize
                  filled
                  max-height="200px"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <v-container>
            <!-- 개인사항 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              개인사항
            </div>
          </v-container>
          <v-container style="border: 2px solid grey;">
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                장애 유형<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-select
                  v-model="data.disabilityType"
                  :items="disabilityList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.disTypeErrMsg"
                ></v-select>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                장애 등급<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-select
                  :items="disabilityGradeList"
                  item-text="value"
                  item-value="id"
                  v-model="data.disabilityGrade"
                  :error-messages="err.disGradeErrMsg"
                ></v-select>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                신장<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="2" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.height"
                  placeholder="ex) 173"
                  suffix="cm"
                  type="number"
                  :error-messages="err.heightErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                체중<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="2" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.weight"
                  placeholder="ex) 55"
                  suffix="kg"
                  type="number"
                  :error-messages="err.weightErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                혈액형<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="2">
                <v-select
                  v-model="data.bloodType"
                  :items="bloodTypeList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.bloodErrMsg"
                ></v-select>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">  
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                휠체어 사용여부<span style="color:red; ">*</span>
              </v-col>
              <v-col class="d-flex justify-center" cols="2" style="border-right: 2px solid grey;">
                <v-switch
                  v-model="data.wheelchair"
                  :label="useWheelchair(data.wheelchair)"
                ></v-switch>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                시력(좌)<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="2" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.eyesightL"
                  placeholder="ex) 1.0"
                  type="number"
                  :error-messages="err.eyeLErrMsg"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                시력(우)<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="2">
                <v-text-field
                  v-model="data.eyesightR"
                  placeholder="ex) 1.0"
                  type="number"
                  :error-messages="err.eyeRErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                결혼여부<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-select
                  v-model="data.maritalStatus"
                  :items="maritalStatusList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.mariErrMsg"
                ></v-select>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                병역여부<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4">
                <v-select
                  v-model="data.militaryService"
                  :items="militaryServiceList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.miliErrMsg"
                ></v-select>
              </v-col>
            </v-row>

            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                최종학력<span style="color:red; ">*</span>
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-select
                  v-model="data.education"
                  :items="educationList"
                  item-text="value"
                  item-value="id"
                  :error-messages="err.eduErrMsg"
                ></v-select>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title" v-if="data.education==16">
                학과명
              </v-col>
              <v-col cols="4" v-if="data.education==16">
                <v-text-field
                  v-model="data.department"
          
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                학교명<span style="color:red; ">*</span>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="data.school"
                  :error-messages="err.schErrMsg"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <v-container>
            <!-- 비상연락망 -->
            <div class="text-h7 mt-6" style="font-weight: 900;">
              비상연락망(선택사항)
            </div>
          </v-container>
          <v-container style="border: 2px solid grey;">
            <v-row style="border-bottom: 2px solid grey;">
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                보호자 성명
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.subGuardianName"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                관계
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.subRelation"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                보호자 전화번호
              </v-col>
              <v-col cols="4" style="border-right: 2px solid grey;">
                <v-text-field
                  v-model="data.subGuardianNum"
                  type="number"
                  style="font-weight: 1000;"
                ></v-text-field>
              </v-col>
              <v-col cols="2" class="d-flex justify-center align-center content-title">
                보호자 이메일
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model="data.subGuardianEmail"
                  
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <v-card-actions>
            <v-row class="mt-10">
              <v-col>
                <v-btn
                  block
                  large
                  class="mb-7"
                  @click="back"
                >
                  이전으로
                </v-btn>
              </v-col>

              <v-col>
                <v-btn
                  block
                  large
                  class="mb-7"
                  @click="next"
                >
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
    // "":필수, null:선택
    data: {
      username: "",
      password: "",
      passwordValid: "",
      email: "",
      name: "",
      birthDate: "",
      gender: "", // 실제 적용시 ""로 초기화
      profileImgSrc: undefined,
      phoneNum: null,
      authNum: null,
      validation: null,
      userZip: "",
      userAddr1: "",
      userAddr2: "",
      userType: 2,

      sportType: "", // 실제 적용시 ""로 초기화
      team: "", // 실제 적용시 ""로 초기화
      company: null,
      career: 0,
      awards: null,

      disabilityType: "", // 실제 적용시 ""로 초기화
      disabilityGrade: "", // 실제 적용시 ""로 초기화
      height: "",
      weight: "",
      bloodType: "", // 실제 적용시 ""로 초기화
      wheelchair: false,
      eyesightL: "",
      eyesightR: "",
      maritalStatus: "", // 실제 적용시 ""로 초기화
      militaryService: "", // 실제 적용시 ""로 초기화
      education: "", // 실제 적용시 ""로 초기화
      school: "",
      department: null,

      divisionName: null,
      divisionNum: null,

      guardianName: "",
      relation: "",
      guardianNum: "",
      guardianEmail: "",
      subGuardianName: null,
      subRelation: null,
      subGuardianNum: null,
      subGuardianEmail: null,
      is_active: false // 가입시 유저 활성화 False로 세팅
    },
    url: null,
    userId: null,
    guardNumCheck: null,
    year: "",
    month: "",
    day: "",
    err: {
      idErrMsg: null, // 서버에서 반환한 아이디 에러 메시지
      pwErrMsg: null, // 서버에서 반환한 패스워드 에러 메시지
      pwCkErrMsg: null,
      nameErrMsg: null, // 서버에서 반환한 이름 에러 메시지
      emailErrMsg: null, // 서버에서 반환한 이메일 에러 메시지
      genderErrMsg: null, // 서버에서 반환한 성별 에러 메시지
      yearErrMsg: null, // 년 에러 메시지
      monthErrMsg: null, // 월 에러 메시지
      dayErrMsg: null, // 일 에러 메시지
      profErrMsg: null,
      zipErrMsg: null, // 서버에서 반환한 우편번호 메시지
      addr1ErrMsg: null,
      addr2ErrMsg: null,
      sportErrMsg: null,
      teamErrMsg: null,
      disTypeErrMsg: null,
      disGradeErrMsg: null,
      heightErrMsg: null,
      weightErrMsg: null,
      bloodErrMsg: null,
      eyeLErrMsg: null,
      eyeRErrMsg: null,
      mariErrMsg: null,
      miliErrMsg: null,
      eduErrMsg: null,
      schErrMsg: null,
      guardNameErrMsg: null,
      relationErrMsg: null,
      guardNumErrMsg: null,
      guardNumCkErrMsg: null,
      guardEmailErrMsg: null,
    },
    idValidFlag: false, // 아이디 중복확인 여부
    numValidFlag: false,
    
    genderList: [ // 성별 리스트
      { type: "남성", value: 1 },
      { type: "여성", value: 2 },
    ],
    bloodTypeList: [], // 혈액형 리스트
    maritalStatusList: [], // 결혼여부 리스트
    militaryServiceList: [], // 병역여부 리스트
    educationList: [], // 최종학력 리스트
    disabilityList: [], // 장애 리스트
    disabilityGradeList: [], // 장애 등급
    sportTypeList: [], // 운동종목 리스트
    companyList: [], // 기업목록 리스트
    teamList: [], // 복지관(훈련기관) 리스트
    
    uploadImageFile:"",
    selectMonth:["01","02","03","04","05","06","07","08","09","10","11","12"], // 월 선택
  }),

  watch: {
    "data.username": function() { // 아이디 체크
      this.idValidFlag = false; // 아이디 바꾸면 아이디 검증 플래그 초기화

      let check = /[a-z0-9]{5,20}/
      let checkEng_A = /[A-Z]/

      if(!this.data.username) {
        this.err.idErrMsg = "필수 정보입니다."
      }
      else if(check.test(this.data.username) == false || checkEng_A.test(this.data.username) == true) {
        this.err.idErrMsg = "5~20자의 영문 소문자, 숫자만 사용 가능합니다."
      }
      else this.err.idErrMsg = ""
    },
    "data.password": function() {// 비밀번호 체크 및 비밀번호 확인 체크
      let check = /[0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]{8,}/
      let checkNum = /[0-9]/
      let checkSpc = /[~!@#$%^&*()_+|<>?:{}]/

      if(check.test(this.data.password) == false || checkSpc.test(this.data.password) == false || checkNum.test(this.data.password) == false) {
        this.err.pwErrMsg = "8자 이상, 특수문자, 숫자를 포함하여야 합니다."
      }
      else {
        this.err.pwErrMsg = ""
      }

      if(this.data.password != this.data.passwordValid){
        this.err.pwCkErrMsg = "비밀번호가 일치하지 않습니다."
      }
      else this.err.pwCkErrMsg = ""
    },
    "data.passwordValid": function() {
      if(this.data.password != this.data.passwordValid){
        this.err.pwCkErrMsg = "비밀번호가 일치하지 않습니다."
      }
      else this.err.pwCkErrMsg = ""
    },
    "data.name": function() {
      if(!this.data.name){
        this.err.nameErrMsg = "필수 정보입니다."
      }
      else this.err.nameErrMsg = ""
    },
    "data.team": function() {
      if(!this.data.team){
        this.err.teamErrMsg = "필수 정보입니다."
      }
      else this.err.teamErrMsg = ""
    },
    "data.sportType": function() {
      if(!this.data.sportType){
        this.err.sportErrMsg = "필수 정보입니다."
      }
      else this.err.teamErrMsg = ""
    },
    "data.guardianNum": function() {
      if(!this.data.guardianNum){
        this.err.guardNumErrMsg = "필수 정보입니다."
      }
      else if(this.data.guardianNum.length != 11) {
        this.err.guardNumErrMsg = "11자리 번호를 입력해주세요."
      }
      else this.err.guardNumErrMsg = ""
    },
    "data.guardNumCheck": function() {
      if(!this.data.guardNumCheck){
        this.err.guardNumCkErrMsg = "필수 정보입니다."
      }
      else if(this.data.guardNumCheck.length != 4){
        this.err.guardNumCkErrMsg = "4자리 인증번호를 입력해주세요."
      }
      else this.err.guardNumCkErrMsg = ""
    },
    "data.guardianEmail": function() {
      let checkEmail = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/

      if(!checkEmail.test(this.data.guardianEmail)) {
        this.err.guardEmailErrMsg = "이메일 형식이 맞지않습니다."
      }
      else this.err.guardEmailErrMsg = ""
    },
  },
  async created() {
    // 공통데이터 가져오기
    await this.$axios
      .get("datasets/api/commondata/")
      .then((res) => {
        for (const data of res.data) {
          // 1 (장애등급)
          if (data.maincategory == 1) {
            this.disabilityGradeList.push(data);
          }
          // 2 (혈액형)
          else if (data.maincategory == 2) {
            this.bloodTypeList.push(data);
          }
          // 3 (결혼여부)
          else if (data.maincategory == 3) {
            this.maritalStatusList.push(data);
          }
          // 4 (병역여부)
          else if (data.maincategory == 4) {
            this.militaryServiceList.push(data);
          }
          // 5 (최종학력)
          else if (data.maincategory == 5) {
            this.educationList.push(data);
          }
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 장애유형 가져오기
    await this.$axios
      .get("datasets/api/disability_type/")
      .then((res) => {
        for (const data of res.data) {
          this.disabilityList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 운동종목 가져오기
    await this.$axios
      .get("datasets/api/sport_type/")
      .then((res) => {
        for (const data of res.data) {
          this.sportTypeList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 기업목록 가져오기
    await this.$axios
      .get("datasets/api/company_list/")
      .then((res) => {
        for (const data of res.data) {
          this.companyList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });

    // 복지관(훈련기관) 가져오기
    await this.$axios
      .get("datasets/api/team_list/")
      .then((res) => {
        for (const data of res.data) {
          this.teamList.push(data);
        }
      })
      .catch((err) => {
        console.log(err.response);
      });
  },

  methods: {
    preview_image() {
      this.url = URL.createObjectURL(this.data.profileImgSrc)
    },
    // id 중복확인 함수
    validId() {
      let check = /[a-z0-9]{5,20}/
      let checkEng_A = /[A-Z]/

      if (!this.data.username) {
        this.err.idErrMsg = "필수 정보입니다.";
      } else if(check.test(this.data.username) == false || checkEng_A.test(this.data.username) == true) {
        this.err.idErrMsg = "5~20자의 영문 소문자, 숫자만 사용 가능합니다."
      } else {
        this.$axios
          .post("users/api/regist/chk_username/", {
            username: this.data.username,
          })
          .then((res) => {
            this.idValidFlag = true;
            this.err.idErrMsg = "";
            console.log(res);
            alert(res.data.msg);
          })
          .catch((err) => {
            console.log(err.response);
             alert(err.response.data.msg);
          });
      }
    },
    // 주소 가져오는 함수
    /* eslint-disable */
    showDaum() {
      new window.daum.Postcode({
        oncomplete: (data) => {
          // 팝업에서 검색결과 항목 클릭했을 때 실행할 코드를 작성하는 부분
          // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
          // 변수의 값이 없는 경우엔 공백('')값 가지므로, 이를 이용하여 분기
          let fullRoadAddr = data.roadAddress; // 도로명 주소 변수
          let extraRoadAddr = ""; // 도로명 조합형 주소 변수
          // 법정동명이 있을경우 추가한다. (법정리는 제외)
          // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
          if (data.bname !== "" && /[동|로|가]$/g.test(data.bname)) {
            extraRoadAddr += data.bname;
          }
          // 건물명이 있고, 공동주택일 경우 추가한다.
          if (data.buildingName !== "" && data.apartment === "Y") {
            extraRoadAddr +=
              extraRoadAddr !== ""
                ? ", " + data.buildingName
                : data.buildingName;
          }
          // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
          if (extraRoadAddr !== "") {
            extraRoadAddr = " (" + extraRoadAddr + ")";
          }
          // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
          if (fullRoadAddr !== "") {
            fullRoadAddr += extraRoadAddr;
          }
          // 우편번호와 주소 정보를 해당 필드에 넣는다.
          this.data.userZip = data.zonecode;
          this.data.userAddr1 = fullRoadAddr;
        },
      }).open();
    },
    // SMS 인증 번호를 받는 함수
    getSmsNumber(phoneNum) {
      this.$axios.post(
        "users/authSms/",
        {"phoneNum": phoneNum}
      )
      .then((res)=>{
      console.log(res)
      alert("입력된 번호로 인증번호를 전송하였습니다.")
      })
      .catch((err)=>{
        console.log(err)
        alert("11자리 번호를 입력해주세요.")
      })
    },
    // SMS 인증 번호를 인증하는 함수
    checkSmsNumber(phoneNum, authNum) {
      this.$axios({
        method: "GET",
        url:"users/authSms/",
        params :{"phoneNum": phoneNum, "authNum": authNum}
      })
      .then((res)=>{
        console.log(res)
        console.log(res.data.result)
        if(res.data.result) {
          this.numValidFlag = true
          alert("인증번호가 일치합니다.")
        }
        else {
          this.numValidFlag = false
          alert("인증번호가 일치하지 않습니다.")
        }
      })
      .catch((err)=>{
        console.log(err)
        alert("4자리 인증번호를 입력해주세요.")
      })
    },
    //date-picker 일 출력 형식 변환 (ex) 3일 => 3
    setDayFormat: function (date) {
      let returnDate = new Date(date).getDate();
      return returnDate;
    },
    // data 리셋 함수
    resetData: function() {
      Object.assign(this.$data.data, this.$options.data()["data"]);
      Object.assign(this.$data.err, this.$options.data()["err"]);
      this.idValidFlag = false;
      this.numValidFlag = false;
    },
    signup() {
      this.$axios
        .post("users/api/regist/", this.data)
        .then((res) => {
          this.userId = res.data.id;
          console.log(this.data.profileImgSrc)
          if (this.data.profileImgSrc) {
            this.sendImages();
          }
          this.moveToPage('Complete');
          console.log(res.data);
          console.log(this.userId);
        })
        .catch(() => {
          console.log("회원가입 실패");
          alert("정보를 정확히 입력해주세요."); // 에러 메시지 출력
        });
    },
    moveToPage: function(val) {
      var router = this.$router;
      return router.push({ name: val });
    },
    back() {
      this.resetData();
      this.moveToPage('Signup');
    },
    next() {
      if (!this.idValidFlag) {
        alert("아이디 중복확인 필요.");
      } 
      else if(!this.numValidFlag){
        alert("보호자 휴대폰 인증번호 확인 필요")
      }
      else{
        this.data.birthDate = this.year + this.month + this.day
        if(!this.totalCheck() && !this.checkDate()) {
          console.log(this.checkDate())
          this.signup();
        }
        else {
          alert("정보를 정확히 입력해주세요.") 
          console.log(this.checkDate())
        }
      }
    },
    useWheelchair(val){
      if(val) return "사용"
      else if(!val) return "미사용"
    },
    //dialog를 띄우기 위한 함수
    showDialog: function () {
      this.$refs.dialogCard.showDialog();
      console.log(this.data.profileImgSrc)
    },
    //dialog를 닫기 위한 함수
    closeDialog: function () {
      this.$refs.dialogCard.closeDialog();
    },
    sendImages() {
      var formdata = new FormData
      formdata.append("profileImgSrc", this.data.profileImgSrc)
      this.$axios
        .patch("users/api/image/" + this.userId + "/", formdata, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((res) => {
          console.log(res)
        })
        .catch((res) => {
          console.log(res)
        })
    },
    checkDate() {
      let check = null

      if(this.year.length != 4){ // 년도 입력을 4자리수를 넘겼을 경우
        this.err.yearErrMsg = "년도 4자리를 정확히 입력해주세요"
        check++
      }
      else if(this.year.length == 4) this.err.yearErrMsg = ""
  
      // 월(month) 체크
      if(!this.month){ // 월 선택을 안했을 경우
        this.err.monthErrMsg = "월 선택을 해주세요"
        check++
      }
      else this.err.monthErrMsg = ""

      // 일(day) 체크
      if(!this.day || this.day == 0){ // 날짜입력을 안했을 경우 (0도 포함)
        this.err.dayErrMsg = "일(날짜) 입력을 해주세요."
        check++
      }
      else if(this.day.length > 2){ // 날짜 입력을 2자리수를 넘겼을 경우
        this.err.dayErrMsg = "일(날짜)의 자릿수는 최대 2자리 입니다."
        check++
      }
      else if(this.day > new Date(this.year,this.month,0).getDate()){ // 해당 월의 마지막날보다 클 경우
        this.err.dayErrMsg = "해당 월에는 "+this.day+"일이 없습니다."
        check++
      }
      else this.err.dayErrMsg = ""

      // 날짜 입력이 1자리수이고, 1~9의 값일 경우 앞에 0을 붙혀줌
      if(0 < this.day && this.day < 10 && this.day.length == 1){
        this.day = "0"+this.day
      }

      if(this.year && this.month && this.day){ // 년월일을 전부 입력했을 때
        var inputDate = this.year+"-"+this.month+"-"+this.day //입력한 날짜
        var today = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10) // 오늘 날짜
        if(new Date(inputDate).getTime() > new Date(today).getTime()){ // 입력한 날짜가 오늘 날짜보다 앞설 경우
          this.err.yearErrMsg = "미래에서 오셨군요 ^^"
          check++
        }
        else if(Math.abs(new Date(today).getTime()-new Date(inputDate).getTime())>3155760000000){ // 입력한 날짜가 오늘 날짜보다 100년 전인 경우
          this.err.yearErrMsg = "정말인가요..?"
          check++
        }
      }

      return check
    },
    totalCheck() {
      let check = null
      //비밀번호 빈값 체크
      if(!this.data.password){
        this.err.pwErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.nameErrMsg = ""

      //비밀번호 확인 빈값 체크
      if(!this.data.passwordValid){
        this.err.pwCkErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.nameErrMsg = ""

      //이름 빈값 체크
      if(!this.data.name){
        this.err.nameErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.nameErrMsg = ""

      //성별 빈값 체크
      if(!this.data.gender){
        this.err.genderErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.genderErrMsg = ""

      //프로필 빈값 체크
      if(!this.data.profileImgSrc){
        this.err.profErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.profErrMsg = ""

      //보호자 성명 빈값 체크
      if(!this.data.guardianName){
        this.err.guardNameErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.guardNameErrMsg = ""

      // 보호자 관계 빈값 체크
      if(!this.data.relation){
        this.err.relationErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.relationErrMsg = ""

      // 보호자 이메일 빈값 체크
      if(!this.data.guardianEmail){
        this.err.guardEmailErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.guardEmailErrMsg = ""

      // 보호자 전화번호 빈값 체크
      if(!this.data.guardianNum){
        this.err.guardNumErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.guardNumErrMsg = ""

      // 보호자 인증번호 빈값 체크
      if(!this.data.guardNumCheck){
        this.err.guardNumCkErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.guardNumCkErrMsg = ""

      // 우편번호 빈값 체크
      if(!this.data.userZip){
        this.err.zipErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.zipErrMsg = ""
      // 기본주소 빈값 체크
      if(!this.data.userAddr1){
        this.err.addr1ErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.addr1ErrMsg = ""
      // 상세주소 빈값 체크
      if(!this.data.userAddr2){
        this.err.addr2ErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.addr2ErrMsg = ""

      // 운동종목 빈값 체크
      if(!this.data.sportType){
        this.err.sportErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.sportErrMsg = ""

      // 복지관(훈련기관) 빈값 체크
      if(!this.data.team){
        this.err.teamErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.teamErrMsg = ""

      // 장애유형 빈값 체크
      if(!this.data.disabilityType){
        this.err.disTypeErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.disTypeErrMsg = ""

      // 장애등급 빈값 체크
      if(!this.data.disabilityGrade){
        this.err.disGradeErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.disGradeErrMsg = ""

      // 신장 빈값 체크
      if(!this.data.height){
        this.err.heightErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.heightErrMsg = ""

      // 체중 빈값 체크
      if(!this.data.weight){
        this.err.weightErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.weightErrMsg = ""

      // 혈액형 빈값 체크
      if(!this.data.bloodType){
        this.err.bloodErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.bloodErrMsg = ""

      // 시력(좌) 빈값 체크
      if(!this.data.eyesightL){
        this.err.eyeLErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.eyeLErrMsg = ""

      // 결혼여부 빈값 체크
      if(!this.data.maritalStatus){
        this.err.mariErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.mariErrMsg = ""

      // 병역여부 빈값 체크
      if(!this.data.militaryService){
        this.err.miliErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.miliErrMsg = ""

      // 최종학력 빈값 체크
      if(!this.data.education){
        this.err.eduErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.eduErrMsg = ""

      // 학교명 빈값 체크
      if(!this.data.school){
        this.err.schErrMsg = "필수 정보입니다."
        check++
      }
      else this.err.schErrMsg = ""

      return check
    },
    onFileSelected(){
      if(this.data.profileImgSrc){
      this.uploadImageFile = URL.createObjectURL(this.data.profileImgSrc)
      }
      else this.uploadImageFile = ""

    },
  },
};
</script>

<style>
  .dialog{
    width:800px;
    height:800px;
    padding:20px;
  }
  .content-title{
    font-weight: 900;
    border-right: 2px solid grey;
    background-color: rgba(238, 238, 238, 0.85);
  }
  input[type="number"]::-webkit-outer-spin-button,
  input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
</style>
