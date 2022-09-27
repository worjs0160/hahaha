<template>
  <v-app>
    <v-responsive>
    <!-- 팝업 영역 시작 -->
        <!-- 기업 근태 출력 시작 -->
        <CompanyAttendancePrint 
          v-show="companyAttendancePrintDialogState" 
          style="position: fixed; z-index: 11;  width:100%; height:100%;"
          :comUserList="comUserList"
          @dialogCoverSet="dialogCoverSet"
          @companyAttendancePrintDialogStateChange="companyAttendancePrintDialogStateChange"
        ></CompanyAttendancePrint>
        <!-- 기업 근태 출력 종료 -->
        <!-- 기업 훈련 출력 시작 -->
        <CompanyWorkPrint 
          v-show="companyWorkPrintDialogState" 
          style="position: fixed; z-index: 11;  width:100%; height:100%;"
          :comUserList="comUserList"
          @dialogCoverSet="dialogCoverSet"
          @companyWorkPrintDialogStateChange="companyWorkPrintDialogStateChange"
        ></CompanyWorkPrint>
        <!-- 기업 훈련 출력 종료 -->
        <!-- 유저 업무 등록하기 시작 -->
        <UserWorkAdd
          v-show="workAddDialogState"
          style="position: fixed; z-index: 11; width:100%; height:100%; background: rgba(0,0,0,.4);"
          :workAddDialogData="workAddDialogData"
          :errMsg="errMsg"
          :trainingImgSlotData="trainingImgSlotData"
          :dataFlag="dataFlag"
          @workAddDialogStateChange="workAddDialogStateChange"
          @soketDelete="soketDelete"
          @dialogCoverSet="dialogCoverSet"
          @userWorkAddData="userWorkAddData"
          @trainingImgDelete="trainingImgDelete"
          @trainingImgAdd="trainingImgAdd"
          @trainingImgFileChange="trainingImgFileChange"
          @workDataValid="workDataValid"
        ></UserWorkAdd>
        <!-- 유저 업무 등록하기 종료 -->
        <!-- 유저 프로필 수정요청 화면 시작 -->
        <div class="scroll-hidden" id="playerProfile" v-show="profileDialogState" v-if="$store.state.userStore.userType == 1" style="position: fixed;z-index: 11; width:100%; height:100%; overflow-y: scroll;">
          <div style="width: 100%;height:100%; padding-top:50px;">
            <AccountUpdate ref="accountUpdate" @closeProfilePopup="closeProfilePopup" @selectProfileUpdateUser="selectProfileUpdateUser" ></AccountUpdate>
          </div>
        </div>
        <!-- 유저 프로필 수정요청 화면 종료 -->
        <!-- 기업 관리 프로필 수정 시작 -->
        <div class="scroll-hidden" id="companyProfile" v-show="companySettingState" style="position: fixed;z-index: 11;  width:100%; height:100%; overflow-y: scroll;">
          <div style="width: 100%; height:100%; padding:50px 0;">
            <CompanyProfileUpdate @closeProfilePopup="closeProfilePopup" @updateCompanyProfile="updateCompanyProfile" ref="callCompanyAccount"></CompanyProfileUpdate>
          </div>
        </div>
        <!-- 기업 관리 프로필 수정 종료 -->
        <!-- 컨설팅 선수관리 프로필 업데이트 시작 -->
        <div class="scroll-hidden" id="consultingProfileUpdate" v-show="consultingSettingState" style="position: fixed;z-index: 11;  width:100%; height:100%; overflow-y: scroll;">
          <div style="width: 100%; height:100%; padding:50px 0;">
            <ConsultingProfileUpdate @closeProfilePopup="closeProfilePopup" @updateProfile="updateProfile" ref="callAccount"></ConsultingProfileUpdate>
          </div>
        </div>
        <!-- 컨설팅 선수관리 프로필 업데이트 종료 -->
        <!-- 근무시간 관리 시작 -->
        <CompanyAttendanceSetting
          ref="companyAttUpdate"
          class="scroll-hidden"
          id="companyAttendanceSetting"
          v-show="companyUserTaskSettingDialogState" 
          style="position: fixed; z-index: 11;  width:100%; height:100%; overflow-y:scroll;"
          @dialogCoverSet="dialogCoverSet"
          @setDialogDate="setDialogDate"
          @companyUserListUpdate="companyUserListUpdate"
          @companyUserTaskSettingDialogStateChange="companyUserTaskSettingDialogStateChange"
        ></CompanyAttendanceSetting>
        <!-- 근무시간 관리 종료 -->
        <!-- 기업 근무일지 수정 시작 -->
        <CompanyWorkModify
          ref="CompanyWorkModifyMethod"
          v-show="companyUserWorkSettingDialogState"
          style="position: fixed;z-index: 11; width:100%; height:100%;"
          :companyUserWorkSettingDialogData="companyUserWorkSettingDialogData"
          @dialogCoverSet="dialogCoverSet"
          @workStateChange="workStateChange"
          @companyUserWorkSettingDialogStateChange="companyUserWorkSettingDialogStateChange"
        ></CompanyWorkModify>
        <!-- 근무일지 수정 종료 -->
        <!-- 기업정보 수정 시작 -->
        <CompanyInfoModify
          v-show="companyInfoDialogState" 
          style="position: fixed; z-index: 11; display: block; width:100%; height:100%;"
          :companyInfoDialogData="companyInfoDialogData"
          @companyInfoUpdate="companyInfoUpdate"
          @dialogCoverSet="dialogCoverSet"
          @showDaum="showDaum"
          @companyInfoDialogStateChange="companyInfoDialogStateChange"
        ></CompanyInfoModify>
      <!-- 기업정보 수정 종료-->
      <!-- 컨설팅 운동선수 프로필 시작 -->
      <div class="scroll-hidden" id="consultingProfile" v-show="consultingPlayerDialogState" style="position: fixed;z-index: 11;  width:100%; height:100%; overflow-y: scroll;">
        <div style="width: 100%; height:100%; padding:50px 0;">
          <ConsultingProfile
            ref="profileMethod"
            :consultingPlayerDialogData="consultingPlayerDialogData"
            :consultingPlayerDialogProfileData="consultingPlayerDialogProfileData"
            @dialogCoverSet="dialogCoverSet"
            @consultingPlayerDialogStateChange="consultingPlayerDialogStateChange"
            @updateProfile="updateProfile"
          >
          </ConsultingProfile>
        </div>
      </div>
      <!-- 컨설팅 운동선수 프로필 종료 -->
      <!-- 운동선수 일정 생성 시작 -->
      <UserScheduleAdd 
        v-show="scheduleAddDialogState" 
        style="position: fixed;z-index: 11;display: block; width:100%; height:100%;"
        :scheduleAddDialogData="scheduleAddDialogData"
        @dialogCoverSet="dialogCoverSet"
        @scheduleAddDialogStateChange="scheduleAddDialogStateChange"
        @scheduleAddData="scheduleAddData"
      >
      </UserScheduleAdd>
      <!-- 운동선수 일정 생성 종료 -->
      <!-- 운동선수 일정 수정 시작 -->
      <UserScheduleUpdate 
        v-show="scheduleUpdateDialogState" 
        style="position: fixed;z-index: 11;display: block; width:100%; height:100%;"
        :scheduleUpdateDialogData="scheduleUpdateDialogData"
        @dialogCoverSet="dialogCoverSet"
        @scheduleUpdateDialogStateChange="scheduleUpdateDialogStateChange"
        @scheduleUpdateData="scheduleUpdateData"
        @scheduleDeleteData="scheduleDeleteData"
      >
      </UserScheduleUpdate>
      <!-- 운동선수 일정 수정 종료 -->
      <!-- 운동선수 알람 시작 -->
      <UserAlarm 
        v-show="userAlarmDialogState" 
        style="position: fixed;z-index: 11; width:100%; height:100%;"
        :issueTrainingList="issueTrainingList"
        @dialogCoverSet="dialogCoverSet"
        @userAlarmDialogStateChange="userAlarmDialogStateChange"
        @userChangeView="userChangeView"
      >
      </UserAlarm>
      <!-- 운동선수 알람 종료 -->
      <!-- 기업 알람 시작 -->
      <CompanyAlarm 
        v-show="companyAlarmDialogState" 
        style="position: fixed;z-index: 11; width:100%; height:100%;"
        :userList="userList"
        :issueTrainingList="issueTrainingList"
        :badgeNum="badgeNum"
        @dialogCoverSet="dialogCoverSet"
        @companyAlarmDialogStateChange="companyAlarmDialogStateChange"
        @companyChangeView="companyChangeView"
      >
      </CompanyAlarm>
      <!-- 기업 알람 종료 -->
  <!-- 팝업 영역 종료 -->


      <v-row class="mt-0 header-height">
        <div class="header-inner inner">
          <v-col cols="1" align="start">
            <!-- 로고 영역 -->
            <div class="header-logo-cover">
              <!-- <v-img
                class="pointer"
                src="@/assets/logo_small_white.png"
                max-height="50"
                max-width="120"
                alt="logo"
                contain
                @click="moveToHome"
              ></v-img> -->
              <svg width="71" height="28" viewBox="0 0 71 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_172_3333)">
                <path d="M48.9601 15.9883H40.344C40.1424 15.9883 39.949 15.9088 39.8065 15.7674C39.6639 15.626 39.5839 15.4342 39.5839 15.2343V6.6876C39.5839 6.48762 39.6639 6.29584 39.8065 6.15444C39.949 6.01303 40.1424 5.93359 40.344 5.93359C40.5456 5.93359 40.7389 6.01303 40.8815 6.15444C41.024 6.29584 41.1041 6.48762 41.1041 6.6876V14.4878H48.9677C49.1693 14.4878 49.3626 14.5672 49.5052 14.7086C49.6477 14.85 49.7278 15.0418 49.7278 15.2418C49.7278 15.4418 49.6477 15.6336 49.5052 15.775C49.3626 15.9164 49.1693 15.9958 48.9677 15.9958L48.9601 15.9883Z" fill="white"/>
                <path d="M24.6168 15.9886H16.0007C15.7991 15.9886 15.6058 15.9091 15.4632 15.7677C15.3207 15.6263 15.2406 15.4345 15.2406 15.2346V10.9669C15.2406 10.7669 15.3207 10.5751 15.4632 10.4337C15.6058 10.2923 15.7991 10.2129 16.0007 10.2129H24.6168C24.8184 10.2129 25.0117 10.2923 25.1543 10.4337C25.2969 10.5751 25.3769 10.7669 25.3769 10.9669C25.3769 11.1669 25.2969 11.3587 25.1543 11.5001C25.0117 11.6415 24.8184 11.7209 24.6168 11.7209H16.7533V14.5032H24.6168C24.8184 14.5032 25.0117 14.5826 25.1543 14.724C25.2969 14.8654 25.3769 15.0572 25.3769 15.2572C25.3769 15.4572 25.2969 15.6489 25.1543 15.7903C25.0117 15.9318 24.8184 16.0112 24.6168 16.0112V15.9886Z" fill="white"/>
                <path d="M24.6168 7.44161H16.0007C15.7991 7.44161 15.6058 7.36217 15.4632 7.22076C15.3207 7.07936 15.2406 6.88757 15.2406 6.6876C15.2406 6.48762 15.3207 6.29584 15.4632 6.15444C15.6058 6.01303 15.7991 5.93359 16.0007 5.93359H24.6168C24.8184 5.93359 25.0117 6.01303 25.1543 6.15444C25.2969 6.29584 25.3769 6.48762 25.3769 6.6876C25.3769 6.88757 25.2969 7.07936 25.1543 7.22076C25.0117 7.36217 24.8184 7.44161 24.6168 7.44161Z" fill="white"/>
                <path d="M34.5669 5.93359H28.1742C27.9726 5.93359 27.7793 6.01303 27.6367 6.15444C27.4942 6.29584 27.4141 6.48762 27.4141 6.6876V15.2343C27.4141 15.4342 27.4942 15.626 27.6367 15.7674C27.7793 15.9088 27.9726 15.9883 28.1742 15.9883C28.3758 15.9883 28.5691 15.9088 28.7117 15.7674C28.8542 15.626 28.9343 15.4342 28.9343 15.2343V7.44161H34.5745C34.7737 7.43155 34.9728 7.46179 35.1599 7.53048C35.3469 7.59917 35.5179 7.70487 35.6625 7.84116C35.8071 7.97746 35.9222 8.14149 36.0009 8.3233C36.0795 8.5051 36.1201 8.70088 36.1201 8.89872C36.1201 9.09656 36.0795 9.29234 36.0009 9.47414C35.9222 9.65595 35.8071 9.81999 35.6625 9.95628C35.5179 10.0926 35.3469 10.1983 35.1599 10.267C34.9728 10.3357 34.7737 10.3659 34.5745 10.3558H31.3819C31.1803 10.3558 30.987 10.4353 30.8444 10.5767C30.7019 10.7181 30.6218 10.9099 30.6218 11.1098C30.6218 11.3098 30.7019 11.5016 30.8444 11.643C30.987 11.7844 31.1803 11.8639 31.3819 11.8639H34.5745C34.974 11.878 35.3723 11.8122 35.7456 11.6703C36.1188 11.5285 36.4595 11.3134 36.7472 11.0381C37.0348 10.7628 37.2637 10.4328 37.4199 10.0678C37.5762 9.7028 37.6567 9.31033 37.6567 8.9138C37.6567 8.51727 37.5762 8.1248 37.4199 7.75983C37.2637 7.39485 37.0348 7.06484 36.7472 6.78951C36.4595 6.51417 36.1188 6.29915 35.7456 6.15728C35.3723 6.0154 34.974 5.94959 34.5745 5.96375L34.5669 5.93359Z" fill="white"/>
                <path d="M52.3046 15.9888C52.1872 15.9887 52.0715 15.9616 51.9664 15.9096C51.7893 15.8193 51.6551 15.6636 51.5925 15.476C51.53 15.2885 51.5441 15.0841 51.6319 14.9068L55.9381 6.36015C56.0015 6.23708 56.0978 6.13365 56.2164 6.06118C56.335 5.98871 56.4715 5.94998 56.6108 5.94922V5.94922C56.7501 5.94998 56.8866 5.98871 57.0052 6.06118C57.1238 6.13365 57.2201 6.23708 57.2835 6.36015L61.5934 14.9068C61.6539 15.0799 61.6488 15.2689 61.579 15.4385C61.5093 15.6081 61.3796 15.7467 61.2144 15.8285C61.0491 15.9102 60.8595 15.9295 60.681 15.8827C60.5024 15.8358 60.3472 15.7262 60.2442 15.5741L56.6108 8.36581L52.9736 15.5741C52.911 15.6973 52.8155 15.8011 52.6976 15.8743C52.5796 15.9474 52.4437 15.987 52.3046 15.9888V15.9888Z" fill="white"/>
                <path d="M13.5 6.01246C13.3173 5.93321 13.1106 5.92832 12.9243 5.99884C12.7381 6.06936 12.5872 6.20964 12.5042 6.38946L9.37247 13.2547L7.64697 9.48465L8.74917 7.01529C8.798 6.84083 8.78191 6.65477 8.70385 6.49111C8.62579 6.32745 8.49097 6.19711 8.32403 6.12392C8.15708 6.05072 7.96916 6.03956 7.79461 6.09247C7.62005 6.14538 7.47051 6.25883 7.37332 6.41208L6.81462 7.65996L6.24453 6.40454C6.21313 6.30174 6.15996 6.20678 6.08856 6.12601C6.01716 6.04525 5.9292 5.98055 5.83055 5.93625C5.7319 5.89195 5.62484 5.86907 5.51655 5.86914C5.40826 5.86921 5.30124 5.89223 5.20265 5.93666C5.10406 5.98109 5.01617 6.0459 4.94488 6.12675C4.87359 6.20761 4.82054 6.30264 4.78928 6.40548C4.75802 6.50833 4.74927 6.61661 4.76362 6.72308C4.77797 6.82954 4.81509 6.93174 4.8725 7.02283L6.01269 9.48843L4.70527 12.3423C4.62655 12.5231 4.62224 12.7272 4.69326 12.9111C4.76428 13.095 4.905 13.244 5.08533 13.3263C5.18131 13.3677 5.28472 13.3895 5.38938 13.3904C5.53495 13.3894 5.67717 13.3469 5.79911 13.2681C5.92106 13.1892 6.01761 13.0773 6.0773 12.9455L6.81083 11.3056L8.68835 15.3584C8.75018 15.4869 8.84741 15.5954 8.96881 15.6713C9.09021 15.7473 9.23083 15.7876 9.37437 15.7876C9.51791 15.7876 9.65851 15.7473 9.77992 15.6713C9.90132 15.5954 9.99856 15.4869 10.0604 15.3584L13.861 6.9889C13.9388 6.81128 13.9446 6.61082 13.8774 6.42904C13.8102 6.24726 13.675 6.0981 13.5 6.01246V6.01246Z" fill="white"/>
                <path d="M70.7795 6.16866C70.6374 6.03051 70.4464 5.95312 70.2475 5.95312C70.0485 5.95312 69.8574 6.03051 69.7154 6.16866L65.9375 9.9123L62.1635 6.16866C62.0171 6.05976 61.836 6.00689 61.6535 6.01976C61.471 6.03262 61.2993 6.11036 61.1699 6.2387C61.0405 6.36704 60.9621 6.53737 60.9492 6.71842C60.9362 6.89946 60.9895 7.07907 61.0993 7.22427L65.185 11.2808V15.2431C65.185 15.4431 65.2651 15.6349 65.4076 15.7763C65.5502 15.9177 65.7435 15.9971 65.9451 15.9971C66.1467 15.9971 66.34 15.9177 66.4826 15.7763C66.6251 15.6349 66.7052 15.4431 66.7052 15.2431V11.2771L70.7947 7.22427C70.932 7.08136 71.0073 6.89076 71.0045 6.69339C71.0016 6.49602 70.9209 6.30763 70.7795 6.16866V6.16866Z" fill="white"/>
                <path d="M6.81079 4.54299C7.26209 4.54299 7.62793 4.18009 7.62793 3.73243C7.62793 3.28477 7.26209 2.92188 6.81079 2.92188C6.3595 2.92188 5.99365 3.28477 5.99365 3.73243C5.99365 4.18009 6.3595 4.54299 6.81079 4.54299Z" fill="white"/>
                <path d="M63.5127 19.8339C63.5119 19.994 63.4634 20.1503 63.3731 20.2831C63.2829 20.4159 63.155 20.5192 63.0056 20.58C62.8563 20.6408 62.6921 20.6563 62.5338 20.6246C62.3756 20.5929 62.2303 20.5154 62.1164 20.4019C62.0025 20.2884 61.9251 20.144 61.8938 19.9868C61.8626 19.8297 61.879 19.6669 61.941 19.519C62.0029 19.3711 62.1077 19.2448 62.242 19.1559C62.3763 19.067 62.5341 19.0195 62.6956 19.0195C62.8032 19.0195 62.9098 19.0406 63.0092 19.0816C63.1085 19.1226 63.1988 19.1826 63.2747 19.2583C63.3506 19.3339 63.4108 19.4237 63.4516 19.5225C63.4924 19.6213 63.5132 19.7271 63.5127 19.8339V19.8339Z" fill="white"/>
                <path d="M35.8706 27.9997C26.5704 27.9997 17.7567 25.832 11.0561 21.8998C4.26053 17.9111 0.334457 12.5275 -9.67318e-07 6.73676C-0.022135 6.63057 -0.0209212 6.5209 0.00355983 6.41522C0.0280409 6.30954 0.0752187 6.21035 0.141862 6.1244C0.208506 6.03845 0.293052 5.96776 0.389738 5.91717C0.486424 5.86658 0.59297 5.83727 0.702113 5.83124C0.811257 5.82521 0.920427 5.84261 1.02218 5.88224C1.12393 5.92186 1.21587 5.98279 1.29172 6.06087C1.36757 6.13895 1.42556 6.23233 1.46172 6.33466C1.49788 6.43699 1.51137 6.54585 1.50126 6.65382C1.80912 11.9319 5.47294 16.8894 11.82 20.6029C18.2811 24.4031 26.8364 26.4955 35.8706 26.4955C43.7645 26.4955 51.4798 24.8442 57.5951 21.8508C57.685 21.7894 57.7871 21.7479 57.8946 21.7291C58.002 21.7104 58.1123 21.7148 58.2179 21.7421C58.3235 21.7694 58.4219 21.8189 58.5065 21.8873C58.5911 21.9556 58.6599 22.0413 58.7081 22.1384C58.7564 22.2354 58.783 22.3417 58.7861 22.4499C58.7893 22.5581 58.769 22.6657 58.7265 22.7654C58.684 22.8651 58.6203 22.9545 58.5399 23.0276C58.4594 23.1008 58.364 23.1559 58.2602 23.1892C51.8333 26.3409 44.1066 27.9997 35.8706 27.9997Z" fill="white"/>
                </g>
                <defs>
                <clipPath id="clip0_172_3333">
                <rect width="71" height="28" fill="white"/>
                </clipPath>
                </defs>
              </svg>
            </div>
          </v-col>

          <!-- 메뉴 탭 영역 -->
          <v-col cols="6" align="start" class="px-4 pre-400" style="
          color: #fff;
          font-size:18px;
          letter-spacing: .3px;
          position: relative;
          ">
            {{myProfile.name}}님 안녕하세요.
          </v-col>

          <v-col cols="5" align="end" style="flex-grow:0; padding:0;">
            <!-- 알람 버튼 영역 -->
            <v-menu bottom offset-y :close-on-content-click="true">
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon big v-bind="attrs" v-on="on" large class="mx-2 py-2">
                  <v-badge
                    v-if="badgeNum!=0"
                    color="red"
                    :content="badgeNum"
                    offset-x="5"
                    offset-y="10"
                  >
                    <v-icon>mdi-bell</v-icon>
                  </v-badge>
                  <v-icon v-if="badgeNum==0">mdi-bell</v-icon>
                </v-btn>
              </template>

              <!-- 운동선수전용 알람 내용 영역 -->
              <div class="main-box-wrap profileBox px-3" style="box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.2);" v-if="$store.state.userStore.userType==1">
                <div class="exitBox">
                  <v-col align="start" class="py-0">
                    <p style="font-weight: bold;">알림</p>
                  </v-col>
                  <v-col align="end" class="py-0">
                    <button type="button">
                      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
                      </svg>
                    </button>
                  </v-col>
                </div>
                <v-row class="px-2" v-if="badgeNum>0">
                  <v-btn class="editBtn" style="width:100% !important; font-weight: 500;" v-for = "(item, idx) in issueCount.length" :key="idx" @click="(userAlarmDialogStateChange(true)), (dialogCoverSet(true))">
                    <v-icon class="mr-1">mdi-alert-circle-outline</v-icon>
                    반려된 훈련일지 {{badgeNum}}건
                  </v-btn>
                </v-row>
                <v-row justify="center" class="px-2" v-if="badgeNum==0">
                  <p style="font-weight: 500;">
                    알림 내용이 없습니다.
                  </p>
                </v-row>
              </div>
              <!-- 기업전용 알람 내용 영역 -->
              <div class="main-box-wrap profileBox px-3" style="box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.2);" v-if="$store.state.userStore.userType==2">
                <div class="exitBox">
                  <v-col align="start" class="py-0">
                    <p style="font-weight: bold;">알림</p>
                  </v-col>
                  <v-col align="end" class="py-0">
                    <button type="button">
                      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
                      </svg>
                    </button>
                  </v-col>
                </div>

                <v-row class="px-2" v-if="badgeNum>0">
                  <v-col class="pa-0">
                    <v-btn class="editBtn" style="width:100% !important; font-weight: 500; font-size: 13px;" @click="(companyAlarmDialogStateChange(true)), (dialogCoverSet(true))">
                      <v-icon class="mr-1">mdi-alert-circle-outline</v-icon>
                      훈련일지 미승인 {{badgeNum}}건
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row justify="center" class="px-2" v-if="badgeNum==0">
                  <p style="font-weight: 500;">
                    알림 내용이 없습니다.
                  </p>
                </v-row>
              </div>

            </v-menu>

            <!-- 프로필 버튼 영역 -->
            <v-menu bottom offset-y :close-on-content-click="true">
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon big v-bind="attrs" v-on="on" large class="mx-2">
                  <!-- <v-icon>mdi-account</v-icon> -->
                  <div class="header-profile-cover">
                    <img :src="myProfile.profile">
                  </div>
                </v-btn>
              </template>

              <!-- 프로필 내용 영역 -->
              <div class="main-box-wrap profileBox" style="
              box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.2);
              ">
                <div justify="center" class="exitBox">
                  <v-col align="start" class="py-0">
                    <p style="font-weight: bold;">프로필</p>
                  </v-col>
                  <v-col align="end" class="py-0">
                    <button type="button">
                      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M7.18836 19.0509C6.81922 19.4201 6.80165 20.0792 7.19715 20.466C7.58387 20.8527 8.24305 20.8439 8.61219 20.4747L13.9911 15.087L19.3788 20.4747C19.7567 20.8527 20.4071 20.8527 20.7938 20.466C21.1718 20.0704 21.1806 19.4288 20.7938 19.0509L15.4149 13.6632L20.7938 8.28431C21.1806 7.90638 21.1806 7.25599 20.7938 6.86927C20.3983 6.49134 19.7567 6.48255 19.3788 6.86048L13.9911 12.2482L8.61219 6.86048C8.24305 6.49134 7.57508 6.47376 7.19715 6.86927C6.81043 7.25599 6.81922 7.91517 7.18836 8.28431L12.5761 13.6632L7.18836 19.0509Z" fill="#646464"/>
                      </svg>
                    </button>
                  </v-col>
                </div>

                <v-btn class="editBtn" v-if="this.$store.state.userStore.userType == 1" @click="(dialogCoverSet(true)), (profileDialogState = true), (accountDataSet())">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9.5 10C10.3284 10 11 9.32843 11 8.5C11 7.67157 10.3284 7 9.5 7C8.67157 7 8 7.67157 8 8.5C8 9.32843 8.67157 10 9.5 10Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M12.8 4H9.6C5.6 4 4 5.6 4 9.6V14.4C4 18.4 5.6 20 9.6 20H14.4C18.4 20 20 18.4 20 14.4V10.4" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 6H19" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                  <path d="M17 8V4" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                  <path d="M5 18L8.82566 15.1435C9.4387 14.6861 10.3233 14.7379 10.8743 15.2643L11.1304 15.5146C11.7356 16.0928 12.7134 16.0928 13.3187 15.5146L16.5468 12.4337C17.1521 11.8554 18.1299 11.8554 18.7351 12.4337L20 13.6419" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  회원정보 수정
                </v-btn>

                <v-btn class="logoutBtn" @click="logout()">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9.5 10C10.3284 10 11 9.32843 11 8.5C11 7.67157 10.3284 7 9.5 7C8.67157 7 8 7.67157 8 8.5C8 9.32843 8.67157 10 9.5 10Z" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M12.8 4H9.6C5.6 4 4 5.6 4 9.6V14.4C4 18.4 5.6 20 9.6 20H14.4C18.4 20 20 18.4 20 14.4V10.4" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 6H19" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                  <path d="M17 8V4" stroke="#646464" stroke-width="1.2" stroke-linecap="round"/>
                  <path d="M5 18L8.82566 15.1435C9.4387 14.6861 10.3233 14.7379 10.8743 15.2643L11.1304 15.5146C11.7356 16.0928 12.7134 16.0928 13.3187 15.5146L16.5468 12.4337C17.1521 11.8554 18.1299 11.8554 18.7351 12.4337L20 13.6419" stroke="#646464" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  로그아웃
                </v-btn>

                <div class="lastBox">
                  <p>마지막 로그인</p>
                  <p>2021.11.15(월) 23:26</p>
                </div>
              </div>

            </v-menu>
          </v-col>
        </div>
      </v-row>

      
      <div style="border-bottom:.5px solid #e1e1e1;">
        <v-row class="sub_header" style="width:1200px; margin:0 auto;">
          <!-- 로고 영역 -->
          <v-col class="d-flex pa-0 justify-left">
          
            <!-- <h4>주식회사 000님 안녕하세요!</h4> -->
            <v-tabs v-model="idx">
              <v-tab class="pre-600" style="color:#2E2E2E; font-size:20px; min-width:0;"
                v-for="item of tabItems"
                :key="item.idx"
                :title="item.name"
                @click="changeView(item.idx)"
                >{{ item.name }}</v-tab>
            </v-tabs>
            
          </v-col>
        </v-row>
      </div>

      <v-main style="height:90%;">
        <!-- 최상단 로딩화면 -->
        <div v-show="loading" class="page-cover">
          <div class="d-flex justify-center align-center" style="height:100%;">
              <pulse-loader :loading="loading" :color="color1" :size="size"></pulse-loader>
          </div>
        </div>
        
      
      
      <v-snackbar
        :color="color"
        absolute
        v-model="snackbar"
        :timeout="timeout"
        right
        top
      >
      <!-- 토스트 메시지 -->
        <v-icon class="mr-2">mdi-check</v-icon>
        <span>{{ this.$store.state.toast.message }}</span>
        <template v-slot:action="{ attrs }">
          <v-btn color="white" text v-bind="attrs" @click="snackbar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>
      <!-- 토스트 메시지 끝 -->
      <div class="scroll-hidden" style="
      width:100%;
      height:100%;
      ">
        <v-container
          class="pa-0 scroll-hidden"
          fluid
          style="height:100%; width:1170px !important;"
        >
          <!-- 동적 컴포넌트 영역(각자의 화면 컴포넌트를 넣는 부분) -->
          <!-- <component style="padding: 2% 10% 0px 10%; height:100%; overflow-x: scroll;"
            :is="this.$store.state.tabStore.selectedTab"
            @coverSetChild="coverSet"
            @dialogCoverSetChild="dialogCoverSet"
            v-if="this.$store.state.tabStore.selectedTab == 'Test_UserApproval'"
          ></component> -->
          <component
            :is="this.$store.state.tabStore.selectedTab"
            ref="childComponent"
            @coverSetChild="coverSet"
            @workAddDialog="workAddDialog"
            @companySettingDialog="companySettingDialog"
            @consultingSettingDialog="consultingSettingDialog"
            @selectAccountProfile="selectAccountProfile"
            @companyUserWorkSettingDialog="companyUserWorkSettingDialog"
            @companyUserTaskSettingDialog="companyUserTaskSettingDialog"
            @companyInfoDialog="companyInfoDialog"
            @companyAttendancePrintDialogStateChange="companyAttendancePrintDialogStateChange"
            @companyWorkPrintDialogStateChange="companyWorkPrintDialogStateChange"
            @consultingPlayerDialog="consultingPlayerDialog"
            @dialogCoverSet="dialogCoverSet"
            @getComUserList="getComUserList"
            @scheduleSelectDate="scheduleSelectDate"
            @scheduleClickData="scheduleClickData"
            @updateAlarm="updateAlarm"
          ></component>
        </v-container>
      </div>
      </v-main>
    </v-responsive>
  </v-app>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import AccountUpdate from "/src/views/test_user/popup/AccountUpdate";
