from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import ProfileModel
from posts.models import PostsModel
from django.contrib.auth.decorators import login_required
from comments.models import CommentsModel
from django.core.paginator import Paginator

# Create your views here.

@login_required
def PublicProfile(request, profile_id):
    profile = get_object_or_404(ProfileModel, id=profile_id)
    post_list = PostsModel.objects.filter(user=profile.user).order_by('-created')
    paginator = Paginator(post_list, 8)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    is_follower = False
    if request.user.is_authenticated:
        is_follower = request.user.profile.is_following(profile.user)
    return render(request, 'public/public_profile.html', {
        'profile':profile,
        'posts':posts,
        'is_follower':is_follower
        })
    
@login_required
def AddComment(request, profile_id ,post_id):
    post = PostsModel.objects.get(id=post_id)
    profile = ProfileModel.objects.get(user=request.user)
    if request.method == 'POST':
        text = request.POST.get('comment')
        comment = CommentsModel(post=post, text=text, user=profile)
        comment.save()
        return redirect('public', profile_id=profile_id)
    return redirect('public', profile_id=profile_id)

@login_required
def DelComment(request, profile_id, com_id):
    comment = CommentsModel.objects.get(id=com_id)
    comment.delete()
    return redirect('public', profile_id=profile_id)

@login_required
def DeletePost(request, profile_id, post_id):
    post = PostsModel.objects.get(id=post_id)
    post.delete()
    return redirect('public', profile_id=profile_id)

@login_required
def follow_unfollow_profile(request, profile_id, action):
    profile = get_object_or_404(ProfileModel, id=profile_id)
    if action == 'follow':
        request.user.profile.follow(profile.user)
    else:
        request.user.profile.unfollow(profile.user)
    return redirect('public', profile_id=profile_id)

def FollowerList(request, profile_id):
    profile = get_object_or_404(ProfileModel, id=profile_id)
    is_follower = False
    if request.user.is_authenticated:
        is_follower = request.user.profile.is_following(profile.user)
    return render(request, 'public/profile_followers.html', {
        'profile':profile,
        'is_follower':is_follower,
    })
    