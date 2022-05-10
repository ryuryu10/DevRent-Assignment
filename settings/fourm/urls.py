from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:article_id>/', views.detail, name='details'),
    path('create/', views.create, name = 'create')
]