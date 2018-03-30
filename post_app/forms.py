from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    """
    Adding bootstrap the hard way to a form. This give us control
    over the form widgets and label.

    content = forms.CharField(
    label='',
    widget=forms.Textarea(
        attrs={
            'placeholder': "Enter post here",
            "class": "form-control"
        }
    ))
    """
    class Meta:
        model = Post
        fields = [
            "content",
        ]

    """
    Custom basic validation from form side

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == 'abc':
            raise forms.ValidationError(
                "Hi! Sorry. Cannot be ABC! But your validation is working.")
        return content

    """
