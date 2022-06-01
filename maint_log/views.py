from django.http import HttpResponse
from django.shortcuts import render

def index(requst):
    return HttpResponse("Hello there, it looks like it is working!")