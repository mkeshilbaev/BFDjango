from django.urls import path, include

from demo.core import views

urlpatterns = [
    path('home', views.index)
]