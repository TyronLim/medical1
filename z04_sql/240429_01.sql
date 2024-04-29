
-- 무결성 제약조건 : 부적합한 자료가 입력되지 않도록 하기 위한 규칙
-- not null, unique, primary key, foreign key, check
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);

-- data입력, 출력, 수정, 삭제 부분 (DML)
insert into member (memNo, id, pw, name, gender, mdate) values(member_sqe.nextval,'aaa','1111','홍길동','남자',sysdate);

insert into member(memNo,id,pw,name,gender) values(member_sqe.nextval,'bbb','1111','유관순','여자');

insert into member values(member_sqe.nextval,'ccc','1111','이순신','남자',sysdate);

select * from member;

--테이블 생성
create table board(
bno number(4) primary key,
id varchar2(30), -- 외래키 등록
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id)
references member(id) --member 테이블의 primary key id
);

insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
board_seq.nextval,'aaa','제목입니다','내용입니다',sysdate,board_seq.currval,0,0,1,'');

insert into board values(board_seq.nextval,'bbb','제목입니다','내용입니다',sysdate,board_seq.currval,0,0,1,'');

insert into board(bno,id,btitle,bcontent,bgroup) values(
board_seq.nextval,'aaa','제목입니다3','내용입니다3',board_seq.currval);

select * from board;
commit;
alter table comments drop constraint FJ_CNO;
alter table board rename to board;
drop table board;

delete board where bno=3;

delete member where id='aaa';

--decode 조건문
select emp_name, department_id, decode(
department_id,
10,'총무기획부',
20,'마케팅',
30,'구매/생산부',
40,'인사부'

)from employees order by department_id asc;


select department_id,department_name from departments;

select * from stu_score order by avg desc;
--90점 - a, 80점 - b, 70점- c

select avg,decode(avg, 90,'a',80,'b',70,'c') from stu_score order by avg desc;

select job_id,salary from employees;
--sh_clerk > salary*15%, ad_asst > *10%, mk_rep > *5%

select job_id, salary, decode(job_id, (select job_id from employees where job_id like '%CLERK'),salary+(salary*0.15),'AD_ASST',salary+(salary*0.1),'MK_REP',salary+(salary*0.05)) as sal2 from employees;

-- primary key 삭제하려면 foreign key 등록되어 있는 데이터를 우선 삭제를 모두 해야 함.
-- primary key 삭제되면 모두 삭제하는 방법 on delete cascade,   모두 존재하는 방법 on uqdate cascade

select job_id from employees where job_id like '%CLERK';

select name, avg from stu_score;

select name, avg, case 
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
else 'F'
end as grade
from stu_score;

--case 구문
select department_id, department_name from departments;
select department_id from employees order by department_id asc;
select department_id, case
when department_id=10 then '총무기획부'
when department_id=20 then '마케팅'
when department_id=30 then '구매/생산부'
when department_id=40 then '인사부'
when department_id=50 then '배송부'
when department_id=60 then 'IT'
when department_id=70 then '홍보부'
when department_id=80 then '영업부'
when department_id=90 then '기획부'
when department_id=100 then '자금부'
when department_id=110 then '경리부'
when department_id=120 then '재무팀'
when department_id=130 then '세무팀'
when department_id=140 then '신용관리팀'
when department_id=150 then '주식관리팀'
when department_id=160 then '수익관리팀'
when department_id=170 then '생산팀'
when department_id=180 then '건설팀'
when department_id=190 then '계약팀'
when department_id=200 then '운영팀'
when department_id=210 then 'IT 지원'
when department_id=220 then 'NOC'
when department_id=230 then 'IT 헬프데스크'
end from employees order by department_id;

select job_id,salary from employees;

select job_id,salary,case
when job_id like '%CLERK' then salary + salary*0.15
when job_id = 'AD_ASST' then salary + salary*0.1
when job_id like '%rep' then salary + salary*0.2
end sal2
from employees order by sal2 asc;

-- 월급 평균 이하인 사람 0.15, 평균이하 0.05인상후 출력


--employees테이블에서 검색. --salary_updown
select salary,emp_name, salary_updown, case 
when salary < (select avg(salary) from employees) then salary + salary*0.05
when salary >= (select avg(salary) from employees) then salary + salary*0.05
end from 

(select employees.*, case 
when salary < 6461 then 'down'
when salary >= 6461 then 'up'
end as salary_updown from employees) order by salary;

--case 2개 사용
select emp_name, salary, case
when salary < (select avg(salary) from employees) then 'down'
when salary >= (select avg(salary) from employees) then 'up'
end as salary_updown,
case
when salary < (select avg(salary) from employees) then salary + salary*0.05
when salary >= (select avg(salary) from employees) then salary + salary*0.05
end as salary_up from employees;

--rank

select * from stu_score;

select total,rank from stu_score order by total desc;

