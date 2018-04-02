from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic.base import RedirectView
from .views import (
    PostListApiView,
    PostCreateApiView,
    RePostApiView,
    # PostUpdateView,
    # PostDeleteView
)
"""
.as_view() makes our class based views into functions
Since we have made our PostListView be our home url and also the
one that implements the search functionality, We use the redirect
view to direct us back to home once done with search.
"""

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/'), name='post_list'),
    url(r'^$', PostListApiView.as_view(), name='post_list_api'),  # api/posts/
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^create/$', PostCreateApiView.as_view(),
        name='post_create_api'),
    url(r'^/(?P<pk>\d+)/repost/$', RePostApiView.as_view(),
        name='repost'),
    # url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(),
    #     name='post_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
