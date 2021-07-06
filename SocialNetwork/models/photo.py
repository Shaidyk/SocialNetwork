from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="images/photo")
    description = models.TextField()
    is_avatar = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
