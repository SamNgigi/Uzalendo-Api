from django.shortcuts import (
    # render,
    # redirect,
    get_object_or_404
)
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .custom_mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import PostModelForm
from .models import Post
# Create your views here.


"""
In class based views we can use our own templates or django
inbuilt out of the box templates for the generic views.

By simply renaming our app template folder and template files to
match django's we will not have to define template name in our views.

Class based views also allow us to pass in mixins that help with
all sorts of functionality.

For example in the PostCreateView class we add our own custom
FormUserNeededMixin that allows us to prohibit unauthenticated
users from posting
"""


class RePostView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_authenticated():
            post_copy = Post.objects.re_post(request.user, post)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(post.get_absolute_url())


class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'post_app/post_update.html'
    # success_url = reverse_lazy("posts:post_list")


class PostCreateView(FormUserNeededMixin, CreateView):
    form_class = PostModelForm
    template_name = 'post_app/post_create.html'
    success_url = reverse_lazy("posts:post_list")


class PostDetailView(DetailView):
    # template_name = 'posts/post_detail.html'
    queryset = Post.objects.all()
    """
    In class based views we actually do not need the function below.

    def get_objects(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        return Post.objects.get(pk)
    """


class PostListView(ListView):
    # template_name = 'posts/post_list.html'
    # queryset = Post.objects.all()
    def get_queryset(self, *args, **kwargs):
        friends = self.request.user.profile.get_following()
        friends_post = Post.objects.filter(user__in=friends)
        my_post = Post.objects.filter(user=self.request.user)
        queryset = (friends_post | my_post).distinct()
        # We want to create a request parameter. We test that with this print
        # It returns an empty query dictionary. i.e <QueryDict:{}>
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        """
        Below we allow for a more robust search using the Q
        lookup that allows us to search multiple models with the
        '|' indicating the 'or' operation.

        We import Q from django.db.models.
        """
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return queryset

    def get_context_data(self, *args, **kwargs):
        """
        This is generally how our content is got originally
        using the ListView generic class.
        """
        content = super(PostListView, self).get_context_data(*args, **kwargs)
        # This renders the create post form on the PostListView view
        content['create_form'] = PostModelForm
        # We redirect to create_post view function once post is submited
        content['create_url'] = reverse_lazy('posts:create_post')
        # print(content)
        return content


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("posts:post_list")
