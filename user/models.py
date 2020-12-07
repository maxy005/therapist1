from django.db import models

from django.utils import timezone


# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    #date = models.DateField(default=timezone.now)
    password = models.CharField(max_length=50)
    handles = models.CharField(max_length=100)
    username=models.CharField(max_length=100,default="")




    def user(self):
        self.save()

    @staticmethod
    def get_phone(phone):
        try:
            return user.objects.get(phone=phone)
        except:
            return False

    def __str__(self):
        return self.first_name

    def isexists(self):
        if user.objects.filter(phone=self.phone):
            return True
        else:
            return False

