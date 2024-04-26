-- 테이블 생성
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- 테이블 구조, 데이터 모두 복사하기
desc employees;

create table emp02 as select * from employees;

select * from emp02;
select * from employees;

-- 테이블 구조만 복사하기
create table emp03 as select * from employees where 1=2;    -- false 값을 고의로 넣어서 행을 빼고 열만 추가
select * from emp03;

-- 테이블이 존재하면서 데이터만 복사하기
select * from emp01;
select * from employees;
insert into emp01(emp_id, emp_name, hire_date)
select employee_id,emp_name,hire_date from employees order by employee)id asc;
insert into emp01 values(207,'홍길동','2024-04-26');

-- 테이블이 존재하면서 데이터만 복사 (구조가 같아야 함)
insert into emp3 select * from employees;
select * from emp01 order by emp_id desc;


drop table s_info;
drop table m_date;

desc member;

-- 타입변경
alter table member modify(stu_name varchar2(30));
desc member;

--column 삭제
alter table member drop column pw;

alter table member add(pw varchar2(30));

-- column 순서 바꾸기

select * from member;

insert into member values(
seq_mno.nextval, 'ggg','김유신','male','1111'
);

-- 컬럼 순서 변경
alter table member modify stu_name invisible;
alter table member modify gender invisible;

alter table member modify stu_name visible;
alter table member modify gender visible;

alter table member set unused(id);  -- column 일시적 사용 제한

select * from member;

alter table member drop unused columns;     -- 사용제한 해제

select * from member;

--테이블 삭제
drop table emp03;

rename emp01 to employees01;

select * from departments;


-- 무결성 제약조건
-- foreign key는 다른 테이블에서 데이터 입력 시
-- 선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인

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

insert into member values('aaa','1111','홍길동','male');
insert into member(id,pw,name) values('bbb',1111,'유관순');
insert into member(id,pw) values('ccc',1111);
insert into member(id) values('ddd');    --error
insert into member(id,pw) values('ddd',1111);
insert into member(id,pw) values('aa',1111);
insert into member(id,pw,name) values('aa',1111,'홍길동');

select * from member;

create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(1,'임태균','PD',033);
insert into emp02(empno,ename,job) values(2,'이순신','soldier');
insert into emp02(empno,ename) values(3,'고구부');
insert into emp02(empno,ename) values(4,'고사유');
insert into emp02(empno,ename) values(5,'고을불');

update emp02 set deptno=30 where empno=1;

select * from emp02;

create table emp03(
empno number(4) unique, -- 중복 방지 ( null은 허용 )
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03 values(1,'홍길동','1',1);
insert into emp03 values(null,'홍길동','1',1);
insert into emp03 values(null,'이순신','1',1);
insert into emp03 values(3,'유관순','2',2);
insert into emp03 values(4,'강감찬','2',2);
insert into emp03 values(null,'임태균','3',3);
select * from emp03;

select * from emp03 where empno = 1;
select * from emp03 where ename = '홍길동' and empno is null;
select * from emp03 where empno is null;
select * from emp03 where empno is not null;

create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp01 values(1,'홍길동','1',1);
insert into emp01 values(2,'고구부','2',2);
insert into emp01 values(3,'고사유','3',3);
insert into emp01 values(4,'홍길동','4',4);

select * from emp01;
select * from emp01 where ename = '홍길동';

--foreign key 외래키
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

insert into emp01 values(1,'홍길동','0001',10);
insert into emp01 values(2,'유관순','0002',20);
insert into emp01 values(3,'이순신','0002',30);

insert into dept01 values(10,'aa');
commit;

-- emp01에 foreign key 추가------------------------------------------------------------------
alter table emp01 add constraint fk_deptno foreign key(deptno)
references dept01(deptno);

alter table emp01 drop constraint fk_deptno;

insert into emp01 values(4,'김구','0003',270);


create table board(
bno number(4) primary key, 
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(1,'aaa','게시글1','내용1');
insert into board values(2,'bbb','게시글2','내용2');
insert into board values(3,'ccc','게시글2','내용2');
insert into board values(4,'ddd','게시글4','내용4');
insert into board values(8,'bbb','게시글8','내용8');

alter table board add constraint fk_id foreign key(id)
references member(id);

commit;
select * from board;

update board set btitle='게시글6' where bno=6;
update board set bcontent='내용6' where bno=6;

--comment 테이블 (댓글테이블)
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
insert into comments values (2,1,'1111','댓글내용2');    --댓글
commit;
select * from comments order by cno;
-- fk 등록 시 설정1 > fk키로 등록되어 있는 모든 데이터를 삭제시키는 것.
-- fk 등록 시 설정2 > fk키로 등록되어 있는 데이터는 모두 존재 시키는 것.

delete board where bno=5;

alter table board drop constraint fk_id; -- 외래키 삭제

select * from comments;
select * from board;

delete board where bno=1;

alter table comments drop constraints fk_bno;

-- fk_cno 삭제가 되면 
alter table comments add constraint fj_cno foreign key(bno)
references board(bno) on delete cascade;

delete comments where cno=2;

--check : 특정값의 범위, 특정값 만 입력되도록 함
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', -- 디폴트값
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in('남자','여자'))
);

insert into emp(empno, ename,job,sal,gender) values(
1,'홍길동','0001',3000,'남자');


insert into emp(empno, ename,job,sal,gender) values(
2,'유관순','0002',4000,'여자');

insert into emp(empno, ename,job,sal,gender) values(
3,'이순신','0004',5000,'중성');  --- 불가. check 제약조건 위배 (남자, 여자)

insert into emp(empno, ename,job,sal,gender) values(
3,'이순신','0004',5000,'남자');

insert into emp(empno, ename,job,sal,gender) values(
4,'강감찬','0005',2000,'남자');

insert into emp(empno, ename,job,sal,gender) values(
5,'김구','0006',1000,'남자');       -- 불가. check 제약조건 위배 (2000~20000)

insert into emp(empno, ename,job,sal,gender) values(
5,'김구','0006',20000,'남자'); 

insert into emp(empno, ename,sal,gender) values(
6,'김유신',10000,'남자');        -- default

select * from emp;






