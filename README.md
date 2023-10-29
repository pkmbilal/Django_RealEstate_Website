
# Real Estate Web App

This is a web application for managing a small realestate business created using Django as backend and Html, Css & JavaScript as frontend, sqlite as Database.
## Authors

[@pkmbilal](https://github.com/pkmbilal) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)



## Features

- Create New Buildings, View All Buildings
- Create New Flats, View All Flats
- Create New Customers, View All Customers
- Create New Receipts, View All Receipts
- Custom Filters for above sections
## Documentation

- Initially create a folder with any name and clone project to that folder using below command
```bash
https://github.com/pkmbilal/Django_RealEstate_Website.git
```
- If Git is not installed in your system, you can download the project folder as zip format with the below link.
```bash
https://github.com/pkmbilal/Authentication_Django.git
```
- Create a virtual environment in the main folder(Not inside actual project folder).
```bash
pip install virtualenv
```
```bash
python<version> -m venv <virtual-environment-name>
```
- Then activate the virtual environment with the below command (Windows).
```bash
cd mainproject_folder_name/<virtual-environment-name>/Scripts
./activate
```
- Once the evnironment is activated, install the dependencies using the below command.
```bash
pip install -r requirements.txt
```
- I have used Sqlite as database. You can use any other database also. If so configure the databases section in settings.py file.
- Once the settings done use the below command to create necessary tables in the new database.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
- After that create a super user to access the admin area. Choose any username, password and email for superadmin.
```bash
python manage.py createsuperuser
```
- Finally run the live server
```bash
python manage.py runserver
```
- By clicking the http://127.0.0.1:8000/ you can open the project in your browser.