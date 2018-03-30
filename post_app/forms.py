from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
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
