from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response

from post_app.models import Post
from .serializers import PostModelSerializer

from .pagination import StandardResultPagination


class LikeToggleApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        post_queryset = Post.objects.filter(pk=pk)
        message = 'Not allowed'
        if request.user.is_authenticated():
            is_liked = Post.objects.like_toggle(
                request.user, post_queryset.first())
            return Response({"liked": is_liked})
        return Response({"message": message}, status=400)


class RePostApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        post_queryset = Post.objects.filter(pk=pk)
        message = "Not allowed!"
        if post_queryset.exists() and post_queryset.count() == 1:
            if request.user.is_authenticated():
                post_copy = Post.objects.re_post(
                    request.user, post_queryset.first()
                )
                if post_copy is not None:
                    data = PostModelSerializer(post_copy).data
                    return Response(data)
                message = "Cannot repost the same post in 1 day"

        return Response({"message": message}, status=400)


class PostListApiView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(PostListApiView, self).get_serializer_context(
            *args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        # We want to display a particular user's post only
        requested_user = self.kwargs.get("username")
        if requested_user:
            # Represents user's post
            queryset = Post.objects.filter(user__username=requested_user)
        else:
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
