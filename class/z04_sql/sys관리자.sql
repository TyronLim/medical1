alter session set "_ORACLE_SCRIPT"=true;

create user ora_user identified by 1111;

grant connect, resource, dba to ora_user;

drop user ora_user2;
drop user ora_user;

revoke connect, resource, dba from ora_user;