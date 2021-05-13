## Objective

Develop a web application for UMGC's Capstone course

## Employee Management System

Design a web application that allows administrator to manage employees
information and documents

### Contributors

Francis Bui, Tuere Lowery, Erick McCoy, Melissa Noirot

#### Technologies

Python, Flask, Oracle RDBMS, Bootstrap, HTML, CSS

<img src="/readme_images/cover.jpg" />

# Table of Contents

## [Overview](#overview)

## [Project Plan](#pp)

## [Requirements Specification](#rs)

## [System Specification](#ss)

## [User’s Guide](#ug)

## [Test Plan and Results](#tp)

## [Current and Alternate Designs](#designs)

## [Development History](#dh)

## [Conclusions](#conclusion)


## <a name="overview"></a>Overview

Our team’s goal was to develop a solution to common internal management problem.
We set out this goal by creating an employee management system that would help
manage the employee in a given company. In essence, the system is a directory of
the current employee as well as their roles and responsibilities within the
company. The application was designed to be robust yet intuitive to allow
administrator the ability to easily record, add, modify, delete, and manage the
data and catalogue of each employee. The design was intended to be modular so
that it would work for a number of different companies in various industries.
Additionally, the modularity of the system was deliberate so it may be further
customizable for the specific needs of each company. Overall, the system has
achieved the results intended. The intention of this report is to provide a
synopsis of the various aspects of our development process and what was done to
achieve the set goal of this project.

#### Individual Contributions

**Francis Bui, Team Lead & UX/UI Engineer**

As the Team Lead, Francis’s responsibilities included analysis and scope of the
assignment as well as the delegation of the responsibilities to each team member
based on their strengths and desired role. Additionally, he led weekly sprint to
see what the progress was, collaborated with each member to identify and fix any
technical issues, to ensure the goals were being met. As the UX/UI Engineer,
Francis designed and lead the design architecture of the web application. Major
responsibilities include designing and building, testing and debugging, ensuring
cross platform compatibility, implementing tools for the design architecture
including, HTML, CSS, Bootstrap, and Jinja templates. Furthermore, he helped
provide training other members on the use of front-end framework and general
support to the rest of the team including backend and documentation.

**Erick McCoy, Back-end & Database Engineer**

As the back-end engineer, Erick’s role included design architecture for the
server-side of the web application. His responsibilities included building the
business logics and controller as well as the API that will be implemented into
the application. Furthermore, Erick maintained the integration of front-end to
the backend. As the database engineer, he devised the database schema and the
various tables, tuples, and attributes associated with them. Erick also provided
the SQL scripts and maintained the seamless integration of the database into the
backend system. Furthermore, Erick provided training to the other team member in
regard to back-end.

**Tuere Lowery, Back-End Support & Test Engineer**

As the back-end support engineer, Tuere assisted Erick in the responsibilities
of the back-end development. One of her major responsibilities was to develop
the back-end classes which would help in the modularity of functionality of the
web application. Furthermore, she provided assistance in other areas of the
backend development including validation the login functionality. As the Test
Engineer, Tuere ensured that the web application performed as expected on
various systems and browsers. She tested each of the function to ensure that it
function as intended. Additionally, she would fix any bugs encountered or
escalated them to Erick for further evaluation.

**Melissa Noirot, Documentation & UX/UI Support Engineer**

As the documentation engineer, Melissa provided effective written materials for
the project. Her responsibilities included the coordination of all documentation
including the planning, modification, and production schedules, among others.
Additionally, she reviewed all of the details and design process to determine
what documentation was required for various phases of the project. Furthermore,
as the role of the UX/UI support engineer, Melissa assisted Francis in the
overall design architecture of the web application. She was responsible for the
design and information of various pages by utilizing the front-end framework as
discussed.

## <a name="pp"></a>Project Plan

**Project Description**

The purpose of this project is to design a web application that allows
administrators to manage employee information and documents. The application
will be created using the Python Flask framework, and will consist of multiple
pages that include the following functionality:

-   **Front-end Functionality:**

    -   User Login Page

    -   Employee Report Page

    -   Dashboard-style Menu

    -   Add Employee Page

    -   Remove Employee Page

    -   User Guide

-   **Back-end Functionality:**

    -   Oracle RDBMS

    -   Bootstrap/HTML/CSS

