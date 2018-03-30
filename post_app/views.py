# from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post
# Create your views here.


"""
In class based views we can use our own templates or django
inbuilt out of the box templates for the generic views.

By simply renaming our app template folder and template files to
match django's we will not have to define template name in our views.
"""


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
        print(content)
        return content
