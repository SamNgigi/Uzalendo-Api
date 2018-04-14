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
from hashtag_app.api.views import HashtagPostAPIView

from accounts_app.views import UserRegisterView

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^hashtag/(?P<hashtag>.*)/$',
        HashTagView.as_view(), name='hashtag'),
    url(r'^api/hashtag/(?P<hashtag>.*)/$',
        HashtagPostAPIView.as_view(), name='hashtag_api'),
    url(r'^posts/', include('post_app.urls', namespace='posts')),
    # Default django authentication urls has to be above custom accounts url
    url(r'^api/search$', SearchPostApiView.as_view(), name='search_api'),
    url(r'^api/accounts/',
        include('accounts_app.api.urls', namespace='accounts_api')),
    url(r'^api/posts/', include('post_app.api.urls', namespace='posts_api')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^', include('accounts_app.urls', namespace='accounts')),
    # Api Auth URLs
    url(r'^api/auth/', include('knox.urls')),
    # React url
    url(r'.*', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