This project was chosen in order to develop a streamlined, easy to navigate
Employee Management Software. It was important for the group to design a system
that manages workflows in a simplistic and user-friendly way. The Employee
Management Software will provide an intuitive dashboard with access to employee
information, tasks, and settings all while ensuring that sensitive employee data
is properly encrypted.

**Possible Strengths of Approach**

A web application can be much more versatile than a desktop application. It can
allow for easy access across devices by logging in through a web page. Many
companies are switching to cloud-based software, which would give the Employee
Management Software a competitive edge.

**Possible Weaknesses of Approach**

While a web application can be more versatile, there are potential weaknesses to
consider. Web applications have many factors to consider, such as internet
access and reliability. Without proper internet access, the application is not
available to users. The application must be developed in a way to maximize user
uptime and foster reliability and trust.

**Alternative Approaches Considered but Not Selected**

A desktop application version of this project was considered, but ultimately the
web application version was chosen.

## Project Scenarios

Scenario \#1: A Human Resources employee is made an administrator of the
Employee Management Software and uses the system to keep track of employee
names, addresses, driver’s license, and social security number information.

Scenario \#2: A department manager uses the Employee Management Software to view
all employees assigned to their department.

Scenario \#3: The human resources department would like to start documenting
notes on employee development plans and uses the Employee Notes field of the
Employee Management Software in order to do this.

Scenario \#4: A company would like to mail out a newsletter to all employees and
uses the Employee Information stored in the Employee Management Software to
retrieve all current mailing addresses.

Scenario \#5: An administrator would like to print out employee reports for a
specific department.

Scenario \#6: Human resources would like to start tracking Social Security
Numbers of employees in the Employee Management Software but wants to ensure
that only company administrators have access to the sensitive data.

**Project Timeline**

| **Project Task**                      | **Estimated Work Time Frame** | **Group Member Assigned** | **Due Date**  |
|---------------------------------------|-------------------------------|---------------------------|---------------|
| Create Project Plan                   | Week 1—2                      | Melissa                   | 30 March 2021 |
| Build Boilerplate Website             | Week 1—2                      | Francis                   | 30 March 2021 |
| Develop Database Schema               | Week 1—2                      | Erick                     | 30 March 2021 |
| Create Function Templates and Objects | Week 1—2                      | Tuere                     | 30 March 2021 |
| Create Test Plan                      | Week 2 – 3                    | All                       | 6 April 2021  |
| Create Main and Login Pages           | Week 2 – 3                    | Francis/Melissa           | 6 April 2021  |
| Deploy and Configure Database         | Week 2—3                      | Erick/Tuere               | 6 April 2021  |
| Create Project Design                 | Week 3—4                      | All                       | 13 April 2021 |
| Create Tabbed Pages                   | Week 3—4                      | Francis/Melissa           | 13 April 2021 |
| Build Controllers                     | Week 3—4                      | Erick/Tuere               | 13 April 2021 |
| Phase 1 Source                        | Week 4—5                      | All                       | 20 April 2021 |
| Connect Front-end to Back-end         | Week 4—5                      | Francis/Melissa           | 20 April 2021 |
| Route Pages to Back-end               | Week 4—5                      | Erick/Tuere               | 20 April 2021 |
| Phase 2 Source                        | Week 5—6                      | All                       | 27 April 2021 |
| Implement AES Encryption              | Week 5—6                      | Francis/Melissa           | 27 April 2021 |
| Phase 3 Source                        | Week 6—7                      | All                       | 4 May 2021    |
| Implement File Upload                 | Week 6—7                      | Francis/Melissa           | 4 May 2021    |
| Finalize Back-end Services            | Week 6—7                      | Erick/Tuere               | 4 May 2021    |
| Finalize and Submit                   | Week 7—8                      | All                       | 11 May 2021   |

*Note: Struck out milestones were removed from the final project*

## <a name="rs"></a>Requirements Specification

