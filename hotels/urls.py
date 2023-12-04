from django.urls import path
from . import views

#Urls for templates 
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('<str:id>', views.hotel_detail, name='detail')
]