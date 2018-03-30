from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import post_detail_view, post_list_view, post_create_view

urlpatterns = [
    # .as_view() makes our class based views into functions
    url(r'^(?P<pk>\d+)/$', post_detail_view, name='post_detail'),
    url(r'^$', post_list_view, name='post_list'),
    url(r'^create/$', post_create_view,
        name='create_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
