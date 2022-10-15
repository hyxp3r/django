from django.shortcuts import get_object_or_404, render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):

    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})