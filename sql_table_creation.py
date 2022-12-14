#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#importing needed modules aswell as pip installing the needed ones 
import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#.env file login 
load_dotenv()
GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USER = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")

connection_string_gcp = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
db_gcp = create_engine(connection_string_gcp)

#show databases 
tableNames_gcp = db_gcp.table_names()
print(db_gcp.table_names)

# creating tables in patients db for: patients, medications, 
# treatment_procedures, conditions, and social determinants
table_prod_patients = """
create table if not exists production_patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

table_prod_medications = """
create table if not exists production_medications (
    id int auto_increment,
    med_ndc varchar(255) default null unique,
    med_human_name varchar(255) default null,
    med_is_dangerous varchar(255) default null,
    PRIMARY KEY (id)
); 
"""
table_prod_patients_medications = """
create table if not exists production_patient_medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (med_ndc) REFERENCES production_medications(med_ndc) ON DELETE CASCADE
); 
"""

table_prod_conditions = """
create table if not exists production_conditions (
    id int auto_increment,
    icd10_code varchar(255) default null unique,
    icd10_description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

table_prod_patient_conditions = """
create table if not exists production_patient_conditions (
    id int auto_increment,
    mrn varchar(255) default null,
    icd10_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (icd10_code) REFERENCES production_conditions(icd10_code) ON DELETE CASCADE
); 
"""
table_prod_treatment = """
create table if not exists production_treatment (
    id int auto_increment,
    treat_cpt varchar(255) default null unique,
    treat_human_name varchar(255) default null,
    PRIMARY KEY (id)
); 
"""

table_prod_patient_treatment = """
create table if not exists production_patient_treatment (
    id int auto_increment,
    mrn varchar(255) default null,
    treat_cpt varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (treat_cpt) REFERENCES production_treatment(treat_cpt) ON DELETE CASCADE
); 
"""

table_prod_social = """
create table if not exists production_social (
    id int auto_increment,
    social_lonic varchar(255) default null unique,
    social_human_name varchar(255) default null,
    PRIMARY KEY (id)
); 
""" 

table_prod_social_patient = """
create table if not exists production_patient_social (
    id int auto_increment,
    mrn varchar(255) default null,
    social_lonic varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (social_lonic) REFERENCES production_social(social_lonic) ON DELETE CASCADE
); 
"""

db_gcp.execute(table_prod_patients)
db_gcp.execute(table_prod_medications)
db_gcp.execute(table_prod_patients_medications)
db_gcp.execute(table_prod_conditions)
db_gcp.execute(table_prod_patient_conditions)
db_gcp.execute(table_prod_treatment)
db_gcp.execute(table_prod_patient_treatment)
db_gcp.execute(table_prod_social)
db_gcp.execute(table_prod_social_patient)