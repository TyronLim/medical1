# import datetime   >  날짜 관련 기능을 가져옴.

import datetime

now = datetime.datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)


# if hour >= 12 : 
#     print('지금은 {}시로, 오후입니다.'.format(hour))
# else :
#     print('지금은 오전입니다.')

# if min%2==0 :
#     print('지금은 %d분이므로 짝수분 입니다.'%min)
# else :
#     print('지금은 %d분이므로 홀수분 입니다.'%min)
    
# if sec%2==0 :
#     print('지금은 {}초이므로 짝수초입니다.'.format(sec))
# else:
#     print('지금은 {}초이므로 홀수초입니다.'.format(sec))


year = now.year
mon = now.month
day = now.day
hour = now. hour
min = now.minute
sec = now.second


# if mon==12 or mon==1 or mon==2 :
#     print('아직 겨울이네요.')
    
# else:
#     print('아직은 봄이 아니에요.')

# if 3 < mon < 11 :
#     print('아직 겨울 아닙니다.')
# else :
#     print('아직 겨울입니다.')
    
# if 24>24-hour>0 and 60>60-min>0 :
#     print('{}시간 {}분이 지나면 다음날이 됩니다.'.format(24-hour-1,60-min)) 
# else :
#     print('{}시간이 지나면 다음날이 됩니다.'.format(24-hour))



# n = int(input('다음날까지 몇시간 몇분 남았는지 알고 싶으면 숫자 1을 입력하세요 : '))
# remt = 13-hour
# remm = 60-min

# if n==1:
#     print('{}시간 {}분이 지나면 다음날이 됩니다.'.format(int(remt),int(remm)))
# else :
#     print('1을 정확히 입력하세요.')



