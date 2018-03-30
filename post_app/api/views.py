from rest_framework import generics

from post_app.models import Post
from .serializers import PostModelSerializer


class PostListApiView(generics.ListAPIView):
    serializer_class = PostModelSerializer

    def get_queryset(self):
        return Post.objects.all()
