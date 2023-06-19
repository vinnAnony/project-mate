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

class UserDetailsSerializer(serializers.ModelSerializer):
    """Serializer to display the User Details to be used on account registration"""

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate_password(self, value):
        """Validating password length"""

        password_length = settings.USER_PASSWORD_LENGTH

        if len(value) < password_length:
            raise serializers.ValidationError(
                f"Password length must be at least {password_length} characters"
            )

        return value

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registration of user
    It ensures that a first user does not exist without an account.
    """

    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    user = UserDetailsSerializer()

    def create(self, validated_data):
        user = dict(validated_data['user'])
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
    
    def validate(self, data):
        """
        Validating if password field data equals confirm_password field data.
        """

        user = dict(data["user"])
        password = user["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    class Meta:
        model = User
        fields = ['id', 'user', 'confirm_password']        