# Bangazon API

Built using Python, Django, and the Django REST Framewor for serving data to the related [client-side application](https://github.com/nss-day-cohort-38/bangazon-ecommerce-web-app-ark-moon) via HTTP request.

## Our ERD:

![bangazon ERD](https://github.com/nss-day-cohort-38/bangazon-ecommerce-api-ark-moon/blob/JP-read-me/bangazonapi/images/BangazonERD_TheArkMoon.png)

## How to access

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

## Testing in Postman

### Registration
1. First things, first you will need an authorization token to successfully request data from the databse. To obtain one, you will need to post to ```localhost:8000/register/``` with the following HTTP request:
```
{
	"username":"test",
	"first_name":"test",
	"last_name":"test",
	"email":"test@test",
	"address":"test",
	"phone_number":"test",
	"password":"test"
}
```
This will return a token object that will serve as your authorization token. Now that you have this token, you can include header with the key "Authorization" with a value of "Token ${your-token here}". This will allow you to use the available functionality for each of the available viewsets.

![Postman Headers](https://github.com/nss-day-cohort-38/bangazon-ecommerce-api-ark-moon/blob/JP-read-me/bangazonapi/images/BangazonPostmanHeaders.png)

### ```/customers```

#### GET

When you perform a get request with a valid auth token on customers, you will be provided with a list of all the customers in your database. You can also get the information for individual customers by using /{customer-id} e.g. ```/1```, ```/2```, etc.

### ```/orderproducts```

#### GET

When you perform a get request, the request will return a list of all the order-product relationships present in that. You can also call individual instances by using /{order-product-id}.

#### POST

When you perform a request with the body of ```{order_id: x, product_id: x}```, the new information will be added to the database. NOTE: There must be order and product already in the database for this to work. Otherwise it will fail the not null constraint.

#### DELETE

When you perform a delete request on a specific instance of orderproduct, for example ```orderproducts/1```, the relationship will be permanently removed from the database.

## Contributors

* Sofia Candiani
* Matt Crook
* Jeremy Mattingly
* Landon Morgan
* Alyssa Nycum
* Jack Parsons

