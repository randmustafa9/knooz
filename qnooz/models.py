from django.db import models

# Create your models here.
#msgtype 1=mgs, 2=she shouldknow

class Kmsgs(models.Model):
    msgK = models.TextField(max_length=1900)
    datek = models.DateTimeField(auto_now_add=True)
    msgtype = models.IntegerField(max_length=2, null=True)
    seen = models.BooleanField(default=False)
    sender = models.CharField(max_length=200, default='')


    def __str__(self):
        return self.msgK
  