from dataclasses import fields
from rest_framework import serializers

from profiles import models
class HelloSerializars(serializers.Serializer):
    
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer User Profile Object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style': {'input_type': 'password'}
          }
         }

    def create(self, validated_data):

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):

        if 'password' in validated_data:
            pasword = validated_data.pop('password')
            instance.set_password(pasword)
            
        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer Profile Feed item Object"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }
