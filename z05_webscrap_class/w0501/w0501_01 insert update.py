import oracledb

# sql devoloper
conn = oracledb.connect(user = "ora_user1",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()  # db와 연결되어 지시자 생성

# 이름 2번째 a가 있는 학생을 출력하시오. 학번으로 순차정렬


# insert 저장하기
# sql = "insert into member values(member_sqe.nextval, 'eee',1111,'김구','남자',sysdate)"
# cursor.execute(sql)
# cursor.execute('commmit')

# update 수정하기
# sql = "update member set name='홍길동' where id = 'aaa'"
# cursor.execute(sql)
# cursor.execute('commmit')

# select 읽어오기
sql = "select * from member"
cursor.execute(sql)         # cursor에 select한 결과값을 저장 (경과값 : list)
data = cursor.fetchall()    # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터를 가져옴.

print("모든 데이터 출력")
for d in data:
    print(d)
    

conn.close()