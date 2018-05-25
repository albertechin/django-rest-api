from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from . import serializers
from . import models
# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    seializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Put request updates an object."""

        return Response({'message':'put'})

    def patch(self, request, pk=None):
        """Patch request updates only fields specified in the request."""

        return Response({'message':'patch'})

    def delete(self, request, pk=None):
        """Delete request deletes an object"""

        return Response({'message':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """TEst API ViewSet"""

    def list(self, request):
        """Return API Viewset"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code.'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by ID."""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({'http_method':'PATCH'})

    def delete(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method':'DELETE'})

class UserProfilesViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

