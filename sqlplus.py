cmd> sqlplus /nolog
SQL> conn  sys/oracle as sysdba
SQL> alter user scott
        identified by oracle
        account unlock;
SQL> conn scott/oracle
SQL> select table_name from user_tables;
SQL> describe emp

describe dept
select * from dept; --모든 데이터 조회
select dname, loc 
from dept;

select deptno from emp;  --14rows
select distinct deptno from emp;
select sal, sal*12 from emp;
select  min(sal), max(sal), sum(sal), avg(sal) from emp;

select empno, ename, sal, deptno
from emp
where deptno=10 ;   ---필터조건    여러 조건인 경우 and, or, not과 함께 사용

#null값의 의미 , 값이 존재하지 않음, 산술연산 , 비교연산, 논리연산 모두 null을 리턴

select deptno, avg(sal)
from emp
group by deptno;  --그룹핑 

select ..........         -------4
from  대상객체    -------1
where 조건         -------2
group by            -------3

부서별 급여평균이 2500이상인 부서번호와 부서평균급여를 검색, 출력
select deptno, avg(sal)
from emp
group by deptno
having avg(sal) >=2500;

select ..........         -------5
from  대상객체    -------1
where 조건         -------2
group by            -------3
having 그룹함수 조건  -----4


select....

테이블에 데이터가 저장된 순서는 데이터 추가한 순서(block에 쌓여진 순서) - heap table
정렬결과를 반환 받으려면
select.... ----5
from 대상객체 ----1
where 조건 ----2
group by ----3
having 그룹함수 조건 ----4
order by 칼럼 asc|desc ----6

select empno, ename, sal
from emp
order by sal desc;

conn/ as sysdba
alter user hr
identified by oracle
account unlock;

conn hr/oracle
desc employees

Quiz>관리자가 없는 사원을 제외하고, 부서로 그룹핑해서 부서별 평균 6000이상인 부서번호와
그 부서의 평균급여를 검색해서 평균급여의 내림차순으로 정렬한 결과를 출력하시오.

manager_id
department_id
salary

answer
select department_id, avg(salary)
from employees
where manager_id is not null
group by department_id
having avg(salary) >= 6000
order by avg(salary) desc;

SQL -
DML(데이터 검색, 데이터 추가, 수정, 삭제)
DDL(객체 생성, 객체구조 변경, 객체 삭제)
DCL(권한주기, 회수)
TCL(트랜직션 제어)

conn scott/oracle
insert into dept(deptno#수, dname#문자)
values(50, 'IT'); ----메모리에만 추가
select *from dept;

conn scott/oracle
insert into dept(deptno#수, dname#문자)
values(60, 'null', 'null'); --insert~values 절로는 1개의 row만 추가됨
select *from dept;


create table tdepp(deptno number(3), dname varchar2(20), loc varchar2(30));
                 desc tdepp
                 select *from tdepp;---row 없음
                 insert into tdepp

                 select * from dept;

                 select * from tdepp;

--row의 컬럼값을 변경
                 update 테이블명 set 컬럼명 = 변경갓,....,'
                 update 테이블명 set 컬럼명 = 변경값,....where 조건;

                 select ename, sal
                 from emp;
                 update emp set sal = 0;
                 select ename, sal
                 from emp;
                 rollback;
                 select ename, sal
                 from emp;
                 
