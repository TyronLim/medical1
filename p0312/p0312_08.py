# 자바 같은 경우 매개변수 개수에 따라 다른 함수 인정.
# 파이썬 이름이 무조건 달라야 함.

# def func(num1):
#     print(num1)
    
    
# def func1(num1,num2,num3):
#     print(num1,num2,num3)

    
# func(1)    
# func1(1,4,7)    # 매개변수 개수를 같이 해야 함 반드시!
    
def func2(num1=0,num2=10,num3=3):        # 키워드 매개변수 = 값이 들어오지 않으면 default의 값으로 설정
    print(num1,num2,num3)
    result = num1+num2+num3
    return result
    
result = func2()
print(result)

    