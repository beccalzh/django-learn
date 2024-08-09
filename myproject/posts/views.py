from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required 

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') # get all posts
    return render(request, 'posts/posts_list.html', {'posts':posts})

def posts_page(request, slug):
    post = Post.objects.get(slug=slug) # get the post with the slug
    return render(request, 'posts/post_page.html', {'post':post})

@login_required(login_url='/users/login/') # protect the page for login requirement
def post_new(request):
    return render(request, 'posts/post_new.html')