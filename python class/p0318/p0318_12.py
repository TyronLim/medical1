# Car 클래스를 선언
# carCount 클래스 변수를 이용해서 숫자를 증가시켜 보세요.
# carNo, color= 'white', door=5, tire=4, speed 
# up_speed 함수를 호출하면 10씩 증가될 수 있게끔
# down_speed 함수를 호출하면 10씩 감소되게끔

# c1 - white, 5, 4, 0 > speed : 30
# c2 - red, 5, 4, 0 > speed : 100
# c3 - silver, 5, 4, 0 > speed : 70
# car_list 추가하고

# car_list에 있는 모든 객체의 모든 color,door,tire,speed를 모두 출력하시오.

car_list = []

class Car:
    carCount = 0
    color = 'white'
    door = 5
    tire = 4
    speed = 0
    
    def up_speed(self):
        self.speed += 10
        
    def down_speed(self):
        self.speed += 10
        
    def __init__(self,carCount,color,door,tire,speed):
        Car.carCount +=1
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        
c1 = Car(0,'white',5,4,0) 
for i in range(3):
    c1.up_speed()
print(c1.carCount,c1.color,c1.door,c1.tire,c1.speed)
car_list.append([c1.carCount,c1.color,c1.door,c1.tire,c1.speed])

c2 = Car(0,'red',5,4,0)
for i in range(10):
    c2.up_speed()
print(c2.carCount,c2.color,c2.door,c2.tire,c2.speed)    
car_list.append([c2.carCount,c2.color,c2.door,c2.tire,c2.speed])
    
c3 = Car(0,'silver',5,4,0)
for i in range(8):
    c3.up_speed()
c3.speed -= 1
print(c3.carCount,c3.color,c3.door,c3.tire,c3.speed) 
car_list.append([c3.carCount,c3.color,c3.door,c3.tire,c3.speed])      #2차 리스트

# car_list.append(c1)
# car_list.append(c2)
# car_list.append(c3)
# car_list = [c1,c2,c3]

# for i in range(len(car_list)):
#     print(car_list[i].carCount, car_list[i].color, car_list[i].door, car_list[i].tire, car_list[i].speed)

for i in car_list:
    # print(i)
    for j in i:
        print(j,end = ' ')
    print()
    