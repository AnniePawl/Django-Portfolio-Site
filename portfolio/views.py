from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Portfolio Home Page")


def contact(request):
    return HttpResponse("Contact Me!")


def greet_by_name(request, name):
    # TODO: Return an HttpResponse that contains a string that includes the given name
    return HttpResponse(f"Hello there, {name}!!!")
