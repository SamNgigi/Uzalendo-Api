from django.conf import settings

from django.db import models

# Create your models here.


class UserProfileManager(models.Manager):
    """
    Function that curates the user queryset to exclude the
    user profile instance when following.

    i.e remove user in query so that they cannot follow themselves.
    """

    def all(self):
        all_profiles = self.get_queryset().all()
        print(dir(self))
        try:
            if self.instance:
                all_profiles = all_profiles.exclude(user=self.instance)
        except self.DoesNotExit:
            pass
        return all_profiles


# Setting up following
class UserProfile(models.Model):
    """
    user.profile is the instance of a user profile

    user.profile.following --> users i follow
    user.followed_by --> users that follow me, giving us the
    reverse relationship. No need for profile here because we
    are currently on our own profile.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile')
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    """
    objects = UserProfileManager() is the same as UserProfile.objects.all()

    We can change it to;
    zed = UserProfileManager() where by in this case we would
    say UserProfile.zed.all()
    """
    objects = UserProfileManager()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)
