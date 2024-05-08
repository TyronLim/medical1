# 클래스 : 사용자정의 변수 (함수도 포함)
# 클래스 : 설계도
class Car:      # 첫 글자가 대문자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    color = 'white'
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0    
    
    def upSpeed(self,sp):
        self.speed += sp
        
    def downSpeed(self,sp):
        self.speed -= sp


# 객체선언을 할 때마다 제품(Car)이 한 개씩 생산
c1 = Car()      # 클래스 객체선언 : Car 클래스에 있는 모든 변수를 사용함
c1.color = 'red'
print(c1.color)
c2 = Car()
print(c2.color)
c3 = Car()





