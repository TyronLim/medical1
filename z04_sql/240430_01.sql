select * from stu_score;
select * from board;
select board.*, member.name from board,member where board.no = member.no;
select * from member;

select name,avg,case 
when avg>=90 then 'A' 
when avg>=80 then 'B'
when avg >=70 then 'C'
when avg>=60 then 'D'
else 'F' end 
from stu_score;

select * from stu_score;

select round(avg(salary),2) from employees;
select * from employees;

select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),to_char(salary*1410,'L999,999,999') kor_salary from employees;

select * from stu_score order by no;

select * from stu_score where avg>=90 order by no;

-- 사원번호, 사원명, 부서번호, 부서명
select employee_id, emp_name, employees.department_id, department_name from employees a, departments b where employees.department_id = departments.department_id;

select * from jobs;
select * from employees;
--사원번호, 사원명, 월급, 최소월급분, 직급, 직급타이틀 출력하시오.
-- 최소월급 몇% 이상을 받고 있는 지 출력. (현재월급-최소월급) / 현재월급 * 100

select employee_id, emp_name, a.salary, min_salary, max_salary, a.job_id, job_title, to_char(round((a.salary-min_salary)/a.salary*100,2)||'%') from employees a, jobs b where a.job_id=b.job_id;

select job_id, job_title from jobs;

-- job_title Manager 글자가 들어가 있는 
-- 사원번호 employee, 사원명, 직급번호, 직급명,월급,최대월급을 출력하시오.
select * from employees;
select * from jobs;

select employee_id, emp_name, b.job_id, job_title, salary, max_salary job_title from employees a, jobs b where a.job_id=b.job_id and job_title like '%Manager%';

select b.user_id,user_address1,user_name,user_phone from Deliver_address a,User b where a.user_id=b.user_id;

create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'E',50,59
);
insert into stu_grade values(
'F',0,59
);

commit;

select * from stu_grade;
update stu_grade set high_score = 89 where grade='B';

select * from stu_score;

-- case when then grade 컬럼 90 이상 A, 80이상 B... 학점을 출력하시오.
select no,name,avg,case 
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg>=50 then 'E'
else 'F'
end as grade
from stu_score order by no;

-- non-equi join
-- 2개 테이블을 join: non=equi join
select no,name,avg, grade
from stu_score, stu_grade
where avg between low_score and high_score
order by no;

select * from stu_score;
select * from stu_grade;

update stu_grade set high_score=61 where grade='F';
commit;

-- 월별 매출액을 기준으로 고객등급

select * from kor_loan_status;

-- 부서별 월급 합계를 출력하시오.
-- 지역별 대출 합계를 출력하시오.
select * from employees;
select department_id, sum(salary) a from employees group by department_id order by a;

select gubun, region,sum(loan_jan_amt) from kor_loan_status group by region,gubun order by region;
select region,sum(loan_jan_amt) from kor_loan_status group by region order by region;

--년도별 지역별 대출 합계금액
select substr(period,1,4) 연도 ,region,sum(loan_jan_amt) from kor_loan_status group by substr(period,1,4),region order by region;

select substr(period,1,4) from kor_loan_status;
select sum(loan_jan_amt) from kor_loan_status;
select * from kor_loan_status;

-- 시간대별,연령대별 판매량 총합을 출력하시오.
select * from lotte_product;
select time_cd, age_cd, sum(purh_amt) a from lotte_product group by time_cd, age_cd order by a desc;

select * from shop_product;

-- 이름별 금액 합계를 출력하시오.
select name,sum(amount) from shop_product where pdate >='2024/03/01' group by name order by name;

-- customer_rank 테이블 생성
-- rank = 100만원 미만 BRONZE / 200만원 미만 SILVER / 300만원 미만 GOLD / 300만원 이상 PLATINUM
-- name, sum(amount), rank 출력하시오. non-equi join으로
create table customer_rank(
min number(9),
max number(9),
grade varchar2(8)
);

insert into customer_rank values(
0,999999,'BRONZE');

insert into customer_rank values(
1000000,1999999,'SILVER');

insert into customer_rank values(
2000000,2999999,'GOLD');

insert into customer_rank values(
3000000,3999999,'PLATINUM');

update customer_rank set max=999999999 where grade='PLATINUM';

select name, grade from customer_rank,shop_product where sum(amount) between min and max;

select * from customer_rank;
select * from shop_product;

select name,s_amount,grade from
(select name,sum(amount) s_amount from shop_product where p_date group by name),customer_rank
where s_amount between min and max;

select name,amount,grade from shop_product,customer_rank where amount between min and max;

select no,name,avg, grade
from stu_score, stu_grade
where avg between low_score and high_score
order by no;

-- rownumber

select * from lotte_product order by std_ym;

-- 순번을 새롭게 부여해서 출력해주는 함수
-- rownum, row_number()
select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt from lotte_product;

select rownum, a.* from lotte_product a
where rownum<=10;



select rnum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from (select rownum rnum, a.* from lotte_product a) b
where rnum >=11 and rnum<=20 order by std_ym;

select rownum, b.* from (select * from lotte_product order by std_ym) b;

select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from lotte_product;

select * from stu_score order by no;

--kor 점수가 높은 순으로 21등부터 30등까지 출력하시오
--순번 21,22,23.....30번을 부여하세요.

select * from (select rownum rnum,b.* from (select * from stu_score a order by total desc) b)c where c.rnum>=21 and c.rnum<=30;

select rownum,b.* from (select * from stu_score a order by total desc) b;


select * from stu_score order by total desc;
select rownum r, a.* from (select * from stu_score order by total desc) a;
select r,b.* from (select rownum r, a.* from (select * from stu_score order by total desc) a) b where r>20 and r<=30 order by b.r;


commit;



