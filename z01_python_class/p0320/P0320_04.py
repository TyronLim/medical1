class Student:
    def __init__(self,name,total):
        self.name = name
        self.total = total

    def __str__(self):
        return f'{self.name},{self.total}'

    def __del__(self):
        return '클래스가 소멸될 때 실행'
    
    def __add__(self,s):
        return self.total + s.total
    
    def __gt__(self,s):         # 크거나 같다고 비교할 때  (순수 클래스는 비교 불가. 함수가 있어야 함)
        return self.total > s.total
    
    # def __eq__(self,s):
    #     return self.total == s.total and self.name == s.name
    
    
    
s1 = Student('홍길동',100)        
s2 = Student('유관순',90)        
s3 = Student('이순신',95)
s4 = Student('홍길동',100)

print(s1)          # 클래스를 출력할 때, str함수 호출
print(s1+s2)       # 클래스를 더하기 할 때, add함수 호출
print(s3<s2)
print(s1==s2)


# a = [1,20,2,45]
# b = [1,30,2,45]
# print(a<b)