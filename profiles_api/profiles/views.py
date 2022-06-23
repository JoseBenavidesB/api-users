
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers, models, permissions



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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        a_viewset = [
            'use actions ( list, create, retrieve, update, partial_update',
            'automaticatly urls map usin ROUTERs',
            'more functionality less code'
        ]
    
        return Response({ 'message': 'hi', 'a_viewset': a_viewset})

class UserProfileViewSets( viewsets.ModelViewSet ):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = ( TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """To create tokens auth user"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedViewSet( viewsets.ModelViewSet ):
    """CRUD"""
    authentication_classes = ( TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer