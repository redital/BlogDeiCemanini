from django.contrib import admin
from django.utils import timezone 

from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

def Publish(modeladmin,request,queryset):
    queryset.update(published_date = timezone.now())
def Unpublish(modeladmin,request,queryset):
    queryset.update(published_date = None)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    inlines = [PostImageAdmin]
    list_display=('title','author','published_date')
    #readonly_fields=('title','author','published_date')
    #list_select_related=['author']
    exclude=['author']
    actions=[Publish,Unpublish]
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    class Meta:
       model = Post

    

class PostImageAdmin(admin.ModelAdmin):
    pass