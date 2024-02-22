from django.urls import path
from . import views

app_name = 'StaticSite'

urlpatterns = [
    path('', views.index, name='index'),
]