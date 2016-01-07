from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Rockleton(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return "User %s data" % self.user