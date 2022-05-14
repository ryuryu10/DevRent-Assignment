from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:article_id>/', views.detail, name='details'),
    path('create/', views.create, name = 'create'),
    path('update/<int:article_id>/', views.update, name='update'),
    path('delete/<int:article_id>/', views.delete, name='delete')
]