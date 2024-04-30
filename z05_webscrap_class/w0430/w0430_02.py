import oracledb

# sql devoloper
conn = oracledb.connect(user = "ora_user1",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()  # db와 연결되어 지시자 생성

# board id 포함 모든 컬럼, mamber테이블의 name컬럼 포함해서 데이터를 가져오기
# board 테이블 id, member테이블 name
# board테이블 모든 컬럼, member 테이블의 name 컬럽을 가져와 출력하시오.
# sql = "select board.*, member.name from board,member where board.bno = member.memno"

# stu_score에서 avg가 90점 이상 A, 80점 이상 B, .... 60점 미만 F
# sql = "select no,name,total avg,case when avg>=90 then 'A' when avg>=80 then 'B' when avg >=70 then 'C' when avg>=60 then 'D' else 'F' end from stu_score"
# 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오.
# 학번,이름,합계,평균,학점
sql = "select * from stu_score order by no"
cursor.execute(sql)         # cursor에 select한 결과값을 저장 (경과값 : list)
data = cursor.fetchall()    # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터를 가져옴.

# print("모든 데이터 출력")

# print('번호\t이름\t총점\t평균\t등급')
# print('-'*50)
# for i in data[:5]:
#     if i[6] >=90:
#         print('{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[5],i[6],'A'))
#     elif i[6] >=80:
#         print('{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[5],i[6],'B'))
#     elif i[6] >=70:
#         print('{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[5],i[6],'C'))
#     elif i[6] >=60:
#         print('{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[5],i[6],'D'))
#     else:
#         print('{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[5],i[6],'F'))

# print(data)


# for d in data:
#     print(d)
    
    # print('학번 :',d[0])
    # print('이름 :',d[1])
    # print('kor :',d[2])
    # print('eng :',d[3])
    # print('math :',d[4])
    # print('total :',d[5])
# print('-'*50)
# print("타입 :",type(data))

sql = "select round(avg(salary),2) from employees"
cursor.execute(sql)
data = cursor.fetchone()
print(data[0])









conn.close()        # 데이터베이스 연결 해제



