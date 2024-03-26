
hight = int(input('키를 입력하세요.'))
age = int(input('나이를 입력하세요.'))

# 1
if hight >=130 :
    print('키가 130cm 이상이므로 놀이기구에 탑승이 가능합니다.')
else :
    print('키가 130cm 미만이므로 놀이기구에 탑승할 수 없습니다.')

# 2 
if age >=10 and hight >= 130 :
    print('키와 나이 조건이 되므로 놀이기구에 탑승할 수 있습니다.')
else :
    print('키 또나 나이가 안 되어서 탑승불가합니다.')
    
# 3
weather = input('오늘의 날씨를 입력하세요. :')
if weather == '비':
    print('우산을 챙겨주세요.')
else :
    print('선크림을 발라주세요.')
    
# 4
if weather == '비' or weather == '눈' :
    print('우산을 챙겨주세요.')
else :
    print('선크림을 발라주세요.')

# 5 not 사용
if not weather == '비':
    print('우산을 챙겨주세요')
else :
    print('선크림을 발라주세요.')
