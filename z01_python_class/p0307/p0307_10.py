

words = [
        {},
        
        {'airplane' : '비행기', 'appel' : '사과', 'bakery' : '빵집',  
        'banana' : '바나나', 'bank' : '은행', 'bean' : '콩',  
        'bicycle' : '자전거', 'boat' : '보트',  'bowl' : '그릇', 'bus' : '버스'},
        
        {'bake':'굽다', 'blow':'불다', 'check':'확인하다',
        'chew':'씹다', 'close':'닫다', 'dance':'춤추다',
        'walk':'걷다', 'work':'일하다', 'drink':'마시다', 'eat':'먹다'},
        
        {"agile":"민첩한", "ambitious":"야망있는", "awkward":"서투른",
        "bountiful":"너그러운", "clumsy":"어설픈", "courteous":"공손한",
        "exrovert":"외향적인", "genial":"상냥한", "introvert":"내향적인", "picky":"까다로운"}
        ]
import random

choice = 1
print(words[choice].keys())
list_w = list(words[choice].keys())
list_w_random = random.sample(list_w,5) 

print(list_w)
print(list_w_random)

for i in list_w_random:
    print(i)
    print(words[1][i])