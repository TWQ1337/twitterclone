from rest_framework import serializers

from django.contrib.auth.models import User



class UserModelSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'followers'
        ]

    def get_followers(self, obj):
        user = obj
        count = user.profile.followed_by.all().count()
        return count



