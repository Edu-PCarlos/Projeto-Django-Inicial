# Generated by Django 5.2.4 on 2025-07-23 23:06

import django.db.models.deletion
import people.models.base
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(people.models.base.get_sentinel_user), related_name='created_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET(people.models.base.get_sentinel_user), related_name='updated_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(people.models.base.get_sentinel_user), related_name='created_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET(people.models.base.get_sentinel_user), related_name='updated_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.curso')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
