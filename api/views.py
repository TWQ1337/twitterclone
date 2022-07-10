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
    context: dict = {'response': 0}
    # If user id is user id reject
    print(request.user)
    print(request.body)
    return Response(context)

# class SubscribeProfileApiView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class =
#     lookup_field = 'pk'


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
