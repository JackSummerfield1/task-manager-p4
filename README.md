# Task Manager

Task Manager is a full-stack, responsive website built with an incentive to get people to become more productive. This website is for educational purposes only!

The website consists of a default Task Manager page where users gain full accessibility to the features when logged in. If not logged in, users are redirected to the login/ signup pages before gaining access the the site.

[Click here](https://task-manager-p4-948686f46531.herokuapp.com/) to go to the Task Manager's Live Wesbite.

![Am I responsive image](documentation/responsive.png)

## Table of Contents

- [Overview](#overview)
- [Agile Methodology](#agile-methodology)
- [User Experience (UX)](#user-experience-ux)
  - [Strategy / Site Goals](#strategy--site-goals)
  - [Scope / User Stories](#scope--user-stories)
  - [Structure / Design Choices](#structure--design-choices)
  - [Skeleton / Wireframes](#skeleton--wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Creating a Local Clone](#creating-a-local-clone)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

[Back To Top](#Task-Manager)

---

## Overview

Task Manager is a responsive website, prioritising mobile users. It is compatible with all current major browsers. The website is built for educational purposes, using Bootstrap and the Django framework.

It gives users the ability to complete simple variations of registration (login/signup) and includes full CRUD functionality.

[Back To Top](#table-of-contents)

---

## Agile Methodology

The plan for this project was carried out using Agile Methodology. GitHub Issues, which can be viewed [here](https://github.com/JackSummerfield1/task-manager-p4/issues?q=is%3Aissue+is%3Aclosed), were used to recored the User Stories.

Each User Story contains Acceptance Criteria which I sometimes had to change after I did the process as it didn't meet the criteria I initially aimed for.

[Here](https://github.com/users/JackSummerfield1/projects/3) is also a link to my KanBan board.

[Back To Top](#Task-Manager)

---

## User Experience (UX)

### Strategy / Site Goals

This Task Manager Website provides a secure and efficient platform for users to manage their tasks. The website allows logged-in users to perform CRUD (Create, Read, Update, Delete) operations on their tasks. User authentication ensures data privacy, and the platform supports role-specific functionalities for users, administrators, and developers.

---

### Scope / User Stories

**As an admin**

- I can manager user accounts so that I can maintain the system's integrity.

- I can monitor user tasks so that I can audit and provide support when needed.

**As a user**

- I can log in to the task manager so that I can securely access my tasks.

- I can view my list of tasks so that I can keep track of what needs to be completed.

- I can create, edit, and delete tasks so that I can manage my workload.

- I can log out of the system so that I can ensure security of my account and all of my tasks will be saved.

**As a developer**

- I can implement new features so that the system stays up-to-date and meets user needs.

- I can debug and maintain the codebase so that the platform runs quickly and efficiently.

### Structure / Design Choices

The website is simple and consistent with its structure. Its structure was designed to be responsive for most devices.

The Navigation menu displays Login Register options if a user is not logged in and the Logout option when logged in. This ensures access control and security is guaranteed and users can only access features once logged in.

The Task List Page clearly provides a list of all the tasks associated with that user. The Add, Edit and Delete options are all clear on how to use.

Confirmation messages are provided to the user when completing something. E.g. signing out, creating a task, editing a task, deleting a task etc. Ensuring the user of every option they choose to do.

Only one custom model has been implemented into this project.

**The Task Model** - User to Task: One-to-Many (A user can create multiple tasks):

**ERD Diagram of the Task Model:**

![Task-Model-ERD](documentation/erd-dia.png)

---

### Skeleton / Wireframes

Wireframes were first sketched on paper and then found some ones that were more appropriate for the structure I wanted to go with.

**Registration Wireframes**

![Registration-Wireframes](documentation/registration-wire.png)

**Task-CRUD-Wireframes**

![Task-CRUD-Wireframes](documentation/task-crud-wire.png)

[Back To Top](#Task-Manager)

## Features

**User Authentication:**

- Secure user login and logout functionality.
  Ensures tasks are only accessible to their respective users.

**Task Management:**

- Create, view, update, and delete tasks easily.
- Each task includes details like title, description, deadline, priority, and completion status.

**Priority Levels:**

- Assign tasks a priority level (Low, Medium, High) to manage workload effectively.

**Completion Tracking:**

- Mark tasks as completed to stay organized and track progress.

**Deadlines:**

- Optional deadlines to help users manage time-sensitive tasks.

**Personalized Task Lists:**

- Users can view a filtered list of tasks specific to their account.

**Responsive Notifications:**

- Success messages after creating, updating, or deleting tasks provide instant feedback.

**Mobile-Friendly Design:**

- Optimized for use on mobile and desktop devices, ensuring accessibility on the go.

**Confirmation for Deletions:**

- A confirmation page ensures users don't accidentally delete tasks.

**Secure Data Management:**

- Tasks are tied to individual user accounts, preventing unauthorized access.

[Back To Top](#Task-Manager)
