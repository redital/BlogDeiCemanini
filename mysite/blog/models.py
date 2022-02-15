#from django.db import models

# Create your models here.

from asyncio.windows_events import NULL
from distutils.command.upload import upload
from django.conf import settings 
from django.db import models 
from django.utils import timezone 
from django.db.models.fields import NOT_PROVIDED



class Post(models.Model):
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)
     picture = models.ImageField(upload_to='blog/static/post/%pk' ,blank=True, null=True)
     has_picture = False

     def publish(self):
         self.published_date = timezone.now()
         self.save()
     def unpublish(self):
         self.published_date = None
         self.save()
     def set_has_picture(self):
         val=self.picture != None and str(self.picture) != ""
         self.has_picture=val
         self.save()

     def __str__(self):
         return self.title
