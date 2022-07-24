from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('pokemon_data/', include('pokemon_data.urls')),
    path('pokemon_trainers/', include('users.urls')),
    
]
