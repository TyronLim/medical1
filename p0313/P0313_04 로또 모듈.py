# 다른 파일에 있는 함수를 사용할 때의 방법
# from lotto import num_generate
# import math                           >> math.floor()
import math as m    #   > 모듈명을 줄여서 사용가능. 별칭 부여
# from math import *    (ceil,floor)    >> 이름()
# while True:
#     lotto.screen()

import lotto as lo   # lotto를 lo로 사용 가능. lo.screen() 등등




# l = [i for i in range(1,46)]
# num_generate(l)




# # ceil 올림
# print(math.ceil(12.2))

# # floor 내림
# print(math.floor(12.9))

# # round 반올림
# print(round(12.6))

print(dir(m))