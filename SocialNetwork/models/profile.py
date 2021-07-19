from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save

import uuid
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    nick = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()

    photo = models.ManyToManyField('Photo', blank=True, related_name='photo')
    video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    token = models.CharField(max_length=50, unique=True, blank=True)
    user_custom_id = models.BigIntegerField(unique=True, blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            if sender.__name__ == 'User':
                Profile.objects.create(user=instance)

    @property
    def get_token(self):
        if not self.token:
            self.token = str(uuid.uuid4())
            return self.token
        else:
            return self.token

    @property
    def get_user_id(self):
        if not self.user_id:
            self.user_custom_id = random.randint(10000000, 99999999)
            return self.user_custom_id
        else:
            return self.user_custom_id

    def __str__(self):
        return f'{self.first_name}, ' \
               f'{self.last_name}, ' \
               f'{self.nick}, ' \
               f'{self.email}, ' \
               f'{self.user_custom_id}'


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')


def first_name_creator(sender, instance, *args, **kwargs):
    if not instance.first_name:
        instance.first_name = instance.user.username
        instance.token = str(uuid.uuid4())
        instance.user_custom_id = random.randint(10000000, 99999999)


pre_save.connect(first_name_creator, sender=Profile)
