from django.shortcuts import render
from .models import Posts
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request, 'index.html')

def PostsList(request):
    posts = Posts.objects.all().order_by('-created_at')
    # Get suggested users (excluding the current user)
    suggested_users = User.objects.exclude(id=request.user.id)[:5] if request.user.is_authenticated else User.objects.none()
    
    context = {
        'posts': posts,
        'suggested_users': suggested_users,
        'form': PostForm(),
    }
    return render(request, 'index.html', context)

@login_required
def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required
def Post_edit(request, post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_create.html', {'form': form})

@login_required
def Post_delete(request, post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'post_delete.html', {'post': post})