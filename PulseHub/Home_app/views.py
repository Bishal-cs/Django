from django.shortcuts import render
from .models import Posts
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect

def Home(request):
    return render(request, 'index.html')

def PostsList(request):
    post = Posts.objects.all().order_by('-created_at')
    return render(request, 'posts_list.html', {'post': post})

def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            redirect('PostsList')
    else:
        pass
    form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def Post_edit(request, post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('PostsList')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_create.html', {'form': form})

def Post_delete(request, post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('PostsList')
    else:
        pass
    return render(request, 'post_delete.html', {'post': post})