# medical1 폴더안 member.csv
# medical1>h0327>aaa 폴더안 medical1>h0327>aaa/member2.csv
# 절대경로 : c:/workspace/medical1>h0327>aaa/member2.csv

with open('h0327/aaa/member2.csv','r',encoding='utf8') as f:
    while True:
        txt = f.readline()
        if txt=='': break
        s_list = txt.strip().split(',')

        print(s_list[1],s_list[2])

for i in s_list:
    print(i)