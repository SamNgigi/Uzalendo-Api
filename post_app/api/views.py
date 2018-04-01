from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from post_app.models import Post
from .serializers import PostModelSerializer

from .pagination import StandardResultPagination


class PostListApiView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self, *args, **kwargs):
        friends = self.request.user.profile.get_following()
        friends_post = Post.objects.filter(user__in=friends)
        my_post = Post.objects.filter(user=self.request.user)
        # distinct makes sure that there are no duplicates.
        queryset = (friends_post | my_post).distinct()
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return queryset


class PostCreateApiView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    # Allows us to only allow authenticated users to post.
    permission_classes = [permissions.IsAuthenticated]

    """
    This function below allows us to attach a user to a post created
    through serialization
    """

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
