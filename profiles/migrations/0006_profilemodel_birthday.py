# Generated by Django 4.1.7 on 2023-03-09 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profilemodel_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
