from django.shortcuts import render
from django.http import HttpResponse
from .models import todolist,item


def index(request,name):
    ls = todolist.objects.get(name=name)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><p>%s</p>"%(ls.name, items.text))
# Create your views here.
