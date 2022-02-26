from msilib.schema import CheckBox
from xml.dom import NoModificationAllowedErr
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, PostImage

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
    pictures = PostImage.objects.filter(post=post)
    post.set_has_picture(pictures)
    if post.has_picture:
        texts=post.text.split("<img>")
        pieces=[]
        print(len(texts))
        print(len(pictures))
        n_intext_pictures=post.text.count('<img>')
        print(n_intext_pictures)
        for i in range(len(texts)-1):
            print(i)
            pieces.append((texts[i],pictures[i]))
            print(pieces[i])
        pieces.append((texts[-1],''))
        more_pictures=[]
        print(len(texts)-1<len(pictures))
        if len(texts)-1<len(pictures):
            print(range(len(texts)-1,len(pictures)))
            for i in range(len(texts)-1,len(pictures)):
                print(i)
                more_pictures.append(pictures[i])
        print(pieces)
        print(more_pictures)
    else:
        pieces=[(post.text,'')]
        more_pictures=[]

    global dark
    if request.method=='POST':
        if len(request.POST.getlist('dark_theme'))==1:
            dark=True
        else:
            dark=False
    return render(request, 'blog/carosello.html', 
                    {'post': post, "pieces":pieces, 
                    'more_pictures':more_pictures,
                    'dark':dark,'indici':range(len(more_pictures)),
                    'carosello':len(more_pictures)>1})
