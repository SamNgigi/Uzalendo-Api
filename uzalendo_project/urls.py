"""uzalendo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# from .views import home. We make PostListView our home page.
from .views import SearchView
from post_app.views import PostListView
from hashtag_app.views import HashTagView
from post_app.api.views import SearchPostApiView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^hashtag/(?P<hashtag>.*)/$',
        HashTagView.as_view(), name='hashtag'),
    url(r'^posts/', include('post_app.urls', namespace='posts')),
    url(r'^', include('accounts_app.urls', namespace='accounts')),
    url(r'^api/search$', SearchPostApiView.as_view(), name='search_api'),
    url(r'^api/accounts/',
        include('accounts_app.api.urls', namespace='accounts_api')),
    url(r'^api/posts/', include('post_app.api.urls', namespace='posts_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
