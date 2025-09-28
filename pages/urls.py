from django.urls import path
from . import views # import views.py in the same directory

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]