select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

--Ÿ�� number : +,-,*,/
select salary,salary * 1400 as won_sal,salary*1400*12 as year_sal from employees;

select * from stu_score;

select department_id from employees;

select nvl(department_id,0) from employees;

--���� ��Ī ��ҹ��� as "".
select salary,salary+(salary*nvl(commission_pct,0)) as real_sal from employees;
select salary, nvl(salary+(salary*commission_pct),salary) as "real_sal" from employees;
select salary from employees;

select salary as "����" from employees;

select * from departments;

-- �μ���ȣ, �μ��̸��� ����Ͻÿ�.
select department_id as "�μ���ȣ", department_name as "�μ��̸�" from departments;

-- �������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� concat
-- concat ȫ�浿, ������, �̼���, ������, �豸 
-- split �и�.

select * from stu_score;
insert into stu_score (no,name,kor,eng,math,total,avg,rank) values
  (8,'���±�',100,100,100,300,100.00,1);
rollback;

update stu_score set 
    total = kor+eng+math,
    avg = kor+eng+math/3,
    rank = 1
    where name='���±�';
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
-- asc �������� desc ��������

select * from stu_score where name='ȫ�浿';

select hire_date from employees order by hire_date;

select emp_name, hire_date from employees where hire_date >='02/01/01';

select hire_date,hire_date+100 from employees;

select round(sysdate-hire_date,3) from employees;

-- ������ġ�� > ||
select emp_name, emp_name||email from employees;

select * from employees;
select emp_name,hire_date,salary from employees where hire_date >= '05/01/01' and hire_date<='06/12/31' and salary>=6000 order by hire_date desc;

-- != <> ^= not
select department_id from employees where department_id!=10 and department_id!=50 order by department_id ;

--5000 �̻� 9000 ����
select emp_name,salary from employees where salary>=5000 and salary<=9000 order by salary;

select name, avg from stu_score where avg>=99;

select * from students;

commit;

update students set name='������' where no=10;

-- ���� 70 �̻�, ��� 75 �̻��� �л�
select name,kor,avg from students where kor>=70 and avg>=75;

-- ���� 80, ���� 70, ���� 90
select name, kor from students where kor=90 or kor=80 or kor=70 order by kor;
rollback;
update students set kor=100,total=100+eng+math, avg=(100+eng+math)/3 where no=1;
select * from students where no=1;

-- �������� 70~90
select name,kor from students where kor>=80 and kor<=90 order by no;

-- between A and B (�̻�����)
select kor from students where kor between 80 and 90;
-- not between A and B
select kor from students where kor not between 80 and 90;

--��¥ between A and B
select * from employees order by hire_date;
select emp_name, hire_date from employees where hire_date between '99/01/01' and '01/12/31' order by hire_date;

-- in > or ������ �ʵ尡 �������� �� �߿� �ϳ��� �˻��� ���
select name,kor from students where kor in(80,70,90);
select name,kor from students where kor not in(80,70,90);

-- �˻��� like Ư�� ���ڿ� ����
select * from students where name like '%ȫ%';   -- ȫ�� ���Ե�
select * from students where name like 'ȫ%';    -- ������ �����ϴ�
select * from students where name like '%��';    --������ ������

--  _��_ >

-- _ : ��ĭ ���� ���.

select * from students where name like '_��%';

select * from students where name like '__t%';

select * from students where name like '__r_';

select * from students where name like '_y%' and length(name)=5;
-- length(name) ����
select name from students where length(name) = 5;

--�̸��� A�� ���۵Ǵ� 
select name from students where name like 'A%';

select name from students where name like '%a%';

--��ҹ��� ���о��� a(A)�� �� �ִ� �л� �˻� >> �ҹ��� ġȯ(lower), �빮�� ġȯ(upper), ù���� �빮��(initcap)
select no,name from students where lower(name) like '%a%';
select no,name from students where lower(name) not like '%a%'; -- a ����X

select manager_id from employees;

select emp_name, manager_id from employees where manager_id =100;
select manager_id from employees where manager_id not like '1%';

select employee_id, emp_name,manager_id from employees where manager_id=null;

select employee_id, emp_name, manager_id from employees where manager_id is null;
select employee_id, emp_name, manager_id from employees where manager_id is not null;

select * from stu_score order by name desc;
select * from students;

--1���� ���� ������ ���� ����, ���ٸ� �Ŀ� ���� ������ ��������
select * from students order by kor desc, eng asc;

select * from students order by total desc;

-- �÷��߰�
alter table students add rank number(3);
desc students;
select * from students;
update students set rank=0;
commit;

--���!!!!!!!!
select no,name,total, rank() over(order by total desc) as rank from students order by no;
update students set rank=13 where no=1;
select * from students;

update students s1 set s1.rank = (select ranks from (select no, rank() over(order by total desc) as ranks from students) s2
where s1.no=s2.no);

update students s1 set rank = 13 where no = 1;

select * from students;

select * from (select * from students where avg >=60);










