from django.shortcuts import render
from django.http import HttpResponse
from .models import todolist,item


def index(response,id):
    ls = todolist.objects.get(id=id)
    return render(response,"main/list.html",{"ls":ls})
# Create your views here.
def home(response):
    return render(response,"main/home.html",{})
