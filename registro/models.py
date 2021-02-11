from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from air_template.settings import AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()
    singup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=AUTH_USER_MODEL)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
