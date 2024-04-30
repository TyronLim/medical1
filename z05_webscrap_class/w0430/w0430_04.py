import oracledb

conn = oracledb.connect(user="ora_user1",password="1111",dsn="localhost:1521/xe")

cursor = conn.cursor()

while True:
    search = input('찾고자 하는 이름을 입력하세요 >> ')
    if search == '-1': break
    # sql = "select * from stu_score"
    sql = f"select * from stu_score where name like '%{search}%' order by no"
    data = cursor.execute(sql)
    data = cursor.fetchall()
    for d in data:
        print(d)

    # for d in data:
    #     if search in d[1]:
    #         print(d)
        print('종료')
        
conn.close()