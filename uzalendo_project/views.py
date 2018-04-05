from django.contrib.auth import get_user_model

from django.db.models import Q


from django.shortcuts import render

from django.views import View


User = get_user_model()


def home(request):
    return render(request, "home.html", {})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        queryset = None

        if query:
            queryset = User.objects.filter(
                Q(username__icontains=query)
            )
        content = {
            "users": queryset,
        }
        return render(request, "search.html", content)
