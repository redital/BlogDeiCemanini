from msilib.schema import CheckBox
from xml.dom import NoModificationAllowedErr
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


dark=False

def post_list(request):
    separatore='/'
    posts = Post.objects.exclude(published_date = None).order_by('-published_date')
    global dark
    if request.method=='POST':
        if len(request.POST.getlist('dark_theme'))==1:
            dark=True
        else:
            dark=False
    return render(request, 'blog/post_list.html', {'posts': posts,'dark':dark})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.set_has_picture()
    global dark
    if request.method=='POST':
        if len(request.POST.getlist('dark_theme'))==1:
            dark=True
        else:
            dark=False
    return render(request, 'blog/post_detail.html', {'post': post,'dark':dark})
