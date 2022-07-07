from rest_framework import serializers

from .models import TweetModel


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TweetModel
        fields = [
            'user',
            'body',
            'timestamp'
        ]

    def get_user(self, obj):
        return obj.created_by.username