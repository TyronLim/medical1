import requests
import oracledb
import math

conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor() # 실행 명령어를 입력받겠다. sql 창을 여는 것.(접속)

num = 1 # 최초 페이지
perCount = 10   #몇 개씩?
startrow = (num-1)*perCount+1
endrow = startrow + perCount-1
        
search = input('찾고자 하는 학생 이름을 입력하세요. >>> ')
sql = f"select count(*) from (select row_number() over(order by no) rnum, a.* from stu_score a \
        where id like '%{search}%')"
cursor.execute(sql)
all_count = cursor.fetchone()

while True:    
    startrow = (num-1)*perCount+1
    endrow = startrow + perCount-1
        
    sql = f"select * from (select row_number() over(order by no) rnum, a.* from stu_score a \
            where id like '%{search}%') where rnum>={startrow} and rnum<={endrow}"
    cursor.execute(sql)
    data = cursor.fetchall()

    ## 개씩 나눠서 보여주도록 구성
    print('[학생 검색 데이터]')
    for d in data:
        print(d)
    print('-'*50)
    print('검색된 페이지 :',num)
    print('검색된 데이터 수 :',all_count[0])
    
    print('1. < 이전')
    print('2. 다음 >')
    print('3. 검색 중지')
    no = input('원하는 번호를 입력하세요.')
    
    if no == '1':
        num -= 1
        
    elif no == '2':
        num += 1
        
    else : break        
    
    if num==0:
        print('<<<<<<< 첫 페이지 입니다 >>>>>>')
        num=1
        continue
        
    if num > math.ceil((all_count[0])/perCount):
        print('<<<<<<< 마지막 페이지입니다 >>>>>>>')
        num = math.ceil((all_count[0])/perCount)
        continue
    
cursor.close()
conn.close()






