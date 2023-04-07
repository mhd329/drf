# from django.shortcuts import render
# Create your views here.


from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(["GET"])
def HelloAPI(request):
    return Response("Hello world!")