from django.contrib import admin
from posts.models import PostsModel

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    readonly_fields = 'created', 'updated',
    list_display = 'title', 'user', 'created'
    ordering = 'created',
    
admin.site.register(PostsModel, PostsAdmin)
