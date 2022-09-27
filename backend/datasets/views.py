from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import *
from .serializers import *

# 회사 가데이터 생성 함수
def create_company(request):
    CompanyList.objects.create(comName="㈜CMS에듀", ceoName="이충국", businessNum="211-87-37049", comNum="02-552-8500", comAddr1="서울시 강남구 테헤란로 521 파르나스타워 21층", managerName="김정석", managerNum="010-0000-0000", introduction=""),
    CompanyList.objects.create(comName="㈜삼성전자", ceoName="김기남", businessNum="124-81-00998", comNum="02-2255-0114", comAddr1="경기 수원시 영통구 삼성로 129 삼성전자공업단지", managerName="수정바랍니다.", managerNum="010-0000-0000", introduction=""),
    CompanyList.objects.create(comName="㈜위플레이", ceoName="허성만", businessNum="865-88-02214", comNum="0507-1486-9321", comAddr1="경기 오산시 부산중앙로 42", managerName="이재건", managerNum="010-0000-0000", introduction="장애인 운동선수 고용 컨설팅"),
    CompanyList.objects.create(comName="㈜카카오", ceoName="여민수", businessNum="120-81-47521", comNum="1899-1326", comAddr1="제주 제주시 첨단로 242", managerName="박금서", managerNum="010-0000-0000", introduction="사고력 기반 융합사고력 교육기업"),

    return HttpResponse("샘플 데이터 입력")

