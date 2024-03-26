# 클래스 한 번 더
import random

# 클래스 선언 = 설계도
class Card:
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number

def random_one():
    num = random.randint(0,51)
    # print('랜덤 숫자 :',num, card_list[num].kind, card_list[num].number)
    return card_list[num]

kind_list = ['spade', 'diamond', 'heart', 'clover']
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]       

# 52장의 카드 생성
card_list = []
for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],num_list[j]))

# 52장의 카드 출력
# for i in range(len(card_list)):
    # print(card_list[i].kind,card_list[i].number)

# 카드 1장 뽑기

# random_one()

# 랜덤카드 5장을 뽑는데, 중복이 되지 않게 하시오.

# random.shuffle(card_list)
# for i in range(5):
#     print(card_list[i].kind, card_list[i].number)

# r_list = random.sample(card_list,5)
# for i in range(5):
#     print(card_list[i].kind, card_list[i].number)

# rand = []

# for i in range(5):
#     num = random_one()
#     rand.append(num)
    
# if rand[0] == rand[1] or rand[0] == rand[2] or rand[0] == rand[3] or rand[0] == rand[4]:
#     del rand[0]
#     rand.append(random_one())
    
# elif rand[1] == rand[2] or rand[1] == rand[3] or rand[1] == rand[4]:
#     del rand[1]
#     rand.append(random_one())

# elif rand[2] == rand[3] or rand[2] == rand[3]:
#     del rand[2]
#     rand.append(random_one())

# elif rand[3] == rand[4]:
#     del rand[3]
#     rand.append(random_one())
            
# for i in rand:
#     print(card_list[i].kind, card_list[i].number)

# temp_list = []

# cnt = 0
# while True:
#     if cnt == 5: break
#     c = random_one()
#     for i in temp_list:
#         if c.kind == i.kind and c.number == i.number:
#             continue
        
#     temp_list.append(c)
#     cnt += 1            

# for i in temp_list:
#     print(i.kind, i.number)
    
# 3. temp_list 저장장소를 1개 만들고, 랜덤뽑기 1장의 카드를 저장장소의 리스트와 비교
temp_list = []
cnt = 0
while True:
    if cnt == 5: break # 랜덤뽑기 카드가 5장일경우 종료
    c = random_one() # 랜덤카드 1장을 뽑기
    for i in temp_list:
        if c.kind == i.kind and c.number == i.number: # 같은 카드가 있으면 다음으로 진행
            continue
    # 중복카드가 없으면 추가
    temp_list.append(c)
    cnt += 1
for i in temp_list:
    print("랜덤1장 뽑기 카드 : ",i.kind,i.number)

