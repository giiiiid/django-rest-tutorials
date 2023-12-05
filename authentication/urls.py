from django.urls import path
from .views import Register

urlpatterns = [
    path('add/', Register.as_view(), name='add')
]