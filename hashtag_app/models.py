from django.db import models

from post_app.models import Post

# Create your models here.


class HashTag(models.Model):
    tag = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_posts(self):
        return Post.objects.filter(content__icontains="#" + self.tag)
