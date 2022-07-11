from rest_framework import serializers

from .models import TweetModel


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TweetModel
        fields = [
            'user',
            'user_id',
            'body',
            'timestamp'
        ]

    def get_user(self, obj):
        return obj.created_by.username

    def get_user_id(self, obj):
        return obj.created_by.id