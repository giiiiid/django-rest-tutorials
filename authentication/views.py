from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework import status
# Create your views here.
class Register(GenericAPIView):

    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)