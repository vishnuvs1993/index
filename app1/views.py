from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("hello world")
def hi(request):
    return render(request,'index.html')    
def sample(request):
    return render(request,'index1.html')    