class Car:
    name = ''
    color = ''
    door = 0
    length = 0
    width = 0
    speed = 0
    
    # 생성자
    def __init__(self,name,color,door,length,width,speed):
        self.name = name
        self.color = color
        self.door = door
        self.length = length
        self.width = width
        self.speed = speed
    
    def up_speed(self,s):
        self.speed += s
        
    def down_speed(self,s):
        self.speed -= s

# 기본 생성자를 사용한 객체=instance선언
c4 = Car()
c4.name = '드뉴아반떼'
c4.color = 'white'
c4.door = 5
c4.length = 2000
c4.width = 1000
c4.up_speed(60)     # 현재 스피드에서 60을 더해줌
c4.up_speed(40)
c4.speed = 50


# 생성자를 사용한 객체=instance선언
c1 = Car('드뉴아반떼','white',5,2000,1000,60)
print('철수의 차 성능 :',c1.name,c1.color,c1.door,c1.length,c1.width,c1.speed)

c2 = Car('드뉴아반떼','green',5,2000,1000,100)
print('영희의 차 성능 :',c2.name,c2.color,c2.door,c2.length,c2.width,c2.speed)

c3 = Car('디올뉴그랜저','white pearl',5,2500,1400,150)
print('반장의 차 성능 :',c3.name,c3.color,c3.door,c3.length,c3.width,c3.speed)




# c1 = Car()
# c1.name = '드뉴아반떼'
# c1.color = 'white'
# c1.door = 5
# c1.length = 2000
# c1.width = 1000
# c1.up_speed(60)     # 현재 스피드에서 60을 더해줌
# c1.up_speed(40)
# c1.speed = 50



# # print('차 성능 :',color,door,length,width,speed)

# # 영희의 차를 1대 생산해서, 색상은  green, 나머지 동일, speed = 100으로 설정해서 출력하세요.

# yh_car = Car()
# yh_car.color = 'green'
# yh_car.door = 5
# yh_car.length = 2000
# yh_car.width = 1000
# yh_car.speed = 100 

    
# # 남궁종철 - 디올뉴그랜저, 화이트펄, speed = 150

# ng_car = Car()
# ng_car.name = '디올뉴그랜저'
# ng_car.color = 'white pearl'
# ng_car.door = 5
# ng_car.length = 2000
# ng_car.width = 1000
# ng_car.speed = 150

# 
# print('남궁종철의 차 성능 :',ng_car.name,ng_car.color,ng_car.door,ng_car.length,ng_car.width,ng_car.speed)
