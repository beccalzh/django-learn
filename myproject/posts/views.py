from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required 
from . import forms

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') # get all posts
    return render(request, 'posts/posts_list.html', {'posts':posts})

def posts_page(request, slug):
    post = Post.objects.get(slug=slug) # get the post with the slug
    return render(request, 'posts/post_page.html', {'post':post})

@login_required(login_url='/users/login/') # protect the page for login requirement
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES) # create a form with the data
        if form.is_valid():
            newpost = form.save(commit=False) # save the form data
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost() # create a new form
    return render(request, 'posts/post_new.html', { 'form': form })