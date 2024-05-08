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
select * from employees;

select phone_number from (
select a.department_id, c.department_name,b.emp_name from employees a, employees b, departments c 
where a.department_id=b.department_id and a.emp_name = 'Pat Fay' and a.department_id = c.department_id; 
)d where d.employees_id = 198;

select * from departments;

update member set name = '홍길동' where memno = 1;

select * from member order by memno;
-- hhh 1111 홍길자 여자 sysdate
delete from member where memno=13;

commit;

create table mem (id varchar2(30) primary key,pw number,name varchar2(30),mdate date);

select * from mem;

--drop table mem;

create table yeogi(
yno number(4) primary key,
titel varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number
);

alter table yeogi change img img varchar2(130); 



select * from yeogi order by yno;
select yeogi_seq.nextval from dual;
drop sequence yeogi_seq; 
delete from yeogi; 


