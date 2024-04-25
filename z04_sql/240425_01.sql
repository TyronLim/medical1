-- ���� ���� ����
select sysdate-1, sysdate, sysdate+1 from dual;

select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;       --�� ���� ù ��, ������ ��
select sysdate-hire_date from employees;                 -- �� ��¥�� (�ϼ�)!!!!!!!!!!!!!!!!!!!!!!!!!
select trunc(months_between(sysdate,hire_date),2) from employees; -- �� ��¥�� (�޼�)!!!!!!!!!!!!!!!!!!!!!!!!!

select trunc(kor,-1) ko, count(trunc(kor,-1)) from stu_score group by trunc(kor,-1) order by ko;    -- trunc �ϴ��� ����

-- hire_date���� ���� ����Ͻÿ�.
select to_char(hire_date,'mm') from employees;
select to_char(hire_date,'yyyy-mm-dd') from employees;

--hire_date 2008�⵵ ���, �⵵�� �ο��� ���
select * from employees;
select hire_date from employees where to_char(hire_date,'yyyy') = 2008;
select hire_date from employees group by to_char(hire_date,'yyyy'); ---------------------------------------------------------------

-- ����ȯ number, character, date
-- number : ��Ģ���� ����, ��ǥǥ�� �ȵ�, ��ȭ ǥ�� �ȵ�
-- char : ��Ģ���� �ȵ�, ��ǥ ǥ�� ����, ��ȭ ǥ�� ����, || ����
-- date : +,- ����, ��¥ ������´� ���� �Ұ�.

-- ������, ��¥�� �⵵�� �й��� �ο��ϱ�. (ko20240001)
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;

select to_char(to_number('123,456,789','999999999')+to_number('156,788','999999'),'999,999,999') from dual;


select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;

select to_char(salary,'999,999') salary from employees;

-- ���� Ÿ���� ��¥ Ÿ������
select 20240426 from dual;
select to_char(20240426)+3 from dual;   --���� �ȿ� ���ڸ� ������ ���ڷ� �������.
select to_date(20240426) from dual;

select emp_name, hire_date from employees where hire_date>to_date(20070101);    -- ���ڸ� ��¥�� ����
select hire_date, emp_name from employees order by hire_date;

-- 08�� ���� �Ի���, ����̸� 2��°�� a�� �� �ִ� ��� ���
select hire_date, emp_name from employees where to_number(to_char(hire_date,'mm'))=8 and emp_name like '_a%';

-- 20070101 ���� �Ի��� ��� �̸� 2��°�� a�� �� �ִ�
select hire_date, emp_name from employees where hire_date>=to_date(20070101) and emp_name like '_a%' order by hire_date;

-- 1,5,8�� �Ի�
select hire_date from employees where to_char(hire_date,'mm') in('01','05','08');

select emp_name from employees where emp_name like '_a%';

select emp_name, hire_date from employees where emp_name like '_a%' and to_char(hire_date,'mm') in('01','05','08') order by hire_date;

select sysdate+'20240401' from dual;
select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;
select * from m_date;
insert into m_date(m_no,m_yesterday,m_today,m_tomorrow) values(
seq_mno.nextval,'2024-04-01',sysdate,sysdate-to_date('2024-04-01')
);

create table eventDate(
eno number,
e_today date,
e_choice date,
e_period number
);
-- �Է� �� ��¥ Ÿ�Կ� ���ڸ� �Է��ص� �����
insert into eventDate values(seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01'));

select * from eventDate;

-- ����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- null�� 0���� ġȯ nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo
select manager_id from employees order by manager_id desc;

select nvl(to_char(manager_id),'CEO') from employees order by manager_id desc;

-- �׷��Լ� count : null ���� �����ϰ� ī��Ʈ
select count(emp_name) from employees; 
select count(manager_id) from employees;    -- null is excluded
select count(*) from employees;     -- ��ü �� ����
select emp_name, manager_id from employees;

-- sum
select sum(salary) from employees;

-- avg
select avg(salary) avg_sal from employees;

-- min 
select min(salary) from employees;

-- max
select max(salary) from employees;

--higher than 6461(salary)
select emp_name, salary from employees where salary > (select avg(salary) from employees);

-- �׷��Լ� : sum, avg, count, min, max

-- �ּ� ������ �޴� ����� ���, �̸�
select employee_id,emp_name,salary from employees where salary=(select min(salary) from employees);
select min(salary) from employees;
select * from employees;

-- �ִ����
select employee_id, emp_name, salary from employees where salary = (select max(salary) from employees);

-- 50���� ����� ��ü ����
select department_id, salary from employees where department_id = 50;

-- kor > 80
select no,name,kor from stu_score where kor > 80;

-- kor > kor_avg, eng > eng_avg
select no,name,kor,eng from stu_score where kor>(select avg(kor) from stu_score) and eng>(select avg(eng) from stu_score);
select avg(kor),avg(eng) from stu_score;

create table s_info (
s_no number,
s_count number
);

insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score where kor>(select avg(kor) from stu_score) and eng>(select avg(eng) from stu_score))
);

