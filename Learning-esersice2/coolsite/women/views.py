from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения women")
def categories(reguest,cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")