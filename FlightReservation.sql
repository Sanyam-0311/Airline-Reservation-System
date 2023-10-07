use alr;
create table login (login_id numeric primary key,login_username varchar(8),user_password varchar(8) not null );
create table permission(per_id numeric primary key, per_role_id int, per_module varchar(70), per_name varchar(35));
create table airlines_enquiry(ae_title varchar(15), ae_id varchar(8) primary key);
create table airlines_booking(ab_source varchar(20),ab_destination varchar(30), ab_flight varchar(15),ab_date date, ab_type varchar(15),ab_id numeric  primary key);
create table ticket(ab_id numeric primary key);
create table passenger(p_id numeric primary key, p_name varchar(35), p_address varchar(70), p_email varchar(55), p_mobile varchar(10));
#Inserting default values into airline enquiry
insert into airlines_enquiry values ('Indigo','IND7408');
insert into airlines_enquiry values ('Jet Airways','JET4509');
insert into airlines_enquiry values ('SpiceJet','SPJ8012');
insert into airlines_enquiry values ('Qatar Airways','QTR6798');
insert into airlines_enquiry values ('Air India','AIR2967');
insert into airlines_enquiry values ('Vistara','VIT3465');
insert into airlines_enquiry values ('Go Air','GAR0412');
select * from permission;
#Inserting default values into login 
insert into login values(1234,null,'qwer');
insert into login values(0000,null,'qwer');
insert into login values(9999,null,'qwer');
insert into ticket values(0000);
#Inserting default values into passenger
insert into passenger values(1234,'Sanyam Shah','Thane,Maharastra','sanyam123@gmail.com',8989898989);
insert into passenger values(0000,'Shreya Joshi','Dhamnod MP','shreya123@gmail.com',8989898988);
insert into passenger values(9999,'Tanishq Mandowara','Bhilwara Rajasthan','tanishq123@gmail.com',8989898980);

#Inserting default values into airlines_booking
insert into airlines_booking values('Mumbai','Indore','Indigo','2022-10-20','Prime',1234);
insert into airlines_booking values('Indore','Mumbai','Indigo','2022-10-19','Prime',0000);
insert into airlines_booking values('Indore','Bhilwara','Air India','2022-10-19','Prime',9999);
insert into ticket values(9999);
select * from passenger;
select * from airlines_booking;
select * from login;
select * from ticket;

delete from airlines_booking where ab_id=0000;
SELECT UCASE(ae_title) FROM airlines_enquiry WHERE  1;
SELECT MAX (mycount) FROM (SELECT ab_flight,COUNT(ab_flight) mycount FROM airlines_booking group by ab_flight);
select count(ab_flight) from airlines_booking where ab_flight='Indigo';
select passenger.p_name,passenger.p_email,passenger.p_id from passenger,airlines_booking where passenger.p_id=airlines_booking.ab_id;
CREATE VIEW user_details AS select p_name,p_email,p_address,p_mobile from passenger inner join ticket on p_id=9999;
select distinct * from user_details;
select distinct passenger.p_name,passenger.p_email from passenger inner join ticket on passenger.p_id=9999;
#select airlines_booking.ab_date,airlines_booking.ab_source,airlines_booking.ab_destination,airlines_booking.ab_flight,airlines_booking.ab_type,airlines_booking.ab_id,ticket.ab_id from airlines_booking inner join ticket on airlines_booking.ab_id=1456;
#select airlines_booking.ab_date,airlines_booking.ab_source,airlines_booking.ab_destination,airlines_booking.ab_flight,airlines_booking.ab_type,airlines_booking.ab_id,ticket.ab_id from airlines_booking inner join ticket on airlines_booking.ab_id=ticket.ab_id;
#select passenger.p_name,passenger.p_email,passenger.p_id from passenger,airlines_booking where passenger.p_id=airlines_booking.ab_id;		#here p_id should be =to ab_id

select passenger.p_name from passenger,airlines_booking where passenger.p_id=airlines_booking.ab_id and airlines_booking.ab_flight='Indigo';
#delete from airlines_booking,passenger ,airlines_booking.ab_id=9999 and ;
select airlines_booking.ab_date,airlines_booking.ab_source,airlines_booking.ab_destination,airlines_booking.ab_flight,airlines_booking.ab_type ,ticket.ab_id from airlines_booking inner join ticket on airlines_booking.ab_id=9999;
select distinct passenger.p_name from passenger,airlines_booking where ab_date='2022-11-01' or ab_date='2022-10-20';