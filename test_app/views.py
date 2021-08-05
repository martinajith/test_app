from django.shortcuts import HttpResponse 

def home(request):
    str = '<h1>welcome1</h1>'
    return HttpResponse(str)