use rbov;

create table patient (
patient_id char(10) primary key,
patient_log_pwd char(60) not null,
patient_name varchar (50) not null,
patient_dob date,
patient_gender varchar (20) not null,
patient_email varchar (80) not null,
patient_phone_no char (10) not null,
patient_address varchar(100) not null
)

select * from patient;

alter table patient add column aadhar_no int(12) unique after patient_phone_no;
alter table patient drop index aadhar_no_1;

update patient set aadhar_no = '123456789123' where patient_id = 'patient001';

insert into patient
(patient_id,patient_log_pwd,patient_name,patient_dob,patient_gender,patient_email,patient_phone_no,patient_address) values 
('patient001','sssdoeidjqurhduqiejdheisehduehdududududuoeidkeudiehduediedue','vicky','1996-09-08','male','vicky@mail.com','9847461523','vizag');