from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    type = [('W','Wlasciciel'),
            ('K','Klient'),
            ]
    user_type = models.CharField(max_length=1,choices=type,default="W")
    def __str__(self):
        return f'{self.user.username} Profile'
