# Generated by Django 3.2.4 on 2021-07-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetwork', '0004_auto_20210706_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token',
            field=models.CharField(default='473c821b-9056-4117-a716-bdfcf80af155', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_custom_id',
            field=models.BigIntegerField(default=10929408, unique=True),
        ),
    ]