# We want to try implement notification.
import re
from django.db.models.signals import post_save

from django.conf import settings
from django.urls import reverse
from django.db import models
# We wanted to use this so that a user cannot retweet on the same day.
from django.utils import timezone

# Importing custom hashtag signal
from hashtag_app.signals import parsed_hashtags

# Importing validators
from .validators import validate_content

# Default profile image


# Create your models here.
# Class responsible for repost. Make a copy of the parent post.
class PostManager(models.Manager):
    def re_post(self, user, parent_object):
        # Makes it that we are always posting a copy of the original.
        # Not a copy of a copy
        if parent_object.parent:
            original_parent = parent_object.parent
        else:
            original_parent = parent_object

        # Make sure we don't keep reposting a reposted post.
        queryset = self.get_queryset().filter(
            user=user,
            parent=original_parent
        ).filter(
            timestamp__year=timezone.now().year,
            timestamp__month=timezone.now().month,
            timestamp__day=timezone.now().day,
        )
        if queryset.exists():
            return None

        object = self.model(
            parent=original_parent,
            user=user,
            content=parent_object.content
        )
        object.save()
        return object


class Post(models.Model):
    # Supposedly a much more robust way if defining the user model.
    parent = models.ForeignKey("self", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=155, validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        """
        What this function does is define a string representation of
        Post instance on the database./admin

        So instead of displaying 'Post object', what it we would see
        instead is the actual content that was recieved as input.
        """
        return str(self.content)

    """
    - Validation inside the model. Appears on whole model and is not
    specific to a field

    def clean(self, *args, **kwargs):
        content = self.content
        if content == 'abc':
            raise ValidationError(
                "
                Hi! Sorry, cannot be ABC.
                But on the bright side your validation is working
                ")
        return super(Post, self).clean(*args, **kwargs)
    """
    # We define our absolute url here

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})


def post_save_reciever(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        # notify user of @ mention. Returns a list of all instances
        user_regex = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regex, instance.content)
        print(usernames)

        """
        notify user of # mentions. Returns a list of all instances.
        We use this together with the our hashtag signal to
        register all new tags hashtag model
        """
        hashtag_regex = r'#(?P<hashtag>[\w.@+-]+)'
        hashtags = re.findall(hashtag_regex, instance.content)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)
        print(hashtags)


post_save.connect(post_save_reciever, sender=Post)
