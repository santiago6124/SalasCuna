drop database if exists SalasCunas;

create database SalasCunas;

use SalasCunas;

CREATE TABLE
    Gender (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255)
    );

CREATE TABLE
    Adress (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255)
    );

CREATE TABLE
    Shift (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255)
    );

CREATE TABLE
    Role (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255)
    );

CREATE TABLE
    Zone (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255)
    );

CREATE TABLE
    User_email (
        id INT PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255)
    );

CREATE TABLE
    Guardian_phone (
        id INT PRIMARY KEY AUTO_INCREMENT,
        phone VARCHAR(255)
    );

CREATE TABLE
    Child_state (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255)
    );

CREATE TABLE
    Cribroom (
        id INT PRIMARY KEY AUTO_INCREMENT,
        max_capacity INT,
        Adress_id INT,
        Zone_id INT,
        Shift_id INT,
        FOREIGN KEY (Adress_id) REFERENCES Adress (id),
        FOREIGN KEY (Zone_id) REFERENCES Zone (id),
        FOREIGN KEY (Shift_id) REFERENCES Shift (id)
    );

CREATE TABLE
    Company (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        phone INT
    );

CREATE TABLE
    Desinfection (
        id INT PRIMARY KEY AUTO_INCREMENT,
        date DATETIME,
        description VARCHAR(255),
        Cribroom_id INT,
        Company_id INT,
        FOREIGN KEY (Cribroom_id) REFERENCES Cribroom (id),
        FOREIGN KEY (Company_id) REFERENCES Company (id)
    );

CREATE TABLE
    Payout (
        id INT PRIMARY KEY AUTO_INCREMENT,
        amount FLOAT,
        date DATE,
        Zone_id INT,
        FOREIGN KEY (Zone_id) REFERENCES Zone (id)
    );

CREATE TABLE
    User (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(255),
        password VARCHAR(255),
        User_email_id INT,
        Role_id INT,
        FOREIGN KEY (User_email_id) REFERENCES User_email (id),
        FOREIGN KEY (Role_id) REFERENCES Role (id)
    );

CREATE TABLE
    Guardian (
        id INT PRIMARY KEY AUTO_INCREMENT,
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
    Child (
        id INT PRIMARY KEY AUTO_INCREMENT,
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
    Cribroom_User (
        id INT PRIMARY KEY AUTO_INCREMENT,
        Cribroom_id INT,
        User_id INT,
        FOREIGN KEY (Cribroom_id) REFERENCES Cribroom (id),
        FOREIGN KEY (User_id) REFERENCES User (id)
    );

CREATE TABLE
    Form (
        id INT PRIMARY KEY AUTO_INCREMENT,
        generation_date DATE,
        Cribroom_User_id INT,
        Role_id INT,
        FOREIGN KEY (Cribroom_User_id) REFERENCES Cribroom_User (id),
        FOREIGN KEY (Role_id) REFERENCES Role (id)
    );