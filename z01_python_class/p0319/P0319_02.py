class Car:
        
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed    # 캡슐화. class 내부에서만 접근이 가능
        
    def up_speed(self,smartKey):
        if smartKey == '0x1100':
            self.__speed += 10
        else :
            print('스마트키가 다릅니다.')    
            
    def down_speed(self):
        self.__speed -= 10
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed = speed
    
# c1 = Car('white',5,4,0)
c2 = Car('red',4,4,0)

c2.set_speed(500)
c2.up_speed('0x1100')
c2.up_speed('0x1111')

print(c2.get_speed())
