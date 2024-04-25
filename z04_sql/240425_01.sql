-- 어제 오늘 내일
select sysdate-1, sysdate, sysdate+1 from dual;

select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;       --이 달의 첫 일, 마지막 일
select sysdate-hire_date from employees;                 -- 두 날짜간 (일수)!!!!!!!!!!!!!!!!!!!!!!!!!
select trunc(months_between(sysdate,hire_date),2) from employees; -- 두 날짜간 (달수)!!!!!!!!!!!!!!!!!!!!!!!!!

select trunc(kor,-1) ko, count(trunc(kor,-1)) from stu_score group by trunc(kor,-1) order by ko;    -- trunc 일단위 버림

-- hire_date에서 월만 출력하시오.
select to_char(hire_date,'mm') from employees;
select to_char(hire_date,'yyyy-mm-dd') from employees;

--hire_date 2008년도 출력, 년도별 인원수 출력
select * from employees;
select hire_date from employees where to_char(hire_date,'yyyy') = 2008;
select hire_date from employees group by to_char(hire_date,'yyyy'); ---------------------------------------------------------------

-- 형변환 number, character, date
-- number : 사칙연산 가능, 쉼표표시 안됨, 원화 표시 안됨
-- char : 사칙연산 안됨, 쉼표 표시 가능, 원화 표시 가능, || 가능
-- date : +,- 가능, 날짜 출력형태는 변경 불가.

-- 시퀀스, 날짜의 년도로 학번을 부여하기. (ko20240001)
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;

select to_char(to_number('123,456,789','999999999')+to_number('156,788','999999'),'999,999,999') from dual;


select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;

select to_char(salary,'999,999') salary from employees;

-- 숫자 타입을 날짜 타입으로
select 20240426 from dual;
select to_char(20240426)+3 from dual;   --문자 안에 숫자만 있으면 숫자로 계산해줌.
select to_date(20240426) from dual;

select emp_name, hire_date from employees where hire_date>to_date(20070101);    -- 숫자를 날짜로 변경
select hire_date, emp_name from employees order by hire_date;

-- 08월 이후 입사입, 사원이름 2번째에 a가 들어가 있는 사람 출력
select hire_date, emp_name from employees where to_number(to_char(hire_date,'mm'))=8 and emp_name like '_a%';

-- 20070101 이후 입사한 사원 이름 2번째에 a가 들어가 있는
select hire_date, emp_name from employees where hire_date>=to_date(20070101) and emp_name like '_a%' order by hire_date;

-- 1,5,8월 입사
select hire_date from employees where to_char(hire_date,'mm') in('01','05','08');

select emp_name from employees where emp_name like '_a%';

select emp_name, hire_date from employees where emp_name like '_a%' and to_char(hire_date,'mm') in('01','05','08') order by hire_date;

select sysdate+'20240401' from dual;
select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;
select * from m_date;
insert into m_date(m_no,m_yesterday,m_today,m_tomorrow) values(
seq_mno.nextval,'2024-04-01',sysdate,sysdate-to_date('2024-04-01')
);

create table eventDate(
eno number,
e_today date,
e_choice date,
e_period number
);
-- 입력 시 날짜 타입에 문자를 입력해도 저장됨
insert into eventDate values(seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01'));

select * from eventDate;

-- 문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- null을 0으로 치환 nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo
select manager_id from employees order by manager_id desc;

select nvl(to_char(manager_id),'CEO') from employees order by manager_id desc;

-- 그룹함수 count : null 값은 제외하고 카운트
select count(emp_name) from employees; 
select count(manager_id) from employees;    -- null is excluded
select count(*) from employees;     -- 전체 행 개수
select emp_name, manager_id from employees;

-- sum
select sum(salary) from employees;

-- avg
select avg(salary) avg_sal from employees;

-- min 
select min(salary) from employees;

-- max
select max(salary) from employees;

--higher than 6461(salary)
select emp_name, salary from employees where salary > (select avg(salary) from employees);

-- 그룹함수 : sum, avg, count, min, max

-- 최소 월급을 받는 사람의 사번, 이름
select employee_id,emp_name,salary from employees where salary=(select min(salary) from employees);
select min(salary) from employees;
select * from employees;

-- 최대월급
select employee_id, emp_name, salary from employees where salary = (select max(salary) from employees);

-- 50번인 사원만 전체 월급
select department_id, salary from employees where department_id = 50;

-- kor > 80
select no,name,kor from stu_score where kor > 80;

-- kor > kor_avg, eng > eng_avg
select no,name,kor,eng from stu_score where kor>(select avg(kor) from stu_score) and eng>(select avg(eng) from stu_score);
select avg(kor),avg(eng) from stu_score;

create table s_info (
s_no number,
s_count number
);

insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score where kor>(select avg(kor) from stu_score) and eng>(select avg(eng) from stu_score))
);

