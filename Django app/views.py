from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    latest = Post.objects.filter(published=True)[:5]
    return render(request, 'blog/index.html', {'latest': latest})

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})