import UserWorkAdd from "/src/views/popup/UserWorkAdd";
// import ProfileWriteWant from "/src/views/popup/ProfileWriteWant";
import ConsultingProfile from "/src/views/popup/ConsultingProfile";
import ConsultingProfileUpdate from "/src/views/popup/ConsultingProfileUpdate";
import CompanyWorkModify from "/src/views/popup/CompanyWorkModify";
// import CompanySettingsCard from "/src/views/popup/CompanySettingsCard";
import CompanyInfoModify from "/src/views/popup/CompanyInfoModify";
import CompanyAttendanceSetting from "/src/views/popup/CompanyAttendanceSetting";
import CompanyAttendancePrint from "/src/views/popup/CompanyAttendancePrint";
import CompanyWorkPrint from "/src/views/popup/CompanyWorkPrint";
import CompanyProfileUpdate from "/src/views/popup/CompanyProfileUpdate";
import UserScheduleAdd from "/src/views/popup/UserScheduleAdd";
import UserScheduleUpdate from "/src/views/popup/UserScheduleUpdate";
import UserAlarm from "/src/views/popup/UserAlarm";
import CompanyAlarm from "/src/views/popup/CompanyAlarm";

export default {
  components: {
    PulseLoader,
    AccountUpdate,
    UserWorkAdd,
    ConsultingProfile,
    ConsultingProfileUpdate,
    CompanyWorkModify,
    CompanyInfoModify,
    CompanyAttendanceSetting,
    CompanyAttendancePrint,
    CompanyWorkPrint,
    CompanyProfileUpdate,
    UserScheduleAdd,
    UserScheduleUpdate,
    UserAlarm,
    CompanyAlarm,
  },
  data: () => ({
    tabItems: {},
    timeout: 2000,
    loading: true,
    dialogCoverState: false,
    profileDialogState: false,
    workAddDialogState: false,
    companySettingState: false,
    consultingSettingState: false,
    companyUserWorkSettingDialogState: false,
    companyUserTaskSettingDialogState: false,
    companyInfoDialogState: false,
    consultingPlayerDialogState: false,
    companyAttendancePrintDialogState: false,
    companyWorkPrintDialogState: false,
    scheduleAddDialogState: false,
    scheduleUpdateDialogState: false,
    userAlarmDialogState: false,
    companyAlarmDialogState: false,
    
    color1: '#5bc0de',
    size: '15px',
    margin: '2px',
    radius: '2px',
    companyUserWorkSettingDialogData: {
      idx:0,
      day:'',
      mark:'',
      date:'',
      endTime:'',
      startTime:'',
      datetime:'',
      createdTime:'',
      modifiedTime:'',
      reason:'',
      rejectedReason:'',
      rejectedTime:'',
    },
    companyUserTaskSettingDialogData: {idx:0,day:'', title:'',contents:'',date:''},
    companyInfoDialogData: {
      id:0,
      comName: "",
      ceoName: "",
      comAddr1: "",
      comAddr2: "",
      comZip: "",
      comNum: "",
      businessNum: "",
      managerName: "",
      managerNum: "",
    },
    consultingPlayerDialogData:{},
    consultingPlayerDialogProfileData:{},
    scheduleAddDialogData:{id:"", title:"",start:"",end:"",contents:"",name:""},
    scheduleUpdateDialogData:{id:"", title:"",start:"",end:"",contents:"",name:""},
    comName: "",
    workAddDialogData: {title:'',contents:'',workDate:'',user:'',name:''},
    trainingData:[],
    // 유저 훈련 이미지 슬롯 관련
    trainingImgSlotLimit:5,
    trainingImgSlotYN:true,
    trainingImgSlotData:[],
    trainingImgSlotChange:0,
    // 유저 훈련 데이터valid 체크 관련
    errMsg:"",
    dataFlag:false,
    //유저 근무 업데이트 값 관련
    creditTime:0,
    attErrMsg:"",
    // 계정 수정 키값
    selectProfileUpdateUser:'',
    // 출력 선수 목록
    comUserList:[],
    //내 프로필
    myProfile:{},
    //알람 데이터 정리용
    userList:[],
    userIdList:[],
    issueCount:[],
    issueTrainingList:[],
    badgeNum:0,
  }),
  async created() {
    await this.$axios
      .get("users/api/image/" + this.$store.state.userStore.id)
      .then((res) => {
          this.myProfile = res.data
      })
    this.selectProfileUpdateUser = this.$store.state.userStore.id;
    // 유저 pk이용하여 로그인 유저정보 가져오기
    await this.$axios
      .get("users/api/user/" + this.$store.state.userStore.id)
      .then((res) => {
        this.$store.commit("setUser", res.data);
        if (res.data.userType == 1) { //근로자 계정 정보
          this.$axios
          .get("users/api/employee/" + this.$store.state.userStore.id)
          .then((employeeRes) => {
              this.$store.commit("setEmployee", employeeRes.data);
          })
        }
        if (res.data.userType == 1) { //근로자 계정 탭 & 알람용 데이터 조회
          this.tabItems = [
            { idx: 0, componentName: "Test_UserHome", name:"메인" },
            { idx: 1, componentName: "Test_UserAttendance", name:"훈련시간" },
            { idx: 2, componentName: "Test_UserWork", name:"훈련일지" },
            // { idx: 3, componentName: "Test_UserApproval", name:"결재관리" },
            { idx: 3, componentName: "Test_UserInfo", name:"회사정보" },
            // { idx: 2, componentName: "Test_UserPay", name:"급여계산" },
          ];

          if(this.$store.state.tabStore.selectedTab.substring(0, 3) != "Test"){
            this.$store.commit("setComponent", {
              idx: 0,
              componentName: "Test_UserHome",
            });
          }else{
            this.$store.commit("setComponent", {idx:this.$store.state.tabStore.idx,componentName:this.$store.state.tabStore.selectedTab});
            this.$store.commit("setSubTab", {idx:this.$store.state.tabStore.subIdx,componentName:this.$store.state.tabStore.selectedSubTab});
          }
        }
        else if (res.data.userType == 2) { // 기업 계정 탭 & 알람용 데이터 조회
          this.tabItems = [
            { idx: 0, componentName: "Test_CompanyHome", name:"메인" },
            { idx: 1, componentName: "Test_CompanyInfo", name:"회사정보" },
            { idx: 2, componentName: "Test_CompanyManage", name:"설정" },
          ];

          if(this.$store.state.tabStore.selectedTab.substring(0, 3) != "Test_C"){
            this.$store.commit("setComponent", {
              idx: 0,
              componentName: "Test_CompanyHome",
            });
          }else{
            this.$store.commit("setComponent", {idx:this.$store.state.tabStore.idx,componentName:this.$store.state.tabStore.selectedTab});
            this.$store.commit("setSubTab", {idx:this.$store.state.tabStore.subIdx,componentName:this.$store.state.tabStore.selectedSubTab});
          }
        }
        else if (res.data.userType == 3) { // 컨설팅 계정
          this.tabItems = [
            { idx: 0, componentName: "ConsultingHome", name:"메인" },
            { idx: 1, componentName: "ConsultingAddition", name:"선수등록" },
          ];
          if(this.$store.state.tabStore.selectedTab.substring(0, 3) != "consulting"){
            this.$store.commit("setComponent", {
              idx: 0,
              componentName: "consultingHome",
            });
          }else{
            this.$store.commit("setComponent", {idx:this.$store.state.tabStore.idx,componentName:this.$store.state.tabStore.selectedTab});
            this.$store.commit("setSubTab", {idx:this.$store.state.tabStore.subIdx,componentName:this.$store.state.tabStore.selectedSubTab});
          }
        }
      })
      .catch(() => {
        console.log("유저정보 가져오기 실패.");
      });

    await this.getTrainingAlarm(this.$store.state.userStore.userType)

    // 서버시간 가져오기
    await this.$axios
      .get("users/get_date/")
      .then((res) => {
        this.$store.commit("setDate", res.data);
      })
      .catch((err) => {
        console.log(err);
        alert("서버시간 가져오기 실패");
      });
      
  },
  computed: {
    idx: {
      get() {
        return this.$store.state.tabStore.idx;
      },
      set() {
        return;
      },
    },
    color: {
      get() {
        return this.$store.getters.getColor;
      },
      set() {},
    },
    snackbar: {
      get() {
        return this.$store.getters.getSnackbar;
      },
      set(val) {
        this.$store.commit("setSnackbar", val);
      },
    },
  },
  beforeUpdate: function() {
    this.$axios
      .get("users/get_date/")
      .then((res) => {
        this.$store.commit("setDate", res.data);
      })
      .catch((err) => {
        console.log(err);
        alert("서버시간 가져오기 실패");
      });
  },
  watch:{
    "workAddDialogData.title": function(){
      this.workDataValid();
    },
    "workAddDialogData.contents": function(){
      this.workDataValid();
    },
  },
  mounted() {
    window.addEventListener('beforeunload', this.unLoadEvent);
  },
  beforeUnmount() {
    window.removeEventListener('beforeunload', this.unLoadEvent); //새로고침이나 페이지 종료시 확인창 띄우기
  },
  methods: {
    unLoadEvent(event) {
      event.preventDefault();
      event.returnValue = '';
    },
    async getTrainingAlarm(userType){
      var subTrainingList=[]
      this.userIdList=[]
      this.userList=[] // 기업에서는 유저별로 알림 구분을 해야함
      this.issueCount=[] // 알림 항목갯수
      this.badgeNum=0 // 총 알림 갯수
      this.issueTrainingList = [] // 훈련일지 알림 리스트

      if(userType == 1){
        //운동선수의 반려된 훈련일지 찾기
        await this.$axios
          .get("trainings/api/trainings/?user_id="+ this.$store.state.userStore.id)
          .then((res) => {
            for(var i=0;i<res.data.length;i++){
              if(res.data[i].state==2){
                this.issueTrainingList.push(res.data[i])
              }
            }
            this.issueCount.push(this.issueTrainingList.length)
            for(var j=0;j<this.issueCount.length;j++){
                this.badgeNum += this.issueCount[j]
            }
            console.log(this.issueTrainingList)
            console.log(this.issueCount)
          })
      }

      if(userType == 2){
        //기업 소속 유저 이름 가져오기
        await this.$axios
          .get("users/api/employee/?comID="+ this.$store.state.userStore.comID)
          .then((res) => {
            for(var i=0;i<res.data.length;i++){
              this.userList.push(res.data[i].name)
              this.userIdList.push(res.data[i].id)
            }
          })

        //유저별 미승인 훈련일지 찾기
        await this.$axios
          .get("trainings/api/trainings/?comID="+ this.$store.state.userStore.comID)
          .then((res) => {
            for(var i=0;i<this.userIdList.length;i++){
              for(var j=0;j<res.data.length;j++){
                if(this.userIdList[i] == res.data[j].user && res.data[j].state == 0){
                  subTrainingList.push(res.data[j])
                }
              }
              this.issueTrainingList.push(subTrainingList)
              this.issueCount.push(subTrainingList.length)
              subTrainingList=[]
            }
            for(var k=0;k<this.issueCount.length;k++){
              this.badgeNum += this.issueCount[k]
            }
          })
      }
    },
    async getComUserList(){
      await this.$axios
      .get("users/api/employee/?comID="+ this.$store.state.userStore.comID)
      .then((res) => {
        this.comUserList = res.data
      })
      .catch((err) => {
        console.log(err);
        console.log("유저 근무정보 가져오기 실패.");
      });
    },
    companyAttendancePrintDialogStateChange(state){
      this.companyAttendancePrintDialogState = state;
    },
    companyWorkPrintDialogStateChange(state){
      this.companyWorkPrintDialogState = state;
    },
    companyUserTaskSettingDialogStateChange(state){
      this.companyUserTaskSettingDialogState = state;
    },
    consultingPlayerDialogStateChange(state){
      this.consultingPlayerDialogState = state;
    },
    companyInfoDialogStateChange(state){
      this.companyInfoDialogState = state;
    },
    companyUserWorkSettingDialogStateChange(state){
      this.companyUserWorkSettingDialogState = state;
    },
    workAddDialogStateChange(state){
      this.workAddDialogState = state;
    },
    scheduleAddDialogStateChange(state){
      this.scheduleAddDialogState = state;
    },
    scheduleUpdateDialogStateChange(state){
      this.scheduleUpdateDialogState = state;
    },
    userAlarmDialogStateChange(state){
      this.userAlarmDialogState = state;
    },
    companyAlarmDialogStateChange(state){
      this.companyAlarmDialogState = state;
    },
    getImageSize : async function(image){
      let _URL = window.URL || window.webkitURL;
      let objectUrl = _URL.createObjectURL(image);
      return new Promise((resolve, reject) => {
          let img = new Image()
          img.onload = () => resolve({
          width : img.width,
          height : img.height
          })
          img.onerror = reject
          img.src = objectUrl
    })
    },

    //업무일지 생성시 valid체크
    workDataValid(){
      this.dataFlag = false
      var checkImage = false
      if(!this.workAddDialogData.title) this.errMsg = "제목을 입력해주세요"
      else if(!this.workAddDialogData.contents) this.errMsg = "내용을 입력해주세요"
      else if(this.trainingImgSlotData.length == 0) this.errMsg = "첨부된 이미지가 없습니다"
      else if(this.trainingImgSlotData.length > 0){
        for(var i=0; i < this.trainingImgSlotData.length; i++){
          if(this.trainingImgSlotData[i].image == null)this.errMsg = "첨부된 이미지가 없습니다"
          else if(this.trainingImgSlotData[i].image != null){
            checkImage = true
          }
        }
      }
      if(this.workAddDialogData.title && this.workAddDialogData.contents && checkImage){
        this.errMsg = ""
        this.dataFlag = true;
      }
    },

    async trainingImgFileChange(file){
      
      console.log(file)
      
      const reader = new FileReader();
      
      reader.onload = (e) => {
        console.log(e.target);
      };
      reader.readAsDataURL(file);

      

      // 업로드 파일에 대해 조건을 걸수 있습니다.

      // if(file.size > 10485760){
      //   this.image2 = undefined;
      //   this.image2Url = "";
      //   this.$emit("snack",{checkedData:true,checkedDataText:"10mb 이하 사진만 업로드 가능합니다."});
      //   return
      // }
      // this.createImage2(file);
    },
    trainingImgAdd(){
      if(this.trainingImgSlotYN){
        this.trainingImgSlotData.push({image:null});
        if(this.trainingImgSlotData.length >= this.trainingImgSlotLimit){
          this.trainingImgSlotYN = false;
        }
      }
    },
    trainingImgDelete(idx){
      this.trainingImgSlotData.splice(idx,1);
      if(this.trainingImgSlotData.length < this.trainingImgSlotLimit){
        this.trainingImgSlotYN = true;
      }
    },
    companyUserWorkUpdate(item){
      
      var update_data = {
        title:item.title,
        contents:item.contents,
        workDate:item.datetime,
      }
        this.$axios({
          method: "PATCH",
          url:
          "trainings/api/trainings/" +
            item.id +
            "/",
          data: update_data,
        }).then(() => {
          this.$emit("saveAction");
        });
    },
    companyUserListUpdate(){
      this.$refs.childComponent.attDataReset();
    },
    companyUserTaskDelete(item){

        this.$axios({
          method: "DELETE",
          url:
          "attendances/api/empAtt/" +
            item.id +
            "/",
        }).then(() => {
          this.$emit("saveAction");
        });
    },
    companyInfoUpdate(item){
      this.$axios({
        method: "PATCH",
        url:
        "datasets/api/company_list/" +
          item.id +
          "/",
        data: item,
      }).then(() => {
        this.$emit("saveAction");
        this.$refs.childComponent.infoDataReset();
        this.$store.dispatch("callToast", {
          msg: "회사정보를 수정하였습니다.",
          result: "success",
        });
      });
    },
    coverSet(state){
      this.loading = state;
    },
    async scheduleAddData(data){
      this.$axios({
        method: "POST",
        url: "calendars/api/calendar/",
        data: data,
      }).then(() => {
        this.$refs.childComponent.getMySchedule();
        this.$store.dispatch("callToast", {
          msg: "일정이 등록되었습니다.",
          result: "success",
        });
      });
    },
    async userChangeView(idx, date, item){
      await this.changeView(idx) // 알람에서 선택된 내용으로 바로가기위해 탭을 훈련일지로 변경
      await this.$refs.childComponent.alarmChangeView(date, item);
    },
    async companyChangeView(idx, date, userIdx){
      await this.changeView(idx)
      await this.$refs.childComponent.alarmChangeView(date, userIdx);
    },
    updateAlarm(){
      this.getTrainingAlarm(this.$store.state.userStore.userType)
    },
    async scheduleUpdateData(data){
      this.$axios({
        method: "PATCH",
        url: "calendars/api/calendar/"+ data.id +"/",
        data: data,
      }).then(() => {
        this.$refs.childComponent.getMySchedule();
        this.$store.dispatch("callToast", {
          msg: "일정을 수정하였습니다.",
          result: "success",
        });
      });
    },
    async scheduleDeleteData(data){
      this.$axios({
        method: "DELETE",
        url: "calendars/api/calendar/"+ data.id +"/",
        data: data,
      }).then(() => {
        this.$refs.childComponent.getMySchedule();
        this.$store.dispatch("callToast", {
          msg: "일정을 삭제하였습니다.",
          result: "success",
        });
      });
    },
    async userWorkAddData(data){
      let sendImgData = []
      let sendImg = []

      let imgChk = false;
      let oneChk = false;
      // 첨부된 이미지가 있는지 확인
      if(this.trainingImgSlotData.length > 0){
        for(var i=0; i < this.trainingImgSlotData.length; i++){
          if(this.trainingImgSlotData[i].image != null){
            var getImageSize = await this.getImageSize(this.trainingImgSlotData[i].image)


            var formData = new FormData();
            formData.append("images", this.trainingImgSlotData[i].image);
            formData.append("width", getImageSize.width);
            formData.append("height", getImageSize.width);
            
            var result = await this.$axios({
              method: 'POST',
              url: "trainings/api/userTrainingsImg/",
              headers: {
                "Content-Type": "multipart/form-data"
              },
              data: formData
            })
            var id = result.data.id
            var images = result.data.images
            var width = result.data.width
            var height = result.data.height
            sendImgData.push(id)
            sendImg.push({'images':images,'id':id,'width':width,'height':height})
            oneChk = true;
            imgChk = false;
          }else{
            if(!oneChk){
              imgChk = true;
            }
          }
        }


      }else{
        imgChk = true;
      }

      if(imgChk){
        console.log('첨부된 이미지가 없습니다.');
        return
      }
      this.$axios({
        method: "POST",
        url: "trainings/api/trainings/",
        data: {'user':data.user,'title':data.title,'contents':data.contents,'workDate':data.workDate, 'images':sendImgData},
      }).then(() => {
        var week = ['일', '월', '화', '수', '목', '금', '토'];
        var dayOfWeek = week[new Date(data.workDate).getDay() -1];
        this.trainingData.push({'day':dayOfWeek,'user':data.user,'title':data.title,'contents':data.contents,'workDate':data.workDate,'images':sendImg,'state':data.state})
        this.trainingImgSlotData = []
        this.$refs.childComponent.getAttTypeData();
        this.$refs.childComponent.inItWeekDates();
        this.$store.dispatch("callToast", {
          msg: "훈련내용 기록이 완료되었습니다.",
          result: "success",
        });
      });
    },
    closeProfilePopup(){
      this.profileDialogState = false;
      this.companySettingState = false;
      this.consultingSettingState = false;
      this.dialogCoverSet(false);  
    },
    updateProfile(){
      this.$refs.childComponent.settingPlayer(); // 컨설팅 선수관리에서 사용
    },
    updateCompanyProfile(){
      this.$refs.childComponent.reloadingHuman(); // 컨설팅 선수관리에서 사용
    },
    workAddDialog(state, data, today){
      this.workAddDialogState = state;
      this.workAddDialogData = {day:'', title:today+" "+data[0].name+" 훈련일지",contents:'',workDate:new Date((Date.now()) - new Date().getTimezoneOffset() * 60000).toISOString(),user:data[0]['user'],name:data[0]['name']};
      this.dialogCoverSet(state);
    },
    companySettingDialog(state, id){
      console.log(id)
      this.companySettingState = state;
      this.dialogCoverSet(state);
      this.$refs.callCompanyAccount.settingAccount(id);
    },
    consultingSettingDialog(state){
      this.consultingSettingState = state;
      this.dialogCoverSet(state);
    },
    companyUserWorkSettingDialog(state, item){
      this.companyUserWorkSettingDialogState = state;
      this.companyUserWorkSettingDialogData = item;
      if(item.stateCode==0 || item.stateCode==2){
        this.companyUserWorkSettingDialogData.state = false
      }
      else if(item.stateCode==1 || item.stateCode==3){
        this.companyUserWorkSettingDialogData.state = true
      }
      this.companyUserWorkSettingDialogData.createdTime = this.dateCALC(item.createdTime)
      this.companyUserWorkSettingDialogData.modifiedTime = this.dateCALC(item.modifiedTime)
      if(item.rejectedTime){
        this.companyUserWorkSettingDialogData.rejectedTime = this.dateCALC(item.rejectedTime)
      }
      this.dialogCoverSet(state);
      console.log(1)
    },
    dateCALC(data){
      var date = new Date(data);
      var month = ('0' + (date.getMonth() + 1)).slice(-2);
      var day = ('0' + date.getDate()).slice(-2);
      var hours = ('0' + date.getHours()).slice(-2); 
      var minutes = ('0' + date.getMinutes()).slice(-2);

      return month+"-"+day+" "+hours+":"+minutes
    },
    companyUserTaskSettingDialog(state, item, name, onTime, offTime){
      this.companyUserTaskSettingDialogState = state;
      this.dialogCoverSet(state);
      this.$refs.companyAttUpdate.settingData(item, name, onTime, offTime)
    },
    companyInfoDialog(state, item){
      //하나씩 넣어줘야 수정하는대로 변경이 적용되지 않음
      this.companyInfoDialogState = state;
      this.dialogCoverSet(state);
      this.companyInfoDialogData.id = item.id;
      this.companyInfoDialogData.comName = item.comName;
      this.companyInfoDialogData.ceoName = item.ceoName;
      this.companyInfoDialogData.comZip = item.comZip;
      this.companyInfoDialogData.comAddr1 = item.comAddr1;
      this.companyInfoDialogData.comAddr2 = item.comAddr2;
      this.companyInfoDialogData.comNum = item.comNum;
      this.companyInfoDialogData.businessNum = item.businessNum;
      this.companyInfoDialogData.managerName = item.managerName;
      this.companyInfoDialogData.managerNum = item.managerNum;
    },
    consultingPlayerDialog(state, val){
      this.dialogCoverSet(state);
      this.consultingPlayerDialogState = state
      this.consultingPlayerDialogData = val
      this.$axios
      .get("consultings/api/image/"+val.id)
      .then((res) => {
        this.consultingPlayerDialogProfileData = res.data
      })
      .catch((err) => {
        console.log(err.response);
      });
      this.$refs.profileMethod.selectStateUpdate(this.consultingPlayerDialogData)
    },
    scheduleSelectDate(state, id, start, end, name){
      this.dialogCoverSet(state);
      this.scheduleAddDialogState = state
      this.scheduleAddDialogData = {user:id, title:"", start: start, end:end, contents:"", name:name}
    },
    scheduleClickData(state, data){
      this.dialogCoverSet(state);
      this.scheduleUpdateDialogState = state
      this.scheduleUpdateDialogData = data
    },
    selectAccountProfile(id){
      this.$refs.callAccount.settingAccount(id);
    },
    dialogCoverSet(state){
      // console.log(document.getElementsByClassName('dialog-cover')[0].replace('on', 'off'))
      if(state){
        document.getElementById('top_cover').classList.replace('off', 'on');
      }else{
        document.getElementById('top_cover').classList.replace('on', 'off');
      }
      this.dialogCoverState = state;
    },
    accountDataSet(){
      this.$refs.accountUpdate.settingAccount();
    },
    soketDelete(){
      this.trainingImgSlotData= [] //이미지 슬롯 초기화(업무일지에서 사용)
    },
    async changeView(event) {
      // 메소드 안에서 사용하는 `this` 는 Vue 인스턴스를 가리킵니다
      const tab = this.tabItems[event];
      await this.$store.commit("setComponent", tab);
      this.getTrainingAlarm(this.$store.state.userStore.userType) // 탭 바뀔때마다 알람 갱신
    },
    moveToLogin: function() {
      var router = this.$router;
      return router.push({ name: "Login" });
    },
    moveToHome: function() {
      const tab = this.tabItems["메인"];
      this.$store.commit("setComponent", tab);
    },
    changeInfo: function() {
      this.$store.commit("setComponent", {
        idx: "",
        componentName: "UserInfo",
      });
    },
    workStateChange(item){
      let year = new Date().getFullYear(); // 현재 년도
      let month = new Date().getMonth() + 1;  // 현재 월
      let date = new Date().getDate();  // 현재 날짜
      let hours = new Date().getHours(); // 현재 시간
      let minutes = new Date().getMinutes(); // 현재 분
      let seconds = new Date().getSeconds(); // 현재 초
      console.log(year+"-"+month+"-"+date+"T"+hours+":"+minutes+":"+seconds)
      
      if(!item.state){
        item.stateCode = 2;
        this.$axios({
          method: "PATCH",
          url:
          "trainings/api/trainings/" +
            item.id +
            "/",
          data: {state:item.stateCode, rejectedReason:item.rejectedReason, rejectedTime:year+"-"+month+"-"+date+"T"+hours+":"+minutes+":"+seconds},
        }).then(() => {
          this.$emit("saveAction");
          this.getTrainingAlarm(this.$store.state.userStore.userType);
          this.$store.dispatch("callToast", {
            msg: "훈련일지를 반려하였습니다.",
            result: "error",
          });
        });
      }else{
        item.stateCode = 1;
        
        this.$axios({
          method: "PATCH",
          url:
          "trainings/api/trainings/" +
            item.id +
            "/",
          data: {state:item.stateCode, rejectedReason:item.rejectedReason, rejectedTime:year+"-"+month+"-"+date+"T"+hours+":"+minutes+":"+seconds},
        }).then(() => {
          this.$emit("saveAction");
          this.getTrainingAlarm(this.$store.state.userStore.userType);
          this.$store.dispatch("callToast", {
            msg: "훈련일지를 승인하였습니다.",
            result: "success",
          });
        });
      }
      this.$refs.childComponent.workDataReset()
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
          this.companyInfoDialogData.comZip = data.zonecode;
          this.companyInfoDialogData.comAddr1 = fullRoadAddr;
        },
      }).open();
    },
    logout() {
      sessionStorage.clear();
      this.moveToLogin();
    },
    setDialogDate(val){
      if(val){
        return this.companyUserTaskSettingDialogData.date.substr(0,4)+"년 "+this.companyUserTaskSettingDialogData.date.substr(5,2)+"월 "+this.companyUserTaskSettingDialogData.date.substr(8,2)+"일"
      }
    },
  },
};
</script>
<style>
.welcome{
  align-self: center;
  margin: unset !important;
}
.page-cover {
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 10;
    background-color: rgb(255, 255, 255);
}
.spinner-div{
  width: 100%;
  height: 100%;
}
.pointer{
  width:100%;
  cursor: pointer;
}

