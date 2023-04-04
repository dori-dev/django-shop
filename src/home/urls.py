from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'home'
urlpatterns = [
    path('', cache_page(60 * 15)(views.Index.as_view()), name='index'),
]
