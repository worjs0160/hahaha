<template>
  <v-container style="height:100%; padding: 0; overflow: hidden;">
    <v-window v-model="step" touchless>
      <v-window-item :value="1">
        <div class="manage-val1-wrap" style="padding: 24px;">
          <div class="manage-val1-title">
            <p class="pre-700">기본정보</p>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>선수 가져오기</h2>
            <v-select
              class="val2-btm-selectBox new-player-val2-input-agency"
              v-model="selectPlayer"
              :items="playerList"
              item-text="name"
              item-value="id"
              filled
              hide-details="false"
            ></v-select>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>아이디</h2>
            <input
              class="inputBox-id"
              type="text"
              placeholder="아이디를 입력해 주세요"
              v-model="data.username"
            />
            <button class="id-chk-btn pre-400" type="button" @click="validId">
              중복 확인
            </button>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>이름</h2>
            <input
              type="text"
              placeholder="이름을 입력해 주세요"
              v-model="data.name"
            />
          </div>

          <div class="manage-val1-pw1Box manage-val1-inputBox">
            <h2>비밀번호</h2>
            <input
              type="password"
              placeholder="비밀번호를 입력해 주세요"
              v-model="data.password"
            />
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>비밀번호 확인</h2>
            <input
              type="password"
              placeholder="비밀번호를 한번 더 입력해 주세요"
              v-model="data.passwordValid"
            />
          </div>

          <span class="manage-val1-errBox pre-400" style="color: red;">{{
            err.basicMessage
          }}</span>
        </div>
        <!--e:manage-val1-wrap-->
      </v-window-item>
      <v-window-item :value="2">

        <div class="manage-val2-wrap input_label_position_transform" style="padding: 24px;">

          <div class="manage-val2-top">
            <div class="manage-val2-title">
              <p class="pre-700">훈련일정</p>
            </div>

            <!-- <div class="manage-value2-top-inputBox">
              <h2>훈련유형 이름</h2>
              <input
                class="inputBox-work-name pre-400"
                type="text"
                placeholder="훈련유형 이름을 입력해 주세요"
                v-model="attData.name"
              />
            </div> -->

            <div class="input73 manage-value2-top-inputBox">
              <h2>훈련시간</h2>
              <div class="times-selectBox">
                <input
                  class="times-input pa-2"
                  type="time"
                  v-model="attData.onTime"
                />

                <span>~</span>

                <input
                  class="times-input pa-2"
                  type="time"
                  v-model="attData.offTime"
                />
              </div>
            </div>

            <!-- <v-row>
              <v-col cols="6">
                <v-card-text class="px-0" style="font-weight: 700;">일 기본 휴게시간</v-card-text>
              </v-col>
              <v-col cols="6">
                <v-select
                  :items="rest"
                  label="휴게시간"
                  outlined
                ></v-select>
              </v-col>
            </v-row> -->

            <div class="manage-value2-top-inputBox">
              <h2>훈련일자</h2>
              <v-btn-toggle
                class="value-btnBox"
                v-model="attData.workDay"
                multiple
              >
                <v-btn value="24" class="px-0">월</v-btn>
                <v-btn value="25" class="px-0">화</v-btn>
                <v-btn value="26" class="px-0">수</v-btn>
                <v-btn value="27" class="px-0">목</v-btn>
                <v-btn value="28" class="px-0">금</v-btn>
                <v-btn value="29" class="px-0">토</v-btn>
                <v-btn value="30" class="px-0">일</v-btn>
              </v-btn-toggle>
            </div>

            <div class="value2-errBox">
              <p class="val2-err1">{{ err.attMessage }}</p>
              <p class="val2-err2" v-if="attData.monthWorkTime">
                주 {{ attData.monthWorkTime }}시간
              </p>
            </div>
          </div>
          <!--e:manage-val2-top-->

          <div class="manage-val2-btm">
            <div class="manage-val2-title manage-val2-title2">
              <p class="pre-700">훈련장소 선택</p>
            </div>

            <div class="manage-val2-btm-info">
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM11.25 8C11.25 7.59 11.59 7.25 12 7.25C12.41 7.25 12.75 7.59 12.75 8V13C12.75 13.41 12.41 13.75 12 13.75C11.59 13.75 11.25 13.41 11.25 13V8ZM12.92 16.38C12.87 16.51 12.8 16.61 12.71 16.71C12.61 16.8 12.5 16.87 12.38 16.92C12.26 16.97 12.13 17 12 17C11.87 17 11.74 16.97 11.62 16.92C11.5 16.87 11.39 16.8 11.29 16.71C11.2 16.61 11.13 16.51 11.08 16.38C11.03 16.26 11 16.13 11 16C11 15.87 11.03 15.74 11.08 15.62C11.13 15.5 11.2 15.39 11.29 15.29C11.39 15.2 11.5 15.13 11.62 15.08C11.86 14.98 12.14 14.98 12.38 15.08C12.5 15.13 12.61 15.2 12.71 15.29C12.8 15.39 12.87 15.5 12.92 15.62C12.97 15.74 13 15.87 13 16C13 16.13 12.97 16.26 12.92 16.38Z"
                  fill="#0081C7"
                />
              </svg>
              <p class="pre-400">
                등록된 IP에서만 훈련시간을 기록할 수 있습니다.<br />
                훈련기관을 선택하면 해당 기관의 IP가 선택됩니다.
              </p>
            </div>

            <div class="manage-value2-top-inputBox">
              <h2>훈련기관</h2>
              <v-select
                @change="selectTeam()"
                class="val2-btm-selectBox new-player-val2-input-agency"
                v-model="data.teamID"
                :items="teamList"
                item-text="teamName"
                item-value="id"
                filled
                hide-details="false"
                rounded
              ></v-select>
            </div>

            <div class="manage-value2-top-inputBox">
              <h2>훈련기관 IP</h2>
              <input
                class="inputBox-work-name new-player-val2-input-ip"
                type="text"
                v-model="ipData.permissionIP"
                readonly
              />
            </div>

            <div class="manage-value2-top-inputBox">
              <h2>GPS 사용여부</h2>
              <v-switch
                v-model="gpsSwitch"
                :label="`${gpsStat.toString()}`"
              ></v-switch>
            </div>

            <div class="value2-btm-errBox">
              <p class="val2-btm-err1">{{ err.ipMessage }}</p>
            </div>
          </div>
          <!--e:manage-val2-btm-->
        </div>
        <!--e:manage-val2-wrap-->
      </v-window-item>

      <v-window-item :value="3">
        <div class="manage-val3-wrap">
          <div class="manage-val3-header">
            <h1 class="pre-400">상세정보</h1>
          </div>

          <div class="val3Box1" style="padding: 24px 24px 32px;">

            <div class="imgBox" style="
            position: relative;
            ">
              <div class="imgBox-hidden">
                <v-img :src="url" alt="" style="
                position: relative;
                z-index: 3;
                height: 100%;
                width: 100%;
                object-fit: cover;
                "></v-img>
              </div>

              <v-file-input
                v-model="profileData.profile"
                @change="preview_image()"
                accept="image/png, image/jpeg, image/bmp"
                prepend-icon="mdi-camera"
                class="detail-profile-img-input"
                label="사진 추가하기"
                style="
                box-shadow: 0px 1px 8px rgba(0, 0, 0, 0.1);
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                border-radius: 5px;
                margin-top: 15px !important;
                "
              ></v-file-input>

              <!-- <div class="profile-inputBox" style="
              width: 100%;
              position: absolute;
              bottom:-50px;
              left: 50%;
              transform: translateX(-50%);
              display: flex;
              justify-content: center;
              align-items: center;
              border-radius: 5px;
              padding: 7px 0;
              box-shadow: 0px 1px 8px rgba(0, 0, 0, 0.1);
              ">

                <v-file-input
                  v-model="profileData.profile"
                  @change="preview_image()"
                  hide-input
                  accept="image/png, image/jpeg, image/bmp"
                  prepend-icon="mdi-camera"
                  show-size
                ></v-file-input>

                <p class="pre-400 kimjinhyeok" style="
                margin: 0;
                ">
                  사진 추가하기
                </p>

              </div> -->
                

            </div>

            <div class="defaultBox">

              <h2 class="pre-600">기본정보</h2>



              <div class="nameBox val3-inputBox">
                <h3>이름</h3>
                <input type="text" placeholder="이름을 입력해 주세요" v-model="data.name">
              </div>

              <div class="genderBox val3-inputBox">
                <h3>성별</h3>
                <div class="genderBox">
                  <!-- gender-active를 주면 색상 변경 -->
                  <v-btn-toggle v-model="data.gender">
                    <v-btn class="gender-male" value="남성">
                      남성
                    </v-btn>
            
                    <v-btn class="gender-woman" value="여성">
                      여성
                    </v-btn>
                  </v-btn-toggle>
                </div>
              </div>

              <div class="birthBox val3-inputBox">
                <h3>생년월일</h3>
                <input type="number" placeholder="생년월일 8자리를 입력해 주세요 (ex.20001203)" v-model="data.birthDate">
              </div>

              <div class="tellBox val3-inputBox">
                <h3>연락처</h3>
                <input type="number" placeholder="(ex.010-1234-5678)" v-model="data.phone">
              </div>

              <div class="addressBox val3-inputBox">

                <div class="addressBox-1">
                  <h3>주소</h3>
                  <input type="text" placeholder="* 우편번호(주소검색)" v-model="data.userZip" readonly>
                  <button class="pre-600" type="button" @click="showDaum">우편번호 검색</button>
                </div>

                <div class="addressBox-2">
                  <div class="address-emptyBox"></div>
                  <input type="text" placeholder="* 기본주소(주소검색)" v-model="data.userAddr1" readonly>
                </div>
              
                <div class="addressBox-3">
                  <div class="address-emptyBox"></div>
                  <input type="text" placeholder="상세주소(입력해 주세요)" v-model="data.userAddr2">
                </div>
                
              </div>

              <div class="guardian-nameBox val3-inputBox">
                <h3>보호자 이름</h3>
                <input type="text" placeholder="보호자 이름을 입력해 주세요" v-model="data.guardianName">
              </div>

              <div class="guardian-tellBox val3-inputBox">
                <h3>보호자 연락처</h3>
                <input type="number" placeholder="보호자 연락처를 입력해 주세요" v-model="data.guardianNum">
              </div>

            </div>

          </div><!--e:val3Box1-->

          <div class="val3Box1 val3Box2" style="padding: 32px 24px;">
            <div class="left-emptyBox"></div>

            <div class="careerBox defaultBox">
              <h2 class="pre-600">경력사항</h2>

              <div class="val3-inputBox">
                <h3>운동종목</h3>
                <v-select
                  v-model="data.sportType"
                  :items="sportTypeList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>경력</h3>
                <input
                  type="text"
                  placeholder="경력을 입력해 주세요"
                  v-model="data.career"
                />
              </div>

              <div class="val3-inputBox">
                <h3>훈련기관</h3>
                <v-select
                  v-model="data.teamID"
                  :items="teamList"
                  item-text="teamName"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>수상경력</h3>
                <input type="text" placeholder="수상경력을 입력해 주세요" />
              </div>
            </div>
          </div>
          <!--e:val3Box2-->

          <div class="val3Box1 val3Box3" style="padding: 32px 24px 0">
            <div class="left-emptyBox"></div>

            <div class="personalBox defaultBox">
              <h2 class="pre-600">개인사항</h2>

              <div class="val3-inputBox">
                <h3>장애유형</h3>
                <v-select
                  v-model="data.disabilityType"
                  :items="disabilityList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>장애등급</h3>
                <v-select
                  v-model="data.disabilityGrade"
                  :items="disabilityGradeList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>신장</h3>
                <input
                  type="number"
                  placeholder="ex) 173"
                  v-model="data.height"
                />
                <p class="input-right-p">cm</p>
              </div>

              <div class="val3-inputBox">
                <h3>체중</h3>
                <input
                  type="number"
                  placeholder="ex) 55"
                  v-model="data.weight"
                />
                <p class="input-right-p">kg</p>
              </div>

              <div class="val3-inputBox">
                <h3>최종학력</h3>
                <v-select
                  v-model="data.education"
                  :items="educationList"
                  item-text="value"
                  item-value="id"
                ></v-select>
              </div>

              <div class="val3-inputBox">
                <h3>학교명</h3>
                <input type="text" v-model="data.school" />
              </div>
            </div>
          </div>
        </div>
        <!--e:manage-val3-wrap-->
      </v-window-item>
      <v-window-item :value="4">
        <div class="manage-val1-wrap manage-val4-wrap" style="padding: 24px;">
          <div class="manage-val1-title">
            <p class="pre-700">기본정보</p>
          </div>

          <div class="manage-val2-btm-info">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM11.25 8C11.25 7.59 11.59 7.25 12 7.25C12.41 7.25 12.75 7.59 12.75 8V13C12.75 13.41 12.41 13.75 12 13.75C11.59 13.75 11.25 13.41 11.25 13V8ZM12.92 16.38C12.87 16.51 12.8 16.61 12.71 16.71C12.61 16.8 12.5 16.87 12.38 16.92C12.26 16.97 12.13 17 12 17C11.87 17 11.74 16.97 11.62 16.92C11.5 16.87 11.39 16.8 11.29 16.71C11.2 16.61 11.13 16.51 11.08 16.38C11.03 16.26 11 16.13 11 16C11 15.87 11.03 15.74 11.08 15.62C11.13 15.5 11.2 15.39 11.29 15.29C11.39 15.2 11.5 15.13 11.62 15.08C11.86 14.98 12.14 14.98 12.38 15.08C12.5 15.13 12.61 15.2 12.71 15.29C12.8 15.39 12.87 15.5 12.92 15.62C12.97 15.74 13 15.87 13 16C13 16.13 12.97 16.26 12.92 16.38Z"
                fill="#0081C7"
              />
            </svg>
            <p class="pre-400">선수등록이 완료되었습니다.</p>
          </div>

          <div class="manage-value1-idBox manage-val1-inputBox">
            <h2>아이디</h2>
            <p class="pre-400">{{ data.username }}</p>
          </div>

          <div class="manage-val1-nameBox manage-val1-inputBox">
            <h2>이름</h2>
            <p class="pre-400">{{ data.name }}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>장애 유형</h2>
            <p>{{disabilityName}}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>훈련 기관</h2>
            <p>{{teamName}}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>운동 종목</h2>
            <p>{{sportName}}</p>
          </div>

          <div class="manage-val1-pw2Box manage-val1-inputBox">
            <h2>훈련 시간</h2>
            <p>{{ attData.onTime }} ~ {{ attData.offTime }}</p>
          </div>
        </div>
        <!--e:manage-val4-wrap-->
      </v-window-item>
    </v-window>
    <v-row class="manage-btnBox" justify="end" style="padding: 24px; margin:0;">
      <v-col align="start" v-if="step > 1 && step < 4">
        <v-btn class="preBtn" @click="back" color="buttonerrer">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="#646464"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M9 12C9.00588 12.217 9.08227 12.403 9.24094 12.5705L13.8129 17.2892C13.9481 17.4256 14.1068 17.5 14.3007 17.5C14.6944 17.5 15 17.1776 15 16.7621C15 16.5637 14.9236 16.3777 14.7884 16.2351L10.6748 12L14.7884 7.76494C14.9236 7.62232 15 7.4425 15 7.23788C15 6.82244 14.6944 6.5 14.3007 6.5C14.1126 6.5 13.9481 6.57441 13.8129 6.71082L9.24094 11.4357C9.0764 11.597 9 11.783 9 12Z"
              stroke-width="0.5"
            />
          </svg>
          이전
        </v-btn>
      </v-col>
      <v-col
        align="end"
        v-if="step == 1 && (validFlag != true || idValidFlag != true)"
      >
        <v-btn class="nextBtn" @click="basicValid" color="gray">
          다음
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="#49ADA9"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M15 12C14.9941 11.783 14.9177 11.597 14.7591 11.4295L10.1871 6.71082C10.0519 6.57441 9.89324 6.5 9.69931 6.5C9.30558 6.5 9 6.82244 9 7.23788C9 7.4363 9.0764 7.62232 9.21156 7.76494L13.3252 12L9.21156 16.2351C9.0764 16.3777 9 16.5575 9 16.7621C9 17.1776 9.30558 17.5 9.69931 17.5C9.88737 17.5 10.0519 17.4256 10.1871 17.2892L14.7591 12.5643C14.9236 12.403 15 12.217 15 12Z"
              stroke-width="0.5"
            />
          </svg>
        </v-btn>
      </v-col>
      <v-col
        align="end"
        v-if="step == 1 && validFlag == true && idValidFlag == true"
      >
        <v-btn class="nextBtn" @click="next" color="buttonsuccess">
          다음
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="#49ADA9"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M15 12C14.9941 11.783 14.9177 11.597 14.7591 11.4295L10.1871 6.71082C10.0519 6.57441 9.89324 6.5 9.69931 6.5C9.30558 6.5 9 6.82244 9 7.23788C9 7.4363 9.0764 7.62232 9.21156 7.76494L13.3252 12L9.21156 16.2351C9.0764 16.3777 9 16.5575 9 16.7621C9 17.1776 9.30558 17.5 9.69931 17.5C9.88737 17.5 10.0519 17.4256 10.1871 17.2892L14.7591 12.5643C14.9236 12.403 15 12.217 15 12Z"
              stroke-width="0.5"
            />
          </svg>
        </v-btn>
      </v-col>
      <v-col align="end" v-if="step == 2 && attValidFlag == true">
        <v-btn class="nextBtn" @click="next" color="buttonsuccess">
          다음
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="#49ADA9"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M15 12C14.9941 11.783 14.9177 11.597 14.7591 11.4295L10.1871 6.71082C10.0519 6.57441 9.89324 6.5 9.69931 6.5C9.30558 6.5 9 6.82244 9 7.23788C9 7.4363 9.0764 7.62232 9.21156 7.76494L13.3252 12L9.21156 16.2351C9.0764 16.3777 9 16.5575 9 16.7621C9 17.1776 9.30558 17.5 9.69931 17.5C9.88737 17.5 10.0519 17.4256 10.1871 17.2892L14.7591 12.5643C14.9236 12.403 15 12.217 15 12Z"
              stroke-width="0.5"
            />
          </svg>
        </v-btn>
      </v-col>
      <!--테스트용 다음버튼-->
      <!-- <v-col align="end">
        <v-btn @click="next" color="gray">다음</v-btn>
      </v-col> -->
      <v-col align="end" v-if="step == 3">
        <v-btn @click="signup">계정 생성</v-btn>
      </v-col>
      <v-col align="end" v-if="step == 4">
        <v-btn @click="backToHome()" color="success2">돌아가기</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    this.ipData.createUser = this.$store.state.userStore.id; //생성자(허용IP)
    this.ipData.company = this.$store.state.userStore.comID; //고용기업(허용IP)
    await this.dataFormat()
    // 공통데이터 가져오기
    await this.$axios
      .get("datasets/api/commondata/")
      .then((res) => {
        for (const data of res.data) {
          // 1 (장애등급)
          if (data.maincategory == 1) {
            this.disabilityGradeList.push(data);
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
    // 선정된 선수리스트 가져오기
    this.getSelectPlayer()
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
    await this.timeSet();
    await this.loadingCover(false);
  },
  data: () => ({
    step: 1,
    times: [],
    //rest:['없음', '30분', '1시간', '1시간 30분', '2시간'],
    selectWorkTime: [],
    data: {
      username: "", // ID
      password: "",
      passwordValid: "",
      createUser: 0,
      modifyUser: null,
      is_superuser: false,
      gender: "",
      //email: "",
      is_staff: false,
      is_active: true,
      name: "",
      profile: "",
      userType: 1,
      birthDate: "",
      phone: "",
      userZip: "", //우편번호
      userAddr1: "",
      userAddr2: "",
      career: null, //운동경력
      awards: "", //수상경력
      height: "",
      weight: "",
      //wheelchair: false,
      //eyesightL: "",
      //eyesightR: "",
      school: "",
      //department: "",
      guardianName: "",
      //relation: "",
      guardianNum: "",
      //guardianEmail: "",
      comID: null,
      attType: 0,
      sportType: null,
      teamID: null,
      disabilityType: null,
      disabilityGrade: null,
      //bloodType: null,
      //maritalStatus: null,
      //militaryService: null,
      education: null,
    },
    dataSet: {},
    createId: "",
    profileData:{
      id:"",
      name:"",
      profile:null,
    },
    imageLoad: 0, // 선수 불러왔을땐 이미지로드 = 1
    profileDataFormat: {},
    imageFlag: false,
    genderList: [ // 성별 리스트
      { type: "남성", value: 1 },
      { type: "여성", value: 2 },
    ],
    attData: {
      name: "",
      onTime: "",
      offTime: "",
      monthWorkTime: "",
      workDay: [],
    },
    attDataSet:[],
    ipData: {
      createUser: 0,
      title: "",
      permissionIP: "",
      place: "",
      company: 0,
    },
    ipDataSet:[],
    onTime: 0,
    offTime: 0,
    err: {
      basicMessage: null,
      attMessage: null,
      onTimeErrMsg: null,
      offTimeErrMsg: null,
      workTimeErrMsg: null,
      ipMessage: null,
    },
    allowedIP: [],
    idValidFlag: false,
    validFlag: false,
    attValidFlag: false,
    disabilityList: [], // 장애 리스트
    disabilityGradeList: [], // 장애 등급
    educationList: [], // 최종학력 리스트
    sportTypeList: [], // 운동종목 리스트
    companyList: [], // 기업목록 리스트
    teamList: [], // 복지관(훈련기관) 리스트
    playerList: [], //기업에 선정된 선수리스트
    noPlayer:[], //선정 선수 데이터 초기화용
    selectPlayer: "",
    gpsSwitch: false,
    gpsStat: "사용안함",
    url: "", // 미리보기용
    teamName: "",
    disabilityName: "",
    sportName: "",
  }),
  methods: {
    async getSelectPlayer(){
      this.playerList = []
      this.playerList.push(this.noPlayer)
      await this.$axios
      .get("consultings/api/player/?comID="+this.$store.state.userStore.comID)
      .then((select) => {
        this.$axios
          .get("users/api/employee/?comID="+this.$store.state.userStore.comID)
          .then((res) => {
            for (const selectData of select.data) {
              if(res.data.findIndex(val=>val.name===selectData.name) == -1){
                this.playerList.push(selectData);
              }
            }
          })
      })
      .catch((err) => {
        console.log(err.response);
      });
    },
    preview_image() {
      this.url = URL.createObjectURL(this.profileData.profile)
      this.imageFlag = true
    },
    pushIP(ipID, userID) {
      this.$axios({
        method: "POST",
        url: "users/api/empRegist/get_allowIP/",
        data: { allowIP: ipID, userID: userID },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    loadingCover(val) {
      this.$emit("coverSetChild", val);
    },
    back() {
      this.step--;
    },
    next() {
      this.step++;
    },
    async timeSet() {
      for (var i = 1; i < 25; i++) {
        if (i < 10) {
          var num = "0" + i;
          this.times.push(num + ":00");
        } else {
          this.times.push(i + ":00");
        }
      }
    },
    async signup() {
      this.attData.name = this.data.name + " 훈련일정"
      this.data.userType = 1
      this.data.createUser = this.$store.state.userStore.id; //생성자 id(계정생성)
      this.data.comID = this.$store.state.userStore.comID; //기업 id(계정생성)
      //근무유형 생성
      await this.$axios({
        method: "POST",
        url: "attendances/api/attType/",
        data: this.attData,
      })
        .then((res) => {
          this.data.attType = res.data.id;
        })
        .catch(() => {
          this.$store.dispatch("callToast", {
            msg: "훈련유형 생성에 실패했습니다 관리자에게 문의바랍니다.",
            result: "error",
          });
        });
      //허용IP 생성
      await this.$axios({
        method: "POST",
        url: "attendances/api/ipRegister/",
        data: this.ipData,
      })
        .then((res) => {
          this.allowedIP.push(res.data.id);
        })
        .catch(() => {
          this.$store.dispatch("callToast", {
            msg: "허용IP 등록에 실패했습니다. 관리자에게 문의바랍니다.",
            result: "error",
          });
        });
      //계정 생성
      await this.$axios({
          method: 'POST',
          url: "users/api/empRegist/",
          data: this.data
        })
        .then(async (res) => {
          this.createId = res.data.id
          if (this.allowedIP) {
            this.pushIP(this.allowedIP, res.data.id);
          }
          this.data.allowedIP = []; //계정 생성후 다음 계정 생성을 위해 허용IP 리스트 비워주기
          this.step = 4;
          this.$store.dispatch("callToast", {
            msg: "성공적으로 선수를 등록하였습니다.",
            result: "success",
          });
        })
        .catch(() => {
          this.$store.dispatch("callToast", {
            msg: "정보입력의 유형이 올바르지 않습니다. 정확히 입력해 주세요.",
            result: "error",
          });
        });

      if(this.imageFlag == true){ // 프로필 이미지가 있을경우
        var formData = new FormData();
        console.log(this.profileData.profile)
        formData.append("profile", this.profileData.profile);
        console.log(formData)
        await this.$axios({
          method: "PATCH",
          url: "users/api/image/" + this.createId + "/",
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          data: formData,
          })
          .then(() => {});
      }
      this.imageFlag = false
      this.url = ""
      this.createId = ""
      console.log(1)
    },
    validId() {
      let check = /[a-z0-9]{5,20}/;
      let checkEng_A = /[A-Z]/;
      if (!this.data.username) {
        this.err.basicMessage = "* 아이디는 필수 정보입니다.";
      } else if (
        check.test(this.data.username) == false ||
        checkEng_A.test(this.data.username) == true
      ) {
        this.err.basicMessage =
          "* 아이디는 5~20자의 영문 소문자, 숫자만 사용 가능합니다.";
      } else {
        this.$axios
          .post("users/api/empRegist/chk_username/", {
            username: this.data.username,
          })
          .then((res) => {
            this.idValidFlag = true;
            this.basicValid();
            alert(res.data.msg);
          })
          .catch((err) => {
            console.log(err.response);
            alert(err.response.data.msg);
          });
      }
    },
    basicValid() {
      //아이디부터 비밀번호까지 순서대로 유효성 체크하는 함수
      this.validFlag = false; // 각 데이터의 내용을 바꾸면 검증 플래그 초기화
      let check = /[a-z0-9]{5,20}/;
      let checkEng_A = /[A-Z]/;
      let checkNum1 = /[0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]{8,}/;
      let checkNum2 = /[0-9]/;
      let checkSpc = /[~!@#$%^&*()_+|<>?:{}]/;
      if (!this.data.username) {
        this.err.basicMessage = "* 아이디는 필수 정보입니다.";
      } else if (
        check.test(this.data.username) == false ||
        checkEng_A.test(this.data.username) == true
      ) {
        this.err.basicMessage =
          "* 아이디는 5~20자의 영문 소문자, 숫자만 사용 가능합니다.";
      } else if (!this.data.name) {
        this.err.basicMessage = "* 이름은 필수 정보입니다.";
      } else if (!this.data.password) {
        this.err.basicMessage = "* 비밀번호는 필수 정보입니다.";
      } else if (
        checkNum1.test(this.data.password) == false ||
        checkSpc.test(this.data.password) == false ||
        checkNum2.test(this.data.password) == false
      ) {
        this.err.basicMessage =
          "* 비밀번호는 8자 이상, 특수문자, 숫자를 포함하여야 합니다.";
      } else if (!this.data.passwordValid) {
        this.err.basicMessage = "* 비밀번호 확인이 필요합니다.";
      } else if (this.data.password != this.data.passwordValid) {
        this.err.basicMessage = "* 비밀번호가 일치하지 않습니다.";
      } else if (this.idValidFlag == false)
        this.err.basicMessage = "* 아이디 중복검사가 필요합니다.";
      else if (
        this.data.username &&
        this.data.name &&
        this.data.password &&
        this.data.passwordValid &&
        this.idValidFlag
      ) {
        this.err.basicMessage = "";
        this.validFlag = true;
      }
    },
    workTimeSet() {
      if (this.onTime && this.offTime && this.attData.workDay.length > 0) {
        this.attData.monthWorkTime =
          (this.offTime - this.onTime) * this.attData.workDay.length;
      }
    },
    attValid() {
      //근무유형 이름부터
      this.attValidFlag = false;
      if (!this.attData.onTime)
        this.err.attMessage = "* 출근시간은 필수입니다.";
      else if (!this.attData.offTime)
        this.err.attMessage = "* 퇴근시간은 필수입니다.";
      else if (!this.attData.workDay)
        this.err.attMessage = "* 근무 요일을 선택해주세요";
      else if ((this.offTime - this.onTime) * this.attData.workDay.length <= 0)
        this.err.attMessage = "* 출퇴근 시간과 근무요일을 확인해주세요";
      else if (!this.ipData.title) {
        this.err.attMessage = "";
        this.err.ipMessage = "* 훈련기관을 선택해주세요";
      } else if (
        this.attData.onTime &&
        this.attData.offTime &&
        this.attData.workDay &&
        this.attData.monthWorkTime &&
        this.ipData.title
      ) {
        this.err.attMessage = "";
        this.err.ipMessage = "";
        this.attValidFlag = true;
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
    async dataFormat(){
      this.dataSet = JSON.parse(JSON.stringify(this.data))
      this.noPlayer = JSON.parse(JSON.stringify(this.data))
      this.noPlayer.id = -1
      this.noPlayer.name = "선수없음"
      this.attDataSet = JSON.parse(JSON.stringify(this.attData))
      this.ipDataSet = JSON.parse(JSON.stringify(this.ipData))
      this.profileDataFormat = JSON.parse(JSON.stringify(this.profileData))
    },
    async backToHome(){
      //돌아갈때 데이터 포맷
      this.step = 1
      this.selectPlayer = ""
      this.err.basicMessage = ""
      this.data = JSON.parse(JSON.stringify(this.dataSet))
      this.attData = JSON.parse(JSON.stringify(this.attDataSet))
      this.ipData = JSON.parse(JSON.stringify(this.ipDataSet))
      this.profileData = JSON.parse(JSON.stringify(this.profileDataFormat))
      this.url = ""
      await this.getSelectPlayer()
      console.log(this.data)
    },
    selectTeam(){
      this.ipData.title = this.teamList[this.data.teamID - 1].teamName;
      this.ipData.permissionIP = this.teamList[this.data.teamID - 1].allowedIP;
      this.teamName = this.teamList[this.data.teamID - 1].teamName;
      this.attValid();
    },
    // URL을 File object로 변환
    async convertURLtoFile(url, name){
      const response = await fetch(url);
      const data = await response.blob();
      const ext = url.split(".").pop(); // url 구조에 맞게 수정할 것
      const filename = name; // url 구조에 맞게 수정할 것
      const metadata = { type: `image/${ext}` };
      return new File([data], filename, metadata)
    },
  },
  watch: {
    "selectPlayer": async function() {
      if(this.selectPlayer == -1){
        this.data = JSON.parse(JSON.stringify(this.dataSet))
        this.data.id = ""
        this.data.name = ""
        this.attData = JSON.parse(JSON.stringify(this.attDataSet))
        this.ipData = JSON.parse(JSON.stringify(this.ipDataSet))
        this.profileData = JSON.parse(JSON.stringify(this.profileDataFormat))
        this.url = ""
        return false
      }
      this.$axios
      .get("consultings/api/player/"+ this.selectPlayer)
      .then((playerData) => {
        // 불러온 선수데이터에서 이미지 처리
        this.$axios
        .get("consultings/api/image/"+ this.selectPlayer)
        .then(async (res) => {
          var startProfile = res.data.profile.substr(0,res.data.profile.lastIndexOf("/")+1) // 프로필 사진 저장위치
          var extension = res.data.profile.substr(res.data.profile.lastIndexOf(".")) // 프로필 사진 확장자

          this.profileData = res.data
          await this.convertURLtoFile(startProfile + playerData.data.name + "_" + playerData.data.id + extension, playerData.data.name + "_" + playerData.data.id)
          .then((fileResult) => {
            this.profileData.profile = fileResult
          })
          this.url = startProfile + playerData.data.name + "_" + playerData.data.id + extension
          this.imageFlag = true
        })

        // 불러온 선수데이터에서 id값을 가지는 데이터들 처리
        this.data=playerData.data
        this.data.bloodType = playerData.data.bloodType.id
        this.data.teamID = playerData.data.team.id
        this.data.team = playerData.data.team.id
        this.data.disabilityGrade = playerData.data.disabilityGrade.id
        this.data.disabilityType = playerData.data.disabilityType.id
        this.data.education = playerData.data.education.id
        this.data.maritalStatus = playerData.data.maritalStatus.id
        this.data.militaryService = playerData.data.militaryService.id
        this.data.sportType = playerData.data.sportType.id
        this.selectTeam()
      })
    },
    "data.username": function() {
      // 아이디 체크
      this.idValidFlag = false; // 아이디 바꾸면 아이디 중복검증 플래그 초기화
      this.basicValid();
    },
    "data.name": function() {
      this.basicValid();
    },
    "data.password": function() {
      // 비밀번호 체크 및 비밀번호 확인 체크
      this.basicValid();
    },
    "data.passwordValid": function() {
      this.basicValid();
    },
    "attData.onTime": function() {
      this.onTime = Number(this.attData.onTime.substr(0, 2));
      this.workTimeSet();
      this.attValid();
    },
    "attData.offTime": function() {
      this.offTime = Number(this.attData.offTime.substr(0, 2));
      this.workTimeSet();
      this.attValid();
    },
    "attData.workDay": function() {
      this.workTimeSet();
      this.attValid();
    },
    gpsSwitch: function() {
      if (this.gpsSwitch == false) this.gpsStat = "사용안함";
      else this.gpsStat = "사용함";
    },
    "profileData.profile": function(){
      this.imageFlag = true
    },
    "data.disabilityType": function() {
      this.disabilityName = this.disabilityList[this.data.disabilityType - 1].value;
    },
    "data.sportType": function() {
      this.sportName = this.sportTypeList[this.data.sportType - 1].value;
    },
  },
};
</script>

<style>
  .background{
    background-color:rgba(240, 240, 240);
    border-radius: 10px;
  }
  .manage-val1-wrap {}
  .manage-val1-wrap .manage-val1-title {
    margin-bottom: 32px;
  }
  .manage-val1-wrap .manage-val1-title p {
    font-size: 18px;
    color: #2e2e2e;
    margin: 0;
  }
  .manage-val1-wrap .manage-val1-inputBox {
    display: flex;
    align-items: center;
    height: 39px;
    margin-bottom: 8px;
  }
  .manage-val1-wrap .manage-val1-inputBox h2 {
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-SemiBold';
    width: 90px;
    margin-right: 28px;
  }
  .manage-val1-wrap .manage-val1-inputBox input {
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    height: 100%;
    width: 370px;
    padding: 0 12px;
    font-size: 16px;
    color: #000;
    font-family: 'Pretendard-Regular';
  }
  .manage-val1-wrap .manage-val1-inputBox input::placeholder {
    color: #b4b4b4;
  }
  .manage-val1-wrap .manage-val1-inputBox input:focus,
  .manage-val1-wrap .manage-val1-inputBox button:focus {
    outline-color: #49ada9;
  }
  .manage-val1-wrap .manage-val1-inputBox .inputBox-id {
    width: 257px;
  }
  .manage-val1-wrap .manage-val1-inputBox .id-chk-btn {
    font-size: 13px;
    color: #49ada9;
    background: #EFF9F8;
    border-radius: 3px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 107px;
    margin-left: 6px;
    transition: all .3s;
  }
  .manage-val1-wrap .manage-val1-inputBox .id-chk-btn:hover {
    background: #49ada9;
    color: #fff;
  }
  .manage-value1-errBox {
    font-size: 13px;
    color: red;
  }
  .manage-btnBox {
    width: 100%;
    margin-top: 44px;
  }
  .manage-btnBox .col {}
  .manage-btnBox button {
    width: 126px !important;
    height: 48px !important;
    background-color: #EFF9F8 !important;
    border-radius: 10px;
    box-shadow: none;
    padding: 0 !important;
    transition: all .5s;
  }
  .manage-btnBox button:hover {
    background: #49ada9 !important;
  }
  .manage-btnBox button:hover span {
    color: #fff !important;
  }
  .manage-btnBox button span {
    font-family: 'Pretendard-Regular';
    font-size: 18px;
    color: #49ada9;
    transition: all .5s;
  }
  .manage-btnBox button span svg {
    transition: all .5s;
  }
  .manage-btnBox .nextBtn span svg {
    margin-left: 14px;
  }
  .manage-btnBox button:hover span svg,
  .manage-btnBox button:focus span svg {
    fill: #fff !important;
  }
  .manage-btnBox .preBtn span svg {
    margin-right: 14px;
  }
  .manage-btnBox .buttonsuccess {
    background-color: #49ada9 !important;
  }
  .manage-btnBox .buttonsuccess span {
    color: #fff !important;
  }
  .manage-btnBox .buttonsuccess span svg {
    fill: #fff !important;
  }
  .manage-btnBox .buttonerrer {
    background: #F5F5F5;
  }
  .manage-btnBox .buttonerrer span {
    color: #646464;
  }
  .manage-btnBox .buttonerrer:hover {
    background-color: rgb(242, 95, 95) !important;
  }

  .manage-val2-top {
    display: flex;
    flex-direction: column;
  }
  .manage-val2-title {
    margin-bottom: 32px;
  }
  .manage-val2-title2 {
    margin-bottom: 12px;
  }
  .manage-val2-title p {
    font-size: 18px;
    color: #2e2e2e;
    margin: 0;
  }
  .manage-value2-top-inputBox {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  .manage-value2-top-inputBox h2 {
    font-size: 16px;
    color: #2e2e2e;
    font-family: 'Pretendard-Regular';
    width: 97px;
    margin-right: 28px;
    font-weight: 500;
  }
  .inputBox-work-name {
    width: 370px;
    height: 39px;
    padding: 0 12px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    color: #000;
    
  }
  .value2-selectBox {
    width: 172px;
    height: 39px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
  }
  .value2-selectBox .v-input__slot {
    height: 39px !important;
    min-height: auto !important;
  }
  .inputBox-work-name::placeholder {
    color: #989898;
  }
  .inputBox-work-name:focus,
  .value2-selectBox:focus {
    outline-color: #49ada9;
  }
  .times-selectBox {
    display: flex;
    align-items: center;
  }
  .times-selectBox span {
    display: block;
    margin: 0 8px;
  }
  .times-input {
    width: 130px;
    height: 39px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
  }
  .times-selectBox fieldset {
    display: none;
  }
  .input_label_position_transform  .times-selectBox label {
    position: unset !important;
  }
  .v-select__slot {
    display: flex;
    align-items: center;
  }
  .v-application--is-ltr .v-text-field .v-input__append-inner {
    margin: 0;
    align-self: unset;
  }
  .manage-value2-top-inputBox .value-btnBox {}
  .manage-value2-top-inputBox .value-btnBox button {
    margin-right: 6px;
    width: 34px !important;
    min-width: auto !important;
    height: 32px !important;
    border-radius: 6px !important;
    background-color: #B4B4B4 !important;
    border: 0 !important;
  }
  .manage-value2-top-inputBox .value-btnBox span {
    color: #fff;
    font-family: 'Pretendard-Regular';
    font-size: 20px;
    font-weight: 400 !important; 
  }
  .v-btn-toggle > .v-btn.v-btn--active {
    background-color: #0081C7 !important;
    color: #fff !important;
  }
  .value2-errBox {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Pretendard-Regular';
    margin-bottom: 30px;
    width: 540px;
  }
  .value2-errBox .val2-err1 {
    color: red;
  }
  .value2-errBox .val2-err2 {
    color: #2e2e2e;
    background-color: #49ada9;
    border-radius: 5px;
    padding: 5px 10px;
    color: #fff;
    margin: 0;
  }
  .manage-val2-btm-info {
    background-color: #E4F2F9;
    display: flex;
    align-items: center;
    padding: 8px;
    border-radius: 3px;
    margin-bottom: 32px;
    width: 495px;
  }
  .manage-val2-btm-info svg {
    margin-right: 8px;
  }
  .manage-val2-btm-info p {
    color: #0081c7;
    font-size: 14px;
    margin: 0;
  }
  .manage-value2-top-inputBox .v-text-field--rounded {
    border-radius: 3px;
    width: 370px;
    height: 39px;
  }
  .val2-btm-selectBox {
    width: 370px;
    height: 39px;
  }
  .val2-btm-selectBox .v-input__slot {
    height: 39px !important;
    min-height: auto !important;
  }
  .manage-value2-top-inputBox {
    width: 495px !important;
  }
  .v-text-field--rounded > .v-input__control > .v-input__slot {
    padding: 0 12px;
  }
  .input_label_position_transform .v-text-field--outlined .v-label--active,
  .input_label_position_transform .v-text-field .v-label--active {
    transform:unset;
    font-size: 12px;
    margin-right: 10px;
  }
  .v-input--selection-controls {
    margin-top: 16px;
    padding-top: 0;
  }
  .v-input__slot {
    margin-bottom: 0;
  }
  .v-input--switch__track {
    border-radius: 16px;
    width: 46px;
    height: 26px;
    left: -3px;
    position: absolute;
    opacity: 0.6;
    right: 2px;
    top: calc(50% - 13px);
  }
  .v-application--is-ltr .v-input--selection-controls__input {
    margin-right: 15px;
  }
  .v-input--selection-controls .v-input__slot > .v-label {
    font-family: 'Pretendard-Regular';
    font-size: 15px;
  }
  .theme--light.v-input--switch .v-input--switch__track {
    /* background-color: #008bd6; */
  }
  .v-input--switch:not(.v-input--switch--flat):not(.v-input--switch--inset) .v-input--switch__thumb {
    color: #fff !important;
  }
  .v-application--is-ltr .v-text-field .v-label {
    font-family: 'Pretendard-Regular';
  }
  .manage-val3-wrap {}
  .manage-val3-wrap .manage-val3-header {
    width: 100%;
    height: 72px;
    border-bottom: .5px solid #b4b4b4;
    display: flex;
    align-items: center;
    padding: 0 24px;
  }
  .manage-val3-wrap h1 {
    font-size: 20px;
    color: #2e2e2e;
    font-weight: 600;
  }
  .manage-val3-wrap .imgBox {
    width: 200px;
    height: 200px;
    margin-right: 32px;
  }
  .manage-val3-wrap .imgBox-hidden {
    width: 200px;
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 6px;
    overflow: hidden;
  }
  .manage-val3-wrap .left-emptyBox {
    width: 200px;
    height: 200px;
    margin-right: 32px;
  }
  .manage-val3-wrap .imgBox img {
    width: 100%;
  }
  .manage-val3-wrap .imgBox .v-input {
    flex: none !important;
  }
  .manage-val3-wrap .imgBox .v-input button {
    margin-right: 20px;
  }
  .manage-val3-wrap .val3Box1 {
    display: flex;
  }
  .defaultBox h2 {
    font-size: 18px;
    color: #2e2e2e;
    margin-bottom: 32px;
  }
  .defaultBox .val3-inputBox {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  .defaultBox .val3-inputBox h3 {
    font-size: 16px;
    color: #000;
    font-family: 'Pretendard-Regular';
    font-weight: 500;
    width: 90px;
    margin-right: 10px;
  }
  .defaultBox .val3-inputBox input {
    width: 370px;
    height: 39px;
    border-radius: 3px;
    border: 1px solid #e1e1e1;
    font-size: 16px;
    color: #000;
    padding: 0 12px;
    font-family: 'Pretendard-Regular';
    font-weight: 500;
  }
  .defaultBox .val3-inputBox input::placeholder {
    color: #989898;
  }
   .defaultBox .val3-inputBox input:focus,
   .addressBox-1 button:focus,
   input:focus,
   textarea:focus {
    outline-color: #49ada9 !important;
  }
  .genderBox {
    display: flex;
    align-items: center;
  }
  .genderBox {
    font-size: 16px;
    color: #fff;
    font-family: 'Pretendard-Regular';
    cursor: pointer;
  }
  .genderBox button {
    transition: all .5s;
  }
  .gender-male {
    border-radius: 3px 0px 0px 3px;
    width: 185px;
    height: 39px;
    border: 1px solid #e1e1e1;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #989898;
  }
  .gender-woman {
    border-radius: 0px 3px 3px 0px;
    width: 185px;
    height: 39px;
    border: 1px solid #e1e1e1;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #989898;
  }
  /* .gender-male:hover,
  .gender-woman:hover {
    background: #47a7da !important;
    border: 1px solid #47a7da !important;
    color: #fff !important;
  } */
  .gender-active {
    background: #0081c7 !important;
    border: 1px solid #0081c7 !important;
    color: #fff !important;
  }
  .addressBox {
    display: flex;
    flex-direction: column;
    margin-bottom: 0 !important;
  }
  .addressBox > div {
    display: flex;
    width: 100%;
    margin-bottom: 10px;
  }
  .addressBox-1 {
    align-items: center;
  }
  .addressBox-1 input {
    width: 257px !important;
  }
  .addressBox-1 button {
    width: 107px;
    height: 39px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #eff9f8;
    border-radius: 3px;
    font-size: 13px;
    color: #49ada9;
    margin-left: 6px;
    transition: all .5s;
  }
  .addressBox-1 button:hover {
    background-color: #49ada9;
    color: #fff;
  }
  .address-emptyBox {
    width: 90px;
    margin-right: 10px;
  }
  .val3Box1 {
    border-bottom: .5px solid #b4b4b4;
  }
  .val3Box3 {
    border-bottom: 0;
  }
  .v-input {
    margin: 0 !important;
    padding: 0 !important;
  }
  .v-input input {
    max-height: unset !important;
  }
  .val3Box1 .v-text-field__details {
    display: none;
  }
  .v-select__selection--comma {
    position: absolute;
    left: 12px;
    font-family: 'Pretendard-Regular';
    font-size: 16px;
  }
  .val3Box1 .v-text-field.v-input--is-focused > .v-input__control > .v-input__slot:after {
    display: none;
  }
  .val3-inputBox .input-right-p {
    position: relative;
    left: 10px;
    top: 7px;
    font-family: 'Pretendard-Regular';
    font-size: 16px;
  }
  .input73 .times-selectBox .v-select__selection--comma {
    left: 73px;
  }
  .manage-val4-wrap p {
    margin: 0;
  }
  .areaColor {
    background: #F5F5F5;
    padding: 10px;
    border-radius: 6px;
  }
  .new-player-val2-input-agency {
    border: 1px solid #e1e1e1;
  }
  .new-player-val2-input-agency div {
    background: none !important;
  }
  .new-player-val2-input-ip {
    background: rgba(0, 0, 0, 0.06);
    border: 0 !important;
  }
  .print-h2 {
    font-size: 18px !important;
  }
</style>
