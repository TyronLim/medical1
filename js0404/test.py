
season = input('몇월입니까? 월까지 입력하세요 >> ')
season = int(season[0:-1])
print(season)
if 3<=season<=5:
    print('봄')
elif 6<=season<=8:
    print('여름')
elif 9<=season<=11:
    print('가을')
elif 12==season or 1<=season<=2:
    print('겨울')
else:
    print('계절이 아닙니다.')
    


