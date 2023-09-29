from rest_framework import serializers

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #exclude = ('password', 'groups', 'user_permissions')
        exclude = ('password', 'groups', 'user_permissions', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login', 'is_superuser')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
