# Generated by Django 4.0.3 on 2022-03-10 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.category')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='theater.Movie_actor', to='theater.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(through='theater.Movie_category', to='theater.category'),
        ),
        migrations.AddField(
            model_name='movie_category',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.movie'),
        ),
    ]
