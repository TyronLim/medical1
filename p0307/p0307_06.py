import random

# random.random()
print(random.random()) # 0-1 사이의 랜덤한 float 출력
print(random.randint(0, 44)) # 0-44까지 랜덤한 int 출력
print(random.randrange(0,3)) # 0-2까지 랜덤한 int 출력

# 리스트를 랜덤으로 섞기
list = [1,2,3,4,5,6,7]
print(list)
random.shuffle(list)
print(list)

# 리스트에서 1개를 랜덤으로 추출
print(random.choice(list))

# 리스트에서 해당되는 개수만큼 랜덤으로 추출 (중복이 안 되게)
print(random.sample(list,3))

w_list = ['토마토','바나나','사과','배','수박','메론','복숭아']

fruit = {'peach':'복숭아', 'orange':'오렌지', 'apple':'사과',
         'pear':'배', 'grapes':'포도', 'mango':'망고','kiwi':'키위'}

print(random.sample(w_list,3))


