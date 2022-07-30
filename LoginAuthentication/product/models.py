from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image= models.ImageField(upload_to ='images/')
    icon =models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    body=models.TextField()
    url= models.TextField()
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)