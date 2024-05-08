# numL = []

# #0에서부터 5까지 넣어보세요
# #append
# print(numL)
# numL.append(0)
# numL.append(1)
# numL.append(2)
# numL.append(3)
# numL.append(4)
# numL.append(5)
# print(numL)
#  # for 문을 사용하여 0~5까지 **[숫자]** 넣기
# #[0,1,2,3,4,5]
# #num[4]
# num=[]
# for i in range(6):   #i는 0에서부터 6 미만까지 1씩 증가
#     num.append(i)
# print(num)

# aa=[1,2,3,4]
# #index를 사용해서 값 읽기
# for i in aa :
#     print(i)
# for i in range(0,4):
#     print(aa[i])
    
# f = ['사과','복숭아','딸기','포도','자몽']
# for i in f:
#     print(i)
# for i in range(0,5):  #리스트의 길이 len 함수는 반복문에서 자주 사용
#     print(f[i])

# #두 가지로 각각 출력    
# c = ['미국','영국','호주','캐나다','일본','중국']
# for i in c:
#     print(i)
# for i in range(0,6):
#     print(c[i])
# for i in range(len(c)):
#     print(c[i])


# 1에서 100까지 numL=[]만들고 출력
# numL = []
# for i in range(100):
#     numL.append(i+1)
#     print(i, end='')
# print()
# print(numL)
# for i in range(99) :
#     print(numL[i])
    
# # 반복문 안에 if문 사용
# for i in range(10):
#     # print(i)            #0 - 9 까지 출력
#     if i == 9 :
#         print('9입니다')
        
# lan = ['영어','스페인어','일본어','중국어']
# for i in lan :
#     if i == '영어':
#         print('영어입니다')
#     else :
#         print('영어가 아닙니다.')


# #2의 배수만 출력 (1-100 사이)
# # 1. 증감 사용
# for i in range(2,101,2):
#     print(i, end=' ')

# # 2. if문 사용
# for i in range(101):
#     if i%2 == 0:
#         print(i)
 
# # 7의 배수만 출력 (1-100 사이)
# # 1. 증감 사용
# for i in range(7,101,7):
#     print(i)

# # 2. if문 사용
# for i in range(1,101):
#     if i%7==0:
#         print(i)
 
# aa = [100,90,86,79,72,52,98,94]     
# # 80점 이상만 합격 출력
# for i in range(len(aa)):
#     if aa[i] >= 80:
#         print('합격')
#     else:
#         print('불합격')

# for a in aa:
#     print(a)
#     if a >= 80:
#         print('합격')
        
# f = ['사과','복숭아','딸기','포도','자몽']
# #딸기가 있으면 딸기, 다른 과일은 다른 과일이라고 출력
# for i in f:
#     # print(i)
#     if i == '딸기' :
#         print('딸기')
#     else:
#         print('다른과일')

num = [1,2,5,7,9,10,23,43]
# 짝수면 짝수, 홀수면 홀수를 출력
for i in num:
    if i%2 == 0:
        print('짝수')
    else:
        print('홀수')

num = [1,2,5,7,9,10,23,43]
# 짝수면 짝수, 홀수면 홀수를 출력
for i in range(len(num)):
    if num[i]%2 == 0:
        print('짝수')
    else:
        print('홀수')

for i in num:
    print(i)

