# class 상속

class Car:  
    count = 0
    
    def __init__(self,color = 'white',door = 5,tire = 4,speed = 0):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
    
    def up_speed(self):
        self.speed += 10
        
    def down_speed(self):
        self.speed -= 10
    
    def stop_speed(self):
        self.speed = 0
        
    
class Ambul_car(Car):   # Car 클래스 상속
    # Car클래스의 모든 것을 가져옴
    def up_speed(self):
        self.speed += 30                ##### 자식클래스 오버라이딩
        
    def up_speed2(self):
        return super().up_speed()                ##### 부모의 함수 오버라이딩 (super() 사용)
        
    color = 'red'
    def siren(self):
        print('사이렌 기능이 추가되었습니다.')

class FireTruck_car(Car):   # Car 클래스 상속
    # Car클래스의 모든 것을 가져옴
        
    def water(self):
        print('물을 뿌리는 기능이 추가되었습니다.')
        


c1 = Ambul_car()
c1.up_speed()       # 자식의 오버라이딩 함수가 적용되어 호출
c1.up_speed2()      # 부모의 오버라이딩 함수가 적용되어 호출 (클래스 내부에 super 사용)
c1.color = 'red'
print(c1.speed)
