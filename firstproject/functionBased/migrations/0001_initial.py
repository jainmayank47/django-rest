# Generated by Django 4.0.1 on 2022-01-20 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('salary', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('pending', 'pending'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
