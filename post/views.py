from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print("hello world 3")
    return HttpResponse('HELLO FROM POST')
