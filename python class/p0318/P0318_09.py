class lotto:
    number = 0
    shape = 'circle'
    
    def __init__(self,number):
        self.number = number
        
# lotto에 1-45까지의 숫자를 입력한 리스트를 생성한 후 출력하시오.
l_list = []



for i in range(45):
    l_list.append(lotto(i+1))
    
print(len(l_list))

for i in range(45):
    print(l_list[i].shape,l_list[i].number)


    
        
        