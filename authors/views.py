from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer =RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            Author.objects.create(user=user)
            return Response({'detail': 'The author has successfully been created.'}, status=201)
        else:
            return Response(serializer.errors, status=400)
