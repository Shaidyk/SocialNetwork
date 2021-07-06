from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
import uuid
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='user__username')
    last_name = models.CharField(max_length=50, null=True, blank=True)
    nick = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()

    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True)
    # TODO friends

    token = models.CharField(max_length=50, unique=True, default=str(uuid.uuid4()))
    user_custom_id = models.BigIntegerField(unique=True, default=random.randint(10000000, 99999999))

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

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


def first_name_creator(sender, instance, *args, **kwargs):
    if not instance.first_name:
        instance.first_name = instance.user.username


pre_save.connect(first_name_creator, sender=Profile)
