from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.Serializer):
    url = serializers.URLField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    content = serializers.CharField()

    def create(self, validated_data):
        new_post = Text.create()
        new_post.content = validated_data['content']
        new_post.save()
        return new_post
