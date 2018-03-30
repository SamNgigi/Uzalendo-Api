# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'post_app/post_update.html'
    success_url = '/posts'


class PostCreateView(FormUserNeededMixin, CreateView):
    form_class = PostModelForm
    template_name = 'post_app/post_create.html'
    success_url = '/posts'


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
    queryset = Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        """
        This is generally how our content is got originally
        using the ListView generic class.
        """
        content = super(PostListView, self).get_context_data(*args, **kwargs)
        content["another_list"] = Post.objects.all()
        # print(content)
        return content


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("home")
