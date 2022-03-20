# Generated by Django 4.0.3 on 2022-03-20 13:36

from django.db import migrations
from uuid import uuid4


class Migration(migrations.Migration):

    def update_uuids(apps, schema_editor):
        Languages = apps.get_model('theater', 'Language')
        Categories = apps.get_model('theater', 'Category')

        for language in Languages.objects.all():
            language.uuid  = uuid4()
            language.save()

        for category in Categories.objects.all():
            category.uuid  = uuid4()
            category.save()

    dependencies = [
        ('theater', '0007_actor_uuid_downloads_uuid_language_uuid_movie_uuid_and_more'),
    ]

    operations = [
        migrations.RunPython(update_uuids)
    ]
