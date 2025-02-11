create database rbov;
use rbov;
create table customer_det(cust_id varchar(32),cust_fname varchar(50),cust_lname varchar(50),cust_email varchar(80));

create table customer_acct(cust_id varchar(32) not null, acct_prod char(3) not null,acct_type char(4) not null, 
acct_no char(12) not null,acct_bal decimal(11,2) not null,
primary key(acct_prod,acct_type,acct_no));

alter table customer_det add primary key(cust_id);
desc customer_det;
desc customer_acct;
alter table customer_det 
modify cust_fname varchar(50) not null default '', 
modify cust_lname varchar(50) not null default '',
modify cust_email varchar(80) not null default '';

alter table customer_acct modify acct_bal decimal(11,2) not null default 0.00;

insert into customer_det values('vicky002','VIGNESH','SOMU','vicky123@gmail.com','12345678');
insert into customer_det values('jimmy001','JIMMY','RASH','jimmyrash@gmail.com');

insert into customer_acct values('vicky001','PER','0001','RBOV00000002',456.98);

select * from customer_det where pass_word != '';
delete  from customer_det where pass_word = '';
select * from customer_acct;

alter table customer_acct add constraint fk_cust_id foreign key(cust_id) references customer_det(cust_id) on delete cascade;
alter table customer_det add pass_word char(8) not null;
alter table customer_det drop password;

create table test(
user_id char(8) primary key,
password char(60) not null
);
select * from test;	

