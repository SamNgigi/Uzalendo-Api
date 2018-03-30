from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    """
    Serializer class resposible for serializing the user object data.

    We export this to post_app so that we can associate it with a post.
    """
    follower_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count'
        ]

    # Method that comes with the SerializerMethodField
    def get_follower_count(self, object):
        print(object.username)
        return 0
