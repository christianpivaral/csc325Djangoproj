from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page of my Django app.</h1>")

def about(request): 
    return HttpResponse("<h1>About Page</h1><p>This is the about page of my Django app.</p>")

@api_view(['GET'])
def api_status(request):
    return Response({
        'status': 'ok',
        'message': 'CSC325 Django REST API is running.',
        'course': 'CSC 325',
    })
