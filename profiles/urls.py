from django.urls import path
from profiles import views

urlpatterns = [
    path('register/', views.Registration, name='register'),
    path('succes/', views.SuccesView, name='succes'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('edit/', views.ProfileDetail, name='profile'),
]