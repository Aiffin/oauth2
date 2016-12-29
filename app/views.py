from django.shortcuts import render
from app.models import Register
from app.serializers import RegisterSerializer
from rest_framework import generics
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

class RegisterList(generics.ListCreateAPIView):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=Register.objects.all()
	serializer_class=RegisterSerializer

class RegisterDetails(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [permissions.IsAuthenticated, TokenHasScope]
	required_scopes = ['register']
	queryset=Register.objects.all()
	serializer_class=RegisterSerializer
