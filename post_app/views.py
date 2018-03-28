from django.shortcuts import render
from .models import Post
# Create your views here.


def post_detail_view(request, id=1):
    obj = Post.objects.get(id=id)
    content = {
        "object": obj,
    }
    return render(request, 'posts/post_detail.html', content)


def post_list_view(request):
    queryset = Post.objects.all()

    content = {
        "object_list": queryset,
    }
    return render(request, 'posts/post_list.html', content)
