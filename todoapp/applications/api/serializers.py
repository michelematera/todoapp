from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from drf_extra_fields.fields import Base64ImageField
from todoapp.applications.todo import models as todo_models
from todoapp.applications.account import models as account_models


class TaskSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = todo_models.Task
        fields = ['id', 'name', 'description', 'deadline', 'image']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = account_models.User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = account_models.User
        fields = ['username', 'email', 'password', 'confirm_password']
