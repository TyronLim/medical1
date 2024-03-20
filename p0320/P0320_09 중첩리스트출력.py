a_list = [
    1,2,3,4,[6,7,8,9],[10,11]
]

for i,j in enumerate(a_list):
    if type(j) != list:
        print(a_list[i])
    else:
        for k in j:
            print(k)
            
            
            

        