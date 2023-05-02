create table Genders (
    id int primary key auto_increment,
    first_name varchar(100),
    description varchar(100)
);

create table Guardian_phones (
id int primary key auto_increment,
phone_number varchar(100)
);

create table Guardians (
id int primary key auto_increment,
first_name varchar(100),
last_name varchar(100),
dni varchar(40),
birthdate date,
phone_id int,
gender_id int,
constraint fk_phone_guardian foreign key (phone_id) references Guardian_phones(id),
constraint fk_gender_guardian foreign key (gender_id) references Genders(id)
);

create table Shifts (
id int primary key auto_increment,
first_name varchar(100),
description varchar(100)
);

create table Zones (
id int primary key auto_increment,
name varchar(100)
);

create table Departments (
id int primary key auto_increment,
name varchar(100)
);

create table Localities (
id int primary key auto_increment,
name varchar(100),
department_id int,
constraint fk_department_locality foreign key (department_id) references Departments(id)
);

create table Districts (
id int primary key auto_increment,
name varchar(100),
locality_id int,
constraint fk_locality_district foreign key (locality_id) references Localities(id)
);

create table Addresses (
id int primary key auto_increment,
street varchar(150),
number int,
latitude varchar(100),
longitude varchar(100),
district_id int,
constraint fk_district_address foreign key (district_id) references Districts(id)
);

create table Cribrooms (
id int primary key auto_increment,
max_capacity int,
address_id int,
zone_id int,
shift_id int,
constraint fk_address_cribroom foreign key (address_id) references Addresses(id),
constraint fk_zone_cribroom foreign key (zone_id) references Zones(id),
constraint fk_shift_cribroom foreign key (shift_id) references Shifts(id)
);

create table User_emails (
id int primary key auto_increment,
email varchar(100)
);

create table Roles (
id int primary key auto_increment,
first_name varchar(100),
description varchar(100)
);

create table Users (
id int primary key auto_increment,
username varchar(255),
password varchar(255),
email_id int,
role_id int,
constraint fk_email_user foreign key (email_id) references User_emails(id),
constraint fk_role_user foreign key (role_id) references Roles(id)
);

create table Children_state (
id int primary key auto_increment,
active boolean,
description varchar(200)
);

create table Children (
    id int primary key auto_increment,
    first_name varchar(100),
    last_name varchar(100),
    dni varchar(40),
    birthdate date,
    registration_date date,
    disenroll_date date,
    gender_id int,
    cribroom_id int,
    shift_id int,
    user_id int,
    guardian_id int,
    children_state_id int,
    constraint fk_gender_children foreign key (gender_id) references Genders(id),
    constraint fk_cribroom_children foreign key (cribroom_id) references Cribrooms(id),
    constraint fk_shift_children foreign key (shift_id) references Shifts(id),
    constraint fk_user_children foreign key (user_id) references Users(id),
    constraint fk_guardian_children foreign key (guardian_id) references Guardians(id),
    constraint fk_childrenstate_children foreign key (children_state_id) references Children_state(id)
);

create table Desinfections (
id int primary key auto_increment,
desinfection_date date,
company varchar(100),
company_phone varchar(100),
cribroom_id int,
constraint fk_cribroom_desinfection foreign key (cribroom_id) references Cribrooms(id)
);

create table Padrones (
id int primary key auto_increment,
generation_date date
);

create table Question_types (
id int primary key auto_increment,
question_type varchar(200)
);

create table Questions (
id int primary key auto_increment,
question varchar(200),
category varchar(200),
question_types_id int,
constraint fk_questiontype_question foreign key (question_types_id) references Question_types(id)
);

create table Options (
id int primary key auto_increment,
question_id int,
constraint fk_question_option foreign key (question_id) references Questions(id)
);

create table Forms (
id int primary key auto_increment,
generation_date date,
user_id int,
cribroom_id int,
constraint fk_user_form foreign key (user_id) references Users(id),
constraint fk_cribroom_form foreign key (cribroom_id) references Cribrooms(id)
);

create table Answers (
id int primary key auto_increment,
answer varchar(200),
question_id int,
form_id int,
constraint fk_question_answer foreign key (question_id) references Questions(id),
constraint fk_form_answer foreign key (form_id) references Forms(id)
);

create table Payouts (
id int primary key auto_increment,
date date,
upcountry int,
capital int
);

create table Paynote (
id int primary key auto_increment,
generation_date date,
category varchar(100),
payout_id int,
constraint fk_payout_paynote foreign key (payout_id) references Payouts(id)
);

create table Cribroom_Paynote(
id int primary key auto_increment,
cribroom_id int,
paynote_id int,
constraint fk_cribroom_cribroompaynote foreign key (cribroom_id) references Cribrooms(id),
constraint fk_paynote_cribroompaynote foreign key (paynote_id) references Paynote(id)
);