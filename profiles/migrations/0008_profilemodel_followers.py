# Generated by Django 4.1.7 on 2023-03-10 06:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0007_alter_profilemodel_bio_alter_profilemodel_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
