select * from students;

select * from students order by name desc;

--drop table students;

alter table students add rank number(3);
update students set rank=0;
select * from students;
select rank() over(order by total desc) rank
from students;

update students set total=0;

select * from students;

update students set total=(kor+eng+math);
update students a set rank = (select no, rank() over(order by total desc) rank
from students) b where s1 a.no = b.no);
--1 update 구문
update students a set rank = (rank)

--2 rank()구문
(select rank() ocer(order by total desc) ranks from students) b;

--3 update 구문 rank구문을 no 컬럼으로 비교(rank 컬럼을 검색)


--4 students 테이블에서 ranks가 들어가 있는 테이블을 넣어줌.
update students a set rank = (
    select ranks from (select no,rank() ocer(order by total desc) ranks from students) b
    where a.no = b.no
);

select no,total,rank from students order by no;

select no, kor, eng, math, total, rank from students order by kor desc, eng asc;

select manager_id from employees order by manager_id desc;

select hire_date from employees order by hire_date desc;

select max(kor)-min(kor) from students;
select min(kor),min(eng),min(math) from students;

select emp_name, hire_date from employees;
select * from employees;

select employee_id, job_id,department_id,hire_date,salary from employees order by hire_date ;

select emp_name, salary from employees order by salary, emp_name desc;

--숫자 함수------------------------------------
select -10, abs (-10) from dual;    -- 절대값
select 34.789, floor(34.789) as f, round(34.789) as r from dual;     -- 소수점 버림,소수점 반올림

select 34.178, round(34.178), round(34.178,2) from dual;        -- 반올림 자릿수

select avg from students;
select round(avg,2) avg from students;

select 34.5678, round(34.5678,-1) from dual;    -- 반올림 정수부분

--trunc 지정한 자릿수 이하 버림
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;

-- 올림
select ceil(34.123) from dual;
select ceil(34.123,2) from dual;-- 안됌. 에러.

select trunc(kor,-1) from students order by kor desc;

select name, trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1) tot from students;

--mod 나머지
select round(100/7,2) from dual;
select mod(10,7) from dual;
select 10/7 from dual;

select employee_id from employees;
select employee_id, mod(employee_id,2) from employees where mod(employee_id,2)=0;

select no from students where mod(no,3)=0;

-- 시퀀스
create sequence seq_no 
increment by 1  --1씩 증가하는 번호 생성
start with 1    --1부터 시작
minvalue 1      --최소값
maxvalue 1000   --최대값
nocycle         --순환 없이
nocache         --캐쉬 사용 안함
;

select seq_no.nextval currval from dual;    --nextval  1씩 증가

select seq_no.currval from dual;      -- currval 시퀀스 번호 확인

--drop table member;

--drop table mem3;

create table member (
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select seq_mno.nextval from dual;

insert into member values(
seq_mno.nextval,'eee','1111','김구','010-5555-5555');

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

select 's0000'||to_char(seq_mno.currval) from dual;

create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache;

--drop sequence seq_kono;

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.currval,'00000')) as stuno from dual; -- trim () 공백제거

create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id vachar2(30),
bdate date,
bhit number(10)
);

--시퀀스 시작1001 증감10 1~99999   > 5번 실행

create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
nocycle
nocache;

select seq_deptno.nextval from dual;

create table emp01(
emppno number(4) primary key,
ename varchar(30),
hire_date date);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

insert into emp01 values(
emp_seq.nextval, '이순신', sysdate);

select * from emp01;

commit;

alter sequence emp_seq
increment by 1001
;

select * from employees;

select employee_id, emp_name, job_id, hire_date from employees order by hire_date;

select employee_id, emp_name,job_id, hire_date, ceil(sysdate-hire_date)||'일' from employees;

select emp_name from empolyees;

select substr(job_id,4)||trim(to_char(employee_id,'0000')) from employees;
select substr(job_id,0,2) from employees;       -- str 자르기

select substr('abcde',1,3) from dual;           -- ('str',a,b) a번째부터 b개를 잘라라!


select * from employees;

select substr(job_id,1,2)||trim(to_char(employee_id,'00000')) from employees;

--날짜 함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

select MONTHS_BETWEEN(SYSDATE,hire_date) 월수, sysdate-hire_date 일수 from employees;   --달 비교, 일 비교

-- 개월수를 추가
select sysdate,add_months(sysdate,2) from dual; --- 현재 날짜에서 2달을 더하라.ㄺ

select next_day(sysdate,'수요일') from dual;   --현재 기준점으로 다음번의 요일이 몇 일인지.

select last_day(sysdate) from dual;     -- 현재 기준점으로 그 달의 마지막 일을 알려줌.

select last_day('2024-02-01') from dual;        -- 2024 02 01 기준점으로 그 달의 마지막 일을 알려줌.





