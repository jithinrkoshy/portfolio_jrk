from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"pf_home/index.html")


def home_page(request):
    return render(request,"pf_home/home_page.html")
