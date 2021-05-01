from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    #a test api view

    def get(self,request,format=None):
        #returns a list of APIView Features
        an_apiview = [
            'Uses HTTP method as function (get,post,patch,put,delete)',
            'Is similar to a traditional django views',
            'gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})