from django.db.models import Q
from rest_framework import generics

from post_app.models import Post
from .serializers import PostModelSerializer


class PostListApiView(generics.ListAPIView):
    serializer_class = PostModelSerializer

    def get_queryset(self, *args, **kwargs):
        searched_posts = Post.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            searched_posts = searched_posts.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return searched_posts
