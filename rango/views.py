from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rangosays hey there partner!")