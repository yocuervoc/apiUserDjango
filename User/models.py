from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    click_couter = models.IntegerField(default=0)
    connected_time = models.IntegerField(default=0)

    def click(self):
        self.click = self.click+1

    def click(self, time):
        self.onnected_time = self.onnected_time+time


"""
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    press_couter = models.IntegerField(default=0)
    connected_time = models.IntegerField(default=0)

    def __str__(self):
        return '{0}{1}'.format(self.first_name, self.last_name)
"""
