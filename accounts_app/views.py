from django.contrib.auth import get_user_model
from django.shortcuts import (
    render,
    get_object_or_404,
)

from django.views.generic import DetailView
from django.views import View
# Create your views here.

User = get_user_model()


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(
            User, username__iexact=self.kwargs.get("username")
        )


class UserFollow(View):
    def get(self):
        return render()
