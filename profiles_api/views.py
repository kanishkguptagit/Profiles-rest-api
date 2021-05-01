from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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