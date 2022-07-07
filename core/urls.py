from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.TemplateView.as_view(template_name='core/fp.html'), name='fp'),
    path('', include('authoperations.urls'))
]

