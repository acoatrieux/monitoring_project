from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

# View
def defaultView(request):
    return render(
        request,
        "website/hello.html",
        {
            "message": "Hello Websites!",
        },
    )