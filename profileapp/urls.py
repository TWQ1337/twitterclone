from django.urls import path
from . import views
app_name = 'profileapp'

urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile')
]