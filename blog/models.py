from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text_1 = models.TextField(blank=True, null=True)
    cover_1 = models.ImageField(upload_to='images/',blank=True, null=True)
    text_2 = models.TextField(blank=True, null=True)
    cover_2 = models.ImageField(upload_to='images/',blank=True, null=True)
    text_3 = models.TextField(blank=True, null=True)
    cover_3 = models.ImageField(upload_to='images/',blank=True, null=True)
    text_4 = models.TextField(blank=True, null=True)
    cover_4 = models.ImageField(upload_to='images/',blank=True, null=True)
    text_5 = models.TextField(blank=True, null=True)
    cover_5 = models.ImageField(upload_to='images/',blank=True, null=True)
    text_6 = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
