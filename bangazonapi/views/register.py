import json 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from django.views.decorators.csrf import csrf_exempt
from bangazonapi.models import Customer

# Csrf_exempt is an access token
@csrf_exempt
def register_user(request): 
    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'], 
        email=req_body['email'], 
        password=req_body['password'], 
        first_name=req_body['first_name'], 
        last_name=req_body['last_name'], 
    )
    # Customer is equal to user that comes from Django and what we specify
    customer = Customer.objects.create(
        phone_number=req_body['phone_number'], 
        address=req_body['address'], 
        user=new_user
    )

    customer.save()
    # Creates association with token and user
    token = Token.objects.create(user=new_user)
    # Django way of converting to JSON
    data = json.dumps({"token": token.key})

    return HttpResponse(data, content_type='application/json')
@csrf_exempt
def login_user(request): 
    req_body = json.loads(request.body.decode())

    if request.method == 'POST': 
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)
        # If the authenticated user already exists
        if authenticated_user is not None: 
            # Retrieve their token
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key, "user": authenticated_user.id})
            return HttpResponse(data, content_type="application/json")
        else: 
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type="application/json")