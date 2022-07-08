import rest_framework.pagination
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
# from django.middleware.csrf import get_token
from rest_framework import generics


from tweets.models import TweetModel
from tweets.serializers import TweetSerializer

from profileapp.serializers import UserModelSerializer
from profileapp.models import ProfileModel


class ListCreateTweetsApiView(generics.ListCreateAPIView):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        user_ids = [user.id,]
        user_ids = user_ids + list(user.profile.follows.all().values_list('id', flat=True))
        return queryset.filter(created_by__id__in=user_ids)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SearchListProfileAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q is None:
            return queryset.none()
        return queryset.filter(username__icontains=q)


# def check_update(request):
#     print(request.user.username)
#     print(request.META)
#     print(request.read())
#     return HttpResponse('bruh')
#
#
# def get_csrf_token(request):
#     token = get_token(request)
#     return JsonResponse({'token': token})