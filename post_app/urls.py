from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import PostDetailView, PostListView

urlpatterns = [
    # .as_view() makes our class based views into functions
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^$', PostListView.as_view(), name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
