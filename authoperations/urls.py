from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'authoperations'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]