| **Requirement ID** | **Requirement Type** | **Requirement Description**                                                                            | **Areas Affected**          |
|--------------------|----------------------|--------------------------------------------------------------------------------------------------------|-----------------------------|
| FR1.0              | Functional           | Users must log into the application with a valid username and password                                 | Log In, Authentication      |
| FR1.1              | Functional           | Users may log out on the Settings page                                                                 | Log Out, Authentication     |
| FR2.0              | Functional           | Only users with administrator-level permissions will be able to view data                              | Permissions, Authentication |
| FR3.0              | Functional           | Employee data can be viewed in the Employee Report Page by selecting an employee from a drop down menu | Employee Report             |
| FR3.1              | Functional           | Employee data can be edited on the Employee Report page                                                | Employee Report             |
| FR3.2              | Functional           | Users can sort employees in the Directory Page                                                         | Directory                   |
| FR3.3              | Functional           | Users can add new employees                                                                            | Add Employee                |
| FR4.0              | Functional           | Users can remove employees                                                                             | Remove Employee             |
| FR5.0              | Functional           | Administrators will be able to upload files for individual employees                                   | File Upload                 |
| FR6.0              | Functional           | Users can access print functionality from any page within EMS                                          | Print                       |
| TR1.0              | Technical            | The application will be developed with Python Flask framework                                          | Development                 |
| TR2.0              | Technical            | The application will use Oracle RDBMS                                                                  | Development                 |
| TR3.0              | Technical            | The application will be compatible with the following desktop browsers: Chrome, Firefox, Edge, Safari  | Compatibility, Development  |
| TR4.0              | Technical            | All Personally Identifiable Information (PII) shall be encrypted with AES encryption                   | Encryption                  |
| UR1.0              | Usability            | The application will support 5 concurrent users                                                        | Performance                 |
| UR2.0              | Usability            | The application shall have 99% uptime                                                                  | Performance                 |

*Note: Struck out requirements were removed from the final project*

## <a name="ss"></a>System Specification

The project will be built with the following technologies:

-   Language: Python

-   Web Framework: Flask

-   Front-end Development Framework: Bootstrap/CSS/HTML

-   Database: Oracle RDBMS

The project will support the following specifications:

-   Desktop Browsers:

    -   Chrome version 89.0.4389.90

    -   Firefox version 87.0

    -   Microsoft Edge version 46.01.2.5140

    -   Safari 14.0.3

The project requires the following client to connect to the Oracle database:

-   Oracle Instant Client for Microsoft Windows 32-bit

    -   Download available on Oracle’s website

## <a name="ug"></a>User’s Guide

**Home Page**

1.  **Log In**

    1.  Enter your email and password into the log in fields in order to access
        your company’s dashboard and secure pages (*Fig. 1)*.

        1.  For locked out accounts, please contact EMS administrators.

2.  **Learn More**

    1.  Click the “Learn More” button on the Home page in order to learn more
        about how EMS can best serve you and your company! (*Fig. 1)*

<img src="/readme_images/img1.jpg" />
*Figure 1 - Home Page*

**Dashboard**

1.  **Report Card**

    1.  The Report Card will direct the user to the Report page

2.  **Directory Card**

    1.  The Directory Card will direct the user to the Directory page

3.  **Add User Card**

    1.  The Add User Card will direct the user to the Add Employee page

4.  **Remove User Card**

    1.  The Remove User Card will direct the user to the Remove Employee page

5.  **Informational Guide Card**

    1.  The Informational Guide Card will direct the user to the Informational
        Guide page

6.  **Settings Card**

    1.  The Settings Card will direct the user to the Settings page

<img src="/readme_images/img2.jpg" />
*Figure 2 – Dashboard*

**Employee Report Page**

1.  **Search by Name**

    1.  The Search by Name dropdown is used to search for current employees

        1.  Employee Searches can be conducted by selecting the employee’s name
            from the dropdown menu

        2.  Click “Get Info” after an employee name is selected to display
            Employee Information.

2.  **Employee Information Card**

    1.  The Employee Information Card displays the information for the employee
        that has been selected via Search Bar (*Fig. 3*)

    2.  The Employee Information Card displays the following employee details
        including:

        1.  Personally Identifiable Information

        2.  Employment

        3.  Department, Position, Title

<img src="/readme_images/img3.jpg" />
*Figure 3 – Employee Report Page*

**Directory**

1.  **Employee Search**

    1.  Allows administrator to look up individual employees by department,
        title, name or Employee ID (*Fig. 4)*

        1.  A dropdown menu will sort employees based on their department,
            title, last name, first name or employee ID

        2.  Once a selection has been made, click the “Select” button

        3.  A table will populate below with a list of sorted employees

<img src="/readme_images/img4.jpg" />
*Figure 4 – Directory*

**Add Employee**

