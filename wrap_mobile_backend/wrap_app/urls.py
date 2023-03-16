from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/login/', obtain_auth_token, name='login'),
    path('api/signup/', UserSignupView.as_view(), name='signup'),
]