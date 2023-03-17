from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    photo = models.ImageField(default='users/pictures/user.png', upload_to='users/pictures', verbose_name='Foto')
    birthday = models.DateField(null=True, blank=True, verbose_name='Cumpleaños')
    bio = models.TextField(blank=True, null=True, verbose_name='Biografia')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):   
        return self.user.username
    
    def follow(self, user):
        self.followers.add(user)
        
    def unfollow(self, user):
        self.followers.remove(user)
        
    def is_following(self, user):
        return self.followers.filter(pk=user.pk).exists()
    
    def followers_count(self):
        return self.followers.count()
    
    def following_count(self):
        return self.user.following.count()
