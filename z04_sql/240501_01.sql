select * from stu_score;

select * from students;

drop table students;

select * from students;

update students set id='aaa',name='홍길동',gender='M' where id='Aurelie';

update students set id='bbb',name='유관순',gender='F' where id='Leonid';

update students set id='ccc',name='이순신',gender='M' where id='Meggie';

update students set id='ddd',name='강감찬',gender='M' where id='Howey' and pw=6654;

update students set id='eee',name='김구',gender='M' where id='Reinwald';

update students set id='fff',name='김유신',gender='M' where id='Jacquelin';

update students set id='ggg',name='홍길자',gender='F' where id='Burl';

update students set id='hhh',name='홍길순',gender='F' where id='Valentin';


select * from students where id='Howey' and pw=6654;
select * from students;
select * from stu_score order by no;
--rollback;
--commit;

select rownum,a.* from students a order by grade;

select a.* from students a;

-- order by 구문 실행
select rownum,a.*from students a order by grade;

-- select > order by > rownum
select * from students order by grade;

select rownum, a.* from (select * from students order by grade) a;

select * from stu_score where avg>=85 and no>=500;


select * from (select * from stu_score where avg>=85) where no>=500;

select * from shop_product;

select  name, amount, pdate from shop_product where pdate>='2024-03-01';

--이름별 구매내역 합계
--sum(amount) 가상으로 만들어진 column 
select name,sum(amount) from shop_product group by name;

select * from customer_rank;
select name, avg from stu_score;
--shop_product, customer_rank
select avg(avg) from (select name, avg, grade from stu_score, stu_grade where avg between low_score and high_score) group by grade;
select * from stu_grade;
select name, avg, grade from stu_score, stu_grade where avg between low_score and high_score;

-- equi join : 같은 컬럼이 2개의 테이블에 존해자혀 2개 컬럼을 이용해 검색하는 방법
-- non-uqui join > 같은 컬럼이 없으면서 2개 테이블을 사용해 검색하는 방법
select name,s_amount,grade from (select name, sum(amount) as s_amount from shop_product
where pdate>='2004/03/01' group by name),customer_rank where s_amount between min and max;

select * from customer_rank;
select * from shop_product;

--update customer_rank set max=19999999

select name, sum(amount) as s_amount from shop_product
where pdate>='2004/03/01' group by name;

select * from(select rownum rnum,b.* from (select * from students order by id) b) where rnum>=11 and rnum<=20 ;

select rownum, b.* from (select rownum rnum, a.* from (select * from students order by id) a) b where rnum>=11 and rnum<=20;

select * from (select row_number() over(order by id) rnum, a.* from students a) where rnum >=11 and rnum<=20;

--self join

select employee_id, emp_name, a.manager_id, a.department_id, department_name from employees a,departments b where a.department_id=b.department_id order by manager_id;

select * from departments;
select * from employees;

--corss join (107*107)
--equi join : 2개 테이블의 같은 컬럼 

-- equi join, self join 같이 사용
select a.employee_id, a.emp_name, a.manager_id, a.department_id, department_name, b.emp_name from employees a,employees b, departments c 
where a.manager_id = b.employee_id and a.department_id = c.department_id
order by a.employee_id;

--self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b where a.manager_id = b.employee_id;

select a.employee_id, a.emp_name, b.manager_id from employees a, employees b;

--john chen과 동일한 부서에 근무하는 사람을 출력하시오.
select * from employees;

-- 사원명, 부서번호, 같이 근무하는 부서번호, 같이 근무하는 사원명
select a.emp_name, a.department_id, b.department_id, b.emp_name from employees a, employees b where a.emp_name='Guy Himuro' and a.department_id = b.department_id;

select * from member;

insert into member values(
member_sqe.nextval, 'eee',1111,'김구','남자',sysdate
);
insert into member values(
member_sqe.nextval, 'fff',1111,'김유신','남자',sysdate
);

insert into member values(
member_sqe.nextval, 'ggg',1111,'홍길순','여자',sysdate
);
desc member;

update member set name='홍길자' where memno=1;

commit;

select * from member;

update member set name = '홍길동' where memno = 1;
















