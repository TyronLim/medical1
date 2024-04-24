select sysdate, hire_date, trunc(sysdate-hire_date,3) from employees;   -- 소수점 3짜까지 남기고 버림.
select sysdate, hire_date, round(sysdate-hire_date,1) from employees;   -- 소수점 1째자리 남기고 반올림

--어제 : sysdate-1 , 내일 : sysdate+1
select sysdate-1 어제, sysdate 오늘, sysdate+1 내일 from dual;

-- 퀴즈 m_no, m_yesterday, m_today, m_tomorrow, m_year 컬럼을 가진 테이블 m_date 생성
-- 어제, 오늘, 내일, 1년 후 날짜를 저장

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

select abs(hire_date-sysdate) from employees;  -- 절대값(양수로 표현)

-- 절대값 abs, 올림 ceil, 반올림 round, 버림 trunc, 내림 floor

select hire_date, round(hire_date,'month') from employees; -- 월을 기준으로 반올림

select hire_date, trunc(hire_date,'month') from employees; -- 월을 기준으로 버림

select trunc(hire_date,'month') 기준일 ,hire_date from employees order by hire_date;
select * from channels;

select period, count(period) from kor_loan_status 
group by period
order by period;

select period from kor_loan_status where period='201111';

select trunc(kor,-1) t_kor,count(trunc(kor,-1)) count from students         --1째 자리에서 버림
group by trunc(kor,-1)
order by t_kor;  

select trunc(hire_date,'month') m_hire_date,count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date;

--drop table stu_score;
--drop table emp01;
--drop table board;

select * from stu_score order by no;
update stu_score set name='관순스' where no=10;

update stu_score set avg=(total/3);

--2개의 날짜에서 월 간격을 확인
select hire_date, floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date) from employees;

-- 개월 추가
select hire_date, add_months(hire_date,6) from employees;

-- last day
select hire_date, last_day(hire_date), round(hire_date,'d') from employees;

select sysdate,round(sysdate,'d') from employees;   -- 요일 반올림 일~토(기준 = 수요일 정오)
select sysdate,trunc(sysdate,'d') from employees;   -- 요일 버림 일~ 토(기분 = 수요일 정오)
select sysdate,trunc(sysdate,'month') from employees;   -- 그 달의 첫째날
select sysdate 현재일,trunc(sysdate,'month') 처음일,last_day(sysdate) 마지막일 from employees;

-- 현재요일
select sysdate, next_day(sysdate,'토요일') from dual;  -- 특정 요일 확인

-- 요일의 처음일
select sysdate, trunc(sysdate,'d') from dual;
select sysdate, next_day(sysdate,'수요일') from dual;


create table board(
bno number(4) primary key, -- 기본키
id varchar2(30),
btitle varchar2(1000),
bcontent clob,             -- 무제한 
bdate date default sysdate,         --- 입력이 없을 시 데이터 자동 입력 됨 (현재 날짜로)
bhit number default 0,
dgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','제목입니다','내용입니다',sysdate,0,board_seq.currval,0,0,'1.jpg');

insert into board(bno,id,btitle,bcontent,dgroup,bfile) values(
board_seq.nextval,'bbb','이벤트 신청','이벤트를 신청합니다.',board_seq.currval,'2.jpg'
);

select * from board;

--형 변환 nnmber, character, date
select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(board_seq.nextval,'0000')) from dual;

select to_char(sysdate,'dy'), to_char(sysdate,'day') from dual;
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

select to_char(hire_date,'yyyy-mm-dd hh:mi:ss mon day') from employees;

select to_char(sysdate,'pm hh24:mi:ss') from dual;    -- 오전 오후 24시간

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

select c_date from stu_score
group by c_date
order by c_date;

-- 문자형 : 사칙연산 불가. 자리수 표시 가능, 쉼표 표시 가능, 날짜형태 표시 (yyyy-mm-dd)
-- 숫자형 : 사칙연산 가능. 자리수 표시 불가, 쉼표 표시 불가
-- 날짜형 : + - 만 가능. months_between 2개 날짜간 달 계산, 날짜 유형 지정해서 출력이 안 됨.

select 10,100, 10+100,to_char(100),10+to_char(300) from dual;   -- 문자형 속 데이터가 숫자면 계산 해줌.
select 10,100, 10+100,to_char(100),10+'100원' from dual;

select 12340000, to_char(12340000),to_char(12340000,'999,999,999') from dual;  -- 숫자를 문자로 변환하면서 쉼표를 넣음
select 12340000, to_char(12340000),to_char(12340000,'000,999,999'),length(to_char(12340000,'000,999,999')) from dual;   -- '0000' 빈자리는 0으로 채움. '9999'는 빈자리 둠.
select length('안녕하세요') from dual;       --length가 숫자도 해줌.
select length(12340000) from dual;     

select 12340000, to_char(12340000,'L999,999,999') from dual;    -- L : 원화, 달러 등 표시 (OS를 구분함)
select 12340000, to_char(12340000,'$999,999,999') from dual;
select 1234.1234,to_char(1234.1234,'000,999.99') from dual;     -- 소수점 자리 표시

select to_char(12345,'0000000000'),to_char(12345,'999,999') from dual; --자리수 to_char 했을 때 앞에 공백 조심. length가 1개 더 나옴.

-- 퀴즈
-- 123,456,789 + 100,000 값 표시. 천단위 출력

select to_char(123456789+100000,'999,999,999') from dual;

select trim(to_char(substr('123,456,789',0,3))||to_char(substr('123,456,789',5,3))||to_char(substr('123,456,789',9,3)))+trim(to_char(substr('100,000',0,3))||
to_char(substr('100,000',5,3)))
from dual;   -- 몇번부터 몇개까지

select to_char(replace('123,456,789',',','')+replace('100,000',',',''),'L999,999,999') from dual;


select to_date('2024-04-24')-to_date('2024-04-01') from dual;       --날짜 계산 : to_date로 변환해 계산.
select to_date('2024/04/24')-to_date('2024/04/01') from dual;
select to_date('24/04/24')-to_date('24/04/01') from dual;
select to_date('20240401') from dual;

select to_char(to_date('20240401'),'yyyy-mm-dd') from dual;

select hire_date from employees
where hire_date >= '20070601';

select c_date from stu_score
where c_date = '2024/04/05';

select sysdate-to_date('2024/04/01') from dual;

select trim(to_char(replace('20,000',',','')-replace('10,000',',',''),'999,999')) from dual;    -- replace로 형 변환
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;          -- to_number로 형 변환

select commission_pct from employees;
-- 실제 월급 = 월급 + 월급*commission  .  실제 월급 출력하기
select salary, commission_pct, (salary + (salary*nvl(commission_pct,0))) 실제월급 from employees;

select commission_pct from employees where commission_pct is null;

select manager_id from employees order by manager_id;

select manager_id, nvl(manager_id,0) from employees order by manager_id desc; 
select manager_id, nvl(to_char(manager_id),'ceo') from employees order by manager_id desc;

commit;








