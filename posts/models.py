import os
from django.db import models
from profiles.models import ProfileModel
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.

class PostsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario')
    profile = models.ForeignKey(ProfileModel, on_delete=models.PROTECT, verbose_name='Perfil')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts', blank=True, null=True, verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')
    
    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
       
    def __str__(self):
        return self.title   
    
@receiver(post_delete, sender=PostsModel)
def delete_images(sender, instance, **kwargs):
    if instance.image:
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.image.name))