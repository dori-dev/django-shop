from django.urls import path
from bucket import views

app_name = 'bucket'
urlpatterns = [
    path('list/', views.BucketList.as_view(), name='bucket'),
]
