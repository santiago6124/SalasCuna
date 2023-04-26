create table Children (
id int primary key,
first_name varchar(100),
last_name varchar(100),
dni varchar(40),
birthdate date,
gender_id int,
id_sala int,
shift_id int,
user_id int,
registration_date date,
guardian_id int,
foreign key (gender_id) references Genders(id),
foreign key (id_sala) references Cribrooms(cribroom_id),
foreign key (shift_id) references Shifts(id),
foreign key (user_id) references Users(id),
foreign key (guardian_id) references Guardians(id)
);

create table Users (
id int primary key,
username varchar(255),
password varchar(255),
email_id int,
role_id int,
foreign key (email_id) references User_emails(id),
foreign key (role_id) references Roles(id)
);

create table Cribrooms (
cribroom_id int primary key,
max_capacity int,
address_id int,
zone_id int,
shift_id int,
foreign key (address_id) references Addresses(id),
foreign key (zone_id) references Zones(id),
foreign key (shift_id) references Shifts(id)
);

create table Zones (
id int primary key,
name varchar(100)
);

create table Guardians (
id int primary key,
first_name varchar(100),
last_name varchar(100),
dni varchar(40),
birthdate date,
telefono_id int,
gender_id int,
foreign key (telefono_id) references Guardian_phones(id),
foreign key (gender_id) references Genders(id)
);

create table Shifts (
id int primary key,
name varchar(100),
description varchar(100)
);

create table Genders (
id int primary key,
name varchar(100),
description varchar(100)
);

create table Roles (
id int primary key,
name varchar(100),
description varchar(100)
);

create table Guardian_phones (
id int primary key,
phone_number varchar(100)
);

create table User_emails (
id int primary key,
email varchar(100)
);

create table Desinfections (
id int primary key,
desinfection_date date,
company varchar(100),
company_phone varchar(100),
cribroom_id int,
foreign key (cribroom_id) references Cribrooms(cribroom_id)
);

create table Addresses (
id int primary key,
street varchar(150),
number int,
latitude varchar(100),
longitude varchar(100),
district_id int,
foreign key (district_id) references Districts(id)
);

create table Districts (
id int primary key,
name varchar(100),
locality_id int,
foreign key (locality_id) references Localities(id)
);

create table Localities (
id int primary key,
name varchar(100),
department_id int,
foreign key (department_id) references Departments(id)
);

create table Departments (
id int primary key,
name varchar(100)
);

create table Padrones (
id int primary key,
generation_date date
);

create table Questions (
id int primary key,
question varchar(200),
category varchar(200),
question_types_id int,
foreign key (question_types_id) references Question_types(id)
);

create table Question_types (
id int primary key,
question_type varchar(200)
);

create table Options (
id int primary key,
question_id int,
foreign key (question_id) references Questions(id)
);

create table Forms (
id int primary key,
generation_date date,
user_id int,
cribroom_id int,
foreign key (user_id) references Users(id),
foreign key (cribroom_id) references Cribrooms(cribroom_id)
);

create table Answers (
id int primary key,
answer varchar(200),
question_id int,
form_id int,
foreign key (question_id) references Questions(id),
foreign key (form_id) references Forms(id)
);

create table Payouts (
id int primary key,
date date,
upcountry int,
capital int
);

create table Paynote (
id int primary key,
generation_date date,
cribroom_id int,
foreign key (cribroom_id) references Cribrooms(cribroom_id)
);

create table Children_state (
id int primary key,
active boolean,
description varchar(200),
children_id int,
foreign key (children_id) references Children(id)
);