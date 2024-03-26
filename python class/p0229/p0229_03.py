# 반복문 for문, while문
'''
for i in range(시작값, 끝값+1, 증감값):
    수행문장
    
while 조건식:
    실행할 문장
    
변수 = 시작값
while 변수 < 끝값 :     이 조건이 참일 떄
    반복구문
    변수 = 변수 + 증가값
'''

# for i in range(0,3,1):
#     print('안녕하세요')

# i = 0
# while i < 3 :
#     print('안녕')
#     i = i+1
    
# # for와 while로 0-10까지 출력
# for i in range(0,11,1):
#     print(i)
    
# i = 0
# while i < 11:
#     print(i)
#     i = i+1
    
# while 사용하기
# 1-10 사이의 3의 배수 출력
# i = 1
# while i < 11:
#     if i%3 == 0:
#         print(i)
#     i = i+1

# # 1-100 사이의 홀수 출력
# j = 1
# while j <= 100:
#     if j%2 != 0:
#         print(j)
#     j += 1

# # 1-100 까지의 합 구하기
# a = 0
# k = 1
# while k < 101:
#     a = a + k
#     k = k + 1
# print(a)

# b = 0
# for i in range(1,101):
#     b+=i                   # 0+1  0+1+2  0+1+2+3  0+1+2+3+4 .... 100까지
# print(b)

# while True:                 # while True는 무조건 참이기 때문에  
#     print('ㅋ')             # while 조건문이 참인 경우 무한히 반복   ctrl + c 로 강제 종료

# while문은 조건문을 잘 만드는게 중요. (변수를 범위 안에 넣기)

# break, continue
# break = 반복문을 빠져나와서 다음단계를 수행
n=0
while n <100:
    print(n)
    if n == 4:
        break
    n+=1
    
breakletter = input('중단할 문자를 입력하세요 >> ')
for letter in 'python':
    if letter == breakletter:
        break
    print(letter)

while True:
    n = int(input('숫자를 입력해주세요'))
    print(n)
    if n == 0:
        print('종료되었습니다.')
        break







