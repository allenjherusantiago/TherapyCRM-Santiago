# TherapyCRM

## Student Details
    Allen Jheru Santiago
    22013022410
    BSIT

## Description of the System

Therapy CRM is a web-based system designed to manage and maintain records for therapy clients. It allows therapists to store customer information such as name, contact details, and diagnosis notes. The system also includes the ability to update customer records, manage notes, and delete records when necessary. The goal is to provide a user-friendly interface to help therapists efficiently manage their client records in a secure and organized manner.

### Features:
- **Customer Records**: Add, update, and delete customer records.
- **Therapist Notes**: Maintain notes or diagnosis for each customer.
- **Search and Filter**: Find specific customer records based on various filters.
- **Authentication**: Secure login and registration for users.

# How to run locally:

## Clone the repository:
    cd thrpy-crm
## Create a virtual environment:
    python -m venv venv
## Activate the virtual environment:
    venv\Scripts\activate
## Install required dependencies:
    pip install -r requirements.txt
## Set up the database
    Make sure to update the database configuration in the settings.py file. 
## Run the migrations to set up the database schema:
    python manage.py migrate
## Create a superuser for the admin panel
    python manage.py createsuperuser
## Run the server
    python manage.py runserver
## Access the application
    http://127.0.0.1:8000/
    
