class Card:
    kind = ''
    number = ''
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number        
    
    def print(self):
        print(self.kind,self.number)

c_list = []
kind = ['spade','diamond','heart','clover']
number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
for i in range(4):
    for j in range(13):
        c = Card(kind[i],number[j])
        c_list.append(c)

for i in range(52):
    print(c_list[i].kind,c_list[i].number)



# # c1에 숫자를 5로 변경하시오.    
# c1 = Card('spade','1')      # 변경전
# c1.number = '5'      # 변경후
# c1.print()

# # c2 'heart','A'
# # 모양을 diamond 변경 후 출력하시오.
# c2 = Card('heart','A')      # 변경전
# c2.kind = 'diamond'    # 변경후
# c2.print()

# c_list = []
# kind = ['spade','diamond','heart','clover']
# number = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
# for i in kind:
#     for j in number:
#         c = [i,j]
#         c_list.append(c)
        
# print(c_list)
