from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='Main page'),
    path('about/', views.about, name='About myself'),
]