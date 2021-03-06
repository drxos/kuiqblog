# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 19:18
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('image', models.ImageField(upload_to='images', verbose_name='Illustration')),
                ('image_alt', models.CharField(max_length=100, verbose_name='Image Alt')),
                ('public', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.Category')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-created'],
                'verbose_name': 'Post',
            },
        ),
    ]
