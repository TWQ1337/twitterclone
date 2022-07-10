from rest_framework import serializers

from django.contrib.auth.models import User

from tweets.serializers import TweetSerializer

class UserModelSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'followers',
        ]

    def get_followers(self, obj):
        user = obj
        count = user.profile.followed_by.all().count()
        return count


class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField(read_only=True)
    tweets = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'followers',
            'tweets'
        ]

    def get_followers(self, obj):
        user = obj
        count = user.profile.followed_by.all().count()
        return count

    def get_tweets(self, obj):
        user = obj
        tweets_qs = obj.tweets.all()[:5]
        return TweetSerializer(tweets_qs, many=True, context=self.context).data



class FollowDataSerializer(serializers.ModelSerializer):
    profile_id = serializers.SerializerMethodField(read_only=True)
    subscriber_id = serializers.CharField(source='pk', read_only=True)
    subscribed = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'profile_id',
            'subscriber_id',
            'subscribed'
        ]

    def get_profile_id():
        return 0