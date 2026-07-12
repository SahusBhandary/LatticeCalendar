from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Get Custom User Model
User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def validate(self, attrs):
        pwd = attrs["password"]
        pwd_confirm = attrs["password_confirm"]

        # Check if passwords match, else raise an error for the confirm password field
        if pwd != pwd_confirm:
            raise serializers.ValidationError({
                "password_confirm" : "Passwords did not match!"
            })

        return attrs

    def create(self, validated_data):
        # Extract Key Fields
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]

        # Remove Unnecessary Fields
        del validated_data["username"]
        del validated_data["email"]
        del validated_data["password"]
        del validated_data["password_confirm"]

        return User.objects.create_user(email=email, username=username, password=password, **validated_data)