# Generated by Django 3.2.9 on 2021-11-19 02:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moviemodel",
            name="actors",
            field=models.ManyToManyField(
                max_length=25000,
                to="movie.ActorModel",
                verbose_name="actors relationship",
            ),
        ),
        migrations.AlterField(
            model_name="moviemodel",
            name="actors_names",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    max_length=25000,
                    null=True,
                    verbose_name="array of actors names",
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="moviemodel",
            name="director",
            field=models.CharField(
                max_length=2500, null=True, verbose_name="Имя актера"
            ),
        ),
        migrations.AlterField(
            model_name="moviemodel",
            name="genre",
            field=models.TextField(
                blank=True, max_length=10000, null=True, verbose_name="movie genre"
            ),
        ),
        migrations.AlterField(
            model_name="moviemodel",
            name="writers",
            field=models.ManyToManyField(
                max_length=25000,
                to="movie.WriterModel",
                verbose_name="writers relationship",
            ),
        ),
        migrations.AlterField(
            model_name="moviemodel",
            name="writers_names",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=25000, verbose_name="array of writers names"
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
