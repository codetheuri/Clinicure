# Clinicure
Clinicure is a web-based health management system designed to streamline patient appointments, treatments, inventory, payment via mpesa and premium subscriptions for medical clinics. It offers a user-friendly interface for clinic staff,   allowing easy management of health records and access to premium health facts.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Features

- **Patient Management:**
  - Add, view, update, and delete patient records.
  - Record patient appointments and treatments.

- **Premium Subscription:**
  - Allow patients to be subscribed to premium features.
  - Send health facts to subscribed patients via email.

- **User Authentication:**
  - Secure user registration, login, and logout.
  - Staff members can perform CRUD operations on patients.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codetheuri/Clinicure.git
2. Install dependencies:
   ``
     pip install -r requirements.txt
  ``
3. Apply Migrations:
   `` python manage.py migrate
    ``
4. Runserver
   ``python manage.py runserver   ``

Usage
Register an account or log in if you are a staff member.
Manage patients, appointments, and treatments.
Allow patients to subscribe to premium features for health facts.   
