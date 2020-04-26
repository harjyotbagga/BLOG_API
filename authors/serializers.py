from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True} }

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        return User.objects.create(password=password, **validated_data)

