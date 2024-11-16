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



select * from employee;