from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# View
def hello(request):
    return HttpResponse("Hello World!")

# View
def test(request):
    return HttpResponse("Hello World!")