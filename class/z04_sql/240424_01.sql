select sysdate, hire_date, trunc(sysdate-hire_date,3) from employees;   -- �Ҽ��� 3¥���� ����� ����.
select sysdate, hire_date, round(sysdate-hire_date,1) from employees;   -- �Ҽ��� 1°�ڸ� ����� �ݿø�

--���� : sysdate-1 , ���� : sysdate+1
select sysdate-1 ����, sysdate ����, sysdate+1 ���� from dual;

-- ���� m_no, m_yesterday, m_today, m_tomorrow, m_year �÷��� ���� ���̺� m_date ����
-- ����, ����, ����, 1�� �� ��¥�� ����

create sequence m_no
increment by 1
minvalue 1
maxvalue 100
nocycle
nocache;

create table m_date(
m_no number(2),
m_yesterday VARCHAR2(15),
m_today varchar(15),
m_tomorrow varchar(15),
m_year varchar(15)
);

insert into m_date values(
m_no.nextval,sysdate-1,sysdate,sysdate+1, sysdate+365);


update m_date set
m_no = m_no.nextval,
m_yesterday = (sysdate-1),
m_today = sysdate,
m_tomorrow = (sysdate+1),
m_year = sysdate+365
;

select * from m_date;

select abs(hire_date-sysdate) from employees;  -- ���밪(����� ǥ��)

-- ���밪 abs, �ø� ceil, �ݿø� round, ���� trunc, ���� floor

select hire_date, round(hire_date,'month') from employees; -- ���� �������� �ݿø�

select hire_date, trunc(hire_date,'month') from employees; -- ���� �������� ����

select trunc(hire_date,'month') ������ ,hire_date from employees order by hire_date;
select * from channels;

select period, count(period) from kor_loan_status 
group by period
order by period;

select period from kor_loan_status where period='201111';

select trunc(kor,-1) t_kor,count(trunc(kor,-1)) count from students         --1° �ڸ����� ����
group by trunc(kor,-1)
order by t_kor;  

select trunc(hire_date,'month') m_hire_date,count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date;

--drop table stu_score;
--drop table emp01;
--drop table board;

select * from stu_score order by no;
update stu_score set name='������' where no=10;

update stu_score set avg=(total/3);

--2���� ��¥���� �� ������ Ȯ��
select hire_date, floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date) from employees;

-- ���� �߰�
select hire_date, add_months(hire_date,6) from employees;

-- last day
select hire_date, last_day(hire_date), round(hire_date,'d') from employees;

select sysdate,round(sysdate,'d') from employees;   -- ���� �ݿø� ��~��(���� = ������ ����)
select sysdate,trunc(sysdate,'d') from employees;   -- ���� ���� ��~ ��(��� = ������ ����)
select sysdate,trunc(sysdate,'month') from employees;   -- �� ���� ù°��
select sysdate ������,trunc(sysdate,'month') ó����,last_day(sysdate) �������� from employees;

-- �������
select sysdate, next_day(sysdate,'�����') from dual;  -- Ư�� ���� Ȯ��

-- ������ ó����
select sysdate, trunc(sysdate,'d') from dual;
select sysdate, next_day(sysdate,'������') from dual;


create table board(
bno number(4) primary key, -- �⺻Ű
id varchar2(30),
btitle varchar2(1000),
bcontent clob,             -- ������ 
bdate date default sysdate,         --- �Է��� ���� �� ������ �ڵ� �Է� �� (���� ��¥��)
bhit number default 0,
dgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','�����Դϴ�','�����Դϴ�',sysdate,0,board_seq.currval,0,0,'1.jpg');

insert into board(bno,id,btitle,bcontent,dgroup,bfile) values(
board_seq.nextval,'bbb','�̺�Ʈ ��û','�̺�Ʈ�� ��û�մϴ�.',board_seq.currval,'2.jpg'
);

select * from board;

--�� ��ȯ nnmber, character, date
select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(board_seq.nextval,'0000')) from dual;

