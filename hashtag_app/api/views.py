from django.db.models import Q
from rest_framework import generics
# from rest_framework import permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response

from post_app.models import Post

from post_app.api.pagination import StandardResultPagination
from post_app.api.serializers import PostModelSerializer

from hashtag_app.models import HashTag


class HashtagPostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    pagination_class = StandardResultPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(HashtagPostAPIView, self).get_serializer_context(
            *args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        hashtag = self.kwargs.get("hashtag")
        hashtag_objects = None
        try:
            hashtag_objects = HashTag.objects.get_or_create(tag=hashtag)[0]
        except Exception:
            pass
        if hashtag_objects:
            queryset = hashtag_objects.get_posts()
            query = self.request.GET.get("q", None)
            if query is not None:
                queryset = queryset.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                )
            return queryset
        return None
