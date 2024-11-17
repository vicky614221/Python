use rbov;
create table employee (
emp_id char (8) primary key, 
emp_fname varchar(20) not null,
emp_mname varchar(20) not null default '',
emp_lname varchar(20) not null,
start_date_tmsp timestamp not null default CURRENT_TIMESTAMP,
end_date_tmsp timestamp,
per_hour_rate decimal(11,2),
last_upd_by char (8),
last_upd_tmsp timestamp not null default CURRENT_TIMESTAMP
);

alter table employee add column dob date null, add column highest_edu varchar(20) not null, add column mobile_no char(10) not null,
add column email_id varchar(80) not null after per_hour_rate;
alter table employee add column gender varchar(10) not null;
alter table employee add column address varchar(100) not null;


insert into employee (emp_id, emp_fname, emp_mname, emp_lname,per_hour_rate,last_upd_by) values
('empdep01','vignesh','','somu',18,'empdep01');
update employee
set emp_mname = 'vicky', email_id = 'vicky@mail.com',dob='1996-04-13',highest_edu = 'BTECH',mobile_no = '9873918391',gender='male',
address = 'door no 7, 9th street, delhi'
where emp_id = 'empdep01';
show create table employee;
select * from employee;