1.  **Adds an Employee**

    1.  Allows administrator to add an employee to the system (*Fig. 5)*

        1.  An empty form will be generated with various text fields

        2.  Some of the text fields will be required, such as personal
            information, position, title, and department, while others may be
            left empty.

        3.  The form will not submit if a required field is left empty

        4.  Once all the required and non-required fields data has been entered,
            administrator will click on the submit button

        5.  The employee will now be added to the database and can be located
            via the various search methods throughout the application

<img src="/readme_images/img5.jpg" />
*Figure 5 - Add Employee*

**Remove Employee**

1.  **Removes an Employee**

    1.  Allows administrator to remove an employee from EMS by selecting the
        employee’s name from the dropdown list and clicking “Select” (*Fig. 6)*

        1.  Selection must be confirmed before employee will be removed

        2.  *Note*: The selected employee will remain in the database for
            archival purposes, but will be marked as an “Inactive” employee
            during this process

<img src="/readme_images/img6.jpg" />
*Figure 6 - Remove Employee*

**Print**

1.  **Print Button**

    1.  The print button can be clicked from any page in EMS in order to print a
        copy of the current page

    2.  A pop-up window will appear in order to configure print settings (*Fig
        7)*

<img src="/readme_images/img7.jpg" />
*Figure 7 - Print*

**Informational Guide**

1.  **Informational Guide Button**

    1.  Clicking on the Informational Guide button will provide instant access
        to this user guide from EMS (*Fig. 8)*

<img src="/readme_images/img8.jpg" />
*Figure 8 - Informational Guide*

**Settings**

1.  **Logs User Out**

    1.  Ends user’s session (*Fig. 9)*

<img src="/readme_images/img9.jpg" />
*Figure 9 - Logout*

## <a name="tp"></a>Test Plan and Results

