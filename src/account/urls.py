from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
]
