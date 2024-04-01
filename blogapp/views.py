from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from blogapp.models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'blogapp/index.html', context={'page_obj': page_obj})
