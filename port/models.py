from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,  default="")
    email = models.CharField(max_length=122,  default="")
    subject = models.CharField(max_length=233,  default="")
    message = models.CharField(max_length=455,  default="")
    date = models.DateField('date published')

    def __str__(self):
        return self.name
