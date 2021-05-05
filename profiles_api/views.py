from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions


class HelloApiView(APIView):
    #a test api view

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        #returns a list of APIView Features
        an_apiview = [
            'Uses HTTP method as function (get,post,patch,put,delete)',
            'Is similar to a traditional django views',
            'gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        # create a hello message with our name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST
                )

    def put (self, request, pk=None):
        #handle updating an object
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        #handle partial update of an object
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        # Delete an object in the database
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    # test api viewsets
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # return hello message
        a_viewset = [
            'Uses action (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with more code'
        ]

        return Response({'message':'Hello', 'a_Viewset':a_viewset})

    def create(self, request):
        # create a new hello message
        serializer = self.serializer_class(data=request.data)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST
                )

    def retrieve (self, request, pk=None):
        #handle getting an object by it's id
        return Response({'http_method':'GET'})

    def update (self, request, pk=None):
        #handle updating an object
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        #handle partial update of an object
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        # handling removing an object in the database
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    #handle creating and updating profiles
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
