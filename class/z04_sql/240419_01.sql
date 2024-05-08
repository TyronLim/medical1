select * from employees;

-- 회원 정보 테이블 생성
create table member(
    id varchar2(20),
    pw varchar2(20),
    name varchar2(20),
    phone varchar2(20)
);

-- 데이터 입력
/* 이것도 주석 */
insert into member(id,pw,name,phone) values ('aaa','1111','유관순','010-2222-2222');
select * from member;

insert into member values ('bbb','2222','홍길동','010-1111-1111');

insert into member(id,name,phone) values('ccc','이순신','010-3333-3333');

insert into member values('ddd','강감찬','010-4444-4444'); --컬럼 수 부족 에러

delete from member where name='임태균';

commit;
select id,pw,name,phone from member;

insert into member values(
    'ddd','1111','강감찬','010-4444-4444'
    );
    
select * from member;
rollback;
commit;

update member set pw='2222';
update member set pw='1111' where id='ccc';

select * from tab;--모든 테이블

desc member;--테이블 타입

--오라클 타입
-- number, date, char, varchar2, clob(대용량글자)

-- number : 정수, 실수
-- number(4) > -9999 ~ 9999

create table mem(
no number,          --길이지정X.
no2 number(4),
no3 number(4,2)
);

insert into mem(no) values(1234567890);
insert into mem(no2) values(9999);
insert into mem(no2) values(1.11); -- 소수점은 삭제해버림.
insert into mem(no2) values(-9999);

insert into mem(no3) values(11.11);
insert into mem(no3) values(111); -- 111.00 (5자리)가 되기에 오류.

select * from mem;

commit;

create table mem2(
    no number(4,2),
    mdate date,       -- 년~초까지 저장 가능
    mdate2 timestamp -- date = timestamp (밀리sec까지 저장 가능)
    
    );
    
insert into mem2(mdate) values('2024-04-19');

insert into mem2(mdate) values(sysdate); -- sysdate : 현재 시간

insert into mem2(mdate2) values(sysdate);
insert into mem2(mdate,mdate2) values(sysdate,sysdate+20);


select * from mem2;
select to_char(mdate,'yyyy-mm-dd hh:mi:ss') from mem2;
select to_char(mdate2, 'yyyy-mm-dd hh:mi:ss:ff') from mem2;

select mdate,mdate+31 from mem2;


select * from employees;

select sysdate-hire_date from employees;

create table mem3(
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);

--char : 고정문자
insert into mem3(tel) values('20203040');
insert into mem3(tel) values('22223333');
insert into mem3(tel) values('111');
insert into mem3(tel) values('123456789');--오류

--varchar2 : 가변문자
insert into mem3(name) values('11112222');
insert into mem3(name) values('홍길동'); --한글 3크기
insert into mem3(name) values('신사임당'); --오류
insert into mem3(name) values('aaa');
insert into mem3(name) values('AAA');
select * from mem;

--select, from 2개의 키워드로 구성 됨.
select * from mem;
--명령어는 대소문자를 가리지 않지만, values의 값들은 구분함. 주의
select * from mem3 where name = 'aaa';

select * from mem3 where lower(name)='aaa'; -- values 값의 대문자를 소문자로 바꿔 검색 lower()

select distinct department_id from employees order by department_id;

select * from departments;

select department_id,department_name from departments;

select * from departments;
select * from employees;
select * from jobs where min_salary >7000 order by min_salary;
select * from products order by prod_subcategory_id;

select * from mem3;
select no,mdate2,tel,name from mem3;

select * from employees;

-- 사원번호(id) 사원이름(e name) 급여(salary) 입사일자(hire_date)

select employee_id,emp_name,salary,hire_date from employees;

desc employees;

select * from stu_score;
drop table stu_score;

create table syu_score(
no number,
name varchar2(10),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number);

insert into stu_score values(
1,'홍길동',100,100,100,300,100,1
);

insert into stu_score values(
2,'이순신',100,100,100,300,100,1
);

insert into stu_score values(
3,'김구',100,100,100,300,100,1
);

commit;

select * from stu_score; 

-- 산술 연산자 number 타입인 경우
select * from stu_score;

insert into stu_score values(
6,'김유신',100,95,96,(100+95+96),(100+95+96)/3,1);
select * from stu_score;

insert into stu_score values(
7,'홍길자',100,100,99,(100+100+99),(100+100+99)/3,1);
select * from stu_score;

select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;
--달러, 원화로 환산 -1381.79
select employee_id, emp_name,salary from employees;

select employee_id, emp_name,salary*1381.79 from employees;

--월급 *12 = 연봉
select salary*12,salary*1381.79*12 from employees;

--커미션(실제월급) = 월급 + 월급*커미션 
select employee_id, emp_name, salary, salary+(salary*commission_pct), commission_pct from employees;

select * from employees;

-- nvl(컬럼,0)  > 컬럽의 null 값을 0으로 표시
select employee_id, emp_name, nvl(commission_pct,0),salary + (salary+nvl(commission_pct,0)) from employees; 

commit;












