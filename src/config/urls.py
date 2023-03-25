"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', 'account')),
    path('', include('home.urls', 'home')),
]
