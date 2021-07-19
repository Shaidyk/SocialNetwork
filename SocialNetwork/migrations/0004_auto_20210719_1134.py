# Generated by Django 3.2.4 on 2021-07-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetwork', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ManyToManyField(blank=True, null=True, to='SocialNetwork.Photo'),
        ),
    ]
