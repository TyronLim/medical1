
-- ���Ἲ �������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);

-- data�Է�, ���, ����, ���� �κ� (DML)
insert into member (memNo, id, pw, name, gender, mdate) values(member_sqe.nextval,'aaa','1111','ȫ�浿','����',sysdate);

insert into member(memNo,id,pw,name,gender) values(member_sqe.nextval,'bbb','1111','������','����');

insert into member values(member_sqe.nextval,'ccc','1111','�̼���','����',sysdate);

select * from member;

--���̺� ����
create table board(
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id)
references member(id) --member ���̺��� primary key id
);

insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
board_seq.nextval,'aaa','�����Դϴ�','�����Դϴ�',sysdate,board_seq.currval,0,0,1,'');

insert into board values(board_seq.nextval,'bbb','�����Դϴ�','�����Դϴ�',sysdate,board_seq.currval,0,0,1,'');

insert into board(bno,id,btitle,bcontent,bgroup) values(
board_seq.nextval,'aaa','�����Դϴ�3','�����Դϴ�3',board_seq.currval);

select * from board;
commit;
alter table comments drop constraint FJ_CNO;
alter table board rename to board;
drop table board;

delete board where bno=3;

delete member where id='aaa';

--decode ���ǹ�
select emp_name, department_id, decode(
department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��'

)from employees order by department_id asc;


select department_id,department_name from departments;

select * from stu_score order by avg desc;
--90�� - a, 80�� - b, 70��- c

select avg,decode(avg, 90,'a',80,'b',70,'c') from stu_score order by avg desc;

select job_id,salary from employees;
--sh_clerk > salary*15%, ad_asst > *10%, mk_rep > *5%

select job_id, salary, decode(job_id, (select job_id from employees where job_id like '%CLERK'),salary+(salary*0.15),'AD_ASST',salary+(salary*0.1),'MK_REP',salary+(salary*0.05)) as sal2 from employees;

-- primary key �����Ϸ��� foreign key ��ϵǾ� �ִ� �����͸� �켱 ������ ��� �ؾ� ��.
-- primary key �����Ǹ� ��� �����ϴ� ��� on delete cascade,   ��� �����ϴ� ��� on uqdate cascade

select job_id from employees where job_id like '%CLERK';

select name, avg from stu_score;

select name, avg, case 
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
else 'F'
end as grade
from stu_score;

--case ����
select department_id, department_name from departments;
select department_id from employees order by department_id asc;
select department_id, case
when department_id=10 then '�ѹ���ȹ��'
when department_id=20 then '������'
when department_id=30 then '����/�����'
when department_id=40 then '�λ��'
when department_id=50 then '��ۺ�'
when department_id=60 then 'IT'
when department_id=70 then 'ȫ����'
when department_id=80 then '������'
when department_id=90 then '��ȹ��'
when department_id=100 then '�ڱݺ�'
when department_id=110 then '�渮��'
when department_id=120 then '�繫��'
when department_id=130 then '������'
when department_id=140 then '�ſ������'
when department_id=150 then '�ֽİ�����'
when department_id=160 then '���Ͱ�����'
when department_id=170 then '������'
when department_id=180 then '�Ǽ���'
when department_id=190 then '�����'
when department_id=200 then '���'
when department_id=210 then 'IT ����'
when department_id=220 then 'NOC'
when department_id=230 then 'IT ��������ũ'
end from employees order by department_id;

select job_id,salary from employees;

select job_id,salary,case
when job_id like '%CLERK' then salary + salary*0.15
when job_id = 'AD_ASST' then salary + salary*0.1
when job_id like '%rep' then salary + salary*0.2
end sal2
from employees order by sal2 asc;

-- ���� ��� ������ ��� 0.15, ������� 0.05�λ��� ���


--employees���̺��� �˻�. --salary_updown
select salary,emp_name, salary_updown, case 
when salary < (select avg(salary) from employees) then salary + salary*0.05
when salary >= (select avg(salary) from employees) then salary + salary*0.05
end from 

(select employees.*, case 
when salary < 6461 then 'down'
when salary >= 6461 then 'up'
end as salary_updown from employees) order by salary;

