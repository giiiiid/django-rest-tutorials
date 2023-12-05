from django.urls import path
from . import views

#Urls for templates 
urlpatterns = [
    path('get', views.get, name='get'),
    # path('new', views.post, name='new'),
    # path('<str:id>', views.hotel_detail, name='detail')
    path('add', views.HotelCreation.as_view(), name='add')
]