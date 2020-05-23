from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    press_couter = models.IntegerField(default=0)

    def __str__(self):
        return '{0}{1}'.format(self.first_name, self.last_name)
