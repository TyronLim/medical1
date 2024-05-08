#중첩 if 

# a = 97
# if a > 90:
#     print('90보다 큽니다.')
# else :
#     print('90보다 작습니다.')
    
# a = 93
# if a > 90:
#     print('90보다 큽니다.')
#     if a <95:
#         print('95보다 작습니다.')
#     else :
#         print('95보다 큽니다.')
# else :
#     print('90보다 작습니다.')
    
# 사과
# apple = 'bad'
# price = 1300

# if apple == 'good' :
#     print ('사과를 구매합니다.')
#     if price <=1000 :
#         print('10개 구매')
#     else :
#         print('3개 구매')
# else :
#     print('사과를 구매하지 않습니다.')
    
    
num = int(input('숫자를 입력하세요 : '))

if num >100 :
    if num%2 ==0:
        print('짝수')
    else :
        print('홀수')
else :
    print('100보다 작다')



