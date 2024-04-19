import requests # 웹 정보, 소스 가져오는 라이브러리

# res = requests.get("http://www.google.com")
# url = "http://www.google.com"
# ---------------------------------------기본 구문---------------------------------------------
url = "http://www.melon.com"
res = requests.get(url)
res.raise_for_status() #에러코드 발생 시 프로그램 종료 ## 처음에 넣어둠. 에러 시 밑 구문은 실행 안 함.
aaa = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=aaa)
res.raise_for_status()
# --------------------------------------------------------------------------------------------
# print(res.status_code)  # 응답코드 값 (200,404,406,500 등)

if res.status_code == requests.codes.OK: # requests.codes.OK = 200(응답코드)
    print("정상적인 페이지 호출")
else:
    print('접근할 수 없음 [에러코드 : ',res.status_code,']')
    

# print(res)



