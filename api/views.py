import rest_framework.pagination
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import generics


from tweets.models import TweetModel
from tweets.serializers import TweetSerializer


class ListCreateTweetsApiView(generics.ListCreateAPIView):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


def check_update(request):
    print(request.user.username)
    print(request.META)
    print(request.read())
    return HttpResponse('bruh')


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'token': token})