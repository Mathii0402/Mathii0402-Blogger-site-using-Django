
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
STATUS=((0,'Working On'),(1,'Publish'))

class post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    msg=models.TextField()
    status=models.IntegerField(choices=STATUS,default=0)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title 

