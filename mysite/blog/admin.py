from django.contrib import admin

from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

class PostImageAdmin(admin.ModelAdmin):
    pass