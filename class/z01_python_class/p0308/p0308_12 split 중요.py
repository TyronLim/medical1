# split() # 문자열 분리

hobby = '게임,골프,독서'
print(hobby.split(',')) # 리스트 타입으로 분리하고 싶을 때 사용  

h_data = '2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합'
print(h_data.split(','))
h_list =h_data.split(',')

print('병상수 :',h_list[4])

a_data = '2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합'
a_list = a_data.split('/')
print('병상수 :',a_list[4])

ss = '%'
print(ss.join('파이썬'))   # ss를 파이썬 사이에 넣어 출력

s_date = '2023/03/08'
s_date_list = s_date.split('/')
print(s_date_list)

s_time = '2024:03:08:16:48:00'
s_time_list = s_time.split(':')
print(s_time_list)

today = '2024/03/08'
# 10년 후의 날짜를 출력하시오. 2034/03/08
today_list = today.split('/')
today_list[0] = int(today_list[0]) + 10
print(today_list)
# future = '{}/{}/{}'.format(today_list[0],today_list[1],today_list[2])
future = '{}/{}/{}'.format(*today_list)                                   # 나열 리스트
print(future)






