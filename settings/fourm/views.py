from django.shortcuts import render
from .models import fourms

def index(requset):
    article = fourms.objects.all()
    return render(requset, 'pages/lists.html', {'article_list': article})