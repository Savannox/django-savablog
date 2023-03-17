from django.urls import path
from contact import views

urlpatterns = [
    path('', views.ContactView, name='contact'),
]