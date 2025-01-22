from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'post': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post:post_list')
    return render(request, 'post/post_confirm_delete.html', {'post': post})