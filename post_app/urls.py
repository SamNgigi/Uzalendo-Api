from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import post_detail_view, post_list_view

urlpatterns = [
    url(r'^1/$', post_detail_view, name='post_detail'),
    url(r'^$', post_list_view, name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
