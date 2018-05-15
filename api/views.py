from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from . import serializers
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