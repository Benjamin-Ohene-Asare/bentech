from django.urls import path
from . import views








urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('error', views.error, name='error'),
    path('myservice', views.myservice, name='myservice'),
    
    path('myservice', views.portfolio, name='portfolio'),
    
  
]