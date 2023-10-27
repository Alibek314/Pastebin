from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = '__all__'

    def create(self, validated_data):
        new_post = Text()
        new_post.content = validated_data['content']
        new_post.create_url()
        new_post.save()
        return new_post
