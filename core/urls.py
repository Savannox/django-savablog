from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('posts/', include('posts.urls')),
    path('accounts/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('public/', include('public.urls')),
]