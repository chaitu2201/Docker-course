from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'basic_site.html')
    #return HttpResponse("Hey, How are you? I am a Django app")
