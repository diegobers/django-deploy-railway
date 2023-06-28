from django.db import models 
from datetime import datetime


class Advertising(models.Model):
  # Infos
  title = models.CharField(null=True, blank=True, max_length=200)
  description = models.TextField(null=True, blank=True)
  adv_type = models.TextField(null=True, blank=True)
  adv_cod = models.IntegerField(null=True, blank=True)
  initial_price = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
  final_price = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
  is_published = models.BooleanField(null=True, default=True, blank=True)
  is_occupied = models.BooleanField(null=True, default=True, blank=True)
  list_date = models.DateField(null=True, default=datetime.today, blank=True)

  # Details
  photo_main = models.ImageField(null=True, blank=True, upload_to='img/product')
  photo_1 = models.ImageField(null=True, blank=True, upload_to='img/product')
  bedrooms = models.IntegerField(null=True, blank=True)
  suite_bedrooms = models.IntegerField(null=True, blank=True)
  bathrooms = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
  garage = models.IntegerField(null=True, default=0, blank=True)
  useful_meters = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
  total_meters = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
  lot_size = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)
  caixa_matricula_cef = models.IntegerField(null=True, blank=True)
  caixa_edital = models.IntegerField(null=True, blank=True)

  # Locations
  address = models.CharField(blank=True ,max_length=200)
  district = models.CharField(blank=True ,max_length=100)
  city = models.CharField(blank=True ,max_length=100)
  state = models.CharField(blank=True ,max_length=100)
  zipcode = models.CharField(blank=True ,max_length=20)


  def __str__(self):
      return self.description