# 함수 선언 : def 이름()
# 함수 호출 : 이름()
# 함수선언 매개변수 개수 맞춰야 함 : def 이름(매개변수) -> 이름(매개변수)
# 리턴의 결과값을 받지 않아도 되지만, 개수는 맞춰야 함.
# 함수 내의 변수는 지역변수여서, 함수가 종료되면 사라짐.
# 함수 내에 변경된 변수값을 전역변수에 반영하고 싶으면 return으로 돌려줘야 함
# 함수 내 global은 전역변수에 선언되어 있는 변수주소를 가져옴.

# 매개변수 리스트, 딕셔너리를 사용할 경우, return할 필요가 없음.

# 함수선언
def func1(a, a_list):
    a = 100
    a_list[0] = 100 # 지역변수
    return a

a=10
a_list = [1,2,3]
# 함수호출
a = func1(a, a_list)   # 2개 이상의 데이터를 저장하는 변수. 주소값을 저장함.


# 데이터 출력
print(a)
print(a_list)









# def func1():
#     global a  # 전역변수를 가져옴
#     a = 100
#     print('fun1 a= ',a)
#     # 지역변수 값을 전역변수에 적용시키는 방법
#     # 코드를 추가하시오.
#     return a

    
# def func2():
#     print('fun2 b =', a+10)
    
# # 전역변수
# a = 20

# a = func1()
# func2()
# print(a)

# def cal(v1,sum):
#     sum = sum+500
#     v1 = v1 + 200        # 지역변수
#     return v1, sum

# sum = 10
# v1 = 1          # 전역변수
# v1, sum = cal(v1,sum)
# print(v1)
# print(sum)
