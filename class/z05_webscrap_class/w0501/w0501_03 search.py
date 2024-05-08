import oracledb

# 데이터 베이스 연결 함수
def connection():
    conn = oracledb.connect(user = "ora_user1",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor()  # db와 연결되어 지시자 생성
    return cursor, conn

def close(conn):
    conn.close()

# employees 이름으로 검색하는 로직 구현하시오.
while True:
    print('1. 이름으로 검색')
    print('2. 이름으로 같은 부서에서 글무하는 사원 조회')
    choice = input('원하는 번호를 입력하세요 >> ')
    if choice == '-1':
        print('검색을 종료합니다.')
        break
    elif choice == '1':
        search = input('검색어를 입력하세요 >> ')
        cursor,conn = connection()
        sql = f"select * from employees where emp_name like '%{search}%'"
        cursor.execute(sql)
        data = cursor.fetchall()

        print('검색 결과')
        print('-'*50)
        for d in data:
            print(d[0],end='\t')
            print(d[1],end='\t')
            print(d[4],end='\t')
            print(d[5],end='\t')
            print(d[6],end='\t')
            print(d[9],end='\t')
            print()
    elif choice == '2':
        cursor,conn = connection()
        search = input('정확한 이름을 입력하세요 >> ')
        sql = f"select b.employee_id,a.department_id, c.department_name,b.emp_name from employees a, employees b, departments c where a.department_id=b.department_id and a.emp_name = '{search}' and a.department_id = c.department_id"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        print('검색 결과')
        print('-'*50)
        for d in data:
            print(d[0], end='\t')
            print(d[1], end='\t')
            print(d[2], end='\t')
            print(d[3])

close(conn)