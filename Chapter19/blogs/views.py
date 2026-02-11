from django.shortcuts import render, redirect
from .models import Blog, BlogPost
from .forms import BlogForm, PostForm

def index(request):
    '''The home page for blog.'''
    return render(request, 'blogs/index.html')

def blogs(request):
    '''Show all blogs.'''
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    '''Show a single blog and all its posts.'''
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.order_by('-date_added')
    context = {'blog':blog, 'posts':posts}
    return render(request, 'blogs/blog.html', context)

# ARRUMAR A PARTIRR DAQUI
def new_blog(request):
    '''Add a new blog.'''
    if request.method != 'POST':
        # No data, blank form
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blogs')
    
    # Display a blank form
    context = {'form' : form}
    return render(request, 'blogs/new_blog.html', context)

def new_post(request, blog_id):
    '''Add a new post for a particular blog.'''
    blog = Blog.objects.get(id=blog_id)

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

def edit_post(request, post_id):
    '''Edit an existing post.'''
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

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