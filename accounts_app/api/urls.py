from django.conf.urls import url

from post_app.api.views import PostListApiView

urlpatterns = [
    url(r'(?P<username>[\w.@+-]+)/posts/$',
        PostListApiView.as_view(), name='list'),  # api/accounts/posts
]
