import oracledb

# sql devoloper
conn = oracledb.connect(user = "ora_user1",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()  # db와 연결되어 지시자 생성

# 이름 2번째 a가 있는 학생을 출력하시오. 학번으로 순차정렬
sql = "select * from stu_score where name like '_a%' order by no"
cursor.execute(sql)         # cursor에 select한 결과값을 저장 (경과값 : list)
data = cursor.fetchall()    # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터를 가져옴.

print("모든 데이터 출력")
for d in data:
    print(d[1])
    
    # print('학번 :',d[0])
    # print('이름 :',d[1])
    # print('kor :',d[2])
    # print('eng :',d[3])
    # print('math :',d[4])
    # print('total :',d[5])
    print('-'*50)
    print("타입 :",type(d))





