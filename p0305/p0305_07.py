aa = [[1,[3,4,5],2,3,4],[5,6],[7,8,9]]
aaa = [[[1,2],[3,4,5]],[[6],[7,8,9]]]
a = [1,2,3,4,5]
# for i in a:
#     print(i)

for i in aa:
    for j in i:
        if isinstance(j,list):
            for k in j:
                print(k)
        else :
            print(j)