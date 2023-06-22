drop database if exists SalasCunas;

create database SalasCunas;

use SalasCunas;

CREATE TABLE
    Cribroom (
        id INT PRIMARY KEY,
        max_capacity INT,
        Adress_id INT,
        Zone_id INT,
        Shift_id INT,
        FOREIGN KEY (Adress_id) REFERENCES Adress (id),
        FOREIGN KEY (Zone_id) REFERENCES Zone (id),
        FOREIGN KEY (Shift_id) REFERENCES Shift (id)
    );

CREATE TABLE
    Desinfection (
        id INT PRIMARY KEY,
        desinfection_date DATE,
        company VARCHAR(255),
        company_phone VARCHAR(255),
        Cribroom_id INT,
        FOREIGN KEY (Cribroom_id) REFERENCES Cribroom (id)
    );

CREATE TABLE
    Payout (
        id INT PRIMARY KEY,
        amount DECIMAL,
        month DATE,
        Zone_id INT,
        FOREIGN KEY (Zone_id) REFERENCES Zone (id)
    );

CREATE TABLE Zone ( id INT PRIMARY KEY, name VARCHAR(255) );

CREATE TABLE
    Child (
        id INT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        dni VARCHAR(255),
        birthdate DATE,
        registration_date DATE,
        disenroll_date DATE,
        Gender_id INT,
        Cribroom_id INT,
        Shift_id INT,
        User_id INT,
        Guardian_id INT,
        Child_state_id INT,
        FOREIGN KEY (Gender_id) REFERENCES Gender (id),
        FOREIGN KEY (Cribroom_id) REFERENCES Cribroom (id),
        FOREIGN KEY (Shift_id) REFERENCES Shift (id),
        FOREIGN KEY (User_id) REFERENCES User (id),
        FOREIGN KEY (Guardian_id) REFERENCES Guardian (id),
        FOREIGN KEY (Child_state_id) REFERENCES Child_state (id)
    );

CREATE TABLE
    User (
        id INT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        User_email_id INT,
        Role_id INT,
        FOREIGN KEY (User_email_id) REFERENCES User_email (id),
        FOREIGN KEY (Role_id) REFERENCES Role (id)
    );

CREATE TABLE
    Cribroom_User (
        id INT PRIMARY KEY,
        Cribroom_id INT,
        User_id INT,
        FOREIGN KEY (Cribroom_id) REFERENCES Cribroom (id),
        FOREIGN KEY (User_id) REFERENCES User (id)
    );

CREATE TABLE
    Guardian (
        id INT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        dni VARCHAR(255),
        birthdate DATE,
        Guardian_phone_id INT,
        Gender_id INT,
        FOREIGN KEY (Guardian_phone_id) REFERENCES Guardian_phone (id),
        FOREIGN KEY (Gender_id) REFERENCES Gender (id)
    );

CREATE TABLE
    Form (
        id INT PRIMARY KEY,
        generation_date DATE,
        Cribroom_User_id INT,
        Role_id INT,
        FOREIGN KEY (Cribroom_User_id) REFERENCES Cribroom_User (id),
        FOREIGN KEY (Role_id) REFERENCES Role (id)
    );