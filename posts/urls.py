from django.urls import path
from posts import views

urlpatterns = [
    path('list/', views.PostView, name='blog'),
    path('create/', views.CreatePost, name='create'),
    path('delete/<int:post_id>', views.DeletePost, name='delpost'),
    path('list/<int:post_id>/comment', views.AddComment, name='comment'),
    path('list/<int:com_id>/comment/delete', views.DelComment, name='delcom'),
]