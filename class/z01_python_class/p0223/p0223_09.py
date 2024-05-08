import datetime
now = datetime.datetime.now()
print(now)

month = now.month

if month > 11:
    print ('겨울')
elif month > 8 :
    print ('가을')
elif month > 5 :
    print ('여름')
elif month > 2 :
    print ('봄')
else :
    print ('겨울')
    

if 3<=month<=5:
    print ('봄')
elif 6<=month<=8:
    print ('여름')
elif 9<=month<=11:
    print('가을')
else :
    print('겨울') 