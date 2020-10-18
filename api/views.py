from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        content = {'message':'Hello, world'}
        return Response(content)

class UserCreate(APIView):
    '''
    Creates the user.
    '''
    def post(self,request,format='json'):
        serialier = UserSerializer(data=request.data)
        if serialier.is_valid():
            user = serialier.save()
            if user:
                token = Token.objects.create(user=user)
                json = serialier.data
                json['token']=token.key
                return Response(json,status=status.HTTP_201_CREATED)
        return Response(serialier.errors,status=status.HTTP_400_BAD_REQUEST)