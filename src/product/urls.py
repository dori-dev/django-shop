from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('<slug:slug>/', views.ProductDetail.as_view(), name='detail'),
    path(
        'category/<slug:slug>/',
        views.CategoryView.as_view(),
        name='category',
    ),
]
