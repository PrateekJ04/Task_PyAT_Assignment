# Automation Task on Selenium with Python Using Pytest Framework

### Automate Test Scenarios on
    - Register Functionality
    - Login Functionality
    - Address Functionality

*****Folder Structure Information*****

#Config-->  This Folder Contains config information Ex. Url, browser etc.

#Page-->    This folder consists of page and locator details

#Tests-->   This folder consists of tests,conftest.py and driver details[setup and teardown]

#allure-results --> This consists of generated allure report

#Utility--> This consists of Config reader 


##### How to run this framework 

====================================================================================

step1:- Copy all Code to your system

step2:- Go to Commandline and type command "cd <your path to project>" and hit enter

step3:- Then type command "pip install -r requirements.txt" and hit enter

step4:- Once all the neccessary installations done , Go to utilities and add your system path to "config.ini" file in config reader

step5:- Go to commandline and type command "pytest" and hit enter
        Note:-  To run parallel tests use command [pytest -n <no. of parallel testcases>] or To run testcases according to markers
        use command[pytest -m "<name of the marker>"]

step6:- After successful execution to generate report type command "allure serve allure-results" 
        [*allure commandline must be present on system]

step7:- Now you have the execution report with all the details such as title,description and pagewise testcases

=====================================================================================
 
***Details*** >>> 

* Design Pattern Used --> Page Object Model
* Libraries/packages Used

    ======================
     * pytest
     * allure-pytest
     * selenium
     * xdist
     * Random
     * Faker

