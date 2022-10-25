# SQL-ERD
1. Made VM on  GCP (10/23)
    #Updated and configed mysqldb and ip (10/23)
    #Made sqldb on gcp (mysql-test) (10/23)
2. Create a new database inside of that mysql instance called patient_portal 
    # done(10/25)
3. Create a python script called (sql_table_creation.py) that creates the following tables inside of patient_portal: patients, medications, treatments_procedures, conditions, and social determinants. Be sure to use a .env file to hide your login credentials 

4. Create a python script called (sql_dummy_data.py) using python and send some dummy data into each of the tables. Please see notes for ideas related to dummy data. 

5. Create an ERD for your DB design using MySQL Work Bench. You must have at least two foreignKeys representing a relationship between at least 2 tables. 

6. Github docs to include: 
- a readme file that describes a) where you setup the mySQL db, b) any issues you ran into 
- a images folder that contains: 
    - screen shot of a ERD of your proposed setup (use either popSQL or mysql work bench) 
    - screen shots of you connected to the sql server, performing the following queries: 
        - Query1: show databases (e.g., show databases;) 
        - Query2: all of the tables from your database (e.g., show tables;)  
        - Query3: select * from patient_portal.medications 
        - Query4: select * from patient_portal.treatment_procedures
        - Query5: select * from patient_portal.conditions