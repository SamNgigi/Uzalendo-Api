from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # .as_view() makes our class based views into functions
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^create/$', PostCreateView.as_view(),
        name='create_post'),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(),
        name='post_update'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(),
        name='post_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
