# 키워드 매개변수. 키워드 매개변수는 제일 뒤에 와야 함.
def cal(a=10,b=10):
    a = a+10
    b = b+20
    result = a+b
    
    return result


num1 = 5
num2 = 7

result = cal()         # 42 

print('현재 숫자 :',num1,num2,result)