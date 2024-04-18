import random

def idpw():

    eng = 'abcdefghijklmnopqrstuvwxyz'
    pw = '1234567890'
    
    member = [['aaa','1111']]

    for i in range(10):
        a = random.choice(eng)
        b = random.choice(eng)
        c = random.choice(eng)
        d = random.choice(pw)
        e = random.choice(pw)
        f = random.choice(pw)
        g = random.choice(pw)
        member.append([a+b+c,d+e+f+g])
    return member
# print(member)






# eng = 'abcdefghijklmnopqrstuvwxyz'
# pw = '1234567890'
# list_id = []
# list_pw = []
# 랜덤함수를 사용하여 3자리 아이디를 10개 생성해서 list에 추가하시오

# for i in range(10):
#     a = random.sample(eng,3)
#     id = a[0]+a[1]+a[2]
#     list_id.append(id)
    
# print(list_id)


# for i in range(10):
#     b = random.choices(pw,k=5)
#     # print(b)
#     pw2 = ''.join(b)
#     # print(pw2)
#     list_pw.append(pw2)
# print(list_pw)

#-------------------------------------------------
# for i in range(10):
#     b = random.choices(pw,k=5)
#     # print(b)
#     pw2 = b.split(',')
#     # print(pw2)
#     list_pw.append(pw2)
# # print(list_pw)