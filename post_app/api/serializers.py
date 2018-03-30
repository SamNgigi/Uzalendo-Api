from rest_framework import serializers

from post_app.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """
    Class that will be resposible for serializing post data.
    """
    class Meta:
        model = Post
        fields = [
            'user',
            'content'
        ]
