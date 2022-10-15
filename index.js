import axios from "axios";
import store from "../store/store";

// axios 인스턴스 생성
const instance = axios.create({
  // baseURL: "http://127.0.0.1:8000/", // 기본 백엔드 서버 주소
  baseURL: "http://54.180.178.255:8000/", // 백엔드 서버 주소
  headers: {
    Authorization: "JWT " + store.state.authStore.access_token,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

/*
  1. 요청 인터셉터
  2개의 콜백 함수를 받습니다.
*/
instance.interceptors.request.use(
  // 요청 성공 직전 호출됩니다.
  // axios 설정값을 넣습니다. (사용자 정의 설정도 추가 가능)
  function(config) {
    config.headers.Authorization = "JWT " + store.state.authStore.access_token;
    return config;
  },
  // 요청 에러 직전 호출됩니다.
  function(error) {
    return Promise.reject(error);
  }
);

/*
  2. 응답 인터셉터
  2개의 콜백 함수를 받습니다.
*/
instance.interceptors.response.use(
  /*
    http status가 200인 경우
    응답 성공 직전 호출됩니다. 
    .then() 으로 이어집니다.
  */
  function(response) {
    return response;
  },

  /*
    http status가 200이 아닌 경우
    응답 에러 직전 호출됩니다.
    .catch() 으로 이어집니다.    
  */
  async function(error) {
    // 에러에서 정보 추출
    const {
      config, // 실패한 기존 요청
      response: { status },
    } = error;

    if (status === 401 && error.response.data.code === "token_not_valid") {
      console.log("액세스 토큰 만료");
      const originalRequest = config;
      const refreshToken = store.state.authStore.refresh_token;
      // 리프레시 토큰 이용하여 새로운 액세스 토큰 요청
      console.log("새로운 토큰 요청");

      try {
        const res = await axios.post("http://54.180.178.255:8000/users/refresh/", {
          refresh: refreshToken,
        });
        console.log("액세스 토큰 재발급 성공");
        // 세션 저장소의 액세스 토큰 업데이트
        store.commit("setAccess", res.data.access);
        // 원래 요청의 헤더에 있는 토큰 새로 발급받은 토큰으로 변경
        originalRequest.headers.Authorization =
          "JWT " + store.state.authStore.access_token;
        // 실패했던 기존 요청 새로운 토큰 이용하여 다시 실행
        return axios(originalRequest);
      } catch (err) {
        console.log(err.response);
        sessionStorage.clear(); // 세션 저장소의 데이터 삭제
        console.log("액세스 토큰 재발급 실패(리프레시 토큰 만료)");
        alert("세션이 만료되었습니다 다시 로그인 해주세요.");
        window.location.href = "http://54.180.178.255:8080/auth/login";
      }
    }
    return Promise.reject(error);
  }
);

export default instance;
