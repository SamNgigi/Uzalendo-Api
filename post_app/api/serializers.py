from rest_framework import serializers

from accounts_app.api.serializers import UserDisplaySerializer
from post_app.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """
    Class that will be resposible for serializing post data.

    Simply post serializers is able to make user of the account's
    serializer for the User model through a foriegn key that ties our
    user in post to the AUTH_USER_MODEL.
    """
    user = UserDisplaySerializer(read_only=True)  # Write only

    class Meta:
        model = Post
        fields = [
            'user',
            'content'
        ]
