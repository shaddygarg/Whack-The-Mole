from django.db import models

# Create your models here.

class UserStat(models.Model):
    username=models.CharField(max_length=200)
    score=models.IntegerField(default=0)
    extra=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.username

