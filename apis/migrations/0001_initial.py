# Generated by Django 2.1.15 on 2023-03-29 10:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movies_name', models.CharField(max_length=20)),
                ('visual_type', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('IMAX', 'IMAX')], max_length=4)),
                ('types', models.CharField(choices=[('action', 'action'), ('romantic', 'romantic'), ('sad', 'sad')], max_length=3)),
                ('review', models.TextField(max_length=50)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='MoviesActors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visual_type', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('IMAX', 'IMAX')], max_length=4)),
                ('types', models.CharField(choices=[('action', 'action'), ('romantic', 'romantic'), ('sad', 'sad')], max_length=3)),
                ('review', models.TextField(max_length=50)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Movies')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Actors')),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='actors',
            field=models.ManyToManyField(through='apis.MoviesActors', to='apis.Actors'),
        ),
    ]
