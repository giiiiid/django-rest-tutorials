from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', include('hotels.urls')),
    path('class/', include('class.urls'))
]
