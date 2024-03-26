# 파일 열기, 저장 함수 - jason 

students = []

with open('stu.txt','r',encoding='utf8') as f:
    while True:
        stu = f.readline().strip()
        if stu == '' : break
        stu_list = stu.split(',')
        print(stu_list)
        student={'stuNo':int(stu_list[0]),'name':stu_list[1],'kor':int(stu_list[2]),'eng':int(stu_list[3]),
                 'math':int(stu_list[4]),'total':int(stu_list[5]),'avg':float(stu_list[6]),'rank':int(stu_list[7])}
        students.append(student)

print(students)


