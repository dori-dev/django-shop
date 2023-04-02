from django.urls import path
from order import views

app_name = 'order'
urlpatterns = [
    path('create/', views.CreateOrderView.as_view(), name='create'),
]
