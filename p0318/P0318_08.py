
# 클래스 5개를 생성해서 kind = 'spade', number = 1,2,3,4,5
# 클래스를 출력하시오.

class Card():
    
    def __init__(self,number):
        Card.kind = 'spade'
        self.number = number

    def print(self):
        print(Card.kind,self.number)

card_list = []

for i in range(13):
    card_list.append(Card(i+1))
# card_list.append(Card('A'))    
# card_list.append(Card('2'))    
# card_list.append(Card('3'))    
# card_list.append(Card('4'))    
# card_list.append(Card('5'))    
# card_list.append(Card('6'))    
# card_list.append(Card('7'))    
# card_list.append(Card('8'))    
# card_list.append(Card('9'))    
# card_list.append(Card('10'))    
# card_list.append(Card('J'))    
# card_list.append(Card('Q'))    
# card_list.append(Card('K'))    


print('리스트 개수 : ',len(card_list))
for i in range(13):
    print('리스트 출력 : ',card_list[i].kind,card_list[i].number)


    
    
    
    
    

# class Card: ## 4개의 변수 : kind, number, width, height
#     width = 100     # 클래스 변수
#     height = 200    # 클래스 변수

#     def __init__(self,kind,number):
#         self.kind = kind
#         self.number = number
#         Card.width = 100
#         Card.height = 200
    
        
# 52장 카드 생성
# shape = ['SPADE','DIAMOND','HEART','CLOVER']
# number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# card_list = []



# for i in range(4):
#     for j in range(13):
#         c = Card(shape[i],number[j])
#         card_list.append(c)

# print (card_list)

# for i in range(52):
#     c = card_list[i]    # c = card 객체
#     print('카드출력 : ',c.kind,c.number)





    