import oracledb

conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

# 평균점수를 입력받아 입력받아 입력한 평균점수 이상의 학생을 출력하시오.
# 반복해서 진행. -1 입력 시 종료

while True:
    a_search = int(input('검색할 평균점수를 입력해주세요(이상) >> '))
    if a_search == -1: break
    b_search = int(input('선택하신 점수의 이상이하를 선택하세요 (1.이상, 2.미만) >> '))
    if b_search == 1:
        sql = f"select * from stu_score where avg>={a_search} order by avg"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d)
    elif b_search == 2:
        sql = f"select * from stu_score where avg<{a_search} order by avg"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d)
    print('검색된 학생 수 :',len(data))    
        
conn.close()