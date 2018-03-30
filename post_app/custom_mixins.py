from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
    """
    This mixin notifies and prohibits a user from making a post if
    they are not authenticated
    """

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ["User must be logged in to continue."]
            )
            return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):
    """
    This mixin in conjuction with the inbuilt LoginRequiredMixin,
    notifies and prohibits a user from updating a post if they
    are not logged in.
    """

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ["This user is not allowed to edit this data."]
            )
