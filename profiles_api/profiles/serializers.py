from rest_framework import serializers

class HelloSerializars(serializers.Serializer):
    
    name = serializers.CharField(max_length=10)
    