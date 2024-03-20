class Car:
    count = 0       # 클래스별수 인식
    
    def __init__(self,color='black',speed=20):
        self.color = color          # init 안에 인스턴스 변수 선언
        self.speed = speed          # init 안에 인스턴스 변수 선언     
        # Car.count = 0  
        
    def up_speed(self):
        self.speed += 100
                
# class 사용을 위해서는 인스턴스 선언

c1 = Car('white',20)      # 인스턴스 선언
c1.count = 10
c1.up_speed()
print(c1.color,c1.speed)
c1.count

c2 = Car()
c2.color = 'red'
print('----')
print(c1.color)
print(c2.color)


print('----')
c2.count = 10           # 기존 클래스를 지우고 인스턴스를 다시 생성함
Car.count = 100
print(c1.count, c2.count)
c2.door = 4

print(c2)
