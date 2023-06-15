from django.db import models 


class Advertising(models.Model):
  description = models.TextField(blank=True)
  photo_main = models.ImageField(null=True, blank=True, upload_to='img/')
     
  def __str__(self):
      return self.description 