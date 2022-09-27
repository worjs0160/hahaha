<h1>We Play</h1>

<h3><형상관리> - 각 brach 명과 역할</h3>
    <ui>
        <li>master - 배포를 위한 완성된 코드를 유지</li>
        <li>develop - 개발 통합을 위한 브랜치. feature 브랜치의 루트</li>
        <li>KJS - </li>
        <li>LJG - </li>
        <li>BKS - </li>
        <li>KJH - </li>
    </ui>
<h3>진행사항</h3>
    <ul>
        <li>
            <h4>2021-05-25</h4>
            <ul>
                <li>djangorestframework-jwt 삭제하고 djangorestframework-simplejwt 설치하여 적용</li>
                <li>vuex와 vuex-persistence 패키지 설치 및 환경구성</li>
            </ul>
        </li>
        <li>
            <h4>2021-05-29</h4>
            <ul>
                <li>UserList 선수 없음 표시 추가하고 몇몇 프론트 오류 수정</li>
                <li>장고 ImageField 사용 위해 Pillow 패키지 설치(pip)</li>
                <li>vue 데이트&타임 피커 사용하기 위해서 2개의 패키지 설치 필요 npm install --save vue-datetime luxon</li>
            </ul>
        </li>
        <li>
            <h4>2021-06-14</h4>
            <ul>
                <li>npm i socket.io-client 채팅을 이용하는 클라이언트 패키지 사용</li>
                <li>채팅 node 서버 경로 SST/frontend/chat-server || npm install cors, express, socket.io 설치 필요 || node app.js 로 실행</li>
                <li>근태관리 및 훈련관리 반응형 사이즈 보완</li>
                <li>근태 생성/수정 시 프론트 데이터 검증 로직 추가</li>
                <li>vuex과 vuetify snackbar를 활용 전역에서 사용가능한 Toast Message 기능 구현 this.$store.dispatch("callToast",{msg:"출력하고자하는 메시지", result: success 또는 fail}) 으로 호출 가능 210618 - 카테고리 앱 생성 - 메인 카테고리 등록 후 자식 카테고리 등록해서 사용</li>
            </ul>
        </li>
        <li>
            <h4>2021-06-18</h4>
            <ul>
                <li>f_backEnd_Bill - Bill(인수증) CRUD API 구현</li>
            </ul>
        </li>
        <li>
            <h4>2021-06-26</h4>
            <ul>
                <li>f_frontEnd_ExcelAxios - 프론트엔드 CRUD 구현 / 수정과 삭제 미완료</li>
            </ul>
        </li>
        <li>
            <h4>2021-07-21</h4>
            <ul>
                <li>chart.js 패키지 npm install chart.js chartkick hchs-vue-charts vue-chartjs vue-chartkick로 다운로드, 에러 발생시 npm install vue-chartjs chart.js@2 --save로 해결 가능</li>
                <li>유저 모델 변경이 있으므로 makemigrations -> migrate</li>
            </ul>
        </li>
        <li>
            <h4>2021-08-24</h4>
            <ul>
                <li>npm install vue-spinner 로딩창에 사용될 스피너 패키지</li>
            </ul>
        </li>
        <li>
            <h4>2021-09-04</h4>
            <ul>
                <li> auth -> signup 컴포넌트 이름 소문자 -> 대문자로 변경해야함</li>
            </ul>
        </li>
        <li>
            <h4>2021-09-09</h4>
            <ul>
                <li>기업페이지 기능 구현에 따라 유저 모델(companyPermission) 추가 makemigrations -> migrate</li>
            </ul>
        </li>
        <li>
            <h4>2021-10-28</h4>
            <ul>
                <li>npm install @mdi/font 명령어로 버전 6.4.95 설치 </li>
            </ul>
        </li>
        <li>
            <h4>2021-12-03</h4>
            <ul>
                <li>기준일 사이 근태 및 훈련일지 가져오는 API 구현</li>
                <li>사용법 : url/?onTime__range=2021-11-28T00:00:00,2021-12-6T00:00:00</li>
            </ul>
        </li>
        <li>
            <h4>2021-12-18</h4>
            <ul>
                <li>네이버 클라우드 플랫폼 client ID, PW 보안을 위해 .env 파일 생성</li>
                <li>pip install django-dotenv 설치</li>
            </ul>
        </li>
        <li>
            <h4>2021-12-20</h4>
            <ul>
                <li>npm install printd 근태, 업무에 사용될 인쇄 양식출력을 위한 프린터 패키지</li>
            </ul>
        </li>
        <li>
            <h4>2022-02-08</h4>
            <ul>
                <li>npm install --save @fullcalendar/vue @fullcalendar/core @fullcalendar/daygrid @fullcalendar/interaction</li>
                <li> 운동선수 홈의 일정관리를 위한 FullCalender 패키지</li>
                <li>https://fullcalendar.io/docs/vue FullCalendar5버전 docs</li>
            </ul>
        </li>
    </ul>
