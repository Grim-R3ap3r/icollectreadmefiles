# University Admin

## Brief Description

University Admin is a web application to help university admin’s maintain the data of students. The Admin has to create a User Profile then that user can add students with the subjects the student has opted to study. Then the Admin can later on see the list of students with the subjects he/she has chosen from My Students button on the home page or from the Navigation bar at the top.

The Admin can edit the subjects in future too or delete a student’s data in case any student opts to drop out or change the subjects. The Web Application provides authentication and privacy capabilities to the user. All data of the user will be stored in an online database and will be protected so that no user without proper credentials can access it.

## Features:
### 1. Signup: 
Enter Username, email and set a password.
<p align="center">
  <img src = "Images/SignUpPage.jpg" >
</p>
  
### 2. Login: 
Users can log in using the email id and password.

<p align="center">
  <img src = "Images/SignInPage.jpg" >
</p>

### 3. Homepage:
* The Homepage displays two options of accessing the list of students added or adding a new Student. 
* Those can be accessed via the navigation bar at the top or from the buttons too.

<p align="center">
  <img src = "Images/HomePage.jpg" >
</p>

### 4. Add Student:
* The User can add a student by filling the form presented.
* The User will have to enter the name, roll number and choose the subjects the given student has opted.  

<p align="center">
  <img src = "Images/AddStudent.jpg" >
</p>

### 5. My Students:
* The user will get the list of previously added students.
* The user can click on the particular student's name and can see the full details of the current student and can choose to edit or delete the student.

 <p align="center">
  <img src = "Images/MyStudents.jpg" >
</p>

### 6. Student Profile:
* The user will get the detailed information of the student with the subjects a particular student has opted to study.
* The user can choose to edit those subjects or even delete the student data by clicking on the delete button presented below the form.

 <p align="center">
  <img src = "Images/EditStudentData.jpg" >
</p>


## Technologies Used
* [HTML](https://devdocs.io/html/): It is the code that is used to structure a web page and its content.
* [CSS](https://devdocs.io/css/): It is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.
* [React.Js](https://github.com/reactjs/reactjs.org "Reactjs") : It makes it painless to create interactive UIs. Design simple views for each state in your application, and React will efficiently update and render just the right components when your data changes.
* [Node.Js](https://github.com/nodejs/node "NodeJs"): It is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser.
* [Express.Js](https://expressjs.com/en/5x/api.html): It is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.
* [MongoDB](https://docs.mongodb.com/ "MongoDB"): It is a document database with the scalability and flexibility that you want with the querying and indexing that you need
* [Redux](https://github.com/reduxjs/redux "Redux"): It helps us to write applications that behave consistently, run in different environments (client, server, and native), and are easy to test.
* [Javascript](https://devdocs.io/javascript/): It is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive.

## DEPLOYMENT LINK
[University Admin Application](https://universityadmin.herokuapp.com/)


## Setup Steps:
1. Open Terminal/Command Prompt.
2. Change the current working directory to the location where you want the cloned directory.
3. Copy the following command in the Terminal/Command Prompt to clone the project:
#### `git clone https://github.com/anujpatidar3/University-Admin.git`
4. Change your current directory to the cloned directory.
5. In the project directory, run: :
#### `node app.js`
Runs the backend on the 5000 port.

6. Change the directory to the client folder and run:
#### `npm start`
Runs the app in the development mode.
Open [https://localhost:3000](https://localhost:3000) to view it in the browser.
