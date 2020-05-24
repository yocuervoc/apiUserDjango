
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
            'click_couter',
            'connected_time',
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
    

    def create(self, data):
        instance = User()
        instance.first_name = data.get('first_name')
        instance.last_name = data.get('last_name')
        instance.email = data.get('email')
        instance.username = data.get('usename')
        instace.click_couter = data.get('click_couter')
        instance.set_password(data.get('password'))
        instance.save()
        return instance
"""