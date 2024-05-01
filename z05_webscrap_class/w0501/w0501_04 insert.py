import oracledb
conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

while True:
    id = input('아이디를 입력하세요 (-1.종료)>> ')
    if id == '-1': break
    
    # id를 가지고 검색을 먼저 한 후 데이터 입력하도록 유도
    sql = f"select id from member where id = '{id}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    # print(data)
    # print(len(data))
    if len(data) != 0:
        print('아이디가 이미 있습니다. 다른 아이디를 입력하세요')
        continue
    
    else:
        pw = input('패스워드를 입력하세요 >> ')
        name = input('이름을 입력하세요 >> ')
        gender = input('성별을 입력하세요 >> ')

        # db연결 해제
        sql = f"insert into member values(member_sqe.nextval,'{id}',{pw},'{name}','{gender}',sysdate)"
        cursor.execute(sql)
        cursor.execute('commit')

        print('입력이 완료되었습니다!')
        print()
        cursor.execute('commmit')
        
    cursor.close()
    conn.close()