# Generated by Django 4.0.1 on 2022-01-31 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generics_views', '0004_alter_frameworkinfo_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frameworkinfo',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology', to='generics_views.technologyinfo'),
        ),
    ]