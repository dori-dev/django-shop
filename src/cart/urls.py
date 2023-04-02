from django.urls import path
from cart import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartDetailView.as_view(), name='detail'),
    path('add/<slug:slug>/', views.CartAddView.as_view(), name='add'),
]
