fruit = {'peach':'복숭아', 'orange':'오렌지', 'apple':'사과',
         'pear':'배', 'grapes':'포도', 'mango':'망고','kiwi':'키위'}

count = {'correct' : 0, 'wrong' : 0}
# 복숭아 영어로 입력해서 정답이면 정답, 오답이면 오답.
for f in fruit:             # f 는 키 값
    eng_in = input('{}를 영어로 입력하세요. >> '.format(fruit[f]))  # << fruit[f] 는 value 값
    print('입력한 단어는 : {}'.format(eng_in))
    if eng_in == f:
        print('정답입니다.')
        count['correct'] += 1
    else : 
        print('오답입니다. 정답은 {}입니다.'.format(f))
        count['wrong'] += 1
    
print('맞힌 개수는 {}, 틀린 개수는 {}입니다.'.format(count['correct'],count['wrong']))



