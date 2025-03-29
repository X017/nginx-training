from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=256,null=True,blank=True)
    creator = models.ForeignKey(User,on_delete=DO_NOTHING,blank=True,null=True)
    def __str__(self):
        return f"{self.category_name}"

class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256,null=True,blank=True)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
