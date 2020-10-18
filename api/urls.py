from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import HelloView,UserCreate

app_name = 'api'

urlpatterns = [
    path('',HelloView.as_view(),name='index'),
    path('token-auth/',obtain_auth_token,name='token_auth'),
    path('create-user/',UserCreate.as_view(),name='account-create'),
]
