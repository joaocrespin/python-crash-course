from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog, BlogPost
from .forms import BlogForm, PostForm


def index(request):
    '''The home page for blog.'''
    return render(request, 'blogs/index.html')

@login_required
def blogs(request):
    '''Show all blogs.'''
    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def blog(request, blog_id):
    '''Show a single blog and all its posts.'''
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request.user)
    posts = blog.blogpost_set.order_by('-date_added')
    context = {'blog':blog, 'posts':posts}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    '''Add a new blog.'''
    if request.method != 'POST':
        # No data, blank form
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blog:blogs')
    
    # Display a blank form
    context = {'form' : form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    '''Add a new post for a particular blog.'''
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request.user)

    if request.method != 'POST':
        # No data, blank form
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blog:blog', blog_id=blog_id)
    
    # Display a blank form
    context = {'blog':blog, 'form' : form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    '''Edit an existing post.'''
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(blog, request.user)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog', blog_id=blog.id)
    
    # Display a blank form
    context = {'post':post, 'blog':blog, 'form' : form}
    return render(request, 'blogs/edit_post.html', context)

def check_blog_owner(blog, user):
    '''Make sure the blog belongs to the current user'''
    if blog.owner != user:
        raise Http404