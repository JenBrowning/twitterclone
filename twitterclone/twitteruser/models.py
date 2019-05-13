from django.contrib.auth.models import User
from django.db import models

class TwitterUser(models.Model):
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username