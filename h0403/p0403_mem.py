
students=[]
count=len(students)+1

with open('student.txt','w',encoding='utf8') as f:

    while True:
        name=input('이름 >> ')
        if name == '0':
            break
        kor=int(input('국어 >> '))
        eng=int(input('영어 >> '))
        math=int(input('수학 >> '))
        total=kor+eng+math
        avg=float('{:.2f}'.format(total/3))
        text = f.write(count,name,kor,eng,math,total,avg,0)
        students.append(text,'\n')
        count += 1
