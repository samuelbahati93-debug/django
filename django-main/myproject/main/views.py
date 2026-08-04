from django.shortcuts import render
from django.http import HttpResponse
from .models import todolist,item
from .forms import createnewlist


def index(response,id):
    ls = todolist.objects.get(id=id)
    return render(response,"main/list.html",{"ls":ls})
# Create your views here.
def home(response):
    return render(response,"main/home.html",{})

def create(response):
    form=createnewlist()
    return render(response,"main/create.html",{"form":form})
