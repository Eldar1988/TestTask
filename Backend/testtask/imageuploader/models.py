from django.contrib.auth.models import User
from django.db import models
from .service import path_and_rename


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=path_and_rename('images/', 'image'))
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'image from {self.user}'

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        ordering = ['-date']


class ImageAction(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='actions')
    type = models.CharField(max_length=100)
    from_image = models.ImageField(upload_to=path_and_rename('story/', 'image'), null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ['-date']
