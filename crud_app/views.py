from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializer import EmploySerialzer
from .models import Company
from rest_framework import status
from rest_framework.exceptions import NotFound
# Create your views here. 


class Employers(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request,id=None):
        if id:
            try:
                obj_company=Company.objects.get(id=id)
            except Company.DoesNotExist:
                raise NotFound({'error':'Employ not found'})
            serializer=EmploySerialzer(obj_company)
            return Response(serializer.data)
        else:
            obj_company = Company.objects.all()
            serializer = EmploySerialzer(obj_company , many=True)
            return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer=EmploySerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data = request.data
        print(data)
        obj=Company.objects.get(id = data['id'])
        serializer = EmploySerialzer(obj , data=data , partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self ,request):
        data = request.data
        print(data)
        obj=Company.objects.get(id = data['id'])
        serializer = EmploySerialzer(obj , data=data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request):
        data = request.data
        obj = Company.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'person deleted'})