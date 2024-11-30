# Generated by Django 5.1.2 on 2024-11-30 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_app', '0001_initial'),
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='author_app.author'),
            preserve_default=False,
        ),
    ]
