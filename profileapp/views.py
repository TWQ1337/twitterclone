from django.shortcuts import render
from django.views import generic

from django.contrib.auth.models import User


class ProfileDetailView(generic.DetailView):
    model = User
    template_name = 'profileapp/profile.html'

