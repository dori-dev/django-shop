from django.urls import path
from payment import views

app_name = 'payment'
urlpatterns = [
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]
