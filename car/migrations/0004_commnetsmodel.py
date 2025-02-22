# Generated by Django 5.0.4 on 2024-06-12 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_brandmodel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='commnetsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsModel', to='car.carmodel')),
            ],
        ),
    ]
