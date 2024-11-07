create database rbov;
use rbov;
create table customer_det(cust_id varchar(32),cust_fname varchar(50),cust_lname varchar(50),cust_email varchar(80));
alter table customer_det add primary key(cust_id);
desc customer_det;
alter table customer_det 
modify cust_fname varchar(50) not null default '', 
modify cust_lname varchar(50) not null default '',
modify cust_email varchar(80) not null default '';

insert into customer_det values('vicky001','VIGNESH','SOMU','vicky123@gmail.com');
insert into customer_det values('jimmy001','JIMMY','RASH','jimmyrash@gmail.com');

select * from customer_det;
