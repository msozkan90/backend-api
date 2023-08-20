"""
Serializers for the user API View.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    This serializer is used to convert User model instances to JSON format and vice versa.
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and save a new User instance.

        This method takes validated data, which should include 'username' and 'password' fields,
        and creates a new User instance with the hashed password before saving it to the database.

        Args:
            validated_data (dict): Validated data containing user information.

        Returns:
            User: The newly created User instance.
        """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user
