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

insert into patient
(patient_id,patient_log_pwd,patient_name,patient_dob,patient_gender,patient_email,patient_phone_no,patient_address) values 
('patient001','sssdoeidjqurhduqiejdheisehduehdududududuoeidkeudiehduediedue','vicky','1996-09-08','male','vicky@mail.com','9847461523','vizag');