select * from s_info;

-- �������� �ְ����� �л�, �������� �ְ����� �л�, �������� �ְ����� �л��� ����Ͻÿ�.
select no,name,kor,eng,math from stu_score 
where kor=(select max(kor) from stu_score) 
or eng=(select max(eng) from stu_score)
or math=(select max(math) from stu_score)
order by kor desc;

select * from employees where salary=(select max(salary) from employees) or salary=(select min(salary) from employees) or salary = trunc((select avg(salary) from employees),-2);
select trunc(avg(salary)) from employees;

select emp_name,salary from employees where salary=(select max(salary) from employees);

select emp_name, salary from employees where salary<=(select avg(salary) from employees) order by salary;

select max(salary) from (select emp_name, salary from employees where salary<=(select avg(salary) from employees) order by salary);

-- ��հ����� ���� ��� �߿� �ִ밪�� ����Ͻÿ�.
-- 1. ��հ����� ���� ���
-- 2. �� �߿� ���� ���� ���
select emp_name, salary from employees where salary=(select max(salary) from (select emp_name, salary from employees where salary<=(select avg(salary) from employees) order by salary));

-- �����Լ�
-- LPAD RPAD : �� ���� ä���
select emp_name, lpad(emp_name,16,'#') from employees; 
select emp_name, rpad(emp_name,15,'#') from employees;

-- ltrim rtrim : ���� ���ֱ�
select emp_name,ltrim(emp_name,'Do') from employees;

select 'ko20240001',ltrim('ko20240001','ko2024') from dual;

select emp_name, substr(emp_name,3,4) from employees;   --substr : (������,����,����)

select substr(job_id,1,2)||employee_id from employees;

select emp_name, length(emp_name) from employees where length(emp_name)>15; --length : ���ڿ� ����

-- ��¥�Լ� : ��¥���� ���ϴ� �� �� ��.
select sysdate+1 from dual; -- ��¥+����
select sysdate-hire_date from employees; -- ��¥-��¥
select round(sysdate,'month') from dual;    -- ���� �ݿø� ��
select trunc(sysdate,'month') from dual;    -- ���� ������ ��
select round(sysdate,'year') from dual;     -- �� �ݿø� ��
select add_months(sysdate,-2) from dual;     -- ���� �� �߰�/����

select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;   -- �ø�, ����, ������, ����

select emp_name from employees;
select emp_name||to_char(hire_date,'yyyy')||'��'||to_char(hire_date,'mm')||'��'||to_char(hire_date,'dd')||'��'||to_char(hire_date,'day') from employees;
select emp_name||to_char(hire_date,'yyyy"��"mm"��"dd"��"') from employees;

select emp_name||to_char(salary+1400,'L000,000,000') from employees;

select '2010-10-10',last_day('20101010') from dual;
select trunc(to_date('20101010'),'month') from dual;

select * from member;

desc member;

-- ���̺� column �߰�!!!!       ** Ŀ��, �ѹ��� �Ұ�
alter table member add gender varchar2(6) default 'female' not null;
-- ���̺� column ����!!          ** Ŀ��, �ѹ� ���� �Ұ�
alter table member drop column phone;
-- ���̺� column ����!!  �̸�, Ÿ��
alter table member rename column name to stu_name;  -- column  �̸� ����!
alter table member modify(stu_name varchar2(50));   -- column  Ÿ�� ����!
alter table member modify(stu_name number(30));    -- Ÿ���� �޶� �Ұ���! (����־�� ��)
alter table member modify(stu_name varchar2(3));    -- ���� ���� ���̰������Ǿ �Ұ���!
alter table member modify(stu_name varchar2(9));
select * from member;
update member set gender = 'male';
update member set stu_name='ȫ';

commit;





