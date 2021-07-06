from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    # TODO video field
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
