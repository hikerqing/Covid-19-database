/*
build the covid 19 database 
*/
create database covid19database;
CREATE TABLE drug
(
	drug_id int,
	drug_name varchar(50),
	drug_status varchar(25),
    drug_type varchar(25),
    primary key (drug_id)
);

CREATE TABLE clinical_trial
(
	trial_id int,
    title varchar(50),
    trial_type varchar(25),
    trial_stage varchar(25),
    trial_status varchar(25),
    record_date date,
    start_date date,
    end_date date,
    bid_institution date,
    trial_institution date,
    primary key (trial_id)
);

CREATE TABLE trial_drug
(
	trial_id int,
	drug_id int,
    primary key(trial_id),
    foreign key(trial_id) references clinical_trial(trial_id),
    foreign key(drug_id) references drug(drug_id)
);

create table researcher
(
	researcher_id int,
    first_name varchar(25),
    last_name varchar(25),
    position varchar(25),
    email varchar(25),
    phonenumber varchar(25),
    department varchar(25),
    primary key (researcher_id)
);

create table institution
(
	institution_id int,
    institution_location varchar(50),
    instituiton_money int,
    institution_email varchar(25),
    institution_phone varchar(25),
    primary key (institution_id)
);

create table institution_researcher
(
	researcher_id int,
	institution_id int,
    primary key (researcher_id),
    foreign key(researcher_id) references researcher(researcher_id),
    foreign key(institution_id) references institution(institution_id)
);

create table experiment
(
	trial_id int,
    batch_id int,
    experiment_description varchar(100),
    start_date date,
    end_date date,
    dose float,
    result varchar(20),
    adverse_reaction varchar(20),
    more_details varchar(50),
    primary key (trial_id, batch_id),
    foreign key (trial_id) references clinical_trial(trial_id)
);

create table researcher_experiment
(
	researcher_id int,
    trial_id int,
	batch_id int,
    division varchar(20),
    primary key(researcher_id),
    foreign key(researcher_id) references researcher(researcher_id),
    foreign key(trial_id,batch_id) references experiment(trial_id,batch_id),
);

CREATE TABLE volunteer
(
    volunteer_id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    gender VARCHAR(5),
    age INT,
    blood_type VARCHAR(5),
    country VARCHAR(10),
    PRIMARY KEY (volunteer_id)
);

CREATE TABLE volunteer_experiment
(
    volunteer_id int,
    trial_id int,
    experiment_id int,
    PRIMARY KEY (volunteer_id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteer(volunteer_id),
    FOREIGN KEY (trial_id) REFERENCES clinical_trial(trial_id),
    FOREIGN KEY (experiment_id) REFERENCES experiment(experiment_id)
);

CREATE TABLE SITE
(
    site_id int,
    country VARCHAR(20),
    province VARCHAR(20),
    city VARCHAR(20),
    other_details VARCHAR(20),
    PRIMARY KEY (site_id)
);

CREATE TABLE hospital
(
    hospital_id int,
    site_id int,
    hospital_name VARCHAR(20),
    PRIMARY KEY (hospital_id,site_id),
    FOREIGN KEY (site_id) REFERENCES SITE(site_id)
);

CREATE TABLE doctor
(
    doctor_id int,
    hospital_id int,
    site_id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    department VARCHAR(20),
    gender VARCHAR(5),
    age INT,
    PRIMARY KEY (doctor_id,site_id ,hospital_id),
    FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id),
    FOREIGN KEY (site_id) REFERENCES SITE(site_id)
);

CREATE TABLE cases
(
    case_id int,
    site_id int,
    first_name varchar(20),
    last_name varchar(20),
    gender varchar(5),
    age int,
    job varchar(20),
    reason VARCHAR(20),
    situation varchar(20),
    suspected_date date,
    confirmed_date date,
    live BOOLEAN,
    left_date date,
    PRIMARY KEY (case_id, site_id),
    FOREIGN KEY (site_id) REFERENCES SITE(site_id) 
);
