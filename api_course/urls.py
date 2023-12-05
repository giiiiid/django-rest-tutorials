from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('hotels/', include('hotels.urls')),
    path('auth/api/', include('authentication.urls')),
]
