print("Hello Python")

print("Hello! " * 3)
print("혼자 공부하다 모르면 동영상 강의를 참고하세요!")

print (5>10)

import math
print (math.pi > 1)

print(False)
print('true')

print (not False)
print (not True)

print (not (5>10))

print ("%d +%d =%d" %(800, 3, 3))

print ("%d < %d" %(5,3))

print ("%10d"%12321) #10자리 수
print ("%010d"%12321) #10자리 수이지만 앞에 0으로 채움

# %d 는 정수
# %f 는 실수

print ("%f" %3.14)
print ("%7.1f"%3.144) #소수점 포함해서 7자리로 출력 & 뒤에는 1자리만
print ("%07.3f" %12.12) #소수점 포함해서 0으로 채움 & 뒤에는 3자리까지
print ("%.1f"%22.1) # .1 안 붙이면 뒤에 파이썬이 000을 넣음 (반올림 함)

# %s 는 문자

print ("%s" %"안녕")
print ("%3s" %"안녕")

# %c는 문자 하나. 한 글자라서 잘 사용은 안 함. s 로 대체 가능

print ("%.2f"%758.12345678)
print ("%010.2f" %25.05)
print ("%d, %f, %s"   %(150.15, 150.15, "150.15"))
print ("*"*10)

print ("%d, %010.2f, %s" %(150.1,150.1,"150.1"))

print("%d"%10+"%d"%12)

