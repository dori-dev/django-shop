"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', 'account')),
    path('bucket/', include('bucket.urls', 'bucket')),
    path('cart/', include('cart.urls', 'cart')),
    path('order/', include('order.urls', 'order')),
    path('pay/', include('payment.urls', 'payment')),
    path('', include('home.urls', 'home')),
    path('', include('product.urls', 'product')),
]
