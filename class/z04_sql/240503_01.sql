-- 사원번호 이름 급여 부서 입사인 상사의 사원번호 출력

select * from employees order by emp_name;
select * from departments;

-- 1번.
select a.employee_id, a.emp_name||'/'||a.job_id "Name",a.salary, b.department_name, a.hire_date, a.manager_id, c.emp_name manager from employees a, departments b, employees c
where a.department_id = b.department_id and a.manager_id = c.employee_id;

-- 2번.
select emp_name "Name",job_id "Job", salary "Salary" , salary*12+100 "increse Ann_salary", (salary+100)*12 "Increase Salary" from employees;

-- 3번.
select emp_name name, salary from employees where salary >=10000 or salary<=7000 order by salary ;
select emp_name name, salary from employees where salary not between 10000 and 7000 order by salary; 

-- 4번.
select emp_name as "E or O name" from employees where lower(emp_name) like '%e%' or lower(emp_name) like '%a%';

-- 5번.
select employee_id, emp_name as "Name",salary, round(salary+(salary*0.123)) as "Increase Salary" from employees where department_id=60;

-- 6번.
select emp_name as "Name", salary*12, (salary*12)+((salary*12)*nvl(commission_pct,0)) t_salary, nvl2(commission_pct,'salary+commossion','salary only') commi from employees;

-- case when ''>'' then 
select case 
when commission_pct is null then 'Salary only'
when commission_pct is not null then 'Salary + Commission'
end as commission from employees;

-- decode ,,
select decode(commission_pct, null, 'Salary only','Salary + Commission') from employees;
select decode(salary, 3000,'A', 4000,'B', 5000,'C') from employees;
select decode(department_id, 10,'A', 20,'B', 30,'C') from employees;

-- 7번.
select department_id,to_char(sum(salary),'$999,999') sum, to_char(round(avg(salary)),'$999,999') avg,
to_char(max(salary),'$999,999') max, to_char(min(salary),'$999,999') min from employees where department_id is not null group by department_id;

-- 8번.
select * from (select job_id, avg(salary) a from employees  where job_id not like '%CLERK%' group by job_id) where a>10000 order by a desc;
--select * from employees where job_id like '%CLERK%';

-- 9번.
select to_char(a.emp_name)||' report to '||to_char(upper(b.emp_name)) report
from employees a, employees b where a.manager_id = b. employee_id(+) order by b.emp_name;

-- 10번.
select f.*, e.department_name from (
select count(department_id) count,department_id from (select a.department_id, b.department_name from employees a, departments b 
where a.department_id = b.department_id)
group by department_id) f, departments e where f.department_id = e.department_id and f.count>=5 order by f.count;

--10번 구글링
SELECT E.DEPARTMENT_ID, D.DEPARTMENT_NAME, COUNT(E.EMPLOYEE_ID)
FROM EMPLOYEES E INNER JOIN DEPARTMENTS D
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_NAME, E.DEPARTMENT_ID
HAVING COUNT(EMPLOYEE_ID) > 5
ORDER BY COUNT(EMPLOYEE_ID) DESC;


-- 추가1
select emp_name, job_id, salary from employees where salary >=(
select salary from employees where emp_name like '%Tucker%');

-- 추가2
select a.emp_name, a.job_id, a.salary, b.* from employees a,(
select department_id, round(avg(salary),2) "Department Avg Salary" from employees group by department_id) b 
where b.department_id = a.department_id order by b.department_id;


create table daum_movie(
dno number,
title varchar2(100),
img varchar2(200),
audience number,
ddate number
);

alter table daum_movie modify(ddate date);

select * from daum_movie;

delete daum_movie dno;

select * from mem;
insert into mem values('aaa','1111','asd','2020.01.22');
insert into mem values('bbb','1111','sss',to_date('2024-06-26 ' || '08:30:00', 'yyyy-mm-dd hh24:mi:ss');

alter table coupang modify(title varchar2(300));

create table coupang(
cno number,
title varchar2(100),
img varchar2(300),
price number(10),
grade number(10),
eval_num number(10)
);

select * from coupang;

create table flight(
fno number,
airline varchar2(100),
departure_time date,
arrival_time date,
flight_time varchar2(20),
price number
);
