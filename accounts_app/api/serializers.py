from django.contrib.auth import get_user_model

from django.urls import reverse_lazy

from rest_framework import serializers

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    """
    Serializer class resposible for serializing the user object data.

    We export this to post_app so that we can associate it with a post.
    """
    follower_count = serializers.SerializerMethodField()
    # To profile
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url'
        ]

    # Method that comes with the SerializerMethodField
    def get_follower_count(self, object):
        # print(object.username)
        return 0

    # function that return the url to a user's posts
    def get_url(self, object):
        return reverse_lazy(
            "accounts:user_details", kwargs={"username": object.username}
        )
