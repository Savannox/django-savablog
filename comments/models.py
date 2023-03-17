from django.db import models
from profiles.models import ProfileModel
from posts.models import PostsModel

# Create your models here

class CommentsModel(models.Model):
    user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, verbose_name='Perfil')
    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, verbose_name='Publicacion')
    text = models.TextField(max_length=200, verbose_name='Comentario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    def __str__(self):
        return self.text[:20]