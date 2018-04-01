from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    UserDetailView,
    UserFollowView,
)
"""
.as_view() makes our class based views into functions
Since we have made our PostListView be our home url and also the
one that implements the search functionality, We use the redirect
view to direct us back to home once done with search.
"""

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(),
        name='user_details'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(),
        name='user_follow'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
