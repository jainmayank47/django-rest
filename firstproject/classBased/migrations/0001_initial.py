# Generated by Django 4.0.1 on 2022-01-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('male', 'm'), ('female', 'f')], default='m', max_length=30)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('pending', 'pending'), ('deleted', 'deleted')], default='pending', max_length=10)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('nick_name', models.SlugField(max_length=10)),
                ('semester', models.IntegerField()),
            ],
            options={
                'db_table': 'student_info',
                'ordering': ['first_name'],
            },
        ),
    ]