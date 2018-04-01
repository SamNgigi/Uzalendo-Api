from django.shortcuts import render

from .models import HashTag

from django.views import View


# Create your views here.
class HashTagView(View):
    def get(self, request, hashtag, *args, **kwargs):
        object, created = HashTag.objects.get_or_create(tag=hashtag)
        content = {
            "object": object
        }
        return render(request, 'hashtags/hashtag.html', content)
