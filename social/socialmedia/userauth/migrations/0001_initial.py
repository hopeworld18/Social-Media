# Generated by Django 5.0.2 on 2024-02-08 05:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id_user', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, default='')),
                ('profileimg', models.ImageField(default='blank_profile_picture.jpg', upload_to='profile_images')),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
