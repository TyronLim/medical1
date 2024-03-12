# 점수를 입력받아서 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 나머지는 F를 출력해보세요.

# num = int(input('점수를 입력하세요 : '))

# if num >= 90 :
#     print('A')
# elif num >=80 :
#     print('B')
# elif num >=70 :
#     print('C')    
# else :
#     print('F')
    
    
#90점이상 시작
# if num >= 90 :
#     if num >= 98:
#         print('A+')
#     elif num >93 :
#         print('A')
#     else :
#         print('A-') 
# elif num >=80 :
#     if num >= 88 :
#         print('B')
#     elif num > 83 :
#         print('B+')
#     else :
#         print('B-')
# elif num >= 70:
#     if num >= 78:
#         print('C+')
#     elif num > 83 :
#         print('C')
#     else :
#         print('C-')
# else :
#     print('F')

a = 90  #점수

if a > 0:
    print('귀하의 점수는')
    if a >= 90 :
        print('90점 이상이므로 A이며, 귀하의 상세점수는')
        if a>97:
            print('A+')
        elif a> 93:
            print('A')
        else :
            print('A-')
    elif a >= 80:
        print('80점 이상이므로 B이며, 귀하의 상세점수는') 
        if a > 97:
            print('B+')
        elif a > 83:
            print('B')
        else :
            print('B-')
        print('입니다.')
    else :
        print ('F')
    print('입니다.')
else :
    print ('점수를 다시 입력하세요.')