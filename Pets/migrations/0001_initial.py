# Generated by Django 4.2.1 on 2023-08-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='cat_foods')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CatToy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='cat_toys')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DogBed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='dog_beds')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DogCollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='dog_collars')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DogFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='dog_foods')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DogToy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='dog_toys')),
                ('price', models.IntegerField()),
            ],
        ),
    ]