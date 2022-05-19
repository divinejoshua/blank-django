from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import NameList, Visitors

# The background task 
from .tasks import addcheck

# Create your views here.
# This view displays ever list and every status 


class FormView(APIView):
    
    def post(self,request):
        data ={}

        serializer = serializers.NameListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            # Background task 
            addcheck.delay()

            data['success'] = True
        else:
            data['error'] = True
      
       
        return Response(data=data)




class VisitorsView(APIView):
    
    def post(self,request):
        data ={}

        instance = Visitors()
        instance.name = "done"
        instance.save()
      
       
        return Response(data=data)

# if NameList.objects.filter(email=request.POST['email']).exists() == False:

