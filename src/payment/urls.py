from django.urls import path
from payment import views

app_name = 'payment'
urlpatterns = [
    path('<int:pk>/', views.PayOrderView.as_view(), name='pay'),
    path('verify/', views.VerifyPaymentView.as_view(), name='verify'),
]
