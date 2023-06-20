from rest_framework import serializers
from django.db import transaction
from django.conf import settings

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password',
        ]

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registration of user
    It ensures that a first user does not exist without an account.
    """
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate_password(self, value):
        """Validating password length"""
        password_length = settings.USER_PASSWORD_LENGTH

        if len(value) < password_length:
            raise serializers.ValidationError(
                f"Password length must be at least {password_length} characters"
            )

        return value

    def validate(self, data):
        """
        Validating if password field data equals confirm_password field data.
        """
        password = data["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password":"Passwords do not match."})

        return data
    
    def create(self, validated_data):
        user = validated_data
        password = user['password']

        with transaction.atomic():
            user = User.objects.create_user(
                username=user['username'], 
                first_name=user['first_name'], 
                last_name=user['last_name'], 
                email=user['email'],
                password=password
            )            

            return user
        
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True,'allow_blank': False}
            }