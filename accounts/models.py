from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models.signals import post_save

from PIL import Image
class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs
        


# Create your models here.
class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE) # user.profile 
    following   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') 
    image       = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # ... more fields ....

    # user.profile.following -- users i follow
    # user.followed_by -- users that follow me -- reverse relationship

    objects = UserProfileManager() # UserProfile.objects.all()
    # # abc = UserProfileManager() # UserProfile.abc.all()

    def __str__(self):
        return str(self.user)

    def get_following(self):
        users  = self.following.all() # User.objects.all().exclude(username=self.user.username)
        return users.exclude(username=self.user.username)

    # def get_follow_url(self):
    #     return reverse_lazy("account:follow", kwargs={"username":self.user.username})
        
    def get_absolute_url(self):
        return reverse_lazy("account:detail", kwargs={"username":self.user})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # solves force insert

        img = Image.open(self.image.path) # Profice image resize

        if img.height > 240 or img.width > 240:
            new_img = (240, 240)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path
