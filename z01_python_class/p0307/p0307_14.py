list =[1,2,3]
alist = [*list] # 깊은 복사 1번 방법
alist = list[:] # 깊은 복사 2번 방법

list[0] = 100

print(alist)

a = 100
b = a
a = 10
print(b)


