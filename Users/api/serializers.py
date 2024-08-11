from rest_framework import serializers
from Users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'address', 'first_name', 'last_name']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password1'],
            address=validated_data['address'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class RegisterLibrianSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'personnel_number']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password1'],
            personnel_number=validated_data['personnel_number'],
            role='L'
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
