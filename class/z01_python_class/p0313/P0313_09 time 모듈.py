import time
import random
#time.sleep()   >> 초마다 출력

for i in range(1,101):
    if i%10 == 0:
        num = random.randint(1,5)
        print(num,'초 대기')
        time.sleep(num)
        print(i)
        
        
