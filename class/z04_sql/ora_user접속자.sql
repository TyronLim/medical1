create table stu_score(
 no number(4) primary key,
 name varchar2(30),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(6)
);

--1개의 데이터입력: insert
insert into stu_score (no,name,kor,eng,math,total,avg) values(
 1,'홍길동',58,99,95,(58+99+95),(58+99+95)/3
 
);

select * from stu_score;

commit;

--데이터 수정 : update
update stu_score set name='홍길자' where no=1;
select * from stu_score;

rollback;
select * from stu_score;

desc stu_score;

--삭제 delete
delete stu_score where no=1;

select * from stu_score;

drop table stu_score;




