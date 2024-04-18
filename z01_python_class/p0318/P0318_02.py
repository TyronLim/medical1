# 함수의 차를 1대 생산

class Car:
    name = ''
    color = ''
    door = 0
    length = 0
    width = 0
    speed = 0
    
    def up_speed(self,s):
        self.speed += s
        
    def down_speed(self,s):
        self.speed -= s

c1 = Car()
c1.name = '드뉴아반떼'
c1.color = 'white'
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60)     # 현재 스피드에서 60을 더해줌
c1.up_speed(40)
c1.speed = 50

print(c1.speed)


# print('차 성능 :',color,door,length,width,speed)

# 영희의 차를 1대 생산해서, 색상은  green, 나머지 동일, speed = 100으로 설정해서 출력하세요.

yh_car = Car()
yh_car.color = 'green'
yh_car.door = 5
yh_car.length = 2000
yh_car.width = 1000
yh_car.speed = 100 

    
# 남궁종철 - 디올뉴그랜저, 화이트펄, speed = 150

ng_car = Car()
ng_car.name = '디올뉴그랜저'
ng_car.color = 'white pearl'
ng_car.door = 5
ng_car.length = 2000
ng_car.width = 1000
ng_car.speed = 150

print('영희의 차 성능 :',yh_car.name,yh_car.color,yh_car.door,yh_car.length,yh_car.width,yh_car.speed)
print('남궁종철의 차 성능 :',ng_car.name,ng_car.color,ng_car.door,ng_car.length,ng_car.width,ng_car.speed)