select to_char(sysdate,'dy'), to_char(sysdate,'day') from dual;
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

select to_char(hire_date,'yyyy-mm-dd hh:mi:ss mon day') from employees;

select to_char(sysdate,'pm hh24:mi:ss') from dual;    -- ���� ���� 24�ð�

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

select c_date from stu_score
group by c_date
order by c_date;

-- ������ : ��Ģ���� �Ұ�. �ڸ��� ǥ�� ����, ��ǥ ǥ�� ����, ��¥���� ǥ�� (yyyy-mm-dd)
-- ������ : ��Ģ���� ����. �ڸ��� ǥ�� �Ұ�, ��ǥ ǥ�� �Ұ�
-- ��¥�� : + - �� ����. months_between 2�� ��¥�� �� ���, ��¥ ���� �����ؼ� ����� �� ��.

select 10,100, 10+100,to_char(100),10+to_char(300) from dual;   -- ������ �� �����Ͱ� ���ڸ� ��� ����.
select 10,100, 10+100,to_char(100),10+'100��' from dual;

select 12340000, to_char(12340000),to_char(12340000,'999,999,999') from dual;  -- ���ڸ� ���ڷ� ��ȯ�ϸ鼭 ��ǥ�� ����
select 12340000, to_char(12340000),to_char(12340000,'000,999,999'),length(to_char(12340000,'000,999,999')) from dual;   -- '0000' ���ڸ��� 0���� ä��. '9999'�� ���ڸ� ��.
select length('�ȳ��ϼ���') from dual;       --length�� ���ڵ� ����.
select length(12340000) from dual;     

select 12340000, to_char(12340000,'L999,999,999') from dual;    -- L : ��ȭ, �޷� �� ǥ�� (OS�� ������)
select 12340000, to_char(12340000,'$999,999,999') from dual;
select 1234.1234,to_char(1234.1234,'000,999.99') from dual;     -- �Ҽ��� �ڸ� ǥ��

select to_char(12345,'0000000000'),to_char(12345,'999,999') from dual; --�ڸ��� to_char ���� �� �տ� ���� ����. length�� 1�� �� ����.

-- ����
-- 123,456,789 + 100,000 �� ǥ��. õ���� ���

select to_char(123456789+100000,'999,999,999') from dual;

select trim(to_char(substr('123,456,789',0,3))||to_char(substr('123,456,789',5,3))||to_char(substr('123,456,789',9,3)))+trim(to_char(substr('100,000',0,3))||
to_char(substr('100,000',5,3)))
from dual;   -- ������� �����

select to_char(replace('123,456,789',',','')+replace('100,000',',',''),'L999,999,999') from dual;


select to_date('2024-04-24')-to_date('2024-04-01') from dual;       --��¥ ��� : to_date�� ��ȯ�� ���.
select to_date('2024/04/24')-to_date('2024/04/01') from dual;
select to_date('24/04/24')-to_date('24/04/01') from dual;
select to_date('20240401') from dual;

select to_char(to_date('20240401'),'yyyy-mm-dd') from dual;

select hire_date from employees
where hire_date >= '20070601';

select c_date from stu_score
where c_date = '2024/04/05';

select sysdate-to_date('2024/04/01') from dual;

select trim(to_char(replace('20,000',',','')-replace('10,000',',',''),'999,999')) from dual;    -- replace�� �� ��ȯ
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;          -- to_number�� �� ��ȯ

select commission_pct from employees;
-- ���� ���� = ���� + ����*commission  .  ���� ���� ����ϱ�
select salary, commission_pct, (salary + (salary*nvl(commission_pct,0))) �������� from employees;

select commission_pct from employees where commission_pct is null;

select manager_id from employees order by manager_id;

select manager_id, nvl(manager_id,0) from employees order by manager_id desc; 
select manager_id, nvl(to_char(manager_id),'ceo') from employees order by manager_id desc;

commit;








