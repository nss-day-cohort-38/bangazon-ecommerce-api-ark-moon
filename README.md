### Bangazon API

Built using Python, Django, and the Django REST Framewor for serving data to the related [client-side application](https://github.com/nss-day-cohort-38/bangazon-ecommerce-web-app-ark-moon) via HTTP request.

# Our ERD:

![bangazon ERD](./bangazon-ecommerce-api-ark-moon/bangazonapi/images/BangazonERD_TheArkMoon.png)

# How to access

1. Clone down this repository and navigate into it in your terminal.
2. Create a virtual environment with the following command
```
python -m venv bangazonEnv
```
3. Start your virtual environment with the following commands:
* For Mac Users:
```
source ./bangazonEnv/bin/activate
```
* For Windows Users:
```
source ./bangazonEnv/Scripts/activate
```
4. Run the following command to install all of the necessary dependencies:
```
pip install -r requirements.txt
```
5. Now that you have created a virtual envirnonment and installed the necessary dependencies inside it, you can now run the following commands:
```
python manage.py makemigrations
```
This will create database structures using the models built in the models directory.
```
python manage.py migrate
```
This will transport those structures into a newly created database.
6. Start up your server with this command:
```
python manage.py runserver
```
