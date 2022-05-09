from django.shortcuts import render
from .models import fourms

def index(requset):
    article = fourms.objects.all()
    return render(requset, 'pages/article_index.html', {'article_list': article})

def detail(request, article_id):
    article = fourms.objects.get(id = article_id)
    return render(request, 'pages/article_detail.html', {'article_detail': article})