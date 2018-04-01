from django.conf import settings

from django.db import models

# Create your models here.

# Setting up following


class UserProfile(models.Model):
    """
    user.profile.following --> users i follow
    user.profile.followed_by --> users that follow me, giving us the
    reverse relationship
    """
    # user.profile
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile')
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    def __str__(self):
        return str(self.following.all().count())
