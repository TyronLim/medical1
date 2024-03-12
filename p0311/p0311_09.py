def cal(a1,a2):
    result1 = a1+a2
    result2 = a1-a2
    result3 = a1*a2
    result4 = float('{:.2f}'.format(a1/a2))
    return result1, result2, result3, result4
 
input1 = int(input('1번째 숫자를 입력하세요.>> '))
input2 = int(input('2번째 숫자를 입력하세요.>> '))

# cal(input1,input2)
result1,result2,result3,result4 = cal(input1,input2)

print('값 :{},{},{},{}'.format(result1, result2, result3, result4))

# 함수의 return을 사용해서 입력된 두 수의 사칙연산 결과값을 출력하시오.
# 20, 10
# 결과값 : 30, 10, 200, 2








# for i in range(10):
#     sum = 0
#     sum += 1                #for 문을 빠져나가면 없어짐

# for i in range(5):
#     result = 1
#     result += 1
    
# print(sum)
# print(result)


# def lim(v1,v2):
#     v1 = 100 + v1
#     v2 = 200 + v2
#     return v1,v2    >> 함수 밖에서 사용하려면 return 값을 돌려줘야 함    

# # 함수호출
# v1 = 1
# v2 = 2
# v1,v2 = lim(v1,v2)

# # 출력
# print(v1,v2)