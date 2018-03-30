from django.contrib import admin

# Register your models here.
from .forms import PostModelForm
from . models import Post


class PostModelAdmin(admin.ModelAdmin):
    form = PostModelForm


admin.site.register(Post, PostModelAdmin)
