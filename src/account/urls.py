from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
