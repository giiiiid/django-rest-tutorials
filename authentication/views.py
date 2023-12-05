from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
# Create your views here.

class Register(GenericAPIView):
    # data = request.data
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    