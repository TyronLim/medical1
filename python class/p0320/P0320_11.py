def jegob(val):
    return val**2

def func(val):
    return val>=3

# def int_change(val):
#     return int(val)

a_list = [1,2,3,4,5]
str_list = ['1','2','3','4','5']

map_list = map(jegob,a_list)
print(list(map_list))

f_list = filter(func,a_list)
print(list(f_list))

# ss_list = map(int_change,str_list)
# print(list(ss_list))

ss_list2 = map(lambda val:int(val),str_list)
print(list(ss_list2))