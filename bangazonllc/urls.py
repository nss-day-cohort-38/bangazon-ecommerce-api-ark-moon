"""bangazonllc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from bangazonapi.models import *
from bangazonapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'sell', Sell, 'sell')
router.register(r'paymenttypes', PaymentTypes, 'paymenttype')
router.register(r'products', Products, 'product')
router.register(r'customers', Customers, 'customer')
router.register(r'users', Users, 'user')
router.register(r'product-types', ProductTypes, 'producttype')
router.register(r'orders', Orders, 'order')
router.register(r'orderproducts', OrderProducts, 'orderproduct')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register_user),
    path('login/', login_user),
] 
# Since there is no route to media folder, 
# This is a static route to the media folder

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)