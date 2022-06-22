from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class HelloApiView(APIView):

    serializers_class = serializers.HelloSerializars
    
    def get(self, request, format=None):
        
        an_apiview = [
            'http methods as functions',
            'similar traditional django view',
            'we have more control about app logic',
            'manual URLs map'
        ]

        return Response({'message':'hello', 'an_apivew': an_apiview})
    
    def post(self, request):

        serializers = self.serializers_class( data = request.data )

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({ 'message': message})
        else:
            return Response(
                serializers.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):

        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk=None):

        return Response({
            'method': 'PATCH'
        })

