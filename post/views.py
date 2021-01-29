from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print("hello world 4")
    return HttpResponse('HELLO FROM POST')
