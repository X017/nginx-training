from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TweetMessage(models.Model):
    text = models.TextField(max_length=2000)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.author} - {self.text}"

    def get_absolute_url(self):
       return reverse('tweet-detail', kwargs={'pk': self.pk})

