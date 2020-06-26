from django.shortcuts import render
from django.http import HttpResponse
import markdown
# Create your views here.

def index(request):
    f = open('README.md', 'r')
    return HttpResponse(markdown.markdown(f.read()))
