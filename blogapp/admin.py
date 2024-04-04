from django.contrib import admin
from .models import Post, FeedBack


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['title']}


admin.site.register(Post, PostAdmin)
admin.site.register(FeedBack)