| **Page**                                          | **Functionality**                 | **Test Case**                                                                                            | **Inputs**                                                                                                                                     | **Expected Output**                                                                                                                                                                | **Pass/Fail** |
|---------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| **Main Page**                                     | Login                             | Verify valid login credentials allows log in                                                             | Valid Credentials                                                                                                                              | User is navigated to EMS Dashboard page and can access secure EMS pages.                                                                                                           | **PASS**      |
|                                                   |                                   | Verify invalid login credentials does not allow user to log in / access secure pages                     | Invalid Credentials                                                                                                                            | User cannot log into EMS / cannot navigate to secure pages                                                                                                                         | **PASS**      |
|                                                   |                                   | Verify that revoking login access from a user no longer allows that user to log in / access secure pages | Credentials are removed from existing user                                                                                                     | User can no longer log into EMS / cannot navigate to secure pages                                                                                                                  | **PASS**      |
|                                                   |                                   | Verify max login attempt of 3 tries before user is locked out and must contact administrator             | Invalid login credentials are used 3+ times                                                                                                    | User receives error message stating they have reached their max number of login attempts and they must contact their administrator. Account is marked as “locked out” in database. | **PASS**      |
|                                                   | “Learn More” Button               | Verify that clicking “Learn More” button results in Contact information pop-up                           | “Learn More” button is clicked                                                                                                                 | “Learn More” pop-up opens                                                                                                                                                          | **PASS**      |
|                                                   | “Contact Us” Button               | Verify that clicking “Contact Us” button results in Contact information pop-up                           | “Contact Us” button is clicked                                                                                                                 | “Contact Us” pop-up opens                                                                                                                                                          | **PASS**      |
| **Dashboard Page**                                | “Report” Card                     | Verify navigation to Reports page                                                                        | “Go to Report” button on the “Report” card is clicked.                                                                                         | User navigates Report page                                                                                                                                                         | **PASS**      |
|                                                   | “Directory” Card                  | Verify navigation to Directory page                                                                      | “Go to Directory” button on the “Directory” card is clicked.                                                                                   | User navigates to Directory page                                                                                                                                                   | **PASS**      |
|                                                   | “Add User” Card                   | Verify navigation to Add User page                                                                       | “Go to Add User” button on the “Add User” card is clicked.                                                                                     | User navigates to Add User page                                                                                                                                                    | **PASS**      |
|                                                   | “Remove User” Card                | Verify navigation to Remove User page                                                                    | “Go to Remove User” button on the “Remove User” card is clicked.                                                                               | User navigates to “Average Salaries” page                                                                                                                                          | **PASS**      |
|                                                   | “Informational Guide” Card        | Verify navigation to Informational Guide page                                                            | “Go to Info Guide” button on the “Informational Guide” card is clicked.                                                                        | User navigates to “Informational Guide” page                                                                                                                                       | **PASS**      |
|                                                   | “Settings” Card                   | Verify navigation to Settings page                                                                       | “Go to Settings” button on the “Settings” card is clicked.                                                                                     | User navigates to “Settings” page                                                                                                                                                  | **PASS**      |
| **Employee Report Page**                          | Search Drop down list             | Verify that searching for a current employee returns valid search information                            | Current Employee’s name is selected from drop down list                                                                                        | Employee details are listed for correct employee                                                                                                                                   | **PASS**      |
|                                                   | Edit button                       | Verify that any changes made to selected employee are updated in the database                            | Update data as needed then click the “Edit” button                                                                                             | Selected employee’s updated information is updated in the database                                                                                                                 | **FAIL**      |
| **Directory Page**                                | “Sort by Category” Drop down list | Verify that sorting by “Department” results in employees sorted by department                            | Select “Department” from drop down and click “Select” button                                                                                   | Employees are sorted by department                                                                                                                                                 | **PASS**      |
|                                                   |                                   | Verify that sorting by “Title” results in employees sorted by title                                      | Select “Title” from drop down and click “Select” button                                                                                        | Employees are sorted by title                                                                                                                                                      | **PASS**      |
|                                                   |                                   | Verify that sorting by “Last Name” results in employees sorted by last name                              | Select “Last Name” from drop down and click “Select” button                                                                                    | Employees are sorted by last name                                                                                                                                                  | **PASS**      |
|                                                   |                                   | Verify that sorting by “First Name” results in employees sorted by first name                            | Select “First Name” from drop down and click “Select” button                                                                                   | Employees are sorted by first name                                                                                                                                                 | **PASS**      |
|                                                   |                                   | Verify that sorting by “Employee ID” results in employees sorted by employee ID                          | Select “Employee ID” from drop down and click “Select” button                                                                                  | Employees are sorted by employee ID                                                                                                                                                | **PASS**      |
| **Add Employee Page**                             | Add Employee                      | Verify that adding employee with valid data correctly creates new entry in the database                  | First name, Last name, SSN, License number, Email, Phone, Address, City, State, Zip, Department, and Title are entered, then hit submit button | New employee record is inserted into the database                                                                                                                                  | **PASS**      |
|                                                   |                                   | Verify that newly created employee is included in the Employee Report                                    | Employee Report is run                                                                                                                         | New employee details are included in report                                                                                                                                        | **PASS**      |
|                                                   |                                   | Verify that newly created employee appears in the Directory Listing                                      | Directory Listing is pulled                                                                                                                    | New employee details are included in Directory listing                                                                                                                             | **PASS**      |
|                                                   |                                   | Verify that attempting to add an employee with invalid data inputs will give a valid error message.      | Invalid input is used for creating employee, i.e., “\$%\$\^\$%” for a phone number.                                                            | Valid error message is given to user stating that input is invalid.                                                                                                                | **PASS**      |
| **Remove Employee Page**                          | Remove Employee                   | Verify that removing an employee deletes employee from database                                          | Employee removed via “Remove Employee” functionality                                                                                           | Specific employee is deleted from database                                                                                                                                         | **PASS**      |
|                                                   |                                   | Verify that removed employee does not show in Employee Report                                            | Employee removed via “Remove Employee” functionality                                                                                           | Specific employee does not show up in Employee Reports                                                                                                                             | **PASS**      |
|                                                   |                                   | Verify that removed employee does not show in Directory listing                                          | Employee removed via “Remove Employee” functionality                                                                                           | Specific employee does not show up in Directory listing                                                                                                                            | **PASS**      |
| **Print Button**                                  | Print Functionality               | Verify that clicking “Print” icon on the Dashboard page produces expected output                         | Print button is clicked from the dashboard page                                                                                                | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
|                                                   |                                   | Verify that clicking “Print” icon on the Employee Report page produces expected output                   | Print button is clicked from the Employee Report page                                                                                          | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
|                                                   |                                   | Verify that clicking “Print” icon on the Directory page produces expected output                         | Print button is clicked from the Directory page                                                                                                | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
|                                                   |                                   | Verify that clicking “Print” icon on the Add Employee page produces expected output                      | Print button is clicked from the Add Employee page                                                                                             | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
|                                                   |                                   | Verify that clicking “Print” icon on the Remove Employee page produces expected output                   | Print button is clicked from the Remove Employee page                                                                                          | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
|                                                   |                                   | Verify that clicking “Print” icon on the Informational Guide page produces expected output               | Print button is clicked from the Informational Guide page                                                                                      | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
|                                                   |                                   | Verify that clicking “Print” icon on the Settings page produces expected output                          | Print button is clicked from the Settings page                                                                                                 | Printer pop-up is displayed, and page can be printed                                                                                                                               | **PASS**      |
| **Informational Guide**                           | Informational Guide               | Verify that the Informational Guide displays as expected on the page                                     | Informational Guide button is clicked                                                                                                          | Informational Guide is displayed                                                                                                                                                   | **PASS**      |
| **Miscellaneous (Not included in specific page)** | Cross-browser Testing             | Verify that EMS pages function as expected in Google Chrome                                              | EMS is accessed via Google Chrome                                                                                                              | EMS functions as designed in Chrome browser                                                                                                                                        | **PASS**      |
|                                                   |                                   | Verify that EMS pages function as expected in Firefox                                                    | EMS is accessed via Firefox                                                                                                                    | EMS functions as designed in Firefox browser                                                                                                                                       | **PASS**      |
|                                                   |                                   | Verify that EMS pages function as expected in Safari                                                     | EMS is accessed via Safari                                                                                                                     | EMS functions as designed in Safari browser                                                                                                                                        | **PASS**      |
|                                                   |                                   | Verify that EMS pages function as expected in Edge                                                       | EMS is accessed via Microsoft Edge                                                                                                             | EMS functions as designed in Edge browser                                                                                                                                          | **PASS**      |

