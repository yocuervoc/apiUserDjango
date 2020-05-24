
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )
"""
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    

    def create(selft, data):
        instance = User()
        instance.first_name = data.get('first_name')
        instance.last_name = data.get('last_name')
        instance.email = data.get('email')
        instance.set_password(data.get('password'))
        instance.save()
        return instance
"""