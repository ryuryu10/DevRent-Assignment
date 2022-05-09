from django.contrib import admin
from django.urls import path, include

from fourm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fourm/', views.index),
]
