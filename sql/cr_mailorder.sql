SET FOREIGN_KEY_CHECKS=0;
Drop table employees cascade constraints;
Drop table parts cascade constraints;
Drop table customers cascade constraints;
Drop table orders cascade constraints;
Drop table odetails cascade constraints;
Drop table zipcodes cascade constraints;
SET FOREIGN_KEY_CHECKS=1;
CREATE TABLE employees (
eno    INT(4),
ename  VARCHAR(18),
zip    VARCHAR(6),
hdate  DATE);
INSERT INTO employees VALUES (1000, 'JOHNS','67226', STR_TO_DATE('12-DEC-1995', '%d-%M-%Y'));
INSERT INTO employees VALUES (1001, 'SMITH','60606',STR_TO_DATE('01-JAN-1992', '%d-%M-%Y'));
INSERT INTO employees VALUES (1002, 'BROWN','50302',STR_TO_DATE('01-SEP-1994', '%d-%M-%Y'));
CREATE TABLE parts(
pno     INT(5),
pname   VARCHAR(30),
qoh     INT(4),
prices  DECIMAL(4,2),
wlevel  INT(2));
INSERT INTO parts VALUES (10506,'Land Before Time I',200,19.99,20);
INSERT INTO parts VALUES (10507,'Land Before Time II',156,19.99,20);
INSERT INTO parts VALUES (10508,'Land Before Time III',190,19.99,20);
INSERT INTO parts VALUES (10509,'Land Before Time IV',60,19.99,20);
INSERT INTO parts VALUES (10601,'Sleep Beauty',300,24.99,20);
INSERT INTO parts VALUES (10701,'When Harry Met Sally',120,19.99,30);
INSERT INTO parts VALUES (10800,'Dirty Harry',140,14.99,30);
INSERT INTO parts VALUES (10900,'Dr. Zhivago',100,24.99,30);
CREATE TABLE customers(
cno     INT(4), 
cname   varchar(18), 
street  varchar(30),
zip     varchar(6),
phone   VARCHAR(15));
INSERT INTO customers VALUES (1111,'CHARES','123 Main St.','67226','316-636-5555');
INSERT INTO customers VALUES (2222,'BERTRAM','237 Ash Ave.','67226','316-689-5555');
INSERT INTO customers VALUES (3333,'BARBARA','111 Inwood St.','60606','316-111-1234');
create table orders(
ono      INT(4),
cno      INT(4),
eno      INT(4),
received date,
shipped  date);
INSERT INTO orders VALUES (1020,1111,1000,STR_TO_DATE('10-DEC-1994', '%d-%M-%Y'),STR_TO_DATE('12-DEC-1994', '%d-%M-%Y'));
INSERT INTO orders VALUES (1021,1111,1000,STR_TO_DATE('12-JAN-1995', '%d-%M-%Y'),STR_TO_DATE('15-JAN-1995', '%d-%M-%Y'));
INSERT INTO orders VALUES (1022,2222,1001,STR_TO_DATE('13-FEB-95', '%d-%M-%Y'),STR_TO_DATE('20-FEB-1995', '%d-%M-%Y'));
INSERT INTO orders VALUES (1023,3333,1000,STR_TO_DATE('20-JUN-1997', '%d-%M-%Y'),null);
create table odetails(
ono    INT(4), 
pno    INT(5), 
qty    INT(3));
INSERT INTO odetails VALUES (1020,10506,1);
INSERT INTO odetails VALUES (1020,10507,1);
INSERT INTO odetails VALUES (1020,10508,2);
INSERT INTO odetails VALUES (1020,10509,3);
INSERT INTO odetails VALUES (1021,10601,4);
INSERT INTO odetails VALUES (1022,10601,1);
INSERT INTO odetails VALUES (1022,10701,1);
INSERT INTO odetails VALUES (1023,10800,1);
INSERT INTO odetails VALUES (1023,10900,1);
create table zipcodes(
zip    varchar(6),
city   varchar(15));
INSERT INTO zipcodes VALUES ('67226','WICHITA');
INSERT INTO zipcodes VALUES ('60606','FORT DODGE');
INSERT INTO zipcodes VALUES ('50302','KANSAS CITY');
INSERT INTO zipcodes VALUES ('54444','COLUMBIA');
INSERT INTO zipcodes VALUES ('66002','LIBERAL');
INSERT INTO zipcodes VALUES ('61111','FORT HAYS');
commit;