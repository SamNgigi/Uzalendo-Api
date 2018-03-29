# from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post
# Create your views here.


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    queryset = Post.objects.all()

    def get_objects(self):
        return Post.objects.get(id=1)


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    queryset = Post.objects.all()
