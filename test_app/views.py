from django.shortcuts import HttpResponse 

def home(request):
    str = '<h1>welcome</h1>'
    return HttpResponse(str)