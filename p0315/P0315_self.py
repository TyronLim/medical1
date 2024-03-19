# import random

# eng = 'abcdefghijklmnopqrstuvwxyz'
# pw = '1234567890'
# b = random.choices(pw,k=5)

# pw = ''.join(b)

# print(pw)

f = open('mem.txt','r',encoding='utf8')
m = f.readline()
mm = m.strip()
# mm = m.strip().split(',')
# while True:
    
#     # if c_id == member[0] and c_pw == member[1]:
#     #     success_flag = 1
#     if m == '': break
#     member = m.strip().split(',')
#     # if id == 
#     print(member)

print(m)

f.close()