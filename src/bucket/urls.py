from django.urls import path
from bucket import views

app_name = 'bucket'
urlpatterns = [
    path('list/', views.BucketList.as_view(), name='list'),
    path('delete/', views.DeleteBucket.as_view(), name='delete'),
    path('download/', views.DownloadBucket.as_view(), name='download'),
]
