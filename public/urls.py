from django.urls import path
from public import views

urlpatterns = [
    path('<int:profile_id>/', views.PublicProfile, name='public'),
    path('<int:profile_id>/followers/', views.FollowerList, name='followerlist'),
    path('<int:profile_id>/<int:post_id>/delete/', views.DeletePost, name='delpos'),
    path('<int:profile_id>/<int:post_id>/comment/', views.AddComment, name='coment'),
    path('<int:profile_id>/<int:com_id>/comment/delete/', views.DelComment, name='delco'),
    path('<int:profile_id>/<str:action>/', views.follow_unfollow_profile, name='followsys'),
]