from django.shortcuts import render
from django.http import HttpResponse
from nodeitem.models import Mobile,Laptop,User,UserSession
from nodeitem.serializers import MobileSerializer,LaptopSerializer,UserSerializer

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status




# Create your views here.

@api_view(["GET","POST"])
def login(request):
    if request.method=="GET":
        article=User.objects.all()
        print(article)
        serializer=UserSerializer(article,many=True)
        return Response(serializer.data)
        
    elif request.method== "POST":
        try:
            data_user=User.objects.get(username=request.data['username'],password=request.data['password'])
            data_pass=User.objects.get()
           
            if data_user and data_pass :
                user=UserSession(username=request.data['username'],password=request.data['password'])
                user.save()
                return Response('login',status=status.HTTP_201_CREATED)
           
        except User.DoesNotExist:
            return Response('no such user',status=404)

@api_view(["GET"])  
def logout(request):
    if request.method=="GET":
        user=UserSession.objects.all()
        user.delete()
        return Response("logout")


@api_view(["GET","POST"])
def mobile_item(request):
    
   
    if request.method=="GET":
        item= Mobile.objects.all()
        sitem=MobileSerializer(item,many=True)
        return Response(sitem.data)

    elif request.method== "POST":
            sitem=MobileSerializer(data=request.data)
            sitem.is_valid(raise_exception=True)
            sitem.save()
            return Response(sitem.data)

@api_view(["GET","PUT","DELETE"])
def mobile_detail(request,pk):
    try:
        mobile=Mobile.objects.get(name=pk)
    except Mobile.DoesNotExist:
        return HttpResponse('no such mobiles',status=404)
    if request.method =="GET":
        serializer=MobileSerializer(mobile)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method =="PUT":
        serializer=MobileSerializer(mobile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method =="DELETE":
        mobile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","POST"])
def laptop_item(request):
    
   
    if request.method=="GET":
        item= Laptop.objects.all()
        sitem=LaptopSerializer(item,many=True)
        return Response(sitem.data)

    elif request.method== "POST":
            sitem=LaptopSerializer(data=request.data)
            sitem.is_valid(raise_exception=True)
            sitem.save()
            return Response(sitem.data)

@api_view(["GET","PUT","DELETE"])
def laptop_detail(request,pk):
    try:
        mobile=Laptop.objects.get(name=pk)
    except Mobile.DoesNotExist:
        return HttpResponse('no such mobiles',status=404)
    if request.method =="GET":
        serializer=LaptopSerializer(mobile)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method =="PUT":
        serializer=LaptopSerializer(mobile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method =="DELETE":
        mobile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)