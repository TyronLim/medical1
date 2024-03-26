with open('student.txt','w',encoding='utf8') as f:
    for i in range(3):
        a = input()
        f.write(f'{a}\n')