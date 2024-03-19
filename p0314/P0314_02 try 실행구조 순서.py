# 외부와의 데이터 전송, 데이터 받기, 외부기기 연결, 다른 프로그램 연결
# 위 외에는 되도록 오류가 발생되지 않도록 하는 게 가장 좋음.
# if else 느낌

print('프로그램 실행')
try:
    print(1)
    print(2)
    print(1/0)   # 에러가 발생
    print(3)
except:
    print(4)
    print(5)
print(6)
print('프로그램 종료')

