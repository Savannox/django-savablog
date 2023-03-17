from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.models import PostsModel
from posts.forms import PostForm
from profiles.models import ProfileModel
from django.core.paginator import Paginator
from comments.models import CommentsModel

# Create your views here.

@login_required
def PostView(request):
    posts_list = PostsModel.objects.all().order_by('-created')
    paginator = Paginator(posts_list, 10)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'posts/post_list.html', {
        'posts':posts,
        })


@login_required
def CreatePost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        profile = ProfileModel.objects.get(user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.profile = profile
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
        return render(request, 'posts/post_create.html', {
            'form':form
        })

@login_required
def DeletePost(request, post_id):
    post = PostsModel.objects.get(id=post_id)
    post.delete()
    return redirect('blog')

@login_required
def AddComment(request, post_id):
    post = PostsModel.objects.get(id=post_id)
    profile = ProfileModel.objects.get(user=request.user)
    if request.method == 'POST':
        text = request.POST.get('comment')
        comment = CommentsModel(post=post, text=text, user=profile)
        comment.save()
        return redirect('blog')
    return redirect('blog')


@login_required
def DelComment(request, com_id):
    comment = CommentsModel.objects.get(id=com_id)
    comment.delete()
    return redirect('blog')