**Known Bugs**

There is a known bug with editing employee information. If a user attempts to
update employee information and save, a success message will appear, however the
information in the database is not currently being updated. The current
workaround for this bug is to delete the user and recreate a new user with the
corrected/updated information. This bug will be addressed in a future release of
EMS.

## <a name="designs"></a>Design and Alternate Designs

**Database Design**

The Employee Management Software is designed using an Oracle Cloud database
consisting of 8 tables:

1.  Users

2.  Employees

3.  Employee Notes

4.  Employee Info

5.  Department

6.  Employee Task Link

7.  Tasks

8.  Status

The database setup diagram is shown in Figure 10.

<img src="/readme_images/img10.jpg" />
*Figure 10 - Database Design*

**Controllers**

There are 8 controllers that have been created in order to fetch the requested
data from the database and return a list:

| **Controller Name**              | **Controller Function**                                                                                                                                                          |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| department_controller.py         | This controller uses the get\_departments() function in order to run the SQL statement “SELECT \* FROM DEPARTMENT” and return the list of departments from the database          |
| employee_info_controller.py      | This controller uses the get\_info() function in order to run the SQL statement “SELECT \* FROM EMPLOYEE_INFO” and return the list of employee info from the database            |
| employee\_notes_controller.py    | This controller uses the get\_notes() function in order to run the SQL statement “SELECT \* FROM EMPLOYEE_NOTES” and return the list of employee notes from the database         |
| employee_task_link_controller.py | This controller uses the get\_link() function in order to run the SQL statement “SELECT \* FROM EMPLOYEE_TASK_LINK” and return the list of employee task links from the database |
| employees_controller.py          | This controller uses the get\_employee() function in order to run the SQL statement “SELECT \* FROM EMPLOYEES” and return the list of employees from the database                |
| status_controller.py             | This controller uses the get\_status() function in order to run the SQL statement “SELECT \* FROM STATUS” and return the list of statuses from the database                      |
| tasks_controller.py              | This controller uses the get\_tasks() function in order to run the SQL statement “SELECT \* FROM TASKS” and return the list of tasks from the database                           |
| Users_controller.py              | Checks the DB if the provided credentials are valid. Will return FALSE if not valid.                                                                                             |

**Classes**

There are 7 classes that have been created for this project:

