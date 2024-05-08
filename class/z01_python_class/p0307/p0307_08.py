import random

fruit = {'peach':'복숭아', 'orange':'오렌지', 'apple':'사과',
         'pear':'배', 'grapes':'포도', 'mango':'망고','kiwi':'키위'}

f_list = list(fruit.keys())   # 키 값 집어 넣기 리스트화
print(f_list)

f_list_ran = random.sample(f_list,4)  # 랜덤리스트 안에 랜덤으로 4개 넣기

print('랜덤추출 : ',end = ' : ')
for f in f_list_ran:                    # for 문을 돌려서 랜덤리스트를 추출하기
    print(fruit[f],end = ' ')
    

