-- ���̺� ����
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- ���̺� ����, ������ ��� �����ϱ�
desc employees;

create table emp02 as select * from employees;

select * from emp02;
select * from employees;

-- ���̺� ������ �����ϱ�
create table emp03 as select * from employees where 1=2;    -- false ���� ���Ƿ� �־ ���� ���� ���� �߰�
select * from emp03;

-- ���̺��� �����ϸ鼭 �����͸� �����ϱ�
select * from emp01;
select * from employees;
insert into emp01(emp_id, emp_name, hire_date)
select employee_id,emp_name,hire_date from employees order by employee)id asc;
insert into emp01 values(207,'ȫ�浿','2024-04-26');

-- ���̺��� �����ϸ鼭 �����͸� ���� (������ ���ƾ� ��)
insert into emp3 select * from employees;
select * from emp01 order by emp_id desc;


drop table s_info;
drop table m_date;

desc member;

-- Ÿ�Ժ���
alter table member modify(stu_name varchar2(30));
desc member;

--column ����
alter table member drop column pw;

alter table member add(pw varchar2(30));

-- column ���� �ٲٱ�

select * from member;

insert into member values(
seq_mno.nextval, 'ggg','������','male','1111'
);

-- �÷� ���� ����
alter table member modify stu_name invisible;
alter table member modify gender invisible;

alter table member modify stu_name visible;
alter table member modify gender visible;

alter table member set unused(id);  -- column �Ͻ��� ��� ����

select * from member;

alter table member drop unused columns;     -- ������� ����

select * from member;

--���̺� ����
drop table emp03;

rename emp01 to employees01;

select * from departments;


-- ���Ἲ ��������
-- foreign key�� �ٸ� ���̺��� ������ �Է� ��
-- ����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ��

--drop table employees01;
--drop table member;
--drop table emp02;
--drop table board;

create table member (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values('aaa','1111','ȫ�浿','male');
insert into member(id,pw,name) values('bbb',1111,'������');
insert into member(id,pw) values('ccc',1111);
insert into member(id) values('ddd');    --error
insert into member(id,pw) values('ddd',1111);
insert into member(id,pw) values('aa',1111);
insert into member(id,pw,name) values('aa',1111,'ȫ�浿');

select * from member;

create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(1,'���±�','PD',033);
insert into emp02(empno,ename,job) values(2,'�̼���','soldier');
insert into emp02(empno,ename) values(3,'����');
insert into emp02(empno,ename) values(4,'�����');
insert into emp02(empno,ename) values(5,'������');

update emp02 set deptno=30 where empno=1;

select * from emp02;

create table emp03(
empno number(4) unique, -- �ߺ� ���� ( null�� ��� )
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03 values(1,'ȫ�浿','1',1);
insert into emp03 values(null,'ȫ�浿','1',1);
insert into emp03 values(null,'�̼���','1',1);
insert into emp03 values(3,'������','2',2);
insert into emp03 values(4,'������','2',2);
insert into emp03 values(null,'���±�','3',3);
select * from emp03;

select * from emp03 where empno = 1;
select * from emp03 where ename = 'ȫ�浿' and empno is null;
select * from emp03 where empno is null;
select * from emp03 where empno is not null;

create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp01 values(1,'ȫ�浿','1',1);
insert into emp01 values(2,'����','2',2);
insert into emp01 values(3,'�����','3',3);
insert into emp01 values(4,'ȫ�浿','4',4);

select * from emp01;
select * from emp01 where ename = 'ȫ�浿';

--foreign key �ܷ�Ű
--drop table emp01;
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

create table dept01(
deptno number(2) primary key,
dept_name varchar2(20)
);

select * from departments;
alter table dept01 modify(deptno number(6));
alter table dept01 modify(deptno number(8));


insert into dept01(deptno,dept_name) select department_id, department_name from departments;

desc dept01;
desc emp01;

desc departments;

insert into emp01 values(1,'ȫ�浿','0001',10);
insert into emp01 values(2,'������','0002',20);
insert into emp01 values(3,'�̼���','0002',30);

insert into dept01 values(10,'aa');
commit;

-- emp01�� foreign key �߰�------------------------------------------------------------------
alter table emp01 add constraint fk_deptno foreign key(deptno)
references dept01(deptno);

alter table emp01 drop constraint fk_deptno;

insert into emp01 values(4,'�豸','0003',270);


create table board(
bno number(4) primary key, 
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(1,'aaa','�Խñ�1','����1');
insert into board values(2,'bbb','�Խñ�2','����2');
insert into board values(3,'ccc','�Խñ�2','����2');
insert into board values(4,'ddd','�Խñ�4','����4');
insert into board values(8,'bbb','�Խñ�8','����8');

alter table board add constraint fk_id foreign key(id)
references member(id);

commit;
select * from board;

update board set btitle='�Խñ�6' where bno=6;
update board set bcontent='����6' where bno=6;

--comment ���̺� (������̺�)
-- cno number(4) primary key, bno number(4) foreign key, cpw varchar2(20)
-- ccontent varchar2(1000)

create table comments(
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno) references board(bno)
);

select * from board;
insert into comments values (2,1,'1111','��۳���2');    --���
commit;
select * from comments order by cno;
-- fk ��� �� ����1 > fkŰ�� ��ϵǾ� �ִ� ��� �����͸� ������Ű�� ��.
-- fk ��� �� ����2 > fkŰ�� ��ϵǾ� �ִ� �����ʹ� ��� ���� ��Ű�� ��.

delete board where bno=5;

alter table board drop constraint fk_id; -- �ܷ�Ű ����

select * from comments;
select * from board;

delete board where bno=1;

alter table comments drop constraints fk_bno;

-- fk_cno ������ �Ǹ� 
alter table comments add constraint fj_cno foreign key(bno)
references board(bno) on delete cascade;

delete comments where cno=2;

--check : Ư������ ����, Ư���� �� �Էµǵ��� ��
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', -- ����Ʈ��
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in('����','����'))
);

insert into emp(empno, ename,job,sal,gender) values(
1,'ȫ�浿','0001',3000,'����');


insert into emp(empno, ename,job,sal,gender) values(
2,'������','0002',4000,'����');

insert into emp(empno, ename,job,sal,gender) values(
3,'�̼���','0004',5000,'�߼�');  --- �Ұ�. check �������� ���� (����, ����)

insert into emp(empno, ename,job,sal,gender) values(
3,'�̼���','0004',5000,'����');

insert into emp(empno, ename,job,sal,gender) values(
4,'������','0005',2000,'����');

insert into emp(empno, ename,job,sal,gender) values(
5,'�豸','0006',1000,'����');       -- �Ұ�. check �������� ���� (2000~20000)

insert into emp(empno, ename,job,sal,gender) values(
5,'�豸','0006',20000,'����'); 

insert into emp(empno, ename,sal,gender) values(
6,'������',10000,'����');        -- default

select * from emp;