| **Class Name**         | **Class**                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class Department       | class Department: def \_*init*\_(self, deptID, deptTitle): self.deptID = deptID self.deptTitle = deptTitle                                                                                                                                                                                                                                                                                                 |
| class EmployeeInfo     | class EmployeeInfo: def \_*init*\_(self, infoID, empID, address, city, state, zipcode, licenseID, ssn): self.infoID = infoID self.empID = empID self.address = address self.city = city self.state = state self.zipcode = zipcode self.licenseID = licenseID self.ssn = ssn                                                                                                                                |
| class EmployeeNotes    | class EmployeeNotes: def \_*init*\_(self, noteID, empID, description, datetime): self.noteID = noteID self.empID = empID self.description = description self.datetime = datetime.now()                                                                                                                                                                                                                     |
| class Employees        | class Employee: def \_*init*\_(self, empID, deptID, fname, lname, title, phone, email): self.empID = empID self.deptID = deptID self.fname = fname self.lname = lname self.title = title self.phone = phone self.email = email def fullname(self): return '{} {}'.format(self.fname, self.lname) def get_department_title(self, list): for val in list: if val.deptID == self.deptID: return val.deptTitle |
| class EmployeeTaskLink | class EmployeeTaskLink: def \_*init*\_(self, linkID, empID, taskID): self.linkID = linkID self.empID = empID self.taskID = taskID                                                                                                                                                                                                                                                                          |
| class Status           | class Status: def \_*init*\_(self, statusID, name): self.statusID = statusID self.name = name                                                                                                                                                                                                                                                                                                              |
| class Tasks            | class Tasks: def \_*init*\_(self, taskID, title, datetime, description, statusID): self.taskID = taskID self.title = title self.datetime = datetime self.description = description self.statusID = statusID def get_status_name(self, list): for val in list: if val.statusID == self.statusID: return val.name                                                                                            |

**Web Services**

There are three web services for this project, Employee Service, User Service
and Validation:

| **Service Name**    | **Functionality**                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------------------------|
| employee_service.py | Handles all client-side logic, including taking values from input fields and sending them over to the controllers. |
| user_service.py     | Grabs values from the input fields on the login page and sends to user_controller for validation.                  |
| validation.py       | Handles all validation logic (checking if values are the correct length or type).                                  |

**Finalized Website Design**

The user interface for Employee Management Software is designed using Bootstrap.
The finalized project design includes the following pages:

**Home Page**

The home page is designed to include a user login in the top right corner. This
log in, shown in Figure 11, will be the required log in for administrators to
access any page after the home page. Figures 12 and 13 show the remainder of the
home page, which will utilize a card design in order to provide more information
about Employee Management Software to potential customers.

<img src="/readme_images/img11.jpg" />
*Figure 11 - Home Page Login*

<img src="/readme_images/img12.jpg" />
*Figure 12 - Home Page Continued*

<img src="/readme_images/img13.jpg" />
*Figure 13 - Home Page Continued*

**Side Navigation Bar**

After logging into the home page, the side navigation bar (Figure 14) will be
visible on every page within the Employee Management Software. This navigation
bar will provide easy access to all of the pages within EMS, including the
Dashboard, Employee Report, Directory, Add Employee, Remove Employee, Print,
Informational Guide and Settings pages.

<img src="/readme_images/img14.jpg" />

**Dashboard**

The dashboard page, shown in Figure 15, has been designed with a card layout in
order to give administrators a quick overview of functions within the system and
easy-access shortcuts to get to the most frequently used functions.

<img src="/readme_images/img15.jpg" />
*Figure 15 - Dashboard Layout*

**Employee Report**

The Employee Report page is designed to allow administrators to search by
Employee Name in order to retrieve the Employee Information details outlined in
Figure 16.

<img src="/readme_images/img16.jpg" />
*Figure 16 - Employee Report Design*

**Directory**

The Directory page lists all employees and displays their Employee ID,
Department, Title, Last Name, First Name, Email and Phone number, as shown in
Figure 17. The “Search by Category” dropdown menu allows different methods of
sorting the data by Department, Title, Last Name, First Name and Employee ID.

<img src="/readme_images/img17.jpg" />
*Figure 17 - Directory Page Design*

**Add Employee**

The Add Employee page is designed as a form for administrators to fill out all
fields as shown in Figure 18. Upon submitting this form, the data will create a
new employee entry in the database and the new employee’s information will now
be available across Employee Management System, such as on the Employee Report
and Directory pages.

<img src="/readme_images/img18.jpg" />
*Figure 18 - Add Employee Design*

**Remove Employee**

The Remove Employee page presents users with a dropdown of all current
employees. The administrator will select the desired employee from the dropdown
menu and click on “Select” to remove the employee (Figure 19). After this action
is taken, the selected employee will no longer appear in Employee Management
Software, such as on the Employee Report or Directory pages.

