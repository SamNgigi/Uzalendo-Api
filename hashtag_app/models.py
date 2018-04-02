from django.db import models

from django.urls import reverse_lazy

from post_app.models import Post

from .signals import parsed_hashtags
# Create your models here.


class HashTag(models.Model):
    tag = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_posts(self):
        return Post.objects.filter(content__icontains="#" + self.tag)

    def get_absolute_url(self):
        return reverse_lazy("hashtags", kwargs={"hashtag": self.tag})


# Function that automatically added our tags to the Hashtag model
def parsed_hashtags_reciever(sender, hashtag_list, *args, **kwargs):
    if len(hashtag_list) > 0:
        for tag_var in hashtag_list:
            new_tag, create = HashTag.objects.get_or_create(tag=tag_var)
    print(args)
    print(kwargs)


parsed_hashtags.connect(parsed_hashtags_reciever)
