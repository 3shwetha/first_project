from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def function1(request):
    return HttpResponse('<h1><marquee>This is our first function based view</marquee></h1>')

def function2(request):
    return HttpResponse('This is our second function based view')