<img src="/readme_images/img19.jpg" />
*Figure 19 - Remove Employee Design*

**Print**

The Print icon will be available in the side navigation pane on all pages after
the home screen. By clicking on this button, users will be able to print the
current page that they are on. The user will receive the default printer pop-up,
as shown in Figure 20.

<img src="/readme_images/img20.jpg" />
*Figure 20 - Print Pop-up*

**Informational Guide**

The Informational Guide (Figure 21) page is designed with a card layout to be an
easy-to-access user guide for Employee Management Software. Users will be able
to access how-tos for each of the pages within the system.

<img src="/readme_images/img21.jpg" />
*Figure 21 - Informational Guide Design*

**Settings**

The settings page is currently designed to allow administrators to log out of
the Employee Management System (Figure 22).

<img src="/readme_images/img22.jpg" />
*Figure 22 - Settings Design*

Alternate Website Designs

The original website concept included the following designs (figures 23-26) that
are no longer being used:

**Home Page Login**

<img src="/readme_images/img23.jpg" />
*Figure 23 - Original Home page design*

<img src="/readme_images/img24.jpg" />
*Figure 24 - Original home page design continued*

**Dashboard**

<img src="/readme_images/img25.jpg" />
*Figure 25 - Original Dashboard design*

**Informational Guide**

<img src="/readme_images/img26.jpg" />
*Figure 26 - Original Informational Guide design*

## <a name="dh"></a>Development History

**Items Removed from Project Scope**

The following items were removed from the orignal project scope:

-   AES Encryption

-   Chat

-   File Upload

-   Employee Tasks

These items were removed during the development phases once it was determined
that it would not be feasible to complete development on these features while
also delivering a fully tested, bug-free project. These features were determined
to be enhancements that were not required for the initial completion of the
project.

**Development Timeline**

| **Development Task**                                                | **Date Completed** |
|---------------------------------------------------------------------|--------------------|
| Boilerplate Website, Database Schema, Function Templates, Objects   | 30 March 2021      |
| Create Main Pages, Create Login Page, Deploy and Configure Database | 6 April 2021       |
| Create Tabbed Pages, Build Controllers                              | 13 April 2021      |
| Connect Front-end to Back-end, Route Pages to Back-end              | 20 April 2021      |
| Finalized Back-end Services                                         | 4 May 2021         |
| Implement Validation Regular Expressions                            | 10 May 2021        |

## <a name="conclusion"></a>Conclusions

**Lessons Learned**

The team learned many lessons regarding project management within the past 8
weeks. This course has given us a newfound respect for the project management
process, as we have experienced the project lifecycle from all roles—project
manager, stakeholder, developer and quality assurance tester. A lesson we have
all learned is that while it is great to be optimistic at the beginning of a
project, it is equally important to be realistic when setting project goals and
timelines, especially when the project length is a short, predetermined amount
of time.

Another lesson that was learned is how easy it can be for project requirements
to change, whether it is due to development constraints or stakeholder changes,
and how important it is for the team as a whole to evaluate these decisions.
Requirement changes do not only impact the development of a project, it filters
down to all areas and causes changes within design, development, testing and
project milestones. It also affects all related documentation, such as
requirements specification, design, test plans, user guides and any other
documentation that may relate to the project requirements. .

**Design Strengths**

The design strengths of this application are the robustness of the application,
through the simplicity in its design. The application performs multiple
functions with regard to the management of the employees. An administrator can
view, add, delete, and modify employee’s data as their responsibilities change.
Additionally, an administrator can quickly view employees in a table format,
filtering employees based on several different parameters such as by their
position, alphabetically, etc. The UX/UI offers a modern and familiar interface
making the application easy to follow. In addition, an intuitive user guide is
also added as a reference to further assist the administrator in the use of the
application.

**Limitations**

One of the main challenges of this class was determining an acceptable project
scope in Weeks 1 and 2. The combination of having an open-ended project prompt
and working with a brand new team meant that it was difficult to gauge what an
appropriate project scope was, while ensuring that all features could be
implemented within the set 8-week timeframe. While our group had to take out
some features to make the project manageable, we believe we did a good job with
initially outlining the project and picking out requirements.

**Suggestions for Future Improvements**

For future improvements on the Employee Management Software project, our group
would be interested in implementing the features that were taken out of the
current project scope, including file upload, Employee Tasks, AES encryption and
potentially a chat feature.
