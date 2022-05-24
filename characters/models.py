from django.db import models
from numpy import character
import uuid

# Create your models here.
class Character(models.Model):
    id = models.AutoField(primary_key=True)
    timesLinked= models.IntegerField(default=0)
    name = models.CharField(max_length=40)

# Create your models here.
class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    character = models.ForeignKey(Character,models.RESTRICT,null=False,default=None)