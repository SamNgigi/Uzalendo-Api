from django.contrib.auth import get_user_model

# from django.http import HttpResponseRedirect
from django.shortcuts import (
    # render,
    redirect,
    get_object_or_404,
)

from django.views.generic import DetailView
from django.views import View

from django.views.generic.edit import FormView

from .forms import UserRegisterForm

from .models import UserProfile
# Create your views here.

User = get_user_model()


class UserRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(
            User, username__iexact=self.kwargs.get("username")
        )

    def get_context_data(self, *args, **kwargs):
        content = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(
            self.request.user, self.get_object())
        content['following'] = following
        content['recommended'] = UserProfile.objects.recommended(
            self.request.user)
        return content


class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_follow_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            # is following
            UserProfile.objects.toggle_follow(request.user, toggle_follow_user)
        return redirect(
            "accounts:user_details", username=username
        )
        """
        or we could do the above like so
        url = reverse(
              "accounts:user_details",
               kwargs={"username": username}
        )
        HttpResponseRedirect(url)
        """