-- rank 함수
select total,rank,rank() over(order by total desc) as ranks from stu_score;
select no, rank() over(order by total desc) as ranks from stu_score;

select total,rank,rank() over(order by total desc) from stu_score;

update stu_score set rank=1 where total = 291;

------------------------------------------------------------------------------------------------------------------------------
update stu_score a set rank= (select ranks from(
select no, rank() over(order by total desc) as ranks from stu_score) b where a.no=b.no);
------------------------------------------------------------------------------------------------------------------------------
select * from stu_score;

select avg(salary) as a from employees;

select department_id, department_name from departments;
select department_id from employees order by department_id asc;
select department_id, case
when department_id=10 then '총무기획부'
when department_id=20 then '마케팅'
when department_id=30 then '구매/생산부'
when department_id=40 then '인사부'
when department_id=50 then '배송부'
when department_id=60 then 'IT'
when department_id=70 then '홍보부'
when department_id=80 then '영업부'
when department_id=90 then '기획부'
when department_id=100 then '자금부'
when department_id=110 then '경리부'
end from employees order by department_id;

select emp_name, department_id from employees;
select department_id, department_name from departments;

select emp_name, employees.department_id, department_name from employees, departments where employees.department_id = departments.department_id;


-- 그룹함수 sum,avg,count,max,min, stddev 표준편차, variance 분산

-- 월급 총합
select sum(salary) from employees;
-- 국어점수 총합 stu_score
select sum(kor) from stu_score;

select * from employees; 
select count(*)from employees;
select count(*)from employees where department_id = 50;

--커미션을 받는 사원의 수를 구하시오.
select count(*) from employees where commission_pct is not null;

select emp.* from employees emp;

-- 전체사원수
select count(*) from employees;

--부서 번호가 50번인 사원 수
select count(*) from employees where department_id=50;

select department_id a, count(department_id) b from employees group by department_id order by a;

-- stu_score에 90점 이상A, 80점 이상B, 70점 이상C, 60점 이상D, 60점 미만F
select name, avg,case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade 
from stu_score;


select case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score;

select count(grade) from (select case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score) where grade = 'A';

select count(grade) from (select case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score) group by grade;

select count(kor) from stu_score where trunc(kor,-1)=90;

select trunc(kor,-1) from stu_score group by trunc(kor,-1) order by trunc(kor,-1);

select count(kor) from stu_score where kor>=90 and kor !=100;

select count(kor) from stu_score where kor>90;
-- 그룹함수 group by 사용
select department_id,count(*) from employees group by department_id order by department_id;

select emp_name,count(emp_name) from employees group by emp_name;

-- 부서별 평균 월급을 구하시오.
select department_id, round(avg(salary),2) from employees group by department_id order by department_id;

select * from employees;
select job_id from employees where job_id like '%CLERK' group by job_id;

or job_id like 'REP' or job_id like 'MAN';

select avg(salary),job_id from employees where job_id like '%CLERK' group by job_id;    -- 정답

select * from employees group by job_id;

select count(substr(job_id,4)) from employees where job_id like '%CLERK';
select * from employees;
select substr(job_id,4),count(substr(job_id,4)) from employees group by substr(job_id,4);       --substr(job_id,4,(length-3)

-- 부서별 최대월급, 최소월급, 평균월급을 출력하시오.

select department_id, count(department_id), sum(salary), max(salary), min(salary), round(avg(salary),2) from employees where department_id is not null group by department_id order by department_id;
select department_id,salary from employees where department_id = 80;

select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- 부서별 사원 수, 커미션을 받는 사원 수를 출력하시오
select count(department_id), count(commission_pct) from employees group by department_id;

select department_id, count(commission_pct) from employees group by department_id;

-- having group by 조건절, where 일반 컬럼의 조건절
select department_id,avg(salary) 
from employees 
where emp_name not like '_a%' 
group by department_id 
having avg(salary) >= (select avg(salary) from employees)+2000
order by avg(salary);

select department_id,avg(salary) from employees where emp_name not like '_a%' group by department_id;

select emp_name from employees where emp_name not like '_a%';

select avg(salary) from employees;

-- 부서별 최대 월급이 7000 이상인 것만 출력하시오.

select department_id, max(salary) from employees group by department_id having max(salary) >= 8000 order by max(salary);

-- 조인
-- RDBMS
select emp_name, department_id, salary from employees;
select department_id, department_name from departments;

select count(*) from employees,departments; -- 107*27

-- equi join = 106개 (null값 제외)
-- 두 테이블 간 같은 column을 가지고 비교해서 해당되는 데이터를 출력
select employee_id, emp_name, employees.department_id, department_name, salary from employees, departments where employees.department_id=departments.department_id;

select department_id, department_name from departments;
select department_id from employees;

select * from board;
select * from member;

update member set name = '홍길동' where id='aaa';

select board.*, member.name from board,member where member.id=board.id;     -- equi 조인!!!!!!!!!!!









