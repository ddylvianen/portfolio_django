from django.db import models
from django.utils import timezone

# Create your models here.
class Projects(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=200, null=True)
   description = models.CharField(max_length=200, null=True)
   img = models.ImageField(upload_to='images', default="default.png")
   url = models.CharField(max_length=500, null=True)
   published_date = timezone.now()
   
   def publish(self):
      self.published_date  = timezone.now()
      self.save()

   def __str__(self):
      return self.title