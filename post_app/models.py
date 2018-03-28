from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    # Supposedly a much more robust way if defuning the user model.
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(max_length=155)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        What this function does is define a string representation of
        Post instance on the database./admin

        So instead of displaying 'Post object', what it we would see
        instead is the actual content that was recieved as input.
        """
        return str(self.content)