select * from s_info;

-- 국어점수 최고점인 학생, 영어점수 최고점인 학생, 수학점수 최고점인 학생을 출력하시오.
select no,name,kor,eng,math from stu_score 
where kor=(select max(kor) from stu_score) 
or eng=(select max(eng) from stu_score)
or math=(select max(math) from stu_score)
order by kor desc;

select * from employees where salary=(select max(salary) from employees) or salary=(select min(salary) from employees) or salary = trunc((select avg(salary) from employees),-2);
select trunc(avg(salary)) from employees;

select emp_name,salary from employees where salary=(select max(salary) from employees);

select emp_name, salary from employees where salary<=(select avg(salary) from employees) order by salary;

select max(salary) from (select emp_name, salary from employees where salary<=(select avg(salary) from employees) order by salary);

-- 평균값보다 낮은 사원 중에 최대값을 출력하시오.
-- 1. 평균값보다 낮은 사원
-- 2. 그 중에 제일 높은 사원
select emp_name, salary from employees where salary=(select max(salary) from (select emp_name, salary from employees where salary<=(select avg(salary) from employees) order by salary));

-- 문자함수
-- LPAD RPAD : 빈 공백 채우기
select emp_name, lpad(emp_name,16,'#') from employees; 
select emp_name, rpad(emp_name,15,'#') from employees;

-- ltrim rtrim : 문자 없애기
select emp_name,ltrim(emp_name,'Do') from employees;

select 'ko20240001',ltrim('ko20240001','ko2024') from dual;

select emp_name, substr(emp_name,3,4) from employees;   --substr : (데이터,순서,개수)

select substr(job_id,1,2)||employee_id from employees;

select emp_name, length(emp_name) from employees where length(emp_name)>15; --length : 문자열 길이

-- 날짜함수 : 날짜끼리 더하는 건 안 됨.
select sysdate+1 from dual; -- 날짜+숫자
select sysdate-hire_date from employees; -- 날짜-날짜
select round(sysdate,'month') from dual;    -- 일자 반올림 월
select trunc(sysdate,'month') from dual;    -- 일자 버려서 월
select round(sysdate,'year') from dual;     -- 달 반올림 년
select add_months(sysdate,-2) from dual;     -- 개월 수 추가/감소

select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;   -- 올림, 내림, 나머지, 제곱

select emp_name from employees;
select emp_name||to_char(hire_date,'yyyy')||'년'||to_char(hire_date,'mm')||'월'||to_char(hire_date,'dd')||'일'||to_char(hire_date,'day') from employees;
select emp_name||to_char(hire_date,'yyyy"년"mm"월"dd"일"') from employees;

select emp_name||to_char(salary+1400,'L000,000,000') from employees;

select '2010-10-10',last_day('20101010') from dual;
select trunc(to_date('20101010'),'month') from dual;

select * from member;

desc member;

-- 테이블에 column 추가!!!!       ** 커밋, 롤백이 불가
alter table member add gender varchar2(6) default 'female' not null;
-- 테이블 column 삭제!!          ** 커밋, 롤백 역시 불가
alter table member drop column phone;
-- 테이블 column 수정!!  이름, 타입
alter table member rename column name to stu_name;  -- column  이름 수정!
alter table member modify(stu_name varchar2(50));   -- column  타입 수정!
alter table member modify(stu_name number(30));    -- 타입이 달라서 불가능! (비어있어야 함)
alter table member modify(stu_name varchar2(3));    -- 기존 행의 길이가오버되어서 불가능!
alter table member modify(stu_name varchar2(9));
select * from member;
update member set gender = 'male';
update member set stu_name='홍';

commit;





