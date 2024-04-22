select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

--타입 number : +,-,*,/
select salary,salary * 1400 as won_sal,salary*1400*12 as year_sal from employees;

select * from stu_score;

select department_id from employees;

select nvl(department_id,0) from employees;

--월급 별칭 대소문자 as "".
select salary,salary+(salary*nvl(commission_pct,0)) as real_sal from employees;
select salary, nvl(salary+(salary*commission_pct),salary) as "real_sal" from employees;
select salary from employees;

select salary as "연봉" from employees;

select * from departments;

-- 부서번호, 부서이름을 출력하시오.
select department_id as "부서번호", department_name as "부서이름" from departments;

-- 여러개의 데이터를 1개로 합쳐서 넘겨야 할 경우 concat
-- concat 홍길동, 유관순, 이순신, 강감찬, 김구 
-- split 분리.

select * from stu_score;
insert into stu_score (no,name,kor,eng,math,total,avg,rank) values
  (8,'임태균',100,100,100,300,100.00,1);
rollback;

update stu_score set 
    total = kor+eng+math,
    avg = kor+eng+math/3,
    rank = 1
    where name='임태균';
rollback;

select * from stu_score;
    

select kor||','||eng||','||math stu from stu_score;

select distinct department_id from employees where department_id is not null;

select distinct manager_id from employees where manager_id is not null;

select * from employees where employee_id >=200 and employee_id <=203;
select employee_id,salary from employees where employee_id =201;

select * from employees;
select * from employees where employee_id<=150 or employee_id >=200 order by employee_id
;

select department_id from employees where department_id=10 or department_id=30 or department_id=50;

select salary from employees where salary >6000 and salary <9000 order by salary;
select emp_name,salary from employees where salary=6000 or salary=7000 or salary=8000;
select emp_name,department_id,salary from employees where department_id=50 and salary >=8000;
-- asc 오름차순 desc 내림차순

select * from stu_score where name='홍길동';

select hire_date from employees order by hire_date;

select emp_name, hire_date from employees where hire_date >='02/01/01';

select hire_date,hire_date+100 from employees;

select round(sysdate-hire_date,3) from employees;

-- 문자합치기 > ||
select emp_name, emp_name||email from employees;

select * from employees;
select emp_name,hire_date,salary from employees where hire_date >= '05/01/01' and hire_date<='06/12/31' and salary>=6000 order by hire_date desc;

-- != <> ^= not
select department_id from employees where department_id!=10 and department_id!=50 order by department_id ;

--5000 이상 9000 이하
select emp_name,salary from employees where salary>=5000 and salary<=9000 order by salary;

select name, avg from stu_score where avg>=99;

select * from students;

commit;

update students set name='관순스' where no=10;

-- 국어 70 이상, 평균 75 이상인 학생
select name,kor,avg from students where kor>=70 and avg>=75;

-- 국어 80, 국어 70, 국어 90
select name, kor from students where kor=90 or kor=80 or kor=70 order by kor;
rollback;
update students set kor=100,total=100+eng+math, avg=(100+eng+math)/3 where no=1;
select * from students where no=1;

-- 국어점수 70~90
select name,kor from students where kor>=80 and kor<=90 order by no;

-- between A and B (이상이하)
select kor from students where kor between 80 and 90;
-- not between A and B
select kor from students where kor not between 80 and 90;

--날짜 between A and B
select * from employees order by hire_date;
select emp_name, hire_date from employees where hire_date between '99/01/01' and '01/12/31' order by hire_date;

-- in > or 동일한 필드가 여러개의 값 중에 하나를 검색할 경우
select name,kor from students where kor in(80,70,90);
select name,kor from students where kor not in(80,70,90);

-- 검색어 like 특정 문자열 포함
select * from students where name like '%홍%';   -- 홍이 포함된
select * from students where name like '홍%';    -- 순으로 시작하는
select * from students where name like '%순';    --순으로 끝나는

--  _길_ >

-- _ : 한칸 공간 사용.

select * from students where name like '_길%';

select * from students where name like '__t%';

select * from students where name like '__r_';

select * from students where name like '_y%' and length(name)=5;
-- length(name) 길이
select name from students where length(name) = 5;

--이름이 A로 시작되는 
select name from students where name like 'A%';

select name from students where name like '%a%';

--대소문자 구분없이 a(A)가 들어가 있는 학생 검색 >> 소문자 치환(lower), 대문자 치환(upper), 첫글자 대문자(initcap)
select no,name from students where lower(name) like '%a%';
select no,name from students where lower(name) not like '%a%'; -- a 포함X

select manager_id from employees;

select emp_name, manager_id from employees where manager_id =100;
select manager_id from employees where manager_id not like '1%';

select employee_id, emp_name,manager_id from employees where manager_id=null;

select employee_id, emp_name, manager_id from employees where manager_id is null;
select employee_id, emp_name, manager_id from employees where manager_id is not null;

select * from stu_score order by name desc;
select * from students;

--1차로 국어 점수로 역순 정렬, 같다면 후에 영문 점수로 순차정렬
select * from students order by kor desc, eng asc;

select * from students order by total desc;

-- 컬럼추가
alter table students add rank number(3);
desc students;
select * from students;
update students set rank=0;
commit;

--등수!!!!!!!!
select no,name,total, rank() over(order by total desc) as rank from students order by no;
update students set rank=13 where no=1;
select * from students;

update students s1 set s1.rank = (select ranks from (select no, rank() over(order by total desc) as ranks from students) s2
where s1.no=s2.no);

update students s1 set rank = 13 where no = 1;

select * from students;

select * from (select * from students where avg >=60);










