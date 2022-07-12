from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from tweets.models import TweetModel
from tweets.serializers import TweetSerializer

from profileapp.serializers import UserModelSerializer, UserProfileSerializer
from profileapp.models import ProfileModel


class ListCreateTweetsApiView(generics.ListCreateAPIView):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        user_ids = [user.id, ]
        user_ids = user_ids + list(user.profile.follows.all().values_list('id', flat=True))
        return queryset.filter(created_by__id__in=user_ids)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MainTweetListApiView(generics.ListAPIView):
    serializer_class = TweetSerializer
    queryset = TweetModel.objects.all()


class SearchListProfileAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q == '':
            return queryset.none()
        return queryset.filter(username__icontains=q)


class ProfileAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'


@api_view(['POST'])
def subscribe_api(request, *args, **kwargs) -> Response:
    """
    Reverses subscription status
    When gets a request
    """
    # Setting up variables
    context: dict = {}
    data: dict = request.data
    sub_status: bool = bool()
    # Check if request data contains user id and profile id
    if not 'profile_id' in data and not 'user_id' in data:
        return Response({
            'Error': 'Bad Request'
        })
    # If user id is user id reject

    if data['profile_id'] == data['user_id']:
        return Response({
            'Error': 'Cannot\'t follow yourself'
        })

    try:
        user = User.objects.get(id=data['user_id'])
        profile = ProfileModel.objects.get(user__id=data['profile_id'])
    except:
        return Response({
            'Error': 'Wrong ids'
        })

    if user.profile.follows.all().filter(user__id=data['profile_id']).exists():
        user.profile.follows.remove(profile)
        sub_status = False
    else:
        user.profile.follows.add(profile)
        sub_status = True
    context.update({
        'sub_status': sub_status
    })
    return Response(context)

