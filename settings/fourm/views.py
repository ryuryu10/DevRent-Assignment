from django.shortcuts import render, get_list_or_404
from .models import fourms

def index(requset):
    article = fourms.objects.all()
    return render(requset, 'pages/article_index.html', {'article_list': article})

def detail(request, article_id):
    article = get_list_or_404(fourms, pk=article_id)
    return render(request, 'pages/article_detail.html', {'article_detail': article})