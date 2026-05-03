from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from .models import Post


@login_required
def create_post(request):
  if request.method=="POST":
      title = request.POST['title']
      content = request.POST['content']

      Post.objects.create(
          title=title,
          content=content,
          author=request.user
      )  
      return redirect('/')
  return render(request,'blog/create_post.html')

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'blog/signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'blog/signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})

    return render(request, 'blog/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if post.author == request.user:
        post.delete()
    
    return redirect('/')