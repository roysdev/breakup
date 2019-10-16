from django.conf import settings
from django.urls import reverse_lazy



from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Blog(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='site_blog')
    title   = models.CharField(max_length=200)
    content = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    # likes     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    # views   = models.IntegerField(default=1)

    # def get_likes(self):
    #     return self.likes.count()


    # def get_absolute_url(self):
    #     return reverse_lazy("posts:detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.title

class SiteUpdate(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news')
    title   = models.CharField(max_length=200)
    content = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    # likes     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    # views   = models.IntegerField(default=1)

    def __str__(self):
        return self.title