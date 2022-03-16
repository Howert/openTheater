# Generated by Django 4.0.3 on 2022-03-16 18:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0005_movie_downloads_alter_downloads_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
