from django.shortcuts import render, redirect


from .forms import PostModelForm
from .models import Post
# Create your views here.


def post_create_view(request):
    form = PostModelForm(request.POST or None)
    content = {
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("post_list")
    return render(request, 'post_app/post_create.html', content)


def post_detail_view(request, id=1):
    obj = Post.objects.get(id=id)
    content = {
        "object": obj,
    }
    return render(request, 'post_app/post_detail.html', content)


def post_list_view(request):
    queryset = Post.objects.all()

    content = {
        "object_list": queryset,
    }
    return render(request, 'post_app/post_list.html', content)
