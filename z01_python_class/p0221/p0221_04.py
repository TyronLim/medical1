
print("안녕하세요?")
print("저는 타이론입니다")

# 하를 하셨으로, 타이론을 티롱으로 바꾸고 싶을 때

print("안녕하셨세요?")
print("저는 티롱입니다")

print("안녕","하셨","세요?")
print("저는", "타이론", "입니다")

insa = "하셨"
nickname = "티롱"
print("안녕",insa,"세요?")
print("저는", nickname, "입니다")

#변수 입력 후 hello world 치기
str1 = "hello"
print(str1)
var1 = 2
str2 = "world"
print(str1,' ', str2)

var4 =100
var3 = var4 #현재 var3도 100이 됨
var2 = var3 #현재 var2도 100이 됨
var1 = var2 
print(var1)
print("var1 :", var1)

var4 = 200

print(var4) # var4의 값을 지금 바꾸더라도 위로 올라가지 않고 현 시점에만. 지금 var1 = 100

fruit1 = "포도"
fruit2 = "딸기"
fruit3 = "수박"

print("나는", fruit1 + "를 좋아합니다.")
print("나는", fruit2 + "를 좋아합니다.")
print("나는", fruit3 + "를 좋아합니다.")

fruit1 = "수박"

print("나는", fruit1 + "를 좋아합니다.")
print("나는", fruit2 + "를 좋아합니다.")
print("나는", fruit3 + "를 좋아합니다.")

fruit2 = fruit1
fruit3 = fruit2     # = 앞에 오는 걸 중심으로 정의함. (fruit1=fruit2 와 fruit2=fruit1은 다름)
print("나는", fruit1 + "를 좋아합니다.")
print("나는", fruit2 + "를 좋아합니다.")
print("나는", fruit3 + "를 좋아합니다.")

city = "서울시"

print("나는", city + "에 살고 있습니다.")

animal = "판다"
print("나는 "+ animal+"를 좋아합니다.")

print("나는", fruit1,"를 좋아한다")