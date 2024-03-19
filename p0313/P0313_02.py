
def cal(num1,num2):
    r_list=[0]*4
    r_list[0] = num1 + num2
    r_list[1] = num1 - num2
    r_list[2] = num1 * num2
    r_list[3] = num1 / num2
    
    return r_list


save_list = []

while True:
    num1 = int(input('첫째 숫자를 입력하세요 >> (0.취소)'))
    if num1 == 0:
        break
    num2 = int(input('둘째 숫자를 입력하세요 >> '))
    r_list = cal(num1,num2)
    save2 = []
    save2.append(num1)
    save2.append(num2)
    save2.append(r_list[0])
    save2.append(r_list[1])
    save2.append(r_list[2])
    save2.append(r_list[3])
    save_list.append(save2)
     
    print(*r_list)      # 리스트일 경우 list = list[0]+list[1]+list[2]+list[3]

# 지금까지 입력한 숫자와 결과값을 모두 출력을 해보세요.
print('[ 현재까지 입력한 숫자, 결과값 : {}]'.format(save_list))

for i in range(len(save_list)):
    print('넣은 숫자 : {},{} / 결과값 : {},{},{},{}'.format(
        save_list[i][0],save_list[i][1],save_list[i][2],save_list[i][3],save_list[i][4],save_list[i][5]
    ))

#-----------------------------------------------------------------------------------#

# def cal2(num1,num2,c):
#     if c == '1':
#         result = num1+num2
    
#     elif c == '2':
#         result = num1-num2

#     elif c == '3':
#         result = num1*num2

#     elif c == '4':
#         result = num1/num2

#     return result

# num1 = int(input('첫째 숫자를 입력하세요 >> '))
# num2 = int(input('둘째 숫자를 입력하세요 >> '))
# c = input('1.더하기 2.빼기 3.곱하기 4.나누기')

# result = cal2(num1,num2,c)
# print(result)

