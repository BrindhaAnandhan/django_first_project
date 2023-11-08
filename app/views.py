from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse("Hi Jampandu, How are You")

def jigelrani(request):
    return HttpResponse("<h1><marqee>Hi I'm jigelrani<marqee></h1> ")