--case 2�� ���
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

-- rank �Լ�
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
when department_id=10 then '�ѹ���ȹ��'
when department_id=20 then '������'
when department_id=30 then '����/�����'
when department_id=40 then '�λ��'
when department_id=50 then '��ۺ�'
when department_id=60 then 'IT'
when department_id=70 then 'ȫ����'
when department_id=80 then '������'
when department_id=90 then '��ȹ��'
when department_id=100 then '�ڱݺ�'
when department_id=110 then '�渮��'
end from employees order by department_id;

select emp_name, department_id from employees;
select department_id, department_name from departments;

select emp_name, employees.department_id, department_name from employees, departments where employees.department_id = departments.department_id;


-- �׷��Լ� sum,avg,count,max,min, stddev ǥ������, variance �л�

-- ���� ����
select sum(salary) from employees;
-- �������� ���� stu_score
select sum(kor) from stu_score;

select * from employees; 
select count(*)from employees;
select count(*)from employees where department_id = 50;

--Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�.
select count(*) from employees where commission_pct is not null;

select emp.* from employees emp;

-- ��ü�����
select count(*) from employees;

--�μ� ��ȣ�� 50���� ��� ��
select count(*) from employees where department_id=50;

select department_id a, count(department_id) b from employees group by department_id order by a;

-- stu_score�� 90�� �̻�A, 80�� �̻�B, 70�� �̻�C, 60�� �̻�D, 60�� �̸�F
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
-- �׷��Լ� group by ���
select department_id,count(*) from employees group by department_id order by department_id;

select emp_name,count(emp_name) from employees group by emp_name;

-- �μ��� ��� ������ ���Ͻÿ�.
select department_id, round(avg(salary),2) from employees group by department_id order by department_id;

select * from employees;
select job_id from employees where job_id like '%CLERK' group by job_id;

or job_id like 'REP' or job_id like 'MAN';

select avg(salary),job_id from employees where job_id like '%CLERK' group by job_id;    -- ����

select * from employees group by job_id;

select count(substr(job_id,4)) from employees where job_id like '%CLERK';
select * from employees;
select substr(job_id,4),count(substr(job_id,4)) from employees group by substr(job_id,4);       --substr(job_id,4,(length-3)

-- �μ��� �ִ����, �ּҿ���, ��տ����� ����Ͻÿ�.

select department_id, count(department_id), sum(salary), max(salary), min(salary), round(avg(salary),2) from employees where department_id is not null group by department_id order by department_id;
select department_id,salary from employees where department_id = 80;

select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- �μ��� ��� ��, Ŀ�̼��� �޴� ��� ���� ����Ͻÿ�
select count(department_id), count(commission_pct) from employees group by department_id;

select department_id, count(commission_pct) from employees group by department_id;

-- having group by ������, where �Ϲ� �÷��� ������
select department_id,avg(salary) 
from employees 
where emp_name not like '_a%' 
group by department_id 
having avg(salary) >= (select avg(salary) from employees)+2000
order by avg(salary);

select department_id,avg(salary) from employees where emp_name not like '_a%' group by department_id;

select emp_name from employees where emp_name not like '_a%';

select avg(salary) from employees;

-- �μ��� �ִ� ������ 7000 �̻��� �͸� ����Ͻÿ�.

select department_id, max(salary) from employees group by department_id having max(salary) >= 8000 order by max(salary);

-- ����
-- RDBMS
select emp_name, department_id, salary from employees;
select department_id, department_name from departments;

select count(*) from employees,departments; -- 107*27

-- equi join = 106�� (null�� ����)
-- �� ���̺� �� ���� column�� ������ ���ؼ� �ش�Ǵ� �����͸� ���
select employee_id, emp_name, employees.department_id, department_name, salary from employees, departments where employees.department_id=departments.department_id;

select department_id, department_name from departments;
select department_id from employees;

select * from board;
select * from member;

update member set name = 'ȫ�浿' where id='aaa';

select board.*, member.name from board,member where member.id=board.id;     -- equi ����!!!!!!!!!!!









