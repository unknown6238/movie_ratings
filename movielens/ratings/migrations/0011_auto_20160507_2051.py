# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 15:34
from __future__ import unicode_literals

from django.db import migrations
from ratings.models import Movie


def set_movie_ratings(apps, schema_editor):
    for movie in Movie.objects.all():
        movie.avg_rating = movie.get_average()['score__avg']
        movie.total_ratings = movie.get_total()['score__count']
        movie.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_auto_20160507_1430'),
    ]

    operations = [
        migrations.RunPython(set_movie_ratings),
    ]