# 복지관 가데이터 생성 함수
def create_team(request):
    TeamList.objects.create(teamName="가평군 장애인복지관", teamNum="031-581-9785", teamAddr1="경기 가평군 가평읍 석봉로191번길 65-19"),
    TeamList.objects.create(teamName="경기도 시각장애인복지관", teamNum="031-856-5300", teamAddr1="경기 의정부시 추동로 140 경기북부상공회의소"),
    TeamList.objects.create(teamName="고양시 장애인종합복지관", teamNum="031-929-1400", teamAddr1="경기 고양시 일산서 탄현로 139 장애인종합복지관"),
    TeamList.objects.create(teamName="과천시 장애인복지관", teamNum="02-2185-8000", teamAddr1="경기 과천시 문원로 40 과천시장애인종합복지관"),
    TeamList.objects.create(teamName="광명 장애인종합복지관", teamNum="02-2616-3700", teamAddr1="경기 광명시 목감로 120 광명장애인종합복지관"),
    TeamList.objects.create(teamName="광주시 성분도복지관", teamNum="031-799-0300", teamAddr1="경기 광주시 도척면 국사봉로 159-10 곤지암성분도복지관"),
    TeamList.objects.create(teamName="구리시 장애인종합복지관", teamNum="031-562-0068", teamAddr1="경기 구리시 이문안로 86-1 구리시장애인종합복지관"),
    TeamList.objects.create(teamName="군포시 장애인종합복지관", teamNum="031-396-3108", teamAddr1="경기 군포시 청백리길 18 군포장애인종합복지관"),
    TeamList.objects.create(teamName="김포시 장애인복지관", teamNum="070-7327-4100", teamAddr1="경기 김포시 김포한강3로 291"),
    TeamList.objects.create(teamName="남양주시 장애인복지관", teamNum="031-592-7150", teamAddr1="경기 남양주시 홍유릉로 273 남양주시보훈회관"),
    TeamList.objects.create(teamName="동두천시 장애인종합복지관", teamNum="031-867-0080", teamAddr1="경기 동두천시 상패로 64 동두천시장애인재활자립작업장"),
    TeamList.objects.create(teamName="부천시 장애인종합복지관", teamNum="032-670-1100", teamAddr1="경기 부천시 역곡로 367 부천시장애인복지관"),
    TeamList.objects.create(teamName="성남시 한마음복지관", teamNum="031-725-9500", teamAddr1="경기 성남시 분당구 야탑로 227"),
    TeamList.objects.create(teamName="성남시 장애인종합복지관", teamNum="031-733-3322", teamAddr1="경기 성남시 중원구 사기막골로150번길 20 장애인종합복지관"),
    TeamList.objects.create(teamName="시흥 장애인종합복지관", teamNum="031-431-9114", teamAddr1="경기 시흥시 정왕대로233번길 27-1"),
    TeamList.objects.create(teamName="안산시 상록장애인복지관", teamNum="031-409-0000", teamAddr1="경기 안산시 상록구 차돌배기로 24-2"),
    TeamList.objects.create(teamName="안산시 장애인복지관", teamNum="031-403-0078", teamAddr1="경기 안산시 단원구 원초로 80 안산시장애인종합복지관"),
    TeamList.objects.create(teamName="안성시 장애인복지관", teamNum="031-673-0556", teamAddr1="경기 안성시 배티로 1097"),
    TeamList.objects.create(teamName="안양시 관악장애인종합복지관", teamNum="031-472-7774", teamAddr1="경기 안양시 만안구 경수대로 1132 장애인복지회관 1동"),
    TeamList.objects.create(teamName="안양시 만안종합사회복지관", teamNum="031-464-9701", teamAddr1="경기 안양시 만안구 박달로 547-1"),
    TeamList.objects.create(teamName="안양시 수리장애인종합복지관", teamNum="031-465-0950", teamAddr1="경기 안양시 만안구 냉천로 39"),
    TeamList.objects.create(teamName="양평군 장애인복지관", teamNum="031-773-9080", teamAddr1="경기 양평군 양평읍 중앙로111번길 36-1 양평장애인복지관"),
    TeamList.objects.create(teamName="여주시 장애인복지관", teamNum="031-883-2100", teamAddr1="경기 여주시 청심로 105"),
    TeamList.objects.create(teamName="오산 장애인종합복지관", teamNum="0507-1404-5229", teamAddr1="경기 오산시 수청로 192 오산세교복지타운 2층"),
    TeamList.objects.create(teamName="용인시 기흥장애인복지관", teamNum="031-895-3200", teamAddr1="경기 용인시 기흥구 용구대로2469번길 94"),
    TeamList.objects.create(teamName="용인시 수지장애인복지관", teamNum="031-270-0200", teamAddr1="경기 용인시 수지구 포은대로 435 수지구청.수지보건소"),
    TeamList.objects.create(teamName="용인시 처인장애인복지관", teamNum="031-320-4800", teamAddr1="경기 용인시 처인구 경안천로 318"),
    TeamList.objects.create(teamName="의왕 희망나래장애인복지관", teamNum="031-467-7300", teamAddr1="경기 의왕시 오전로 27"),
    TeamList.objects.create(teamName="의정부시 장애인종합복지관", teamNum="031-850-5300", teamAddr1="경기 의정부시 용민로 160 의정부시장애인종합복지관"),
    TeamList.objects.create(teamName="이천시 장애인종합복지관", teamNum="031-637-6720", teamAddr1="경기 이천시 신둔면 석동로 3"),
    TeamList.objects.create(teamName="파주시 장애인종합복지관", teamNum="031-959-7020", teamAddr1="경기 파주시 법원읍 술이홀로1333번길 63 파주시장애인종합복지관"),
    TeamList.objects.create(teamName="평택 북부장애인복지관", teamNum="031-615-3975", teamAddr1="경기 평택시 이충동 산12"),
    TeamList.objects.create(teamName="평택 에바다장애인종합복지관", teamNum="031-692-2362", teamAddr1="경기 평택시 팽성읍 노와길 447"),
    TeamList.objects.create(teamName="하남시 장애인복지관", teamNum="031-794-2266", teamAddr1="경기 하남시 미사강변남로 56"),

    return HttpResponse("샘플 데이터 입력")

