from django.shortcuts import render
from django.views import View

from blogapp.models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'blogapp/index.html', {'posts': posts})
