from django.utils.timesince import timesince
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
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]

    def get_date_display(self, object):
        return object.timestamp.strftime("%b %d  %Y | %I:%M %p")

    def get_timesince(self, object):
        return timesince(object.timestamp) + " ago"