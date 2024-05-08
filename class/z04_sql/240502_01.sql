--equi 조인 : department_id
select * from employees;

select * from departments;

select employee_id, emp_name, a.department_id, department_name from employees a, departments b where a.department_id = b.department_id;

select * from stu_score;
select * from students;
-- 홍길동 학생
-- 학생 성적의 모든 내용과 전화번호, 이메일, 과, 학년

select no,name,kor,eng,math,total,avg,rank,c_date from stu_score where name='홍길동';
select id,name,phone,email,major,grade from students where name='홍길동';

select no,id,a.name,phone,email,major,grade,kor,eng,math,total,avg,rank,c_date from stu_score a,students b where a.name='홍길동' and a.name = b.name;

select count(*) from stu_score;

alter table students add no number(38);

select * from students;
select * from stu_score;

update students b set no=(select rnum from (
select rownum rnum,id from students a)) where a.id=b.id ;



--alter table students change no number(37);
select rownum rnum,id from students a;
(select rnum from (
select rownum rnum,id from students a));

update students b set no= a.rnum from (select rownum rnum,id from students) a where b.id=a.id;

drop table students;
drop table stu_score;

-- equi join : 2개 테이블 join > 1개의 동일한 컬럼이 있어야 함.
-- 동일한 컬럼은 종복이 없어야 함.

select a.id,a.name,phone,total,avg from students a, stu_score b where a.id=b.id order by name;

select * from students where id='Ermentrude';

-- self join > 동일한 테이블 2개를 가지고 서로 join
select a.employee_id, a.emp_name, a.department_id, a.job_id,a.manager_id,b.emp_name from employees a,employees b where a.manager_id = b.employee_id order by department_id;

desc stu_score;

desc students;

drop table students;

select * from students order by no;

select * from stu_score;

update stu_score a set rank = (select ranks from (select no,id,rank() over(order by total desc) as ranks,rank,total from stu_score) b where a.no=b.no);

--rank 
select ranks from (select no,id,rank() over(order by total desc) as ranks,rank,total from stu_score) b;

select no,id,rank() over(order by total desc) as ranks,rank,total from stu_score b;

select * from students;
select * from member;

alter table member add no number;

select rownum, id from member;
update member a set no = ( select rnum from ( select rownum rnum, id from member) b 
where a.id = b.id);

-- rank, id
select rownum, id from member;
-- 그 중에서 rnum만 들고 오기( 
select rnum from (select rownum, id from member) b where a.id=b.id;

update stu_score set rank=0;

commit;
select total, rank from stu_score order by total desc;
select total, rank() over(order by total desc) ranks from stu_score;
select total, row_number() over(order by total desc) ranks from stu_score;

-- stu_score에 rank 순위를 update하시오. 
select * from stu_score;

update stu_score a set rank = (select ranks from (select no, total,rank() over(order by total desc) ranks from stu_score) b  where a.no=b.no) ;
select ranks from (select no, total,rank() over(order by total desc) ranks from stu_score) b;

select * from stu_score;

select * from (
select rownum rnum, a.* from 
(select * from stu_score order by total desc) a) where rnum >= 11 and rnum <= 20;

select * from (
select row_number() over(order by total desc) rnum, a.* from stu_score a) where rnum >= 11 and rnum <= 20;

-- outer join : 값이 충족되지 않는 행도 출력되도록 하는 것. null 값이 있는 반대편 항목에 (+) 넣으면 됨.
stu_score a order by total desc;
select * from ;
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b where a.manager_id = b.employee_id(+);
--self join manager_id, 이름

--outer join 
select emp_name, b.department_id, department_name from employees a, departments b where a.department_id(+) = b.department_id order by department_id;

select department_id from departments;

--- ansi join
select * from employees cross join departments;
select * from employees,departments;

select a.department_id, department_name from employees a, departments b where a.department_id = b.department_id;

--ansi inner join - using
select a.department_id, department_name from employees a inner join departments b on a.department_id = b.department_id;
select * from employees join departments using (department_id);

select department_id, department_name from employees natural join departments;

-- ansi outer join  : left outer join, right outer join, full outer join
select a.emp_name,a.manager_id, b.emp_name from employees a left outer join employees b on a.manager_id=b.employee_id;
-- 기본 sql : left, right만 가능
select a.emp_name,a.manager_id, b.emp_name from employees a, employees b where a.manager_id=b.employee_id(+);

select * from stu_score;

select a.* from (select row_number() over(order by no) rnum, id,kor,eng,math,total,avg,rank from stu_score where id like '%a%') a where rnum>10 and rnum<=20;

select row_number() over(order by no) rnum, a.* from stu_score a where id like '%a%';

create table melon(
mno number primary key,
rank number,
v_rank number,
img varchar2(130),
title varchar2(100),
singer varchar2(100),
likeNum number
);

desc melon;

select * from melon order by mno;

--delete from melon;

create table yanolja(
yno number primary key,
img varchar2(150),
title varchar2(100),
grade number,
grade_num number,
price number
);

select * from yanolja;




