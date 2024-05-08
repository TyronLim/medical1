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
--1 update ����
update students a set rank = (rank)

--2 rank()����
(select rank() ocer(order by total desc) ranks from students) b;

--3 update ���� rank������ no �÷����� ��(rank �÷��� �˻�)


--4 students ���̺��� ranks�� �� �ִ� ���̺��� �־���.
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

--���� �Լ�------------------------------------
select -10, abs (-10) from dual;    -- ���밪
select 34.789, floor(34.789) as f, round(34.789) as r from dual;     -- �Ҽ��� ����,�Ҽ��� �ݿø�

select 34.178, round(34.178), round(34.178,2) from dual;        -- �ݿø� �ڸ���

select avg from students;
select round(avg,2) avg from students;

select 34.5678, round(34.5678,-1) from dual;    -- �ݿø� �����κ�

--trunc ������ �ڸ��� ���� ����
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;

-- �ø�
select ceil(34.123) from dual;
select ceil(34.123,2) from dual;-- �ȉ�. ����.

select trunc(kor,-1) from students order by kor desc;

select name, trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1) tot from students;

--mod ������
select round(100/7,2) from dual;
select mod(10,7) from dual;
select 10/7 from dual;

select employee_id from employees;
select employee_id, mod(employee_id,2) from employees where mod(employee_id,2)=0;

select no from students where mod(no,3)=0;

-- ������
create sequence seq_no 
increment by 1  --1�� �����ϴ� ��ȣ ����
start with 1    --1���� ����
minvalue 1      --�ּҰ�
maxvalue 1000   --�ִ밪
nocycle         --��ȯ ����
nocache         --ĳ�� ��� ����
;

select seq_no.nextval currval from dual;    --nextval  1�� ����

select seq_no.currval from dual;      -- currval ������ ��ȣ Ȯ��

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
seq_mno.nextval,'eee','1111','�豸','010-5555-5555');

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

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.currval,'00000')) as stuno from dual; -- trim () ��������

create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id vachar2(30),
bdate date,
bhit number(10)
);

--������ ����1001 ����10 1~99999   > 5�� ����

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
emp_seq.nextval, '�̼���', sysdate);

select * from emp01;

commit;

alter sequence emp_seq
increment by 1001
;

select * from employees;

select employee_id, emp_name, job_id, hire_date from employees order by hire_date;

select employee_id, emp_name,job_id, hire_date, ceil(sysdate-hire_date)||'��' from employees;

select emp_name from empolyees;

select substr(job_id,4)||trim(to_char(employee_id,'0000')) from employees;
select substr(job_id,0,2) from employees;       -- str �ڸ���

select substr('abcde',1,3) from dual;           -- ('str',a,b) a��°���� b���� �߶��!


select * from employees;

select substr(job_id,1,2)||trim(to_char(employee_id,'00000')) from employees;

--��¥ �Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

select MONTHS_BETWEEN(SYSDATE,hire_date) ����, sysdate-hire_date �ϼ� from employees;   --�� ��, �� ��

-- �������� �߰�
select sysdate,add_months(sysdate,2) from dual; --- ���� ��¥���� 2���� ���϶�.��

select next_day(sysdate,'������') from dual;   --���� ���������� �������� ������ �� ������.

select last_day(sysdate) from dual;     -- ���� ���������� �� ���� ������ ���� �˷���.

select last_day('2024-02-01') from dual;        -- 2024 02 01 ���������� �� ���� ������ ���� �˷���.





