from django.shortcuts import render
from django.http import HttpResponse

def show_user(request):
    return HttpResponse("This is user page")