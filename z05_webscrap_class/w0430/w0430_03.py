import oracledb

conn = oracledb.connect(user = "ora_user1",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()  # db와 연결되어 지시자 생성
# conn = oracledb.connect(user = "ora_user1",password="1111",dsn="lacalhost:1521/xe")

# employees 테이블에서 사번,이름,월급,실제월급(월급+월급*커미션),월급 *1410 원화로 환산해서
# 천단위 표시해서 출력하시오.
# sql = "select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),trim(to_char(salary*1410,'L999,999,999')) kor_salary from employees"
# 부서별 평균월급, 최대월급, 최소월급을 출력하시오.
# for d in data:
#     print(d[0],d[1],d[2],d[3],'￦'+d[4].replace('?',''))
sql = "select department_id,round(avg(salary),2),max(salary),min(salary) from employees group by department_id order by department_id"

cursor.execute(sql)
data = cursor.fetchall()

for d in data:
    print('부서번호\t평균월급\t최대월급\t최소월급')
    print('{}\t\t{}\t\t{}\t\t{}'.format(d[0],d[1],d[2],d[3]))
    print('-'*50)



conn.close()        # 데이터베이스 연결 해제



