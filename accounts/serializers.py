from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UserData, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "email", "username", "password"]

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long")
        if value[0].isdigit():
            raise serializers.ValidationError("Username cannot start with a number.")
        return value

    def validate_password(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Password must be at least 5 characters long.")

        if not any(char.isdigit() for char in value) or not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Password must contain both letters and numbers.")

        return value

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"
        

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data.pop('follower', None)
        print(validated_data)
        return Follow.objects.create(follower=request.user, **validated_data)
