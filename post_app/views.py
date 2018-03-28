from django.shortcuts import render

# Create your views here.


def post_detail_view(request, id=1):
    return render(request, 'posts/post_detail.html', {})


def post_list_view(request):
    return render(request, 'posts/post_list.html', {})