def create_sample(request):

    MainCategory.objects.bulk_create(
        [
            MainCategory(name="장애등급"),
            MainCategory(name="혈액형"),
            MainCategory(name="결혼여부"),
            MainCategory(name="병역여부"),
            MainCategory(name="최종학력"),
            MainCategory(name="유저타입"),
            MainCategory(name="근무요일"),
        ]
    )

    key_1 = MainCategory.objects.get(name="장애등급")
    key_2 = MainCategory.objects.get(name="혈액형")
    key_3 = MainCategory.objects.get(name="결혼여부")
    key_4 = MainCategory.objects.get(name="병역여부")
    key_5 = MainCategory.objects.get(name="최종학력")
    key_6 = MainCategory.objects.get(name="유저타입")
    key_7 = MainCategory.objects.get(name="근무요일")

    # 장애등급 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_1, value="경증"),
            SubCategory(maincategory=key_1, value="중증"),
        ]
    )

    # 혈액형 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_2, value="A"),
            SubCategory(maincategory=key_2, value="B"),
            SubCategory(maincategory=key_2, value="O"),
            SubCategory(maincategory=key_2, value="AB"),
        ]
    )

    # 결혼여부 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_3, value="미혼"),
            SubCategory(maincategory=key_3, value="기혼"),
        ]
    )

    # 병역여부 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_4, value="필"),
            SubCategory(maincategory=key_4, value="미필"),
            SubCategory(maincategory=key_4, value="면제"),
        ]
    )
    
    # 최종학력 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_5, value="초졸"),
            SubCategory(maincategory=key_5, value="중졸"),
            SubCategory(maincategory=key_5, value="고졸"),
            SubCategory(maincategory=key_5, value="초대졸"),
            SubCategory(maincategory=key_5, value="대졸"),
            SubCategory(maincategory=key_5, value="석사"),
            SubCategory(maincategory=key_5, value="박사"),
        ]
    )

    # 유저타입 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_6, value="코치"),
            SubCategory(maincategory=key_6, value="선수"),
            SubCategory(maincategory=key_6, value="복지관"),
            SubCategory(maincategory=key_6, value="기관"),
            SubCategory(maincategory=key_6, value="영업사원"),
        ]
    )

    # 근무요일 데이터 생성
    SubCategory.objects.bulk_create(
        [
            SubCategory(maincategory=key_7, value="월요일"),
            SubCategory(maincategory=key_7, value="화요일"),
            SubCategory(maincategory=key_7, value="수요일"),
            SubCategory(maincategory=key_7, value="목요일"),
            SubCategory(maincategory=key_7, value="금요일"),
            SubCategory(maincategory=key_7, value="토요일"),
            SubCategory(maincategory=key_7, value="일요일"),
        ]
    )
    
    # 장애유형 테이블 생성, 삽입
    DisabilityType.objects.bulk_create(
        [
            DisabilityType(value="절단 및 기타장애"),
            DisabilityType(value="척수장애"),
            DisabilityType(value="청각장애"),
            DisabilityType(value="지적장애"),
            DisabilityType(value="뇌성마비"),
            DisabilityType(value="시각장애"),
        ]
    )

    # 운동종목 테이블 생성, 삽입
    SportType.objects.bulk_create(
        [
            SportType(value="골볼"),
            SportType(value="농구"),
            SportType(value="론볼"),
            SportType(value="배드민턴"),
            SportType(value="보치아"),
            SportType(value="볼링"),
            SportType(value="사격"),
            SportType(value="수영"),
            SportType(value="승마"),
            SportType(value="사이클"),
            SportType(value="양궁"),
            SportType(value="육상"),
            SportType(value="탁구"),
        ]
    )

    # 기업목록 테이블 생성, 삽입
    # CompanyList.objects.bulk_create(
    #     [
    #         CompanyList(comName="㈜CMS에듀", ceoName="이충국", businessNum="211-87-37049", comNum="02-552-8500", comAddr1="서울시 강남구 테헤란로 521 파르나스타워 21층", managerName="김정석", managerNum="010-0000-0000", introduction=""),
    #         CompanyList(comName="㈜삼성전자", ceoName="김기남", businessNum="124-81-00998", comNum="02-2255-0114", comAddr1="경기 수원시 영통구 삼성로 129 삼성전자공업단지", managerName="수정바랍니다.", managerNum="010-0000-0000", introduction=""),
    #         CompanyList(comName="㈜위플레이", ceoName="허성만", businessNum="865-88-02214", comNum="0507-1486-9321", comAddr1="경기 오산시 부산중앙로 42", managerName="이재건", managerNum="010-0000-0000", introduction="장애인 운동선수 고용 컨설팅"),
    #         CompanyList(comName="㈜카카오", ceoName="여민수", businessNum="120-81-47521", comNum="1899-1326", comAddr1="제주 제주시 첨단로 242", managerName="박금서", managerNum="010-0000-0000", introduction="사고력 기반 융합사고력 교육기업"),
    #     ]
    # )

    # 팀 목록 테이블 생성, 삽입
    # TeamList.objects.bulk_create(
    #     [
    #         TeamList(teamName="가평군 장애인복지관", teamNum="031-581-9785", teamAddr1="경기 가평군 가평읍 석봉로191번길 65-19"),
    #         TeamList(teamName="경기도 시각장애인복지관", teamNum="031-856-5300", teamAddr1="경기 의정부시 추동로 140 경기북부상공회의소"),
    #         TeamList(teamName="고양시 장애인종합복지관", teamNum="031-929-1400", teamAddr1="경기 고양시 일산서 탄현로 139 장애인종합복지관"),
    #         TeamList(teamName="과천시 장애인복지관", teamNum="02-2185-8000", teamAddr1="경기 과천시 문원로 40 과천시장애인종합복지관"),
    #         TeamList(teamName="광명 장애인종합복지관", teamNum="02-2616-3700", teamAddr1="경기 광명시 목감로 120 광명장애인종합복지관"),
    #         TeamList(teamName="광주시 성분도복지관", teamNum="031-799-0300", teamAddr1="경기 광주시 도척면 국사봉로 159-10 곤지암성분도복지관"),
    #         TeamList(teamName="구리시 장애인종합복지관", teamNum="031-562-0068", teamAddr1="경기 구리시 이문안로 86-1 구리시장애인종합복지관"),
    #         TeamList(teamName="군포시 장애인종합복지관", teamNum="031-396-3108", teamAddr1="경기 군포시 청백리길 18 군포장애인종합복지관"),
    #         TeamList(teamName="김포시 장애인복지관", teamNum="070-7327-4100", teamAddr1="경기 김포시 김포한강3로 291"),
    #         TeamList(teamName="남양주시 장애인복지관", teamNum="031-592-7150", teamAddr1="경기 남양주시 홍유릉로 273 남양주시보훈회관"),
    #         TeamList(teamName="동두천시 장애인종합복지관", teamNum="031-867-0080", teamAddr1="경기 동두천시 상패로 64 동두천시장애인재활자립작업장"),
    #         TeamList(teamName="부천시 장애인종합복지관", teamNum="032-670-1100", teamAddr1="경기 부천시 역곡로 367 부천시장애인복지관"),
    #         TeamList(teamName="성남시 한마음복지관", teamNum="031-725-9500", teamAddr1="경기 성남시 분당구 야탑로 227"),
    #         TeamList(teamName="성남시 장애인종합복지관", teamNum="031-733-3322", teamAddr1="경기 성남시 중원구 사기막골로150번길 20 장애인종합복지관"),
    #         TeamList(teamName="시흥 장애인종합복지관", teamNum="031-431-9114", teamAddr1="경기 시흥시 정왕대로233번길 27-1"),
    #         TeamList(teamName="안산시 상록장애인복지관", teamNum="031-409-0000", teamAddr1="경기 안산시 상록구 차돌배기로 24-2"),
    #         TeamList(teamName="안산시 장애인복지관", teamNum="031-403-0078", teamAddr1="경기 안산시 단원구 원초로 80 안산시장애인종합복지관"),
    #         TeamList(teamName="안성시 장애인복지관", teamNum="031-673-0556", teamAddr1="경기 안성시 배티로 1097"),
    #         TeamList(teamName="안양시 관악장애인종합복지관", teamNum="031-472-7774", teamAddr1="경기 안양시 만안구 경수대로 1132 장애인복지회관 1동"),
    #         TeamList(teamName="안양시 만안종합사회복지관", teamNum="031-464-9701", teamAddr1="경기 안양시 만안구 박달로 547-1"),
    #         TeamList(teamName="안양시 수리장애인종합복지관", teamNum="031-465-0950", teamAddr1="경기 안양시 만안구 냉천로 39"),
    #         TeamList(teamName="양평군 장애인복지관", teamNum="031-773-9080", teamAddr1="경기 양평군 양평읍 중앙로111번길 36-1 양평장애인복지관"),
    #         TeamList(teamName="여주시 장애인복지관", teamNum="031-883-2100", teamAddr1="경기 여주시 청심로 105"),
    #         TeamList(teamName="오산 장애인종합복지관", teamNum="0507-1404-5229", teamAddr1="경기 오산시 수청로 192 오산세교복지타운 2층"),
    #         TeamList(teamName="용인시 기흥장애인복지관", teamNum="031-895-3200", teamAddr1="경기 용인시 기흥구 용구대로2469번길 94"),
    #         TeamList(teamName="용인시 수지장애인복지관", teamNum="031-270-0200", teamAddr1="경기 용인시 수지구 포은대로 435 수지구청.수지보건소"),
    #         TeamList(teamName="용인시 처인장애인복지관", teamNum="031-320-4800", teamAddr1="경기 용인시 처인구 경안천로 318"),
    #         TeamList(teamName="의왕 희망나래장애인복지관", teamNum="031-467-7300", teamAddr1="경기 의왕시 오전로 27"),
    #         TeamList(teamName="의정부시 장애인종합복지관", teamNum="031-850-5300", teamAddr1="경기 의정부시 용민로 160 의정부시장애인종합복지관"),
    #         TeamList(teamName="이천시 장애인종합복지관", teamNum="031-637-6720", teamAddr1="경기 이천시 신둔면 석동로 3"),
    #         TeamList(teamName="파주시 장애인종합복지관", teamNum="031-959-7020", teamAddr1="경기 파주시 법원읍 술이홀로1333번길 63 파주시장애인종합복지관"),
    #         TeamList(teamName="평택 북부장애인복지관", teamNum="031-615-3975", teamAddr1="경기 평택시 이충동 산12"),
    #         TeamList(teamName="평택 에바다장애인종합복지관", teamNum="031-692-2362", teamAddr1="경기 평택시 팽성읍 노와길 447"),
    #         TeamList(teamName="하남시 장애인복지관", teamNum="031-794-2266", teamAddr1="경기 하남시 미사강변남로 56"),
    #     ]
    # )

    return HttpResponse("샘플 데이터 입력")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


