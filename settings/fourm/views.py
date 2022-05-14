from django.shortcuts import render, get_object_or_404, redirect
from .models import fourms
from .forms import WRITE_Form

def index(requset):
    article = fourms.objects.all()
    return render(requset, 'pages/article_index.html', {'article_list': article})

def detail(request, article_id):
    article = get_object_or_404(fourms, id=article_id)
    return render(request, 'pages/article_detail.html', {'article_detail': article})

def create(requset):
    if requset.method == "POST":
        form = WRITE_Form(requset.POST)
        new_page = form.save()
        return redirect('details', article_id=new_page.id)
    else:
        form = WRITE_Form()
        return render(requset, 'pages/article_create.html', {'form':form})

def update(request, article_id):
    article = fourms.objects.get(id=article_id)
    if request.method == "POST":
        article.title = request.POST['title']
        article.body = request.POST['content']
        article.save()
        return redirect(f'/detail/{article_id}',{'article_update':article})
    else:
        article=fourms()
        return render(request, 'article_update.html', {'article_update':article})

def delete(request, article_id):
    article = fourms.objects.get(id = article_id)
    article.delete()