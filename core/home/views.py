from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "home/index.html")

def success_page(request):
    return HttpResponse("<h3>this is succeess page</h3>")