# 장애유형 ViewSet
class DisabilityTypeViewSet(viewsets.ModelViewSet):
    queryset = DisabilityType.objects.all()
    serializer_class = DisabilityTypeSerializer


# 운동종목 ViewSet
class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


# 기업목록 ViewSet
class CompanyListViewSet(viewsets.ModelViewSet):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer

    # Naver API Geocoding 주소 -> 경도, 위도 변환
    def create(self, request, *args, **kwargs):
        try:
            comAddr = request.data["comAddr1"]
            add_urlenc = parse.quote(comAddr) # 아스키코드 형식이 아닌 글자를 URL 인코딩
            url = os.environ.get("naver_geocoding_url") + add_urlenc
            request_url = Request(url)
            request_url.add_header('X-NCP-APIGW-API-KEY-ID', os.environ.get("naver_client_ID"))
            request_url.add_header('X-NCP-APIGW-API-KEY', os.environ.get("naver_client_PW"))
            try:
                response = urlopen(request_url) # URL에 해당하는 Response Instance를 Return
            except HTTPError as e:
                print('HTTP Error!')
                latitude = None
                longitude = None
            else:
                rescode = response.getcode() # status code 리턴
                if rescode == 200:
                    response_body = response.read().decode('utf-8') # utf-8: 유니코드를 위한 가변 길이 문자 인코딩 방식
                    response_body = json.loads(response_body) # json 형식으로 주소 Return
                    if response_body['addresses'] == [] :
                        print("'result' not exist!")
                        latitude = None
                        longitude = None
                    else:
                        latitude = response_body['addresses'][0]['y'] # 경도
                        longitude = response_body['addresses'][0]['x'] # 위도
                        print("Success!")
                else:
                    print('Response error code : %d' % rescode)
                    latitude = None
                    longitude = None
        except:
            latitude = None
            longitude = None

        # remember old state
        _mutable = request.data._mutable
        # set to mutable
        request.data._mutable = True
        # сhange the values you want
        request.data['latitude'] = latitude
        request.data['longitude'] = longitude
        # set mutable flag back
        request.data._mutable = _mutable
        return super().create(request)


# 복지관(훈련기관) ViewSet
class TeamListViewSet(viewsets.ModelViewSet):
    queryset = TeamList.objects.all()
    serializer_class = TeamListSerializer