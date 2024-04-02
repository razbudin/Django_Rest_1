from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from .forms import SignUpForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'blogapp/index.html', context={'page_obj': page_obj})


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'blogapp/post_detail.html', context={'post': post})


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'blogapp/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blogapp/signup.html', context={
            'form': form,
        })
