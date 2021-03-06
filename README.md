# Bangazon API

Built using Python, Django, and the Django REST Framework for serving data to the related [client-side application](https://github.com/nss-day-cohort-38/bangazon-ecommerce-web-app-ark-moon) via HTTP request.

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
1. First things first, you will need an authorization token to successfully request data from the database. To obtain one, you will need to post to ```localhost:8000/register/``` with the following HTTP request:
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
This will return a token object that will serve as your authorization token. Now that you have this token, you can include a header with the key "Authorization" and a value of "Token ${your-token here}". This will allow you to use the available functionality for each of the available viewsets.

![Postman Headers](https://github.com/nss-day-cohort-38/bangazon-ecommerce-api-ark-moon/blob/JP-read-me/bangazonapi/images/BangazonPostmanHeaders.png)

### ```/customers```

#### GET

When you perform a get request with a valid auth token on customers, you will be provided with a list of all the customers in your database. You can also get the information for individual customers by using /{customer-id} e.g. ```/1```, ```/2```, etc.

### ```/orderproducts```

There is automatated unit testing available for this viewset. Run ```python manage.py test``` to execute testing.

#### GET

When you perform a get request, the request will return a list of all the order-product relationships present in that. You can also call individual instances by using /{order-product-id}.

#### POST

When you perform a request with the body of ```{order_id: x, product_id: x}```, the new information will be added to the database. NOTE: There must be order and product already in the database for this to work. Otherwise it will fail the not null constraint.

#### DELETE

When you perform a delete request on a specific instance of orderproduct, for example ```orderproducts/1```, the relationship will be permanently removed from the database.

### ```/orders```

There is automatated unit testing available for this viewset. Run ```python manage.py test``` to execute testing.

#### GET

When you perform a get request with a valid auth token, the API will return a list of all of the orders ASSOCIATED WITH THAT USER'S AUTH TOKEN. It is not possible in this database to get a list of all of the orders. However, it is possible to obtain the information for a specific order regardless of auth status by using the order's id, eg. ```orders/1```.

#### POST

When a user performs a post with the body ```{}``` and with a valid auth token in the headers, a new order using the customer information provided by the auth token will be added to the database.

#### DELETE

When the user performs a delete on an instance of order, the data will be removed from the database and an empty object will be returned to the user.

### ```/paymenttypes```

There is automatated unit testing available for this viewset. Run ```python manage.py test``` to execute testing.

#### GET

When you perform a get request with a valid auth token, the API will return a list of payment types associated with the user's auth token. IT IS NOT POSSIBLE TO GET A LIST OF ALL PAYMENT TYPES. However, one can currently get individual payment types without an auth token. This a security fix that will be patched in a later update.

#### POST

When the user performs a post with an auth token in the headers and a body of ```{"merchant_name": "test", "account_number": "test", "expiration_date": "test"}```, that information will be added to the database.

#### DELETE

When the user performs a delete request on a specific incidence of payment type, the payment type will be deleted from the database.

### ```/products```

#### GET

When the user requests information from the products viewset, the API returns a list of all products currently in the database. The user can also retrieve instances of individual products by using ```products/{product-id}```.

#### PATCH

Used to change the quantity in the product object. When the user performs a patch request with a body of ```{"quantity": {any-integer}}```, the product is updated with the new quantity. Used on the front end to subtract from the quantity of products that are currently in inventory once an order is completed.

#### DELETE

When the user performs a delete request on an example of a product, the product is cleared from the database.

### ```/sell```

#### POST

When the user does a post request with a valid auth token, the body of the request will be posted to the database.

IMPORTANT NOTE: When posting in Postman, use the "form-data" body format instead of raw JSON. This will allow for the easier uploading of files for images. Example:
![post in sell](https://github.com/nss-day-cohort-38/bangazon-ecommerce-api-ark-moon/blob/JP-read-me/bangazonapi/images/BangazonPostmanPostProductBody.png)

## Contributors

* [Sofia Candiani](https://github.com/sncandiani)
* [Matt Crook](https://github.com/mattcrook)
* [Jeremy Mattingly](https://github.com/halcyonvagabond)
* [Landon Morgan](https://github.com/Iandonmorgan)
* [Alyssa Nycum](https://github.com/alyssanycum)
* [Jack Parsons](https://github.com/jcksnparsons)
