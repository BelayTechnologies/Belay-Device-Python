#!/usr/bin/python
# -*- coding: utf-8 -*-

import database.Database
import sys

def create_device_db(db, db_name='Device'):
    try:
        db._execute("CREATE DATABASE if not exists %s" % db_name)
        db._execute("use %s" % db_name)
        return True
    except:
        return None

def create_table_device_properties(db):
    db._execute("CREATE TABLE if not exists Device_Properties \
                (Property_Id int NOT NULL AUTO_INCREMENT, \
                 Property_Name varchar(255) NOT NULL, \
                 Property_Info varchar(255) NOT NULL, \
                 PRIMARY KEY (Property_Id), \
                 UNIQUE (Property_Name));")

def create_table_manager_information(db):
    db._execute("CREATE TABLE if not exists Manager_Information \
                (Manager_Id int NOT NULL AUTO_INCREMENT, \
                 Manager_Name varchar(255) NOT NULL, \
                 Manager_Status varchar(255) NOT NULL, \
                 Manager_Wait int NOT NULL, \
                 Manager_Logfile varchar(255), \
                 PRIMARY KEY (Manager_Id));")

def create_table_test_information(db):
    db._execute("CREATE TABLE if not exists Test_Information \
                 (Test_Id int NOT NULL AUTO_INCREMENT, \
                  Test_Name varchar(255) NOT NULL, \
                  Test_Status varchar(255) NOT NULL, \
                  Total_SUT int,PRIMARY KEY (Test_Id), \
                  UNIQUE (Test_Name));")

def create_table_hypervisor_information(db):
    db._execute("CREATE TABLE if not exists Hypervisor_Information \
                 (Hypervisor_Id int NOT NULL AUTO_INCREMENT, \
                  IP_Address varchar(255) NOT NULL, \
                  Hypervisor_Username varchar(255) NOT NULL, \
                  Hypervisor_Password varchar(255) NOT NULL, \
                  Hypervisor_Type varchar(255) NOT NULL, \
                  Hypervisor_Version varchar(255) NOT NULL, \
                  Hypervisor_Manager varchar(255), \
                  Hypervisor_Datacenter varchar(255) NOT NULL, \
                  Hypervisor_Datastore varchar(255) NOT NULL, \
                  Hypervisor_Status varchar(255) NOT NULL, \
                  Max_Concurrent int NOT NULL, \
                  PRIMARY KEY (Hypervisor_Id), \
                  UNIQUE (IP_Address));")

def create_table_template_vm_information(db):
    db._execute("CREATE TABLE if not exists Template_VM_Information \
                 (Template_VM_ID int NOT NULL AUTO_INCREMENT, \
                  OS_Name varchar(255) NOT NULL, \
                  OS_Version varchar(255) NOT NULL, \
                  OS_Service_Pack varchar(255) NOT NULL, \
                  OS_Arch varchar(255) NOT NULL, \
                  OS_Username varchar(255) NOT NULL, \
                  OS_Password varchar(255) NOT NULL, \
                  PRIMARY KEY (Template_VM_ID));")

def create_table_agent_information(db):
    db._execute("CREATE TABLE if not exists Agent_Information \
                 (Agent_Id int NOT NULL AUTO_INCREMENT, \
                  Agent_Type varchar(255) NOT NULL, \
                  Hypervisor_Type varchar(255) NOT NULL, \
                  AgentScript_Path varchar(255) NOT NULL, \
                  Agent_Status varchar(255) NOT NULL, \
                  Hypervisor_ID int, \
                  PRIMARY KEY (Agent_Id), \
                  FOREIGN KEY (Hypervisor_ID) \
                  REFERENCES Hypervisor_Information(Hypervisor_ID), \
                  UNIQUE (Agent_Type));")

def create_table_sut_information(db):
    db._execute("CREATE TABLE if not exists SUT_Information \
                 (SUT_Id int NOT NULL AUTO_INCREMENT, \
                  SUT_Name varchar(255) NOT NULL, \
                  SUT_Status varchar(255) NOT NULL, \
                  SUT_RemoteConsoleLink varchar(255), \
                  Test_Name varchar(255), \
                  Template_VM_Name varchar(255) NOT NULL, \
                  SUT_Console_Active varchar(255), \
                  Template_VM_ID int, \
                  Hypervisor_ID int, \
                  Hypervisor_IP varchar(255), \
                  Agent_Type varchar(255) NOT NULL, \
                  Hypervisor_Type varchar(255) NOT NULL, \
                  Agent_Logfile varchar(255), \
                  PRIMARY KEY (SUT_Id), \
                  FOREIGN KEY (Test_Name) \
                  REFERENCES Test_Information(Test_Name), \
                  FOREIGN KEY (Hypervisor_ID) \
                  REFERENCES Hypervisor_Information(Hypervisor_ID), \
                  FOREIGN KEY (Template_VM_ID) \
                  REFERENCES Template_VM_Information(Template_VM_ID), \
                  UNIQUE (SUT_Name));")

def create_table_test_cases(db):
    db._execute("CREATE TABLE Test_Cases \
                 (Testcase_Id int NOT NULL AUTO_INCREMENT, \
                  Testcase_name varchar(255) NOT NULL, \
                  Testcase_Script varchar(255) NOT NULL, \
                  Testcase_Status varchar(255) NOT NULL, \
                  Testcase_Result varchar(255), \
                  SUT_Name varchar(255), \
                  PRIMARY KEY (Testcase_Id), \
                  FOREIGN KEY (SUT_Name) \
                  REFERENCES SUT_Information(SUT_Name));")

def create_table_software_information(db):
    db._execute("CREATE TABLE Software_Information \
                 (Software_Id int NOT NULL AUTO_INCREMENT, \
                  SW_Manufacturer varchar(255) NOT NULL, \
                  SW_Name varchar(255) NOT NULL, \
                  SW_Version varchar(255) NOT NULL, \
                  PRIMARY KEY (Software_Id));")

def create_table_testcase_logfiles(db):
    db._execute("CREATE TABLE TestCase_Logfiles \
                 (Logfile_Id int NOT NULL AUTO_INCREMENT, \
                  Testcase_Id int, \
                  SUT_Name varchar(255), \
                  Testcase_name varchar(255), \
                  Logfile_Path varchar(255), \
                  Logfile varchar(255), \
                  PRIMARY KEY (Logfile_Id));")

def deploy_device(db):
    create_table_device_properties(db)
    create_table_manager_information(db)
    create_table_test_information(db)
    create_table_hypervisor_information(db)
    create_table_template_vm_information(db)
    create_table_agent_information(db)
    create_table_sut_information(db)
    create_table_test_cases(db)
    create_table_software_information(db)
    create_table_testcase_logfiles(db)

if __name__ == '__main__':
    sql = database.Database.ConnectSQL(db=None)
    # Create Device DB
    if not create_device_db(sql):
        print "Unable to create DB: Device"
        sys.exit(3)
    print "DB Device is created"

    sql = database.Database.ConnectSQL(db="Device")
    deploy_device(sql)
    print vars(sql)