.main_header > .v-toolbar__content{
  display: block !important;
  padding: 4px 0;
}
.sub_header{
  /* box-shadow: 0px 2px 4px -1px rgb(0 0 0 / 20%), 0px 4px 5px 0px rgb(0 0 0 / 14%), 0px 1px 10px 0px rgb(0 0 0 / 12%); */
  height: 48px;
}
.dialog-cover.on {
  height: 100%;
  position: fixed;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 10;
}
@media screen and (min-width: 960px){
  .v-card {
    max-height: 650px;
    overflow-y: auto;
  }
}
.fade-in-box {
  display: inline-block;
  background: yellow;
  padding: 10px;
  animation: fadein 0.5s;
  -moz-animation: fadein 0.5s; /* Firefox */
  -webkit-animation: fadein 0.5s; /* Safari and Chrome */
  -o-animation: fadein 0.5s; /* Opera */
}
.trainingImgSlot {

}
.imgSlotY {
  cursor: pointer;
}
.imgSlotN {
  
}
@keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
@-moz-keyframes fadein { /* Firefox */
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
@-webkit-keyframes fadein { /* Safari and Chrome */
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
@-o-keyframes fadein { /* Opera */
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
.jin {background: tomato !important;}
.jin2 {background: rosybrown !important;}
.background{
  background-color:rgba(240, 240, 240);
  border-radius: 10px;
}
.inner {
  width: 1170px;
  margin: 0 auto;
}
.home-card{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.header-height {
  flex: none;
  margin: 0;
  height: 60px;
  background: linear-gradient( to right, #61C0BD, #008CD6 );
}
.header-inner {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header-logo-cover {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.header-profile-cover {
  background: #CAE5F4;
  width: 40px;
  height: 40px;
  border-radius: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
.header-profile-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.sub-header {
  display: flex;
  justify-content: flex-start;
}
.work-update-row2 {
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 23px;
}
.editBtnBoxWrap .btnBox {
  display: flex;
  justify-content: center;
  align-items: center;
}
.editBtnBoxWrap button {
  width: 126px !important;
  height: 48px !important;
  border-radius: 10px !important;
  font-family: 'Pretendard-Regular';
  font-size: 18px !important;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: none;
}
.editBtnBoxWrap .edit1btn {
  background-color: #f5f5f5 !important;
  color: #2e2e2e !important;
  margin-right: 10px;
}
.editBtnBoxWrap .edit2btn {
  background: #EFF9F8 !important;
  color: #49ADA9 !important;
  margin-right: 10px;
}
.editBtnBoxWrap .deletebtn {
  background: #FFF0E6 !important;
  color: #FF6B00 !important;
}
.work-update-row3 .dateBox h2 {
  color: #2e2e2e;
  font-size: 20px;
  margin: 0;
  margin-bottom: 5px;
}
.work-update-row3 .dateBox p {
  margin: 0;
  color: #646464;
  font-size: 16px;
}
.work-update-row3 .timeBox {
  display: flex;
  align-items: center;
  margin: 27px 0 70px;
}
.work-update-row3 .timeBox .mark {
  background: #61C0BD;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 11.5px;
  margin-right: 8px;
  border: 0;
  width: 43px;
  height: 22px;
}
.work-update-row3 .timeBox .mark0 {
  background: #49ADA9;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 11.5px;
  margin-right: 8px;
  border: 0;
  width: 83px;
  height: 22px;
}
.work-update-row3 .timeBox .mark1 {
  background: #FF6B00;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 11.5px;
  margin-right: 8px;
  border: 0;
  width: 83px;
  height: 22px;
}
.work-update-row3 .timeBox > p {
  color: #646464;
  font-size: 16px;
  margin: 0;
}
.work-update-row4 > h2 {
  font-size: 22px;
  color: #2e2e2e;
  margin: 0 0 18px;
}
.work-update-row4 .timeinputBox,
.work-update-row4-1 .timeinputBox {
  display: flex;
  align-items: center;
}
.work-update-row4 div {
  width: 240px !important;
}
.work-update-row4-print div {
  width: 260px !important;
}
.work-update-row4 label {
  left: 20px !important;
  top: 9px !important;
}
.work-update-row4 .timeinputBox input {
  width: 257px;
  height: 39px;
  border: 1px solid #E1E1E1;
  border-radius: 3px;
  text-align: right;
  padding-right: 21px !important;
  font-family: 'Pretendard-Regular';
}
.work-update-row4-1 .timeinputBox input {
  width: 257px;
  height: 39px;
  border: 1px solid #E1E1E1;
  border-radius: 3px;
  padding: 0 25px;
  font-family: 'Pretendard-Regular';
  font-size: 15px;
}
.workplusBox {
  margin:20px 0 62px;
}
.workplusBox p {
  color: #646464;
  font-size: 16px;
  margin: 5px 0;
}
.btnBox22 {
  width: 100%;
  display: flex;
  justify-content: flex-end;
}
.btnBox22 button {
  background: #F5F5F5 !important;
  border-radius: 10px !important;
  width: 126px !important;
  height: 48px !important;
  font-size: 18px !important;
  color: #646464;
  box-shadow: none;
}
.atten-2222 {}
.atten-2222 div {
  min-height:0;
}
.atten-2222 .btnBox {
  width: 107px;
  height: 39px;
  /* background: #61C0BD; */
  border-radius: 3px;
  position: relative;
}
.atten-2222 .btnBox .v-input {
  position: absolute;
  z-index: 3;
  left: 8px;
  top: 8px;
}
.atten-2222 .btnBox label {
  transition: all .3s;
  font-size: 13px;
  font-family: 'Pretendard-Regular';
  margin: 0;
  width: 107px !important;
  height: 39px !important;
  background: #ff6a0036;
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FF6B00;
}
.v-input--selection-controls__input .v-icon {
  color: #FF6B00;;
}
.atten-2222 .btnBox .success2--text + label {
  background: #61c0bd4a;
  color: #61C0BD;
}
.v-application .success2--text {
  color: #61C0BD !important;
}
.atten-row1 {
  display: flex;
  align-items: center;
  margin: 32px 0 24px;
}
.atten-row1 h2 {
  color: #2E2E2E;
  font-size: 20px;
  margin: 0;
  margin-right: 16px;
}
.atten-row1 p {
  font-size: 16px;
  color: #0081c7;
  margin: 0;
}
.atten-row2 {
  margin-bottom: 22px;
}
.atten-row2 h2 {
  margin: 0;
  color: #2e2e2e;
  font-size: 18px;
  margin-bottom: 10px;
}
.atten-row2 p {
  margin: 0;
  font-size: 16px;
  color: #2e2e2e;
}
.profileBox {
  width: 270px;
  padding: 18px 24px;
}
.profileBox .exitBox {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  margin-bottom: 15px;
}
.profileBox .editBtn {
  margin-bottom: 12px;
}
.profileBox .logoutBtn {
  margin-bottom: 28px;
}
.profileBox .editBtn,
.profileBox .logoutBtn {
  width: 222px !important;
  height: 48px !important;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  border: none !important;
  box-shadow: none !important;
  border-radius: 10px !important;
}
.profileBox .editBtn svg,
.profileBox .logoutBtn svg {
  margin-right: 30px;
}
.profileBox .lastBox {}
.profileBox .lastBox p {
  font-size: 15px;
  color: #989898;
  font-family: 'Pretendard-Regular';
  margin: 0;
}
.v-menu__content {
  border-radius: 20px !important;
}
.jinBtn {
  font-family: 'Pretendard-Regular' !important;
  font-size: 18px !important;
  box-shadow: none;
  width: 126px !important;
  height: 48px !important;
  border-radius: 10px;
}
</style>
