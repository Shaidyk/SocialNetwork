from django.db import models

import cloudinary.uploader
import cloudinary.api

from SocialNetwork.settings import DEBUG, CLOUDINARY_URL


class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="images/photo", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_avatar = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    @property
    def img_uploader(self):
        if DEBUG:
            upload_to = "images/photo"
            return upload_to
        else:
            upload_to = cloudinary.utils.cloudinary_url(
                self.image,
                width=150,
                height=200,
                crop="fill")
            return upload_to
