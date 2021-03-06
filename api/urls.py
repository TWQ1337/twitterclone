from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('tweets/', views.ListCreateTweetsApiView.as_view(), name='list'),
    path('profiles/', views.SearchListProfileAPIView.as_view(), name='search-profiles'),
    path('profiledata/<int:pk>', views.ProfileAPIView.as_view(), name='profile-data'),
    path('subscribe/', views.subscribe_api, name='subscribe-endpoint'),
    path('alltweets/', views.MainTweetListApiView.as_view(), name='all-tweets')
]