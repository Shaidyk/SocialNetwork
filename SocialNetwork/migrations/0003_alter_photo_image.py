# Generated by Django 3.2.4 on 2021-07-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetwork', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/photo'),
        ),
    ]
