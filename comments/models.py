
from django.urls import reverse_lazy
from django.utils import timezone

from django.conf import settings

from django.db import models

class Comment(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post    = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    text    = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes   = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse_lazy("posts:detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.text




