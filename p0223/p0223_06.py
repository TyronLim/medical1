# if - else
# if - elif - else 
# if 조건문1 :
#     실행문
# elif 조건문2
#     실행문2
# else:
#     실행문3
# >조건문 1이 참이면 실행문1 실행 후 종료.
# >조건문 1이 거짓이고, 조건문 2가 참이면 실행문2 실행 후 종료

# 조건문1, 조건문2가 거짓이면 실행문3 실행 후 종료

# weather = '비'
# if weather == '비':
#     print('비가 오네요')
# elif weather == '눈':
#     print('눈이 오세요.')
# else : 
#     print('선크림을 발라주세요')
    
# 변수가 양수면 양수, 음수면 음수, 0이면 0이라고 출력해보세요.
# num = int(input('숫자를 입력해보세요 : '))

# if num > 0 :
#     print('양수')
# elif num < 0 :
#     print('음수')
# else :
#     print('0')
    
    
# 돈이 만원이상 [택시를 탄다] 이천원이상 [버스를 탄다]
# 천원 이상 [따릉이를 빌린다] 나머지 [걸어간다]

money = 12000

if money >= 10000:
    print('택시를 탄다')
elif 2000 <= money:
    print('버스를 탄다')
elif 1000 <= money:
    print('따릉이를 빌린다')
else :
    print('걸어간다')

