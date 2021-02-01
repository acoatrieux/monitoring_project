from django.shortcuts import render

# Create your views here.

# View
def hello(request):
    return HttpResponse("Hello World!")