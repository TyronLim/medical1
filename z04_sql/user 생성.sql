alter session set "_ORACLE_SCRIPT"=true;

create user "ora_user1" identified by "1111";

grant connect, resource, dba to "ora_user1";