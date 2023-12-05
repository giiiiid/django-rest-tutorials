from django.urls import path
from .views import Register, Login

urlpatterns = [
    path('add/', Register.as_view(), name='add'),
    path('login/', Login.as_view(), name='login')
]