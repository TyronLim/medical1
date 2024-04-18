# stu.txt 파일을 읽어 출력하시오.

# f = open('stu.txt','r',encoding='utf8')
students = []
with open('stu.txt','r',encoding='utf8') as f:

    while True:
        txt = f.readline().strip()
        if txt == '' : break
        t_list = txt.split(',')
        # print("{},{},{},{},{},{},{},{}".format(*t_list))
        s_dic = {'stuNo':int(t_list[0]),'name':t_list[1],'kor':int(t_list[2]),
            'eng':int(t_list[3]),'math':int(t_list[4]),'total':int(t_list[5]),
            'avg':float(t_list[6]),'rank':int(t_list[7])}
        # s_dic['stuNo'] = t_list[0]
        # s_dic['name'] = t_list[1]
        # s_dic['kor'] = t_list[2]
        # s_dic['eng'] = t_list[3]
        # s_dic['math'] = t_list[4]
        # s_dic['total'] = t_list[5]
        # s_dic['avg'] = t_list[6]
        students.append(s_dic)
        
print(students)        

# f.close()