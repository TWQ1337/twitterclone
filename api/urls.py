from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    # path('tweets/', views.check_update, name='list'),
    # path('token/', views.get_csrf_token, name='token'),
    path('tweets/', views.ListCreateTweetsApiView.as_view(), name='list'),
    path('profiles/', views.SearchListProfileAPIView.as_view(), name='search-profiles')
]